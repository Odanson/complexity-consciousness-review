#!/usr/bin/env python3
"""
Draw a reproducible calibration sample for the Elicit head-to-head test.

This pulls a random sample of N records (default 200) from the LOCKED PubMed
search (the same FULL_QUERY used by pilot_search.py — imported, not copied, so
the two can never drift), fetches each record's title + abstract, and writes:

    calibration_<N>_screening.csv   <- your blind hand-screening instrument
    calibration_<N>.ris             <- upload this into Elicit
    calibration_seeds.ris           <- the 8 empirical seeds, for a separate
                                       known-positive recovery check (optional)

The random draw is SEEDED (default 20260525), so re-running reproduces the
exact same 200 records — this is what makes the test auditable.

Usage:
    python3 calibration_sample.py                 # 200 records, seed 20260525
    python3 calibration_sample.py --n 200 --seed 20260525
    python3 calibration_sample.py --no-seeds      # skip the seeds RIS

No external dependencies (stdlib only), same as pilot_search.py. With an
NCBI API key in NCBI_API_KEY the rate limit relaxes from 3 to 10 req/s.

Run this on your own machine — it needs network access to NCBI E-utilities.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import random
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from typing import Optional

# Single source of truth for the search: import the locked query + seeds.
from pilot_search import FULL_QUERY, EMPIRICAL_SEEDS, API_KEY, DELAY_S, USER_AGENT

ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

# Decision vocabulary + allowed exclusion reasons, kept in the header of the
# screening CSV so the rubric travels with the instrument.
DECISION_VOCAB = "include | maybe | exclude"
EXCLUSION_REASONS = (
    "population (not consciousness-relevant) ; "
    "exposure (no quantitative complexity measure) ; "
    "data (no neural recording) ; "
    "publication-type (editorial/protocol/non-study) ; "
    "not-retrievable ; other"
)


def _get(url: str, data: Optional[bytes] = None, retries: int = 2,
         backoff_s: float = 1.5) -> Optional[bytes]:
    req = urllib.request.Request(url, data=data,
                                 headers={"User-Agent": USER_AGENT})
    last_exc: Optional[Exception] = None
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.read()
        except Exception as exc:  # noqa: BLE001
            last_exc = exc
            if attempt < retries:
                time.sleep(backoff_s)
    print(f"  ! request failed after retries: {last_exc}", file=sys.stderr)
    return None


def _params(params: dict) -> dict:
    return {**params, "api_key": API_KEY} if API_KEY else params


def fetch_all_pmids(query: str) -> list[str]:
    """Page through esearch to retrieve every PMID matching the query."""
    pmids: list[str] = []
    retstart = 0
    page = 5000
    while True:
        url = ESEARCH + "?" + urllib.parse.urlencode(_params({
            "db": "pubmed", "retmode": "json", "term": query,
            "retstart": retstart, "retmax": page,
        }))
        raw = _get(url)
        if raw is None:
            break
        idlist = json.loads(raw.decode("utf-8")).get(
            "esearchresult", {}).get("idlist", [])
        if not idlist:
            break
        pmids.extend(idlist)
        if len(idlist) < page:
            break
        retstart += page
        time.sleep(DELAY_S)
    return pmids


def _text(node: Optional[ET.Element]) -> str:
    if node is None:
        return ""
    return "".join(node.itertext()).strip()


def fetch_records(pmids: list[str]) -> dict[str, dict]:
    """efetch title/abstract/journal/year/authors for a list of PMIDs."""
    out: dict[str, dict] = {}
    batch = 150
    for i in range(0, len(pmids), batch):
        chunk = pmids[i:i + batch]
        data = urllib.parse.urlencode(_params({
            "db": "pubmed", "retmode": "xml", "rettype": "abstract",
            "id": ",".join(chunk),
        })).encode("utf-8")
        raw = _get(EFETCH, data=data)
        if raw is None:
            continue
        try:
            root = ET.fromstring(raw)
        except ET.ParseError as exc:
            print(f"  ! XML parse error: {exc}", file=sys.stderr)
            continue
        for art in root.findall(".//PubmedArticle"):
            pmid = _text(art.find(".//PMID"))
            title = _text(art.find(".//ArticleTitle"))
            # Structured abstracts have several AbstractText children with
            # Label attributes; concatenate them in order.
            chunks = []
            for ab in art.findall(".//Abstract/AbstractText"):
                label = ab.get("Label")
                txt = _text(ab)
                chunks.append(f"{label}: {txt}" if label else txt)
            abstract = " ".join(c for c in chunks if c).strip()
            journal = _text(art.find(".//Journal/Title"))
            year = _text(art.find(".//JournalIssue/PubDate/Year")) \
                or _text(art.find(".//JournalIssue/PubDate/MedlineDate"))[:4]
            authors = []
            for a in art.findall(".//AuthorList/Author"):
                ln = _text(a.find("LastName"))
                ini = _text(a.find("Initials"))
                if ln:
                    authors.append(f"{ln} {ini}".strip())
            out[pmid] = {
                "pmid": pmid, "title": title, "abstract": abstract,
                "journal": journal, "year": year, "authors": authors,
            }
        time.sleep(DELAY_S)
    return out


def write_screening_csv(path: str, records: list[dict]) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        # A comment row carrying the rubric (Excel shows it; the analysis
        # script skips any row whose pmid is not numeric).
        f.write(f"# DECISIONS: {DECISION_VOCAB}\n")
        f.write(f"# EXCLUSION REASONS: {EXCLUSION_REASONS}\n")
        f.write("# Screen BLIND to Elicit. Fill my_decision for every row; "
                "add my_primary_exclusion_reason only when excluding.\n")
        w = csv.writer(f)
        w.writerow(["pmid", "title", "journal", "year", "abstract",
                    "my_decision", "my_primary_exclusion_reason"])
        for r in records:
            w.writerow([r["pmid"], r["title"], r["journal"], r["year"],
                        r["abstract"], "", ""])


def _ris_record(r: dict) -> str:
    lines = ["TY  - JOUR"]
    for au in r.get("authors", []):
        lines.append(f"AU  - {au}")
    if r["title"]:
        lines.append(f"TI  - {r['title']}")
    if r["abstract"]:
        lines.append(f"AB  - {r['abstract']}")
    if r["journal"]:
        lines.append(f"JO  - {r['journal']}")
    if r["year"]:
        lines.append(f"PY  - {r['year']}")
    # AN = accession number; keep the PMID here so it survives the round-trip
    # into Elicit and back, which is what lets us join the two decision sets.
    lines.append(f"AN  - {r['pmid']}")
    lines.append(f"UR  - https://pubmed.ncbi.nlm.nih.gov/{r['pmid']}/")
    lines.append("ER  - ")
    return "\n".join(lines)


def write_ris(path: str, records: list[dict]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(_ris_record(r) for r in records) + "\n")


def resolve_seed_pmids() -> list[str]:
    pmids = []
    for _label, lookup in EMPIRICAL_SEEDS:
        url = ESEARCH + "?" + urllib.parse.urlencode(_params({
            "db": "pubmed", "retmode": "json", "term": lookup, "retmax": 1}))
        raw = _get(url)
        if raw:
            ids = json.loads(raw.decode("utf-8")).get(
                "esearchresult", {}).get("idlist", [])
            if ids:
                pmids.append(ids[0])
        time.sleep(DELAY_S)
    return pmids


def main() -> None:
    ap = argparse.ArgumentParser(description="Draw the Elicit calibration sample.")
    ap.add_argument("--n", type=int, default=200, help="sample size (default 200)")
    ap.add_argument("--seed", type=int, default=20260525, help="random seed")
    ap.add_argument("--no-seeds", action="store_true",
                    help="skip writing the known-positive seeds RIS")
    args = ap.parse_args()

    started = datetime.now(timezone.utc).isoformat(timespec="seconds")
    here = os.path.dirname(os.path.abspath(__file__))
    print(f"Calibration sampler started {started} UTC")
    print(f"API key: {'yes' if API_KEY else 'no (0.4 s pacing)'} | "
          f"n={args.n} | seed={args.seed}\n")

    print("Retrieving all PMIDs for the locked FULL_QUERY ...")
    all_pmids = fetch_all_pmids(FULL_QUERY)
    print(f"  → {len(all_pmids):,} records in the PubMed intersection")
    if len(all_pmids) < args.n:
        print("  ! fewer records than requested sample size; aborting",
              file=sys.stderr)
        sys.exit(1)

    rng = random.Random(args.seed)
    sample_pmids = sorted(rng.sample(all_pmids, args.n), key=int)
    print(f"  → drew {args.n} (seed {args.seed})\n")

    print("Fetching titles + abstracts ...")
    recmap = fetch_records(sample_pmids)
    records = [recmap[p] for p in sample_pmids if p in recmap]
    missing = [p for p in sample_pmids if p not in recmap]
    if missing:
        print(f"  ! {len(missing)} records returned no metadata: "
              f"{', '.join(missing[:10])}{' ...' if len(missing) > 10 else ''}")
    print(f"  → fetched {len(records)} records\n")

    csv_path = os.path.join(here, f"calibration_{args.n}_screening.csv")
    ris_path = os.path.join(here, f"calibration_{args.n}.ris")
    write_screening_csv(csv_path, records)
    write_ris(ris_path, records)
    print(f"Wrote: {csv_path}")
    print(f"Wrote: {ris_path}")

    if not args.no_seeds:
        print("\nResolving the 8 empirical seeds (known-positive check) ...")
        seed_pmids = resolve_seed_pmids()
        seed_recs = list(fetch_records(seed_pmids).values())
        seeds_path = os.path.join(here, "calibration_seeds.ris")
        write_ris(seeds_path, seed_recs)
        print(f"Wrote: {seeds_path}  ({len(seed_recs)} seeds)")

    # A tiny provenance file so the draw is auditable in the OSF log.
    prov = os.path.join(here, f"calibration_{args.n}_provenance.txt")
    with open(prov, "w", encoding="utf-8") as f:
        f.write(f"Calibration sample provenance\n")
        f.write(f"Run (UTC): {started}\n")
        f.write(f"Sample size: {args.n}\n")
        f.write(f"Random seed: {args.seed}\n")
        f.write(f"Population (FULL_QUERY) size at run time: {len(all_pmids)}\n")
        f.write(f"Sampled PMIDs ({len(records)}):\n")
        f.write(", ".join(r["pmid"] for r in records) + "\n")
    print(f"Wrote: {prov}")
    print("\nNext: screen the CSV blind, then upload the RIS to Elicit.")


if __name__ == "__main__":
    main()
