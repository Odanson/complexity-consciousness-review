#!/usr/bin/env python3
"""
Pilot PubMed search for the complexity-of-consciousness scoping review.

Runs four hit-count queries (Block 1, Block 2, Block 3, full intersection)
against the NCBI E-utilities API, then verifies that a list of seed papers
is captured by the full query.

Usage:
    python3 pilot_search.py

No external dependencies (only stdlib). Be polite to NCBI: this script
inserts a 0.4 s delay between requests, which keeps it under the
3 requests-per-second guideline for unauthenticated access.

If you have an NCBI API key, set the environment variable
    NCBI_API_KEY=...
to raise the rate limit to 10 req/s.

Outputs a clean Markdown report to ./pilot_search_report.md.
"""

from __future__ import annotations

import json
import os
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from typing import Optional

API_KEY = os.environ.get("NCBI_API_KEY", "").strip()
DELAY_S = 0.12 if API_KEY else 0.4
ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
USER_AGENT = "complexity-consciousness-pilot/0.1 (research; contact: samson)"

# ---------------------------------------------------------------------------
# Search blocks — keep in sync with §B6 of the protocol.
# ---------------------------------------------------------------------------

BLOCK_1 = (
    '(consciousness OR "state of consciousness" OR "levels of consciousness" '
    'OR "loss of consciousness" OR unconscious* OR wakefulness OR arousal '
    'OR anesthesi* OR anaesthesi* OR sedation OR propofol OR sevoflurane '
    'OR ketamine OR xenon OR sleep OR NREM OR REM OR "slow wave sleep" '
    'OR "vegetative state" OR "unresponsive wakefulness syndrome" OR UWS '
    'OR "minimally conscious state" OR MCS OR coma OR "locked-in syndrome" '
    'OR LIS OR psychedelic* OR psilocybin OR LSD OR DMT OR ayahuasca '
    'OR meditation OR mindfulness OR dream* OR lucid)'
)

BLOCK_2 = (
    '("Lempel-Ziv" OR LZc OR LZ76 OR LZW OR compressibility '
    'OR "Kolmogorov complexity" OR "Kolmogorov signal complexity" OR KSC '
    'OR "perturbational complexity" OR PCI OR "PCI-state" OR "ST-PCI" '
    'OR "state transitions complexity index" '
    'OR "integrated information" OR IIT OR phi '
    'OR "causal density" OR "causal emergence" OR "phi-ID" '
    'OR "information decomposition" OR "state differentiation" '
    'OR entropy OR "sample entropy" OR "approximate entropy" '
    'OR "permutation entropy" OR "multiscale entropy" OR "spectral entropy" '
    'OR "transfer entropy" OR "mutual information" OR "Granger causality" '
    'OR "weighted symbolic mutual information" OR wSMI '
    'OR "neural complexity" OR "matching complexity" '
    'OR "neural avalanche*" OR criticality OR "branching parameter" '
    'OR "long-range temporal correlation*" OR "detrended fluctuation analysis" OR DFA '
    'OR "multifractal" OR "MF-DFA" '
    'OR "fractal dimension" OR "correlation dimension" OR "Hurst exponent" '
    'OR Lyapunov OR chaos '
    'OR "intrinsic dimensionality" OR "participation ratio" OR manifold '
    'OR "small-world" OR modularity OR "rich-club" OR "hierarchical complexity" '
    # Generic complexity phrasings (added in v0.3 pilot to capture papers
    # like Sitt 2014 that describe the analytic without naming a measure):
    'OR "signal complexity" OR "signal diversity" OR "EEG complexity" '
    'OR "complexity measure*" OR "complexity marker*" '
    # Phase / dynamical-systems coupling family added in v0.4 (Lucia):
    'OR "phase-locking value" OR PLV OR "phase locking value" '
    'OR "weighted phase-lag index" OR wPLI '
    'OR metastability OR "chimera state*" OR "chimera-state*" '
    'OR "phase coherence" OR "phase synchron*" '
    # TTC / Temporospatial-Theory measures added in v0.4.1 from
    # Chis-Ciure, Melloni & Northoff 2024 NBR (Yaron paper):
    'OR "autocorrelation window" OR ACW '
    'OR "power-law exponent" OR PLE '
    'OR "temporal receptive window*" OR TRW '
    'OR "scale-free" OR "scale free" '
    'OR "global signal topography" OR "GS-topography")'
)

BLOCK_3 = (
    '(EEG OR electroencephalograph* OR MEG OR magnetoencephalograph* '
    'OR iEEG OR ECoG OR intracranial OR "local field potential*" OR LFP '
    'OR fMRI OR BOLD OR "functional magnetic resonance" '
    'OR "single-unit" OR "multi-unit" OR "two-photon" OR "calcium imaging" '
    'OR "wide-field" OR neuroimag* OR "brain activity" OR "neural recording*" '
    # TMS-EEG paradigm (added to capture papers like Casali 2013 / PCI-line
    # whose abstracts describe TMS-evoked cortical responses rather than
    # writing "EEG" verbatim):
    'OR TMS OR "TMS-EEG" OR "TMS-evoked" OR "TMS evoked" '
    'OR "transcranial magnetic stimulation")'
)

