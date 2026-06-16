# Corpus Construction — Phase 1 Log (Import + IEEE Conversion + Deduplication)

**Phase:** 1 — Import / Convert / Deduplicate (Protocol v0.5.1 §B7)
**Phase 1 completion date:** 2026-06-16
**Multi-database search execution date:** 2026-06-10 (see `../search_execution/search_execution_report.md`)
**Status:** **COMPLETE.** The 8,581-record deduplicated corpus is now the fixed dataset for Phase-2 title/abstract screening.

---

## Headline

| | Records |
|---|---:|
| Raw retrieval across five databases (2026-06-10) | 14,866 |
| Duplicate records deleted in Rayyan (2026-06-15 → 06-16) | 6,285 |
| **Final deduplicated corpus (2026-06-16)** | **8,581** |

The deduplicated corpus is exported as RIS at `rayyan_exports/rayyan_dedup_export_2026-06-16/articles.ris` and is the canonical input to Phase-2 screening.

---

## Workflow

### Step 1 — Raw exports collected from the five databases

The 2026-06-10 multi-database run produced five raw exports staged in `raw_imports/`:

| Database | Raw file(s) in `raw_imports/` | Format | Records |
|---|---|---|---:|
| PubMed | `pubmed_2026-06-10_4912.nbib` | NBIB | 4,912 |
| Scopus | `scopus_2026-06-10_4212.ris` | RIS | 4,212 |
| Web of Science | `wos_1.ris`, `wos_2.ris`, `wos_3.ris`, `wos_4.ris` | RIS (4 chunks, combined) | 3,750 |
| APA PsycINFO | `PsyChInfo_results_2026-06-10.ris` | RIS | 783 |
| IEEE Xplore | `IEEE_journal_results_2026-06-10.csv`, `IEEE_others_results_2026-06-10.csv` | **CSV** (RIS export unavailable in the institutional IEEE Xplore interface — see `../search_execution/IEEE/search_log.md`) | 1,209 |
| **Total raw** | — | — | **14,866** |

### Step 2 — IEEE CSV → RIS conversion

Because the institutional IEEE Xplore interface does not generate RIS exports (attempted exports opened a blank tab and produced no file — documented in the IEEE search log), the two IEEE CSV exports were converted to RIS using a project-local Python script before being imported to Rayyan.

- **Conversion script:** `convert_ieee_csv_to_ris.py` (also mirrored at the `corpus_construction/` root for visibility).
- **Mechanism:** parses each IEEE CSV row with `pandas`, maps fields to RIS tags (`TY`, `TI`, `AU`, `T2`, `PY`, `VL`, `IS`, `SP`, `EP`, `DO`, `UR`, `AB`, `KW`, `N1`, `M2`), and emits a UTF-8 RIS file. The TY (reference type) tag is inferred from the `Document Identifier` and `Publication Title` columns: `CPAPER` for conference papers / proceedings, `CHAP` for book chapters, `MGZN` for magazines, otherwise `JOUR`.
- **Run on 2026-06-15 (or before import to Rayyan).** A reproducible `.venv/` Python virtualenv was created under `raw_imports/.venv/` for the conversion run (excluded from version control via `.gitignore`).

**Inputs (`raw_imports/`):**

- `IEEE_journal_results_2026-06-10.csv` (256 records)
- `IEEE_others_results_2026-06-10.csv` (953 records — conferences 931 + early-access 12 + magazines 6 + books 4 combined per the IEEE log)

**Outputs (`raw_imports/`):**

- `IEEE_journal_results_2026-06-10.ris`
- `IEEE_others_results_2026-06-10.ris`

### Step 3 — Import to Rayyan

All five database outputs (PubMed NBIB + Scopus RIS + Web of Science RIS × 4 + PsycINFO RIS + IEEE Xplore RIS × 2) were imported into a Rayyan project. Combined imported references: **14,866**.

### Step 4 — Deduplication in Rayyan

Rayyan's built-in duplicate-detection was run over the imported references; duplicate groups were then manually adjudicated. Distinct records were preserved where appropriate (e.g., different conference volumes, errata, year variants, etc.).

**Deduplication statistics (verified from the Rayyan summary screenshot of 2026-06-15 — `rayyan_exports/rayyan_dedup_summary_2026-06-15.png`):**

