# Next-phase checklist — after title/abstract screening reconciliation

**Date started:** 2026-09-10
**Last updated:** 2026-11-10 (screening complete: both retests done, 529 included + 7 additions = 536; extraction pilot sample drawn)
**Owner:** Samson Odan
**Scope:** post-Elicit-reconciliation → adjudication → full-text screening → extraction → appraisal → synthesis
**Companion:** `protocol/prisma_protocol_v0.5.2.md` §B7 (steps 6+), §B8, §B10, §B11

---

## Phase 1 — Close out the title/abstract tier

- [x] **1.1** *(done 2026-09-11; 39 adjudications, see run_log §7f/§7g)* Adjudicate the 32 priority disagreements in `screening/disagreements_for_adjudication_2026-09-10.csv` (only rows tagged `true_elicit_miss_priority_adjudication`). For each: read the abstract, decide whether the human decision stands or should flip. Add a column `adjudicated_decision` (Include / Exclude / Maybe) and `adjudication_notes`. Save as `disagreements_adjudicated_2026-09-10.csv` in the same folder.
- [x] **1.2** *(supervisor confirmed the Carhart-Harris 2014 and Luppi 2022 exclusions; reported by Samson 2026-10-07; add the confirmation date/wording to `admin/seed_exclusion_review_2026-09-10.md`)* Supervisor spot-check on the two human-Excluded empirical seeds — Carhart-Harris 2014 (entropic brain) and Luppi 2022 (synergistic core). Confirm the human-Exclude with the supervisor or flip. Record decision in `admin/seed_exclusion_review_2026-09-10.md`.
- [x] **1.3** (done 2026-10-07; see run log §7k - dedup hypothesis NOT confirmed; 1,027 recomputed; 570554060 flagged) Investigate the 1,034 unexplained coverage-gap records (Elicit no-verdict, not in no-abstract manifest). Spot-check 20 randomly; if pattern is confirmed as "workspace-library dedup casualty from pre-reset chaos," log a one-line note in the run log. No re-screening.
- [x] **1.4** (done 2026-10-07; adjudication count corrected to 39, see §7g) Log the production reconciliation outcome in `calibration/calibration_results.md` — add a "Production outcome (2026-09-10)" section: recall 96.0%, κ 0.401, PABAK 0.501, kappa-paradox explanation, coverage-gap decomposition, 32-record adjudication summary.
- [x] **1.5** *(done)* Freeze the final Include set for full-text screening. Final: 1,313 records in Rayyan (1,196 Include + 117 Maybe after adjudication; 1,310 distinct after resolving the Gallez ×2 and Lambooij duplicates). Frozen file `screening/final_full_text_screening_set_v2_2026-10-05.csv`; the 2026-09-10 file (1,311 rows) is superseded (run_log §7g).

## Phase 2 — Full-text screening (§B7 step 6, solo human)

- [x] **2.1** *(full texts available for all 1,313 records, confirmed by Samson 2026-10-07; no unavailable-records manifest needed)* Retrieve full texts for the 1,313-record set. Use library access, ILL, and author-requests for the tail; document any records where full text cannot be obtained in `screening/full_text_unavailable_manifest.csv`.
- [x] **2.2** *(concluded 2026-10-05; 1,313 screened: 530 included / 783 excluded at conclusion; after the retest adjudication now 529 / 784 after retest adjudication, run log §7n–§7o)* Full-text screen each record against §B4 include/exclude criteria. Deliverable: `screening/full_text_screening_decisions_2026-10-05.csv` (notes, `exclusion_category`, `exclusion_category_short`; includes carry the metrics note). Authoritative export: `screening/rayyan_full_text_screening_all_decisions_2026-10-05/`.
- [x] **2.3** *(done 2026-11-10. Title/abstract: 96.5% agreement, κ 0.836 three-way / 1.00 Maybe=Include, run log §7l. Full text: 96.2% agreement, κ 0.922, run log §7m; target ≥ 0.8 met. 5 full-text disagreements adjudicated 2026-11-10, run log §7n: Maybes resolved to Include 2026-11-10, §7o: 529 Include / 784 Exclude.)* Intra-rater test-retest on a 10% random sample re-screened after ≥ 1 month (§B7 requirement; earliest ~2026-11-05). Compute self-agreement κ; target ≥ 0.8. Sample drawn 2026-10-07: n = 131, seeded, proportionally stratified (53 Include / 78 Exclude); see run_log §7h and `screening/full_text_retest_BLIND_rescreen_2026-10-07.csv`. Any flips change the include/exclude counts, so re-run the counts, update the decisions CSV, and append a dated note to the run log.
- [x] **2.4** *(DONE 2026-11-10: final PRISMA counts and diagram in `screening/prisma_flow_counts_FINAL_2026-11-10.md`; counts final at 529 Include / 784 Exclude; 536 with the seven additions, `screening/final_included_set_with_additions_2026-11-10.csv`; IEEE count verified; only the final PRISMA diagram figure remains) (draft counts in `screening/prisma_flow_counts_DRAFT_2026-10-07.md`; final waits for 2.3; numbers above are provisional until 2.3 is done; methodology-only seeds §B9b to be added after verification)* Update the PRISMA flow diagram with the identified → screened → included counts through this tier.

