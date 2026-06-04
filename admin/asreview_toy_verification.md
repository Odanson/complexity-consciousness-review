# ASReview toy-set verification

**Purpose.** Confirm ASReview installs cleanly, ingests an RIS file, runs active-learning prioritisation, and exports decisions — *before* you depend on it in Phase 3 Weeks 6–7.

**Time.** ~20 minutes the first time; ~2 minutes thereafter.

**Inputs.** No external data needed — we reuse the 200-record `calibration_200.ris` already on disk as the toy set.

---

## Steps

```bash
# 1. Install ASReview into a clean venv (keeps it isolated from system Python).
cd "/Users/odanson/Lab Rotations/PredictiveLab/Complexity/Complexity"
python3 -m venv .venv-asreview
source .venv-asreview/bin/activate
pip install --upgrade pip
pip install asreview

# 2. Smoke test — version + help.
asreview --version
asreview lab --help | head -20

# 3. Launch the LAB UI in your browser. Stops the toy-set verification here
#    if all you want is "did it install."
asreview lab
#    → opens http://localhost:5000

# 4. In the LAB UI:
#    - Create new project: "complexity-toy-200"
#    - Mode: oracle
#    - Dataset: upload calibration_200.ris
#    - Prior knowledge: pick 1 clear include + 1 clear exclude from the 200
#      (e.g., the Brain dynamic organization paper as include, the
#       Percutaneous aspiration paper as exclude)
#    - Model: defaults (TF-IDF + naive Bayes is fine for a smoke test)
#    - Start review
#    - Label ~20 records to exercise the active-learning loop
#    - Stop → Export → CSV of labelled decisions

# 5. Verify the export
ls -la asreview_export*.csv
head -3 asreview_export*.csv
```

## What "verified" means

You are good to go to Phase 3 if **all four** are true:

- `asreview lab` launches without errors and you can reach the UI in the browser.
- The 200-record RIS uploads and shows all 200 records in the project.
- The active-learning loop reorders records as you label (the top-of-queue paper changes meaningfully after the first 5 labels).
- You can export a CSV showing per-record `included` (1 / 0) + `time` columns.

If any one fails, document the error and post on the ASReview issue tracker before depending on it for the bulk pass. Plan B (if ASReview is blocked when Phase 3 starts): bulk-screen via Elicit alone in priority order by Elicit's `Screening score`, treating the score as a soft prioritisation signal in lieu of ASReview's active-learning queue.

## Coupling with Elicit in Phase 3

In the bulk pass, ASReview and Elicit run **independently in parallel** over the same deduplicated corpus:

- ASReview handles human-in-the-loop prioritisation (you screen in the order it suggests).
- Elicit runs once over the whole corpus and produces per-criterion + binary decisions on every record (offline, no prioritisation).
- After the human pass is done, the two decision sets are joined by PMID and reconciled with the same `calibration_analysis.py` logic used for the 200-record calibration.

The two tools answer different questions: ASReview *speeds up* the human pass; Elicit *provides the second-screener verdict*. They are not redundant.