FULL_QUERY = f"({BLOCK_1}) AND ({BLOCK_2}) AND ({BLOCK_3})"

# ---------------------------------------------------------------------------
# Seed papers. Each is verified by a distinctive title fragment.
# If the verification fails because the PMID isn't found, the title
# fragment may need updating; if PMID is found but not captured by the
# full query, that flags a search-strategy gap.
# ---------------------------------------------------------------------------

# Empirical seeds — must be captured by the full intersection.
EMPIRICAL_SEEDS = [
    ("Casali et al. 2013 Sci Transl Med (PCI)",
     'Casali[Author] AND 2013[PDAT] AND consciousness[Title]'),
    ("Casarotto et al. 2016 Ann Neurol (PCI in DOC)",
     'Casarotto[Author] AND 2016[PDAT] AND stratification[Title]'),
    ("Schartner et al. 2015 PLoS ONE (LZc anaesthesia)",
     'Schartner[Author] AND 2015[PDAT] AND EEG[Title]'),
    ("Schartner et al. 2017 Neurosci Conscious (psychedelics)",
     'Schartner[Author] AND 2017[PDAT] AND MEG[Title]'),
    ("Sitt et al. 2014 Brain (DOC EEG markers)",
     'Sitt[Author] AND 2014[PDAT] AND consciousness[Title]'),
    ("Carhart-Harris et al. 2014 (entropic brain)",
     'Carhart-Harris[Author] AND 2014[PDAT] AND entropic[Title]'),
    ("Toker et al. 2022 PNAS (consciousness and chaos)",
     'Toker[Author] AND 2022[PDAT] AND consciousness[Title]'),
    # Disambiguated 2026-05-28: the bare 'synergistic[Title]' lookup also
    # matched Luppi 2022 NeuroImage "Metastability, fractal scaling, and
    # synergistic information processing"; adding 'core[Title]' pins this
    # to the intended Nat Neurosci 2022 "A synergistic core for human brain
    # evolution and cognition" paper.
    ("Luppi et al. 2022 Nat Neurosci (synergistic core)",
     'Luppi[Author] AND 2022[PDAT] AND synergistic[Title] AND core[Title]'),
]

# Methodology-only seeds — included via §B4 exception, not via the
# database search. We only confirm the PMID resolves; we do NOT require
# the full intersection to capture them (they have no neural-data
# application, so they will and should fail Block 3).
METHODOLOGY_SEEDS = [
    ("Tononi-Sporns-Edelman 1994 PNAS (neural complexity)",
     'Tononi[Author] AND 1994[PDAT] AND complexity[Title]'),
    ("Oizumi-Albantakis-Tononi 2014 PLoS Comput Biol (IIT 3.0)",
     'Oizumi[Author] AND 2014[PDAT] AND phenomenology[Title]'),
    # Moved from EMPIRICAL_SEEDS after v0.4.1 pilot confirmed Block 3
    # fails (correctly — the paper is a methodology/review proposing
    # the Measure Centrality Index framework, not an empirical study).
    ("Chis-Ciure, Melloni & Northoff 2024 NBR (Measure Centrality Index)",
     'Chis-Ciure[Author] AND 2024[PDAT] AND centrality[Title]'),
]


def _http_json(params: dict, retries: int = 1, backoff_s: float = 1.5) -> Optional[dict]:
    if API_KEY:
        params = {**params, "api_key": API_KEY}
    url = ESEARCH + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    last_exc: Optional[Exception] = None
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as exc:  # noqa: BLE001
            last_exc = exc
            if attempt < retries:
                time.sleep(backoff_s)
    print(f"  ! request failed after retry: {last_exc}", file=sys.stderr)
    return None


def fetch_count(query: str) -> Optional[int]:
    data = _http_json({"db": "pubmed", "retmode": "json",
                       "rettype": "count", "term": query})
    if data is None:
        return None
    try:
        return int(data["esearchresult"]["count"])
    except (KeyError, TypeError, ValueError):
        return None


def fetch_pmids(query: str, retmax: int = 5) -> list[str]:
    data = _http_json({"db": "pubmed", "retmode": "json",
                       "term": query, "retmax": retmax})
    if data is None:
        return []
    return list(data.get("esearchresult", {}).get("idlist", []))


