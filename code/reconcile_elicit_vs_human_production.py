#!/usr/bin/env python3
"""
Production reconciliation — Elicit AI second-screener vs Rayyan human screening
on the full 8,581-record deduplicated corpus.

Inputs (all under /mnt/Complexity):
  - screening/human_title_abstract_decisions_customizations_log.csv   Rayyan latest 'included' per article
  - screening/human_title_abstract_decisions_2026-09-08.csv           Rayyan article metadata (for source/journal)
  - screening/
      Elicit - screen-results-elicit_workflow_1_export_2026-09-10.csv
      Elicit - screen-results-elicit_workflow_2_export_2026-09-10.csv
      elicit_split_manifest.csv                                Original RIS index -> part_number
      elicit_unassessable_no_abstract_manifest.csv             No-abstract records (coverage gap docs)
  - calibration/calibration_seeds.ris                          8 empirical seed PMIDs

Outputs (screening/):
  - elicit_vs_human_production_2026-09-10.csv                  Per-record: human + elicit + agreement class + per-criterion calls
  - elicit_vs_human_production_report.md                       Headline metrics + coverage-gap + seed gate + cross-tabs
  - disagreements_for_adjudication_2026-09-10.csv              The substantive-disagreement subset (recall failures)

No external dependencies; stdlib only.
"""
from __future__ import annotations
import csv, os, re, sys, math
from io import StringIO
from collections import Counter, defaultdict

csv.field_size_limit(sys.maxsize)

ROOT = "/sessions/optimistic-practical-lamport/mnt/Complexity"
DEP  = f"{ROOT}/screening"
RAY  = f"{ROOT}/screening"

W1_CSV   = f"{DEP}/Elicit - screen-results-elicit_workflow_1_export_2026-09-10.csv"
W2_CSV   = f"{DEP}/Elicit - screen-results-elicit_workflow_2_export_2026-09-10.csv"
CUST_CSV = f"{RAY}/human_title_abstract_decisions_customizations_log.csv"
ART_CSV  = f"{RAY}/human_title_abstract_decisions_2026-09-08.csv"
MANIFEST = f"{DEP}/elicit_split_manifest.csv"
UNASSESSABLE = f"{DEP}/elicit_unassessable_no_abstract_manifest.csv"
SEEDS_RIS = f"{ROOT}/calibration/calibration_seeds.ris"

OUT_PER_RECORD = f"{DEP}/elicit_vs_human_production_2026-09-10.csv"
OUT_REPORT     = f"{DEP}/elicit_vs_human_production_report.md"
OUT_DISAGREE   = f"{DEP}/disagreements_for_adjudication_2026-09-10.csv"

# --- helpers ---------------------------------------------------------------

def read_csv_lax(path):
    """Read a possibly-NUL-contaminated CSV via utf-8-sig."""
    with open(path, "rb") as f: raw = f.read()
    cleaned = raw.replace(b"\x00", b"").decode("utf-8-sig", errors="replace")
    return list(csv.DictReader(StringIO(cleaned)))

def strip_prefix(s):
    return re.sub(r"^rayyan-", "", (s or "").strip())

# --- load Rayyan human decisions + metadata --------------------------------

