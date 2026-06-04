#!/usr/bin/env python3
"""
Compute the Elicit head-to-head agreement statistics.

Joins your blind hand-screening file with Elicit's exported decisions on PMID
and reports, for the two raters (you vs Elicit):

  * raw percent agreement (binary include/exclude, and 3-category)
  * Cohen's kappa (binary) with a Landis-Koch interpretation band
  * weighted (linear) kappa for the ordered 3-category case
  * PABAK (prevalence-adjusted bias-adjusted kappa) for the binary case
  * the 2x2 confusion table
  * the asymmetric cross-tab that actually matters for a scoping review:
    "of the papers I would INCLUDE, how many did Elicit drop?"
  * a written list of every disagreement, for adjudication

Neither rater is treated as ground truth; this is an agreement study, not an
accuracy study. (A separate known-positive check on the seeds answers the
"does Elicit drop papers we know belong?" question directly.)

Usage:
    python3 calibration_analysis.py \
        --mine    calibration_200_screening.csv \
        --elicit  elicit_export.csv

Column auto-detection handles the common Elicit export shapes; override with
--elicit-id-col / --elicit-decision-col if needed. No external dependencies.
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from datetime import datetime, timezone

INCLUDE = "include"
EXCLUDE = "exclude"
MAYBE = "maybe"
ORDER = {EXCLUDE: 0, MAYBE: 1, INCLUDE: 2}


# --------------------------------------------------------------------------
# Reading + normalising decisions
# --------------------------------------------------------------------------

def _norm_decision(value: str) -> str:
    """Map free-text decisions to include / maybe / exclude."""
    v = (value or "").strip().lower()
    if not v:
        return ""
    if v in {"include", "included", "in", "yes", "y", "1", "true"}:
        return INCLUDE
    if v in {"exclude", "excluded", "out", "no", "n", "0", "false"}:
        return EXCLUDE
    if v in {"maybe", "unclear", "uncertain", "?", "possibly"}:
        return MAYBE
    if v.startswith("inc"):
        return INCLUDE
    if v.startswith("exc"):
        return EXCLUDE
    if v.startswith("may"):
        return MAYBE
    return v  # leave unknown values visible rather than silently dropping


def _read_rows(path: str) -> list[dict]:
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        # Skip leading comment lines (the rubric rows in the hand-screen CSV).
        lines = [ln for ln in f if not ln.lstrip().startswith("#")]
    reader = csv.DictReader(lines)
    return [ {(k or "").strip(): (v or "") for k, v in row.items()}
             for row in reader ]


def _find_col(fieldnames: list[str], candidates: list[str],
              contains: list[str]) -> str | None:
    lower = {fn.lower(): fn for fn in fieldnames}
    for c in candidates:
        if c in lower:
            return lower[c]
    for fn in fieldnames:
        if any(tok in fn.lower() for tok in contains):
            return fn
    return None


def _extract_pmid(value: str) -> str:
    """Pull an 8-digit-ish PMID out of an id/url cell."""
    m = re.search(r"\b(\d{6,9})\b", value or "")
    return m.group(1) if m else (value or "").strip()


def load_mine(path: str) -> dict[str, str]:
    rows = _read_rows(path)
    out = {}
    for r in rows:
        pmid = _extract_pmid(r.get("pmid", ""))
        if pmid:
            out[pmid] = _norm_decision(r.get("my_decision", ""))
    return out


def load_elicit(path: str, id_col: str | None,
                dec_col: str | None) -> dict[str, str]:
    rows = _read_rows(path)
    if not rows:
        return {}
    fns = list(rows[0].keys())
    id_col = id_col or _find_col(
        fns, ["pmid", "an", "accession", "id", "uid"],
        ["pmid", "accession", "pubmed", "url", "id"])
    dec_col = dec_col or _find_col(
        fns, ["decision", "screening decision", "include", "status", "label"],
        ["decision", "screen", "include", "status", "label"])
    if id_col is None or dec_col is None:
        print(f"  ! could not auto-detect Elicit columns. Found: {fns}",
              file=sys.stderr)
        print("    Re-run with --elicit-id-col and --elicit-decision-col.",
              file=sys.stderr)
        sys.exit(2)
    print(f"  Elicit id column   = {id_col!r}")
    print(f"  Elicit decision col= {dec_col!r}")
    out = {}
    for r in rows:
        pmid = _extract_pmid(r.get(id_col, ""))
        if pmid:
            out[pmid] = _norm_decision(r.get(dec_col, ""))
    return out


# --------------------------------------------------------------------------
# Statistics (stdlib only)
# --------------------------------------------------------------------------

def cohens_kappa(pairs: list[tuple[str, str]], cats: list[str]) -> float:
    n = len(pairs)
    if n == 0:
        return float("nan")
    idx = {c: i for i, c in enumerate(cats)}
    k = len(cats)
    m = [[0] * k for _ in range(k)]
    for a, b in pairs:
        m[idx[a]][idx[b]] += 1
    po = sum(m[i][i] for i in range(k)) / n
    row = [sum(m[i]) for i in range(k)]
    col = [sum(m[i][j] for i in range(k)) for j in range(k)]
    pe = sum((row[i] / n) * (col[i] / n) for i in range(k))
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)


def weighted_kappa_linear(pairs: list[tuple[str, str]],
                          cats_ordered: list[str]) -> float:
    n = len(pairs)
    if n == 0:
        return float("nan")
    idx = {c: i for i, c in enumerate(cats_ordered)}
    k = len(cats_ordered)
    o = [[0.0] * k for _ in range(k)]
    for a, b in pairs:
        o[idx[a]][idx[b]] += 1
    row = [sum(o[i]) for i in range(k)]
    col = [sum(o[i][j] for i in range(k)) for j in range(k)]
    w = [[1 - abs(i - j) / (k - 1) for j in range(k)] for i in range(k)]
    po = sum(w[i][j] * o[i][j] for i in range(k) for j in range(k)) / n
    pe = sum(w[i][j] * (row[i] / n) * (col[j] / n)
             for i in range(k) for j in range(k))
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)


def landis_koch(k: float) -> str:
    if k != k:  # NaN
        return "undefined"
    if k < 0:
        return "poor (worse than chance)"
    if k < 0.20:
        return "slight"
    if k < 0.40:
        return "fair"
    if k < 0.60:
        return "moderate"
    if k < 0.80:
        return "substantial"
    return "almost perfect"


# --------------------------------------------------------------------------
# Report
# --------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mine", required=True, help="your hand-screen CSV")
    ap.add_argument("--elicit", required=True, help="Elicit export CSV")
    ap.add_argument("--elicit-id-col", default=None)
    ap.add_argument("--elicit-decision-col", default=None)
    ap.add_argument("--maybe-as", choices=["include", "exclude"],
                    default="include",
                    help="how to collapse 'maybe' for the binary analysis "
                         "(default include: high-sensitivity scoping screen)")
    ap.add_argument("--out", default="calibration_results.md")
    args = ap.parse_args()

    mine = load_mine(args.mine)
    elicit = load_elicit(args.elicit, args.elicit_id_col,
                         args.elicit_decision_col)

    shared = sorted(set(mine) & set(elicit), key=lambda x: int(x) if x.isdigit() else 0)
    only_mine = set(mine) - set(elicit)
    only_elicit = set(elicit) - set(mine)

    # Drop rows where either decision is blank/unknown before scoring.
    valid = [p for p in shared
             if mine[p] in ORDER and elicit[p] in ORDER]
    skipped = [p for p in shared if p not in valid]

    def collapse(d: str) -> str:
        if d == MAYBE:
            return INCLUDE if args.maybe_as == INCLUDE else EXCLUDE
        return d

    pairs3 = [(mine[p], elicit[p]) for p in valid]
    pairs2 = [(collapse(mine[p]), collapse(elicit[p])) for p in valid]

    n = len(valid)
    agree3 = sum(1 for a, b in pairs3 if a == b)
    agree2 = sum(1 for a, b in pairs2 if a == b)
    raw3 = agree3 / n if n else float("nan")
    raw2 = agree2 / n if n else float("nan")

    k_bin = cohens_kappa(pairs2, [EXCLUDE, INCLUDE])
    k_3 = cohens_kappa(pairs3, [EXCLUDE, MAYBE, INCLUDE])
    wk = weighted_kappa_linear(pairs3, [EXCLUDE, MAYBE, INCLUDE])
    pabak = 2 * raw2 - 1 if n else float("nan")

    # Binary 2x2: rows = mine, cols = elicit
    cell = {(a, b): 0 for a in (EXCLUDE, INCLUDE) for b in (EXCLUDE, INCLUDE)}
    for a, b in pairs2:
        cell[(a, b)] += 1
    mine_inc = cell[(INCLUDE, INCLUDE)] + cell[(INCLUDE, EXCLUDE)]
    elicit_kept_of_my_inc = cell[(INCLUDE, INCLUDE)]
    recall_of_my_includes = (elicit_kept_of_my_inc / mine_inc) if mine_inc else float("nan")

    disagreements = [(p, mine[p], elicit[p]) for p in valid
                     if collapse(mine[p]) != collapse(elicit[p])]
    # The dangerous direction for a scoping review: I'd include, Elicit drops.
    elicit_dropped_my_includes = [
        p for p in valid
        if collapse(mine[p]) == INCLUDE and collapse(elicit[p]) == EXCLUDE]

    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    here = os.path.dirname(os.path.abspath(args.out)) or "."
    dis_path = os.path.join(here, "calibration_disagreements.csv")
    with open(dis_path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["pmid", "my_decision", "elicit_decision", "direction"])
        for p, a, b in disagreements:
            direction = ("I-include / Elicit-exclude"
                         if collapse(a) == INCLUDE and collapse(b) == EXCLUDE
                         else "I-exclude / Elicit-include"
                         if collapse(a) == EXCLUDE and collapse(b) == INCLUDE
                         else "maybe-boundary")
            w.writerow([p, a, b, direction])

    lines = []
    lines.append("# Elicit head-to-head — agreement results\n")
    lines.append(f"Computed: {now} UTC\n")
    lines.append(f"Records you screened: {len(mine)} | "
                 f"Elicit screened: {len(elicit)} | "
                 f"overlap scored: {n}\n")
    if skipped:
        lines.append(f"> {len(skipped)} overlapping records skipped "
                     f"(blank/unrecognised decision on one side).\n")
    if only_mine or only_elicit:
        lines.append(f"> Not matched: {len(only_mine)} only in your file, "
                     f"{len(only_elicit)} only in Elicit's "
                     f"(check the PMID join if these are non-zero).\n")
    lines.append(f"> 'maybe' collapsed to **{args.maybe_as}** for binary stats.\n")

    lines.append("\n## Headline numbers\n")
    lines.append("| Metric | Value | Interpretation |")
    lines.append("|---|---:|---|")
    lines.append(f"| Raw agreement (binary) | {raw2:.1%} | — |")
    lines.append(f"| Cohen's kappa (binary) | {k_bin:.3f} | {landis_koch(k_bin)} |")
    lines.append(f"| PABAK (binary) | {pabak:.3f} | prevalence-adjusted |")
    lines.append(f"| Raw agreement (3-category) | {raw3:.1%} | — |")
    lines.append(f"| Cohen's kappa (3-category) | {k_3:.3f} | {landis_koch(k_3)} |")
    lines.append(f"| Weighted kappa (linear) | {wk:.3f} | {landis_koch(wk)} |")
    lines.append(f"| Elicit's recall of YOUR includes | {recall_of_my_includes:.1%} | "
                 f"the number that matters most |")

    lines.append("\n## Binary confusion table (rows = you, cols = Elicit)\n")
    lines.append("| | Elicit: exclude | Elicit: include |")
    lines.append("|---|---:|---:|")
    lines.append(f"| **You: exclude** | {cell[(EXCLUDE, EXCLUDE)]} | {cell[(EXCLUDE, INCLUDE)]} |")
    lines.append(f"| **You: include** | {cell[(INCLUDE, EXCLUDE)]} | {cell[(INCLUDE, INCLUDE)]} |")

    lines.append("\n## The direction that matters for a scoping review\n")
    if elicit_dropped_my_includes:
        lines.append(f"Elicit **excluded {len(elicit_dropped_my_includes)} "
                     f"paper(s) you would have kept** — inspect these first:\n")
        lines.append(", ".join(elicit_dropped_my_includes))
    else:
        lines.append("Elicit did **not** drop any paper you would have kept. "
                     "(Zero false-negatives against your judgement.)")

    lines.append(f"\n## Disagreements\n")
    lines.append(f"{len(disagreements)} of {n} records disagree "
                 f"(binary). Full list with directions written to "
                 f"`calibration_disagreements.csv`.\n")

    with open(args.out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print("\n".join(lines))
    print(f"\nWrote: {args.out}")
    print(f"Wrote: {dis_path}")


if __name__ == "__main__":
    main()