def main() -> None:
    started = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"Pilot search started at {started} UTC")
    print(f"API key: {'yes' if API_KEY else 'no (using 0.4 s pacing)'}\n")

    counts = {}
    for name, q in [
        ("Block 1 (consciousness)", BLOCK_1),
        ("Block 2 (complexity)", BLOCK_2),
        ("Block 3 (neural data)", BLOCK_3),
        ("Block 1 AND Block 2 AND Block 3", FULL_QUERY),
    ]:
        print(f"Running: {name}")
        n = fetch_count(q)
        counts[name] = n
        print(f"  → {n:,}" if isinstance(n, int) else "  → (failed)")
        time.sleep(DELAY_S)

    print("\nEmpirical seeds — must be captured by the full intersection:")
    seeds = []
    blocks = [("B1", BLOCK_1), ("B2", BLOCK_2), ("B3", BLOCK_3)]
    for label, lookup in EMPIRICAL_SEEDS:
        time.sleep(DELAY_S)
        pmids = fetch_pmids(lookup, retmax=3)
        if not pmids:
            seeds.append((label, lookup, None, {}, None, "empirical"))
            print(f"  - {label}: no PMID found for lookup query")
            continue
        pmid = pmids[0]
        block_status = {}
        for tag, q in blocks:
            time.sleep(DELAY_S)
            n = fetch_count(f"{pmid}[uid] AND ({q})")
            block_status[tag] = bool(n)
        time.sleep(DELAY_S)
        full_n = fetch_count(f"{pmid}[uid] AND ({FULL_QUERY})")
        is_captured = bool(full_n)
        seeds.append((label, lookup, pmid, block_status, is_captured, "empirical"))
        b_str = "  ".join(f"{t}:{'+' if block_status[t] else '-'}" for t in ("B1", "B2", "B3"))
        flag = "captured" if is_captured else "MISSED"
        print(f"  - {label}: PMID {pmid} | {b_str} | full: {flag}")

    print("\nMethodology-only seeds — included via §B4 exception, not via search:")
    for label, lookup in METHODOLOGY_SEEDS:
        time.sleep(DELAY_S)
        pmids = fetch_pmids(lookup, retmax=3)
        if not pmids:
            seeds.append((label, lookup, None, {}, None, "methodology"))
            print(f"  - {label}: no PMID found for lookup query")
            continue
        pmid = pmids[0]
        seeds.append((label, lookup, pmid, {}, None, "methodology"))
        print(f"  - {label}: PMID {pmid} (no full-query check; included by exception)")

    finished = datetime.now(timezone.utc).isoformat(timespec="seconds")

    # ----------------------------------------------------------------------
    # Write a Markdown report next to this script.
    # ----------------------------------------------------------------------
    report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "pilot_search_report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# Pilot PubMed search — report\n\n")
        f.write(f"Run: {started} → {finished} UTC\n\n")
        f.write("## Hit counts\n\n")
        f.write("| Query | Count |\n|---|---:|\n")
        for k, v in counts.items():
            f.write(f"| {k} | {v:,} |\n" if isinstance(v, int) else f"| {k} | (failed) |\n")
        f.write("\n## Empirical seeds — per-block diagnosis\n\n")
        f.write("| Seed paper | PMID | B1 | B2 | B3 | Full query |\n"
                "|---|---|:-:|:-:|:-:|:-:|\n")
        tick = lambda b: ("✓" if b else "✗")
        for label, _frag, pmid, block_status, captured, kind in seeds:
            if kind != "empirical":
                continue
            if pmid is None:
                f.write(f"| {label} | — | — | — | — | — |\n")
                continue
            cap = "✓" if captured else "**✗ — investigate**"
            f.write(f"| {label} | {pmid} | {tick(block_status['B1'])} "
                    f"| {tick(block_status['B2'])} | {tick(block_status['B3'])} | {cap} |\n")
        f.write("\n## Methodology-only seeds (included by exception)\n\n")
        f.write("| Seed paper | PMID |\n|---|---|\n")
        for label, _frag, pmid, _bs, _c, kind in seeds:
            if kind != "methodology":
                continue
            f.write(f"| {label} | {pmid or '— (lookup failed)'} |\n")
        f.write("\n## Notes\n\n")
        f.write("- If Block 1 ∧ Block 2 ∧ Block 3 returns more than 20 000 records,\n"
                "  tighten Block 1 to explicit state-change contexts (drop bare\n"
                "  *wakefulness* / *arousal*).\n")
        f.write("- If any seed is **not captured**, diagnose and revise the\n"
                "  search before locking the protocol. Common causes: term\n"
                "  appears only in the body (need to broaden field tags) or a\n"
                "  block synonym is missing.\n")
        f.write("- This is a PubMed-only pilot. The final search will be\n"
                "  replicated in Scopus, Web of Science, PsycINFO, IEEE Xplore,\n"
                "  and Embase per §B5 of the protocol.\n")

    print(f"\nReport written to: {report_path}")


if __name__ == "__main__":
    main()