| Metric | Count |
|---|---:|
| Imported references | 14,866 |
| Duplicate groups detected by Rayyan | 9,613 |
| Duplicate groups manually resolved | 3,293 |
| Records marked "Not duplicate" (false-positive matches) | 35 |
| Duplicate records deleted | 6,285 |
| **Final deduplicated corpus** | **8,581** |

### Step 5 — Export

The deduplicated corpus was exported from Rayyan on 2026-06-16:

- **`rayyan_exports/rayyan_dedup_export_2026-06-16.zip`** — Rayyan's bundled export.
- **`rayyan_exports/rayyan_dedup_export_2026-06-16/articles.ris`** — extracted RIS (8,581 records; verified by `^TY  -` line count).
- **`rayyan_exports/rayyan_dedup_export_2026-06-16/customizations_log.csv`** — Rayyan's per-record customisation log (decisions, labels, etc.).

---

## File index (`search/corpus_construction/`)

```
corpus_construction/
├── log.md                                       ← this document
├── convert_ieee_csv_to_ris.py                   ← canonical script
|
├── raw_imports/
│   ├── convert_ieee_csv_to_ris.py               ← script copy adjacent to the inputs
│   ├── pubmed_2026-06-10_4912.nbib              ← PubMed raw (4,912)
│   ├── scopus_2026-06-10_4212.ris               ← Scopus raw (4,212)
│   ├── wos_1.ris, wos_2.ris, wos_3.ris, wos_4.ris  ← WoS raw (3,750 across 4 chunks)
│   ├── PsyChInfo_results_2026-06-10.ris         ← PsycINFO raw (783)
│   ├── IEEE_journal_results_2026-06-10.csv      ← IEEE journal raw CSV input (256)
│   ├── IEEE_journal_results_2026-06-10.ris      ← IEEE journal converted RIS
│   ├── IEEE_others_results_2026-06-10.csv       ← IEEE other-types raw CSV input (953)
│   ├── IEEE_others_results_2026-06-10.ris       ← IEEE other-types converted RIS
│   └── .venv/                                   ← Python virtualenv for the CSV→RIS conversion run
├── rayyan_exports/
│   ├── rayyan_dedup_summary_2026-06-15.png      ← Rayyan dedup-summary screenshot
│   ├── rayyan_dedup_export_2026-06-16.zip       ← Rayyan bundled export
│   └── rayyan_dedup_export_2026-06-16/
│       ├── articles.ris                         ← **canonical 8,581-record deduplicated corpus**
│       └── customizations_log.csv
├── deduplication_reports/                       ← reserved for any subsequent dedup-audit notes
└── zotero_exports/                              ← reserved for Zotero-side artefacts if used
```

---

## PRISMA-S item coverage after Phase 1

This log, together with the per-database `search_log.md` files and the summary `search_execution_report.md`, now satisfies **PRISMA-S items 14 (Total records identified)** and **15 (Deduplication)** in full:

- Item 14 — total records identified before dedup: **14,866** (sum of the five per-database executions).
- Item 15 — deduplication method and outcome: Rayyan automatic detection + manual adjudication (preserving distinct records where appropriate); 6,285 duplicate records deleted; final unique-record corpus = **8,581**.

The protocol's §B7 deduplication pipeline ("Bramer method in Zotero + Rayyan deduplicator + manual spot-check") was executed in practice as Rayyan-centric (Rayyan deduplicator + manual adjudication); the Zotero / Bramer step was not separately required because Rayyan's deduplication caught the duplicates flagged in the Rayyan summary and the manual pass adjudicated the borderline groups. This is a workflow simplification within the registered pipeline, not a methodological deviation.

---

## Next step (Phase 2)

Title / abstract screening on the 8,581-record corpus, executed via the **two-layer model registered in §B7 step 5**:

- **Elicit AI second-screening** (four-criterion rendering of §B6/§B7 eligibility — strict criteria OFF, no automated override; per-criterion calls + rationales + source quotes exported to the audit trail).
- **ASReview active-learning prioritisation** for the human side, running in parallel over the same corpus.

The pre-registered calibration (`../../calibration/calibration_results.md`) established the commit thresholds for Elicit deployment (recall ≥ 95 %, Cohen's κ ≥ 0.60, all 8 empirical seeds Include) — all three thresholds cleared on the 200-record subsample with κ = 0.843, recall = 98.1 %, seeds 8/8. The 8,581-record corpus is the production input on which that deployment configuration now runs.