print("Loading Rayyan human decisions…")
human = {}  # aid -> {'included': '1'/'-1'/'0', 'reason_tags': [...]}
with open(CUST_CSV, encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        aid = row["article_id"]
        key = row["key"]
        if key == "included":
            human.setdefault(aid, {"included": "", "reason_tags": []})
            human[aid]["included"] = row["value"]
        elif key.startswith('"__EXR__') or key.startswith('__EXR__') or key.startswith('"'):
            human.setdefault(aid, {"included": "", "reason_tags": []})
            human[aid]["reason_tags"].append(key.strip('"'))
INC_MAP = {"1": "Include", "-1": "Exclude", "0": "Maybe"}
print(f"  human decisions: {len(human)}")

print("Loading Rayyan article metadata…")
art_by_aid = {}
with open(ART_CSV, encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        aid = strip_prefix(row["key"])
        art_by_aid[aid] = {
            "doi": (row.get("doi") or "").strip().lower(),
            "title": (row.get("title") or "").strip(),
            "year": row.get("year", ""),
            "journal": row.get("journal", ""),
            "publisher": row.get("publisher", ""),
        }
print(f"  articles: {len(art_by_aid)}")

# --- load split manifest ---------------------------------------------------

print("Loading split manifest…")
manifest = {}  # aid -> part_number
with open(MANIFEST, encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        aid = row["rayyan_article_id"]
        if aid:
            manifest[aid] = int(row["part_number"])
print(f"  manifest rows with aid: {len(manifest)}")

# --- load unassessable manifest -------------------------------------------

unassessable = set()
with open(UNASSESSABLE, encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        aid = row["rayyan_article_id"]
        if aid: unassessable.add(aid)
print(f"  unassessable (no-abstract in Rayyan source): {len(unassessable)}")

# --- load seed PMIDs -------------------------------------------------------

seed_pmids = []
with open(SEEDS_RIS, encoding="utf-8", errors="replace") as f: text = f.read()
for rec in re.split(r"\nER  -\s*\n", text):
    for line in rec.splitlines():
        if line.startswith("AN  - "):
            seed_pmids.append(line[6:].strip())
seed_pmids = [p for p in seed_pmids if p]
print(f"  empirical seed PMIDs: {len(seed_pmids)}  {seed_pmids}")

# Map seed PMIDs to Rayyan article_ids via articles.csv (pubmed_id column)
seed_aids = set()
with open(ART_CSV, encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        pmid = (row.get("pubmed_id") or "").strip()
        if pmid in seed_pmids:
            seed_aids.add(strip_prefix(row["key"]))
print(f"  seed rayyan_article_ids (matched via pubmed_id): {len(seed_aids)}")

# --- load Elicit exports ---------------------------------------------------

def load_elicit(path, workflow_label):
    rows = read_csv_lax(path)
    out = []
    for r in rows:
        an = strip_prefix(r.get("Imported AN") or r.get("imported AN") or "")
        # Only keep records whose AN matches a rayyan_article_id in our manifest
        if an not in manifest: continue
        rec = {
            "aid": an,
            "workflow": workflow_label,
            "elicit_verdict": r.get("Screening judgement", ""),
            "elicit_relevance": r.get("Relevance rating (0-5)", ""),
            "elicit_exclusion_reason": r.get("Exclusion reason", ""),
            "c1": r.get("Consciousness Research Context", ""),
            "c2": r.get("Empirical Neural Data Application", ""),
            "c3": r.get("Quantitative Complexity-Family Measures Applied", ""),
            "c4": r.get("Eligible Study Type", ""),
        }
        out.append(rec)
    return out

print("Loading Elicit W1…")
w1 = load_elicit(W1_CSV, "W1")
print(f"  W1 corpus records (filtered via manifest): {len(w1)}")
print("Loading Elicit W2…")
w2 = load_elicit(W2_CSV, "W2")
print(f"  W2 corpus records (filtered via manifest): {len(w2)}")

# Detect intra-corpus overlap between W1 and W2 (should be ~0 if partitioning was clean)
w1_aids = {r["aid"] for r in w1}
w2_aids = {r["aid"] for r in w2}
overlap = w1_aids & w2_aids
print(f"  W1 ∩ W2 (should be 0): {len(overlap)}")

# Merge (if there's overlap, W1 wins arbitrarily; document overlap for the report)
elicit = {}
for r in w1: elicit[r["aid"]] = r
for r in w2:
    if r["aid"] not in elicit: elicit[r["aid"]] = r
print(f"  Merged Elicit corpus records: {len(elicit)}")

# --- build joined per-record table -----------------------------------------

def classify(human_dec, elicit_verdict):
    e = (elicit_verdict or "").strip().lower()
    e = "include" if e == "include" else ("exclude" if e == "exclude" else "")
    if human_dec == "Maybe":
        return "human_maybe"
    if not e:
        return "no_elicit_verdict"
    if human_dec == "Include" and e == "include": return "agree_include"
    if human_dec == "Exclude" and e == "exclude": return "agree_exclude"
    if human_dec == "Include" and e == "exclude": return "disagree_recall_miss"     # substantive
    if human_dec == "Exclude" and e == "include": return "disagree_permissive"      # expected under strict-OFF
    return "unknown"

rows_out = []
class_counts = Counter()
for aid in sorted(manifest.keys(), key=lambda x: int(x)):
    h = human.get(aid, {})
    h_val = h.get("included", "")
    h_dec = INC_MAP.get(h_val, "UNKNOWN")
    e = elicit.get(aid, {})
    e_ver = e.get("elicit_verdict", "")
    cls = classify(h_dec, e_ver)
    class_counts[cls] += 1
    art = art_by_aid.get(aid, {})
    reason_tags = "|".join(h.get("reason_tags", []))[:400]
    rows_out.append({
        "rayyan_article_id": aid,
        "part_number": manifest.get(aid, ""),
        "doi": art.get("doi", ""),
        "title": art.get("title", ""),
        "year": art.get("year", ""),
        "journal": art.get("journal", ""),
        "human_decision": h_dec,
        "human_reason_tags": reason_tags,
        "elicit_verdict": e_ver,
        "elicit_relevance": e.get("elicit_relevance", ""),
        "elicit_exclusion_reason": e.get("elicit_exclusion_reason", ""),
        "elicit_workflow": e.get("workflow", ""),
        "c1_consciousness": e.get("c1", ""),
        "c2_neural_data": e.get("c2", ""),
        "c3_complexity_measure": e.get("c3", ""),
        "c4_study_type": e.get("c4", ""),
        "agreement_class": cls,
        "in_unassessable_manifest": "yes" if aid in unassessable else "no",
        "is_seed": "yes" if aid in seed_aids else "no",
    })

with open(OUT_PER_RECORD, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows_out[0].keys()))
    w.writeheader(); w.writerows(rows_out)
print(f"Wrote {OUT_PER_RECORD}  ({len(rows_out)} rows)")

# --- disagreement subset (substantive: recall misses) --------------------

with open(OUT_DISAGREE, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows_out[0].keys()))
    w.writeheader()
    for r in rows_out:
        if r["agreement_class"] == "disagree_recall_miss":
            w.writerow(r)
print(f"Wrote {OUT_DISAGREE}")

# --- metrics --------------------------------------------------------------

# Confusion on rows where BOTH have a decision (exclude human_maybe and no_elicit_verdict)
paired = [r for r in rows_out if r["agreement_class"] in ("agree_include","agree_exclude","disagree_recall_miss","disagree_permissive")]
n_paired = len(paired)
tp = sum(1 for r in paired if r["agreement_class"] == "agree_include")   # human include ∧ elicit include
tn = sum(1 for r in paired if r["agreement_class"] == "agree_exclude")   # human exclude ∧ elicit exclude
fn = sum(1 for r in paired if r["agreement_class"] == "disagree_recall_miss")   # human include ∧ elicit exclude
fp = sum(1 for r in paired if r["agreement_class"] == "disagree_permissive")    # human exclude ∧ elicit include

po = (tp + tn) / n_paired if n_paired else float("nan")
# Cohen's kappa
row_incl = tp + fn
row_excl = fp + tn
col_incl = tp + fp
col_excl = fn + tn
pe = (row_incl*col_incl + row_excl*col_excl) / (n_paired**2) if n_paired else float("nan")
kappa = (po - pe) / (1 - pe) if pe < 1 else float("nan")
# PABAK
pabak = 2*po - 1
# Recall of human-includes
recall = tp / (tp + fn) if (tp+fn) else float("nan")
# Precision (of elicit-includes vs human-includes)
precision = tp / (tp + fp) if (tp+fp) else float("nan")

# Seed gate
seed_verdicts = [(r["rayyan_article_id"], r["elicit_verdict"], r["human_decision"]) for r in rows_out if r["is_seed"] == "yes"]
seeds_included_by_elicit = sum(1 for _,ev,_ in seed_verdicts if (ev or "").strip().lower() == "include")

# Part-level breakdown
part_breakdown = defaultdict(Counter)
for r in rows_out:
    part_breakdown[r["part_number"]][r["agreement_class"]] += 1

# Coverage
have_elicit = sum(1 for r in rows_out if r["elicit_verdict"])
no_elicit   = sum(1 for r in rows_out if not r["elicit_verdict"])

# Elicit exclusion-reason distribution (on excludes only)
elicit_excl_reasons = Counter(r["elicit_exclusion_reason"] for r in rows_out if r["elicit_verdict"].lower() == "exclude" and r["elicit_exclusion_reason"])

# --- report ---------------------------------------------------------------

def pct(x, d=1): return f"{100*x:.{d}f}%"

lines = []
lines.append(f"# Production reconciliation — Elicit vs Rayyan human, full 8,581-record corpus\n")
lines.append(f"**Date:** 2026-09-10 · **Author:** Samson Odan\n")
lines.append(f"**Inputs:** `Elicit - screen-results-elicit_workflow_1_export_2026-09-10.csv` (5,002×54) + `Elicit - screen-results-elicit_workflow_2_export_2026-09-10.csv` (3,116×45) + Rayyan `customizations_log.csv` (8,581 final decisions).\n")

lines.append("## 1. Coverage against the human tier\n")
lines.append(f"| | Count | % of 8,581 |")
lines.append(f"|---|---:|---:|")
lines.append(f"| Corpus records total (Rayyan-deduplicated) | 8,581 | 100.0% |")
lines.append(f"| Records with an Elicit verdict | {have_elicit} | {pct(have_elicit/8581)} |")
lines.append(f"| Records with NO Elicit verdict (coverage gap) | {no_elicit} | {pct(no_elicit/8581)} |")
lines.append(f"| Records in no-abstract unassessable manifest | {len(unassessable)} | {pct(len(unassessable)/8581)} |")
lines.append(f"\nCross-tab of the no-Elicit-verdict cohort against the unassessable manifest:\n")
in_manifest_no_verdict   = sum(1 for r in rows_out if not r["elicit_verdict"] and r["in_unassessable_manifest"]=="yes")
not_in_manifest_no_verdict = sum(1 for r in rows_out if not r["elicit_verdict"] and r["in_unassessable_manifest"]=="no")
lines.append(f"- Explained by no-abstract manifest: **{in_manifest_no_verdict}** ({pct(in_manifest_no_verdict/max(no_elicit,1))} of the gap)")
lines.append(f"- Unexplained by the manifest: **{not_in_manifest_no_verdict}** ({pct(not_in_manifest_no_verdict/max(no_elicit,1))} of the gap) — need per-record inspection")
lines.append("")

lines.append("## 2. Headline agreement metrics (paired records only)\n")
lines.append(f"Paired records (both raters have a verdict, excluding Rayyan `Maybe` and no-Elicit-verdict): **{n_paired}**\n")
lines.append(f"| Metric | Value | Pre-registered calibration commit threshold |")
lines.append(f"|---|---:|---|")
lines.append(f"| Raw agreement (Po) | **{pct(po)}** | — |")
lines.append(f"| Cohen's κ | **{kappa:.3f}** | ≥ 0.60 |")
lines.append(f"| PABAK | {pabak:.3f} | — |")
lines.append(f"| Recall of human-includes | **{pct(recall)}** | ≥ 95% |")
lines.append(f"| Precision (Elicit-includes vs human-includes) | {pct(precision)} | — |")
lines.append("")

lines.append("### 2 × 2 confusion (paired)\n")
lines.append(f"|                       | Elicit Include | Elicit Exclude | Row total |")
lines.append(f"|---|---:|---:|---:|")
lines.append(f"| **Human Include**  | {tp} (agree)   | {fn} (recall miss) | {row_incl} |")
lines.append(f"| **Human Exclude**  | {fp} (permissive) | {tn} (agree)     | {row_excl} |")
lines.append(f"| Column total | {col_incl} | {col_excl} | {n_paired} |")
lines.append("")

lines.append("### Comparison to calibration outcome\n")
lines.append("| Metric | Calibration (n=194 paired) | Production ({} paired) |".format(n_paired))
lines.append(f"|---|---:|---:|")
lines.append(f"| Cohen's κ | 0.843 | {kappa:.3f} |")
lines.append(f"| Recall of human-includes | 98.1% | {pct(recall)} |")
lines.append(f"| Substantive disagreements (recall misses) | 0 (after adjudication) | {fn} |")
lines.append("")

lines.append("## 3. Empirical-seed gate\n")
lines.append(f"Seeds present in the corpus: **{len(seed_verdicts)}** of 8 (per calibration_seeds.ris).")
lines.append(f"Seeds returned Include by Elicit under production: **{seeds_included_by_elicit}** of {len(seed_verdicts)}")
lines.append(f"Pre-registered pass criterion: 8/8 Include.\n")
lines.append(f"| Seed rayyan_article_id | Elicit verdict | Human decision |")
lines.append(f"|---|---|---|")
for aid, ev, hd in seed_verdicts:
    lines.append(f"| {aid} | {ev or '—'} | {hd} |")
lines.append("")

lines.append("## 4. Agreement classes (all 8,581 records)\n")
lines.append("| Class | Count | % of 8,581 |")
lines.append("|---|---:|---:|")
for cls in ("agree_include","agree_exclude","disagree_recall_miss","disagree_permissive","human_maybe","no_elicit_verdict","unknown"):
    n = class_counts.get(cls, 0)
    lines.append(f"| `{cls}` | {n} | {pct(n/8581)} |")
lines.append("")

lines.append("## 5. Part-level breakdown (W1 = part 1, records 1–5,000; W2 = part 2, records 5,001–8,581)\n")
lines.append("| Class | Part 1 | Part 2 |")
lines.append("|---|---:|---:|")
for cls in ("agree_include","agree_exclude","disagree_recall_miss","disagree_permissive","human_maybe","no_elicit_verdict"):
    lines.append(f"| `{cls}` | {part_breakdown[1].get(cls,0)} | {part_breakdown[2].get(cls,0)} |")
lines.append("")
lines.append("This tests the W2-composition hypothesis (W2's lower Elicit include rate is composition-driven — later part of the corpus is IEEE conference + older PubMed records). If Part 2 has a much higher `agree_exclude` share and comparable `disagree_recall_miss` share, the hypothesis holds.\n")

if elicit_excl_reasons:
    lines.append("## 6. Top Elicit exclusion reasons (on Elicit-Exclude verdicts)\n")
    lines.append("| Reason | Count |")
    lines.append("|---|---:|")
    for reason, n in elicit_excl_reasons.most_common(12):
        lines.append(f"| {reason[:120]} | {n} |")
    lines.append("")

if overlap:
    lines.append(f"## 7. W1–W2 overlap warning\n")
    lines.append(f"Detected {len(overlap)} corpus records appearing in BOTH workflow exports. W1 wins in the merge; overlap listed for inspection.\n")

lines.append("## 8. Immediate next steps\n")
lines.append(f"1. **Review the `disagree_recall_miss` subset** ({fn} records) → `disagreements_for_adjudication_2026-09-10.csv`. These are the substantive concerns — records where the human said Include but Elicit said Exclude. Classify each as (a) true Elicit miss vs (b) aggregation-drift boundary case (per the calibration disagreement classification method in `calibration/calibration_disagreements_classified.csv`).")
lines.append(f"2. **Investigate any unexplained coverage gap** ({not_in_manifest_no_verdict} records) — records with no Elicit verdict that are not in the no-abstract manifest. Likely candidates: workspace-library dedup casualties from the messy part-2 attempts, or records that were in the deleted part-2 first-attempt library and never re-uploaded.")
lines.append(f"3. **Update `calibration/calibration_results.md`** with the production κ / recall / substantive-disagreement counts alongside the calibration numbers.")
lines.append(f"4. **Proceed to full-text screening** on the reconciled Include set: records classified as `agree_include` are highest priority; `disagree_permissive` records (Elicit-Include, human-Exclude) are secondary — human decision governs per §B7; `human_maybe` records go to full-text triage.")

with open(OUT_REPORT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print(f"Wrote {OUT_REPORT}")

# --- short console summary -------------------------------------------------
print()
print("=" * 60)
print("RECONCILIATION SUMMARY")
print("=" * 60)
print(f"Records with Elicit verdict:  {have_elicit} / 8,581  ({pct(have_elicit/8581)})")
print(f"Paired records:                {n_paired}")
print(f"Cohen's κ:                     {kappa:.3f}   (calibration: 0.843)")
print(f"Recall of human-includes:      {pct(recall)}   (calibration: 98.1%)")
print(f"Substantive disagreements:     {fn}   (calibration: 0 post-adjudication)")
print(f"Empirical-seed gate:           {seeds_included_by_elicit}/{len(seed_verdicts)}  (target: 8/8)")
print(f"Coverage gap (no Elicit):      {no_elicit}  of which {in_manifest_no_verdict} in no-abstract manifest, {not_in_manifest_no_verdict} unexplained")