## Phase 3 — Data extraction (§B8)

- [ ] **3.1** *(10 papers drawn 2026-11-10: `extraction/pilot_sample_2026-11-10.csv`, seed 20261110; extraction not yet started)* Pilot the extraction form (`extraction/pq1_measure_extraction_form_v1.xlsx`) on 10 randomly-selected included papers. One row per (paper, measure). Any field that couldn't be reliably filled → revise the form, version-bump to v2, document changelog in `extraction/pq1_measure_extraction_codebook.md`.
- [ ] **3.2** Bulk extraction on all remaining included papers using the piloted form.
- [ ] **3.3** Intra-rater test-retest on a 10% random sample re-extracted after ≥ 1 month; deviations logged and resolved by re-reading the source.
- [ ] **3.4** Supervisor review of extraction outputs at each month-end milestone. Feedback captured in `admin/extraction_supervisor_feedback_YYYY-MM.md`.

## Phase 4 — Critical appraisal (§B10)

- [ ] **4.1** Pilot the six-item measurement-methodology checklist on the same 10-paper set used for the extraction pilot. Revise the rubric if needed.
- [ ] **4.2** Apply the checklist to every (paper, measure) row. Save into `synthesis/table_5_critical_appraisal_summary.csv` (header already in place).
- [ ] **4.3** Flag rows with high-concern on items 1, 5, or 6 for the misapplication register.

## Phase 5 — Synthesis (§B11)

- [ ] **5.1** Populate the four registered summary tables (`synthesis/table_1_*.csv` through `table_4_*.csv`) from the extraction data. Headers already fixed.
- [ ] **5.2** Populate the two support tables (spatial-scale, theory-anchoring).
- [ ] **5.3** Generate the measure × consciousness-state coverage heatmap. Save to `synthesis/figures/coverage_heatmap.png`.
- [ ] **5.4** Populate the misapplication register (`synthesis/misapplication_register.csv`) using extractor flags + §B10 items 1/5/6.
- [ ] **5.5** Populate the PQ5/PQ6/PQ7 sub-analysis tables (`pq5_theory_provenance.csv`, `pq6_proxy_convergence.csv`, `pq7_posthoc_reinterpretation.csv`).
- [ ] **5.6** Run the within-corpus citation-network analysis via Citationchaser. Save edges CSV + figure + narrative.
- [ ] **5.7** Write the decision-support appendix (`synthesis/decision_support_appendix.md`).
- [ ] **5.8** Write the PQ4 gaps section (`synthesis/pq4_gaps.md` + `gaps_table.csv`).

## Phase 6 — Manuscript

- [ ] **6.1** Draft Methods section — reference the frozen protocol and document every operational deviation candidly (multi-workflow Elicit split, workspace-library complications, coverage gap, kappa-paradox).
- [ ] **6.2** Draft Results section around the synthesis outputs.
- [ ] **6.3** Draft Discussion — measure-choice implications; measure–theory pairings; open methodological problems; how the results position the doctoral thesis Q1/Q2/Q3.
- [ ] **6.4** Supervisor review round.
- [ ] **6.5** Preprint on bioRxiv concurrent with journal submission (§B13).

## Standing rules across all phases

- Log any protocol deviation in the amendments log with rationale.
- Never edit a frozen artefact (Elicit exports, human decisions, split manifest); create a new file if you need to modify.
- Save all outputs into the folder its §B section names in the protocol — no scratch files in the repo root.
- Weekly progress note in `admin/weekly_progress_YYYY-MM-DD.md` — one paragraph, what advanced, what's blocked.
