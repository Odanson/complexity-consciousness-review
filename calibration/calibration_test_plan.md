# Elicit head-to-head — test plan

**Companion to:** `elicit_assessment.md` · `prisma_protocol.md` v0.5
**Goal.** Convert "Lucia says Elicit is fast" into our own number: screen the same 200 abstracts by hand and in Elicit, blind to each other, then measure agreement and Cohen's κ. The result decides how much of the bulk screen we lean on Elicit for — or whether we use it at all.
**Time.** ~1 afternoon (≈2–3 h of hand-screening + a few minutes of Elicit runtime + the analysis script).

This is **pre-registered**: the design and the commit thresholds (bottom of this doc) are fixed *before* any numbers are seen, so the decision can't be rationalised after the fact.

---

## Design in one line

A two-rater agreement study where **neither rater is ground truth**. The human reviewer (Samson) and Elicit each screen the identical 200 records, independently, against the §B6/§B7 criteria. The plan reports agreement, κ, and — the number that matters most for a scoping review — whether Elicit ever drops a paper the human would keep.

Two methodological points worth stating plainly:

- **Neither is "right."** This measures concordance, not accuracy. That is the honest framing for a single human vs an AI tool. The separate seeds check (below) is the one place we *do* have known-correct answers.
- **Sample source caveat.** The 200 are drawn from the locked **PubMed** intersection (available today). The real Week-5 calibration will run on the full deduplicated six-database corpus. For deciding whether to *trust the tool*, the PubMed slice is representative; just note it in the writeup.

---

## Step 1 — Draw the sample (~5 min)

```bash
cd "/Users/odanson/Lab Rotations/PredictiveLab/Complexity/Complexity"
python3 calibration_sample.py            # 200 records, seed 20260525
```

It imports the locked `FULL_QUERY` straight from `pilot_search.py` (so the two can't drift), draws a **seeded** random 200 (re-running reproduces the exact same set), fetches titles + abstracts, and writes:

- `calibration_200_screening.csv` — the blind screening instrument
- `calibration_200.ris` — the file uploaded to Elicit
- `calibration_seeds.ris` — the 8 empirical seeds, for the known-positive check
- `calibration_200_provenance.txt` — run time, seed, population size, the 200 PMIDs (goes in the OSF log)

---

## Step 2 — Hand-screen, blind (~2–3 h)

Open `calibration_200_screening.csv` (Excel/Numbers). For each row fill **`my_decision`** with `include`, `maybe`, or `exclude`, and add a **`my_primary_exclusion_reason`** only when excluding (allowed reasons are listed in the file header).

Do this **before** looking at any Elicit output — anchoring to Elicit's call destroys the test. Apply exactly the §B6/§B7 criteria I'll use for the deployment. Save as CSV.

---

## Step 3 — Run Elicit on the same 200 (~10–15 min)

1. New systematic review → on the protocol setup page paste the **research question** and the **PECO + eligibility criteria** from §B6/§B7 (let it auto-suggest criterion questions, then edit to match ours).
2. **Strict criteria: OFF** — this is a scoping review; we keep borderline papers. (Important: the default for a rigorous SLR is on.)
3. In the source-gathering step choose **upload papers** and upload `calibration_200.ris` (don't run a fresh semantic search — we want the identical 200).
4. Run title/abstract screening. Spot-check a few source-quote rationales to confirm the criteria were understood, but **do not override** anything — we want Elicit's unaided decisions for the comparison.
5. **Export** the screening decisions as **CSV/Excel**. Make sure the export includes the **identifier/PMID** column and the **decision** column. Save it (e.g. `elicit_export.csv`).

*(Optional, 5 min — known-positive check: run `calibration_seeds.ris` through the same criteria. All 8 are papers we know belong; any that Elicit excludes is a real red flag, independent of the κ result.)*

---

## Step 4 — Compute the stats (~1 min)

```bash
python3 calibration_analysis.py \
    --mine   calibration_200_screening.csv \
    --elicit elicit_export.csv
```

It joins the two files on PMID and writes `calibration_results.md` plus `calibration_disagreements.csv`. Output:

- raw agreement (binary include/exclude, and 3-category)
- Cohen's κ (binary), 3-category κ, and linear-weighted κ
- PABAK (because screening prevalence is lopsided — most papers exclude — and plain κ can look artificially low under that imbalance)
- the 2×2 confusion table
- **Elicit's recall of *my* includes** — of the papers I'd keep, the % Elicit also kept
- the list of every disagreement, flagged by direction

If the auto-join reports unmatched records, the script reports them explicitly; re-run with `--elicit-id-col`/`--elicit-decision-col` once Elicit's actual column names are known.

---

## Pre-registered decision thresholds

Judge against these **before** looking at the numbers. The scoping-review priority is sensitivity: a tool that quietly drops relevant papers is disqualifying, even with a high κ.

**Commit to Elicit as AI second-screener for the bulk screen** if *all three* hold:

1. **Recall of my includes ≥ 95%** — i.e. Elicit drops ≤ 1 in 20 of the papers I'd keep. This is the gate that matters most.
2. **Cohen's κ (binary) ≥ 0.60** (substantial) — and the disagreements are defensible on reading.
3. **All 8 seeds screened IN** on the known-positive check.

**Use it only as decision-support (the human reviewer screens everything, Elicit flags possible misses)** if recall is 90–95% or κ is 0.40–0.60 — useful, but not trusted to make calls alone.

**Don't adopt it for screening** if recall < 90%, κ < 0.40, or it excludes any seed — the manual + ASReview path stays primary.

Whatever the outcome, the result and the disagreement list go into the OSF audit trail, and the chosen mode is recorded as a §B7 amendment ("AI-assisted second screening (Elicit), human-reconciled"). Note Elicit's version/run-date — its accuracy moves between releases, so the version is part of reproducibility.

---

*Test plan only — no protocol changes until the numbers are in.*
