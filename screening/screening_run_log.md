# Elicit deployment — production run log

**Companion to:** `protocol/prisma_protocol_v0.5.1.md` §B7 step 5 · `protocol/elicit_screening_prompts.md` · `calibration/calibration_results.md` · `calibration/calibration_test_plan.md`
**Corpus:** `search/corpus_construction/rayyan_exports/rayyan_dedup_export_2026-06-16/articles.ris` (8,581 unique records, frozen 2026-06-16 — same file used for Rayyan human screening completed 2026-09-08)
**Deployment date:** **2026-09-10** (this run, not the corpus-export date)
**Reviewer / operator:** Samson Odan

**Upload split — Elicit 5,000-record file cap.** Elicit's SR-workflow importer rejects files > 5,000 records ("File contains 8,581 entries, which exceeds the limit of 5,000. Please split the file into smaller parts and try again"). The frozen 8,581-record corpus is therefore split into two files, uploaded sequentially into the *same* Elicit workflow so a single per-criterion export is produced:

- `articles_part_1_of_2.ris` — 5,000 records (original RIS order, records 1–5000).
- `articles_part_2_of_2.ris` — 3,581 records (records 5001–8581).
- `elicit_split_manifest.csv` — every record's original index, part number, rayyan_article_id, DOI, title, year, TY. Used at reconciliation to confirm every record ended up in exactly one part.

The split is **sequential** (records 1–5000 → part 1; records 5001–8581 → part 2). No shuffling. Rationale: Elicit scores every paper independently against the four criteria (§B7 step 5); the file boundary has no per-record effect. Sequential preserves original Rayyan ordering, is trivially auditable, and every record is either in part 1 or part 2 by index — no split-key ambiguity.

*Preferred upload path.* Create one Elicit SR workflow with the frozen research question + four criterion prompts + strict-OFF + no override. Upload part 1, wait for ingest confirmation, then use Elicit's "Add papers" action to upload part 2 into the same workflow. This produces a single consolidated per-criterion export covering all 8,581 records.

*Fallback (if "Add papers" isn't available on your Elicit tier).* Create two SR workflows with **identical** configuration (paste the research question and four criterion prompts from `protocol/elicit_screening_prompts.md` verbatim into both; strict OFF in both; no override in both). Upload part 1 to workflow A and part 2 to workflow B. Export separately and merge the two per-criterion CSVs before reconciliation. The `elicit_split_manifest.csv` is your join key.

> Human screening in Rayyan is **frozen** as of 2026-09-08 (`screening/2026-09-08_00-47-00/customizations_log.csv` — 8,581 articles, 1,221 Include / 117 Maybe / 7,243 Exclude, one final `included` decision per article). No changes will be made to those decisions while Elicit runs. Reconciliation happens only after the Elicit pass is complete.

---

## 0. Pre-flight (before pressing Run)

- [ ] **Config equivalence with the calibrated deployment (`elicit_screening_prompts.md`).** Paste the research question and all four criterion prompts *verbatim* into the Elicit workflow; screenshot the configuration screen for the audit trail.
  - [ ] Research question — pasted verbatim.
  - [ ] Criterion 1 (Consciousness Research Context) — pasted verbatim.
  - [ ] Criterion 2 (Empirical Neural Data Application) — pasted verbatim.
  - [ ] Criterion 3 (Quantitative Complexity-Family Measures Applied) — pasted verbatim.
  - [ ] Criterion 4 (Eligible Study Type) — pasted verbatim.
  - [ ] **Strict criteria: OFF** (scoping-review default; strict-AND override was pre-registered as rejected — see `calibration/calibration_results.md` §"Correction to the deployment-rule recommendation").
  - [ ] No additional post-aggregation override rule enabled.
- [ ] **Elicit version / build recorded at run start:** `_______________________________`  (any version string or build ID visible in the Elicit UI).
- [ ] **Corpus file uploaded:** `articles.ris` (8,581 TY records verified by RIS parse). SHA-256 (optional but recommended): `_______________________________`.
- [ ] **Screenshots captured** of: (a) research-question screen, (b) four-criterion configuration, (c) strict-mode toggle, (d) import summary after Elicit ingests the file.

## 1. Import outcome (Elicit-reported — authoritative)

| Metric | Value |
|---|---:|
| Human screening universe (Rayyan, frozen) | 8,581 |
| Submitted to Elicit (part 1) | 5,000 |
| Submitted to Elicit (part 2) | 3,581 |
| **Total submitted to Elicit** | **8,581** |
| Successfully uploaded by Elicit (part 1) | **4,840** |
| — of which enriched with metadata | 4,651 |
| — of which enriched with full-text PDF | 1,306 |
| — of which uploaded but unenriched | 189 (= 4,840 − 4,651) |
| Duplicates skipped by Elicit (part 1) | **160** *(already in workspace library)* |
| Part-1 accounting | 4,840 uploaded + 160 duplicates skipped = 5,000 ✓ |
| Successfully uploaded by Elicit (part 2) | **3,322** |
| — of which enriched with metadata | 3,050 |
| — of which enriched with full-text PDF | 1,059 |
| — of which "metadata only" (no abstract, cannot be used in workflows) | **387** *(Elicit's explicit label)* |
| Duplicates skipped by Elicit (part 2) | **259** |
| Part-2 accounting | 3,322 uploaded + 259 duplicates skipped = 3,581 ✓ |
| **Total successfully uploaded across both parts** | **8,162** |
| **Total duplicates skipped across both parts** | **419** (160 + 259) |
| Ingest date/time part 1 (Elicit-reported) | 2026-09-10 |
| Ingest date/time part 2 (Elicit-reported) | 2026-09-10 |

### 1a. Part-1 "Removed before screening" (Elicit UI, 2026-09-10)

Of the 4,840 papers uploaded in part 1, **Elicit removes 241 before screening begins**. Breakdown as visible in the Elicit "Removed before screening" modal:

| Removal reason | Count | Notes |
|---|---:|---|
| No abstract or full text | 109 | Elicit could not obtain an abstract *or* a full-text PDF, even after its own metadata enrichment (Semantic Scholar / OpenAlex / Crossref). |
| *(second reason category — visible in modal, not yet recorded)* | 132 | Fill in when the second modal section is captured: reason label + count. |
| **Total removed before screening (part 1)** | **241** | |
| **Screened by Elicit (part 1)** | **4,599** | 4,840 uploaded − 241 removed. |

**Coverage-gap update — good news vs the pre-flight projection.** The pre-flight `elicit_unassessable_no_abstract_manifest.csv` projected ~1,533 no-abstract records in the first 5,000 (30.7% of 5,000, based on the RIS `AB` count). Elicit removes only **109** in part 1 for "no abstract or full text" — an order of magnitude smaller. The gap between the RIS count and Elicit's count is explained by Elicit's enrichment step (4,651 of 4,840 enriched with external-API metadata), which appears to have successfully resolved abstracts for many of our RIS-no-AB records. This substantially reduces the coverage-gap workload projected in §1 above.

*Reconciliation note.* The pre-flight `elicit_unassessable_no_abstract_manifest.csv` will need a post-hoc update after Elicit's exports are in: cross-check the manifest's 2,632 records against Elicit's actual "removed before screening" list per part, and downgrade the "unassessable" flag for records Elicit did successfully resolve. Elicit's UI shows the Rayyan `AN` field as `rayyan-570549980` — same identifier as our `rayyan_article_id` (with `rayyan-` prefix), so the join is straightforward.

### 1a-bis. Part-1 workflow — final "Removed before screening" (after all upload sessions)

The "Removed before screening" counter stabilised at **594** (grew 241 → 462 → 594 across the three snapshots as Elicit finished background enrichment and duplicate-detection). Final breakdown from the modal:

| Removal reason (part 1) | Count |
|---|---:|
| No abstract or full text | **264** |
| Duplicate files removed during upload (Elicit fuzzy title + authors match) | **330** |
| **Total removed before screening** | **594** ✓ (264 + 330) |

The 330 "duplicate files removed during upload" is important — this is Elicit's own dedup catching pairs the Rayyan deduplicator classified as distinct. Common causes: preprint + published version with different DOIs; erratum record + main paper; conference version + journal version; slight metadata drift across databases. To be inspected post-run: how many of the 330 are true corpus-integrity duplicates (Rayyan misses) vs how many are Elicit false-positive dedups (over-aggressive fuzzy matching).

### 1a-ter. Library count vs part-1 upload — the 5,266 explained

The Elicit UI shows **"All papers (5,266) · Library (5,266) · Imported papers (5,266)"** for the workflow. This is 426 more than the 4,840 part-1 papers Elicit reported uploaded, and matches the 5,000 cap plus the 266 fuzzy-dedup carve-outs almost exactly. Most likely explanation:

> Library (5,266) = 4,840 (part 1 uploaded to this workflow) + ~426 (pre-existing workspace-library papers from prior Elicit work in this account — the 200-record calibration, the 16-paper equivalence-audit trial, the seed-gate re-run, and any other prior upload not deleted).

The workspace library is account-wide, not workflow-specific. When a new workflow is created, Elicit appears to attach the entire library to it by default. The 160 "duplicates skipped" in part 1 were papers Elicit recognised as already in the library and did not re-import — but they were already in the workflow's screening set via the library attachment.

### 1a-quater. Workflow-1 final screening set + coverage

| Metric | Value |
|---|---:|
| Papers in workflow-1 library | 5,266 |
| Removed before screening | 594 |
| **Papers workflow-1 will actually screen** | **4,672** |
| Human-screened corpus (Rayyan, frozen) | 8,581 |
| **Coverage of workflow-1 alone** | **4,672 / 8,581 = 54.4%** |
| **Records with no Elicit verdict from workflow 1** | **3,909** (45.6%) |

A workflow-1-only deployment gives less than half the coverage of the human tier. This makes the second workflow (§1c) mandatory, not optional.

### 1b. Blocker — Elicit workflow paper-cap (5,000)

**Part 2 could not be added to the part-1 workflow.** After the 3,322-paper upload succeeded at the workspace/library level, attempting to attach them to the existing workflow returned:

> Paper limit of 5000 reached
> No papers were added. Remove some sources to add more.

So the 5,000 cap is per-*workflow*, not per-file. The pilot plan of "Add papers into the same workflow" is therefore infeasible for this corpus. The fallback registered in the split-plan header applies: **run two workflows with byte-identical configuration**, one per part, and merge the per-criterion CSVs at reconciliation via `elicit_split_manifest.csv`.

### 1c. Part-2 workflow setup — required actions

**Important context.** Part 2's 3,322 "uploaded" papers do *not* appear in the workspace library (library still shows 5,266, unchanged from post-part-1 upload). The "Paper limit of 5000 reached — No papers were added" error either rolled back the library additions or blocked them entirely. The "3,322 papers successfully uploaded" number Elicit displayed was likely parse-success, not library-persistence.

**Safe sequential path (recommended — no risk to workflow 1 data):**

1. [ ] **Screen workflow 1 to completion.** Do not delete anything until the workflow-1 per-criterion export is safely saved to this folder. This preserves 4,672 Elicit verdicts.
2. [ ] **Export workflow-1 results.** Per-criterion CSV + rationale + source quote, plus the binary-verdict CSV. Save into `screening/` following the §3 filename convention.
3. [ ] **Delete the workspace library.** Use the "Delete 5266 papers" button on the library view — only after step 2 confirms the export is on disk. This frees the 5,000-cap slot.
4. [ ] **Create workflow 2 with byte-identical configuration** (research question + four prompts verbatim from `protocol/elicit_screening_prompts.md`; strict OFF; no override). Confirm each field character-for-character against the audit note.
5. [ ] **Upload `articles_part_2_of_2.ris` (3,581 records)** into the empty workspace. This sits comfortably under the 5,000 cap.
6. [ ] **Record workflow-2 numbers** in a parallel §2a section below (papers uploaded, duplicates skipped, removed before screening, actual screened).
7. [ ] **Screen workflow 2 to completion, export.**
8. [ ] **Reconcile** — merge workflow-1 and workflow-2 exports via `elicit_split_manifest.csv`, then join to the Rayyan human decisions.

**Alternative — fresh Elicit account for workflow 2.**
Trades a bit of setup overhead for zero risk to the workflow-1 library. Use if the "Delete 5266 papers" action makes you nervous or if Elicit support has an academic-tier upgrade path that removes the cap.

**Do NOT** try to upload part 2 into a second workflow on the *same* account without first freeing the workspace library — Elicit's workspace-wide library attachment will re-apply the same cap.

### 1c-bis. Workflow-2 slot — clean re-upload after library reset (2026-09-10)

| Metric | Value |
|---|---:|
| Submitted to workflow-2 (part 2) | 3,581 |
| Successfully uploaded | **3,565** |
| — enriched with metadata | 3,271 (91.8%) |
| — enriched with full-text PDF | 1,141 |
| Duplicates skipped (workspace library residual) | **16** *(clean — was 3,385 in the pre-reset attempt)* |
| Removed before screening | **439** |
| — No abstract or full text | 430 |
| — Duplicate files removed during upload | 9 |
| **Papers workflow-2 will actually screen** | **3,126** (= 3,565 − 439) |
| **Corpus coverage — workflow 1 (corpus records only)** | ~4,576 |
| **Corpus coverage — workflow 2 (all records are corpus records; no prior-work carry-over after library reset)** | ~3,126 |
| **Combined Elicit coverage** | **~7,702 / 8,581 ≈ 89.8%** |
| Coverage gap (records with no Elicit verdict, mostly no-abstract) | ~879 |

The clean re-upload was possible after:
1. Workspace library was cleared (all 8,950 papers deleted).
2. Old workflow-2 (with mixed-provenance 713-paper screening set) was discarded.
3. Fresh SR workflow created with byte-identical config (research question + four criterion prompts + strict OFF + no override).
4. `articles_part_2_of_2.ris` uploaded into the fresh workspace.

The 16 residual duplicates are Elicit's fuzzy matcher catching titles similar to workflow-1's still-attached papers (workflow 1 was not deleted since its export is safely on disk). Noise-level; will surface at reconciliation only if any of the 16 correspond to a paper Rayyan classified as distinct — will be checked when merging exports.

### 1d. Duplicates across parts — investigate before treating as coverage gaps

Cumulative workspace-library duplicates flagged: **419** (160 in part 1, 259 in part 2). Sources:

1. Papers from prior Elicit work in the same account — 200-record calibration, 16-paper equivalence-audit trial, seed-gate re-run, etc. (Expected — this was flagged in §1a-bis.)
2. Part-2 records that Elicit's fuzzy-title dedup matches to part-1 records. These would be interesting: our Rayyan-deduplicated 8,581 corpus should have no true cross-part duplicates, so any part-2 duplicate that resolves against a part-1 record represents either an Elicit false-positive dedup (fuzzy-title collision) or a real duplicate that Rayyan missed (preprint + published version; errata + main; etc.).

Action: after the part-2 workflow finishes ingest, export the Elicit duplicate list (if available) and split the 259 into "against prior-work library" vs "against part 1". Only the second category needs a corpus-level integrity check.

### 1e. Notes on the part-1 ingest (2026-09-10)

- **160 duplicates skipped** are papers already present in the Elicit workspace library from earlier work in this account — the 200-record calibration subsample, the 16-paper equivalence-audit trial, the seed-gate re-run, and any other prior uploads (`calibration/calibration_elicit_export_*.csv`). These are not corpus-internal duplicates: the 8,581-record RIS was already Rayyan-deduplicated.
- **CRITICAL — verify in the Elicit UI before running screening:** do the 160 duplicates *still receive a screening decision* under this workflow, or are they excluded from this workflow's export entirely? Two outcomes have very different reconciliation consequences:
  - *If Elicit adds the pre-existing library papers to this workflow's screening set:* no action needed — they get scored and appear in the export.
  - *If Elicit excludes them from this workflow's export:* record them as coverage gaps analogous to the no-abstract records, and if any of the 8 empirical seeds sit in the duplicate set, re-check the seed gate manually before deployment sign-off.
  - Documented outcome (fill in): `_______________________________`.
- The **189 unenriched uploads** are records Elicit accepted but could not augment with metadata from its APIs. These likely overlap heavily with the no-abstract subset (2,632 records) documented in `elicit_unassessable_no_abstract_manifest.csv`. Elicit may still score them from title alone, or may skip; verify in the UI and record: `_______________________________`.
- The **full-text PDF enrichment (1,306 / 4,840 ≈ 27%)** is an Elicit bonus for later full-text screening — not needed for the current title/abstract tier.

Reconcile the Elicit-reported numbers against the RIS audit:

- **RIS records with an abstract (`AB` tag):** 5,949
- **RIS records with no abstract:** 2,632 → cross-checked against Rayyan CSV `abstract` column: **2,631** genuinely have no abstract in source; **1** appears to have been dropped by the RIS exporter alone (single record — noise). Detailed record-level manifest: `elicit_unassessable_no_abstract_manifest.csv` (this folder).
- If Elicit reports ingested ≠ 5,949, note the delta here and reconcile: `_______________________________`.

## 2. Run

Elicit surfaces a **50-source pilot → full-run** flow in the UI. This is Elicit's own UX pilot for criteria refinement; it is *not* the methodological calibration for this review — that was already run and cleared (`calibration/calibration_test_plan.md`, `calibration/calibration_results.md`, 200 records, κ = 0.843, recall 98.1%, seeds 8/8, all commit thresholds passed).

**Policy on criteria refinement during Elicit's UX pilot: DO NOT refine.** The four criterion prompts and the deployment configuration (strict OFF, no override) are frozen and OSF-registered. Any prompt edit made in response to the 50-paper pilot would (a) void the pre-registration, (b) trigger the change-control clause in `protocol/elicit_screening_prompts.md` (full re-calibration on a fresh seeded random sample), and (c) break decision-equivalence with the human tier already applied to the 8,581-record corpus. The 50-paper pilot is used here for **observation only** — to confirm the frozen prompts behave as calibrated in this deployment context — then proceed to the full run with no changes.

### Screening-set totals for workflow 1

Elicit reports **5,002 sources** for the full-run step. This is `library (5,266) − no-abstract-or-full-text (264) = 5,002`. So the 330 records tagged "duplicate files removed during upload" in the "Removed before screening" modal do *appear* in the screening set (the modal-level label is somewhat misleading — those records are not excluded from screening, only flagged as duplicates in the import-summary UI). Revised coverage:

| Metric | Value |
|---|---:|
| Full-run screening set (Elicit-reported) | 5,002 |
| Of which prior-work library carry-over (not from this corpus) | ~426 |
| Of which corpus records from part 1 that will be screened | ~4,576 |
| Corpus records not in workflow 1 (part 2 + no-abstract) | ~4,005 |
| **Workflow-1 coverage of the 8,581 corpus** | **~4,576 / 8,581 ≈ 53%** |

The ~426 prior-work records screened here (calibration subsample, 16-paper trial, seed re-run, other) are not part of the current 8,581 corpus — their verdicts should be filtered out at reconciliation by joining Elicit's per-record output against `elicit_split_manifest.csv` and keeping only records whose `rayyan_article_id` matches a row in the manifest.

### Pilot-step observation checklist (50 papers)

- [ ] **Pilot run started** (Elicit-reported): `_______________________`
- [ ] **Pilot run completed** (Elicit-reported): `_______________________`
- [ ] Skim the 50-paper verdicts and per-criterion calls. Look for behaviour consistent with the calibration outcome: on-topic complexity-in-consciousness papers passing all four criteria; off-topic papers failing on C1 or C3; theoretical-only papers failing on C3 or C4. No numerical target here — this is a sanity check, not a re-calibration.
- [ ] **No prompt edits made** based on the pilot: `[ confirm ]`. If any edit is applied, stop and open a change-control ticket per `protocol/elicit_screening_prompts.md`.
- [ ] Note any Elicit-side anomalies from the pilot: `_______________________________`.

### Full-run checklist

- [x] **Full run started** (Elicit-reported): 2026-09-10
- [x] **Full run completed** (Elicit-reported): 2026-09-10
- [x] No mid-run configuration changes.
- [ ] Any Elicit-side warnings, timeouts, or partial-batch messages captured here: `_______________________________`.

### Screening outcomes — both workflows (Elicit-reported, 2026-09-10)

| Workflow | Evaluated | Include | Exclude | Include rate | Export CSV (in this folder) | Rows × Cols |
|---|---:|---:|---:|---:|---|---|
| W1 (part 1) | 5,002 | 2,222 | 2,780 | 44.4% | `Elicit - screen-results-elicit_workflow_1_export_2026-09-10.csv` | 5,002 × 54 |
| W2 (part 2, clean re-upload) | 3,116 | 845 | 2,271 | 27.1% | `Elicit - screen-results-elicit_workflow_2_export_2026-09-10.csv` | 3,116 × 45 |
| **Combined** | **8,118** | **3,067** | **5,051** | **37.8%** | — | — |

Notes: W1 rows include ~426 prior-work library carry-over (calibration subsample, 16-paper trial, seed re-run) that will be filtered at reconciliation. W2's lower include rate is consistent with the second half of the Rayyan-deduplicated RIS being disproportionately IEEE conference records and older PubMed entries — to be verified at reconciliation via database-source × include-rate cross-tab.

### Workflow-1 screening outcome (Elicit-reported, 2026-09-10)

| Metric | Value | % of evaluated |
|---|---:|---:|
| Abstracts evaluated | 5,002 | 100.0% |
| Included | **2,222** | 44.4% |
| Excluded | **2,780** | 55.6% |
| In-UI report cap | 80 (display only — full CSV export contains all 5,002) | — |

**Include-rate observation (not a re-calibration).** Elicit's 44.4% include rate is substantially more permissive than the human tier's 14.2% (1,221 / 8,581) on the full corpus. This is *expected* under the calibrated deployment configuration and does not indicate configuration drift:

- Strict-criteria OFF (as pre-registered) — Elicit's aggregated verdict is score-based and permissive at the borderline. The calibration explicitly rejected strict-AND because it dropped recall of human-includes to 77.7% (below the 95% pre-registered floor); the trade-off is that as-deployed retains borderline papers as `Include`.
- On the calibration subsample (200 records, blind n = 194), **recall of human-includes was 98.1%** — Elicit was permissive but rarely missed a real Include. Substantive disagreements were 0.
- The role of the Elicit tier in this deployment is second-screener recall assurance, not selective agreement. High include rate + high recall is the intended profile.

Real assessment happens at reconciliation (§5 of this log), where per-record Elicit verdicts are joined to Rayyan human decisions.

## 3. Export (most granular result Elicit permits)

Save all four artefacts into this folder (``):

- [ ] `elicit_binary_verdicts_YYYY-MM-DD.csv` — Elicit's aggregated Include/Exclude verdict per record.
- [ ] `elicit_per_criterion_calls_YYYY-MM-DD.csv` — per-record yes/no/maybe on each of the four criteria.
- [ ] `elicit_per_criterion_rationales_YYYY-MM-DD.csv` — per-criterion rationale text and highlighted source quote (matches the calibration export shape).
- [ ] `elicit_no_abstract_omissions_YYYY-MM-DD.csv` — Elicit's own list of records it did not process (if provided). Cross-check against `elicit_unassessable_no_abstract_manifest.csv`.

If Elicit does not offer a single CSV with rationale + quote per criterion, combine what it does offer and note the schema mismatch here: `_______________________________`.

## 4. Unassessable-record documentation (not a new human-screening pass)

Human screening for the 2,632 no-abstract records is **already complete in Rayyan** (their `included` decisions are in `customizations_log.csv`, and the same values are copied into the `human_decision` column of `elicit_unassessable_no_abstract_manifest.csv`). The purpose of the manifest is *audit-trail documentation* — recording which records did not receive an Elicit second-screener decision, and why — not to trigger a second human pass.

Baseline human decisions on those 2,632 records (from the manifest): **180 Include · 33 Maybe · 2,419 Exclude**. If Elicit ingests fewer or more of these, note the delta here after the run: `_______________________________`.

## 5. Reconciliation plan (deferred until Elicit run is complete)

To run *after* the export is in place, not during Elicit's pass:

1. Join Elicit's per-record verdict to the Rayyan `included` decision on `article_id` / DOI / title (in that order of preference — the calibration join script in `code/` handles the fallback chain).
2. Compute production-run headline metrics on the assessable subset (records Elicit actually processed):
   - Cohen's κ (binary, as-deployed).
   - Raw agreement.
   - Recall of human-Includes.
   - Substantive-disagreement count and classification (aggregation drift vs criterion drift vs true difference).
3. Report on the *un*assessable subset (records Elicit could not process): the human `included` distribution, no Elicit-side numbers.
4. Empirical-seeds gate: verify the 8/8 empirical seeds are `Include` under the production Elicit verdict (same pass criterion as the calibration).
5. Compare production metrics to the pre-registered calibration commit thresholds (recall ≥ 95%; κ ≥ 0.60; 8/8 seeds) documented in `calibration/calibration_test_plan.md`. Production is not gated on these — they were the calibration commit thresholds — but a substantial drop should be diagnosed and recorded.
6. Reconciliation output: `elicit_vs_human_production_YYYY-MM-DD.csv` + `elicit_vs_human_production_report.md` in this folder.

## 6. Deviations / notes

Free-text log for anything discovered during the run that isn't captured above (Elicit UI behaviour, unexpected error text, subset re-runs, etc.):

- …

## 7f. Phase 1 closure — adjudication complete and Rayyan updated (2026-09-11)

**Title/abstract-tier adjudication and reconciliation complete.** Rayyan updated to reflect 32 disagreement adjudications.

| Metric | Value |
|---|---:|
| Adjudicated disagreements | 32 |
| — Adjudicated to Include (upheld) | 14 |
| — Adjudicated to Exclude (Elicit was correct) | 25 |
| Original human-Include (frozen 2026-09-08) | 1,219 |
| Final Include (after Rayyan update 2026-09-11) | **1,196** |
| Human-Maybe (unchanged) | 117 |
| **Total records ready for full-text screening** | **1,313** |

Rayyan manually updated 2026-09-11 to flip the 25 adjudicated-to-Exclude records. Adjudication rationales documented in `disagreements_for_adjudication_2026-09-10.csv` (39 rows). Empirical-seed exclusion rationale documented in `admin/seed_exclusion_review_2026-09-10.md`.

## 7g. Post-closure correction — shared Rayyan IDs, duplicate pairs, and the full-text set (2026-10-05)

> *Note (2026-11-10): the full-text figures in this section (530 / 783) are superseded by §7n–§7o (529 / 784) after the retest adjudication. Kept as the record of what was true on the date written.*

**Trigger.** During full-text screening (concluded 2026-10-05), the frozen full-text input `final_full_text_screening_set_2026-09-10.csv` held 1,311 rows, while Rayyan held 1,313 records. Rayyan was correct; the CSV was not.

**Cause.** Seven pairs of duplicate records share a DOI and, in the Elicit split manifest, share a Rayyan article ID (8,581 manifest rows, 8,574 unique IDs). `reconcile_elicit_vs_human_production.py` keys rows by `rayyan_article_id`, so each pair collapsed to one row. Two records (570549920 Gallez; 570554409 Lambooij) were therefore missing from the 1,311-row CSV.

**Effect on figures.** Original human-Include is 1,221 (not 1,219 as in §7f); 1,196 after the adjudication flips; 39 adjudications (not 32). Elicit-vs-human metrics were computed on 8,574 unique IDs. The pair-level detail is in the `flag` / `flag_note` columns of `final_full_text_screening_set_v2_2026-10-05.csv`.

**Supersession.** `final_full_text_screening_set_2026-09-10.csv` is superseded by `final_full_text_screening_set_v2_2026-10-05.csv` (1,313 rows). The old file is frozen and left untouched.

**Resolutions (2026-10-05).**
- Gallez (570549920, 570552482): both Include at title/abstract; resolved to Exclude. Characterises chaotic dynamics in EEG with nonlinear dynamical-systems methods; not an investigation of consciousness-complexity relationships. 570552482 is recorded as the duplicate.
- Lambooij (570554409): resolved to Exclude. Outside consciousness-mechanism scope; evaluates an animal stunning method for welfare and meat quality, using EEG and an approved metric (correlation dimension) for a practical welfare purpose.
- Final full-text input: 1,313 records in Rayyan; 1,310 distinct records after these three resolutions (1,193 Include + 117 Maybe).

**Full-text outcome (Rayyan updated 2026-10-05/06).** 1,313 records screened: **530 included, 783 excluded** (0 undecided, 0 maybe). These counts are provisional: sample checks on the includes (and the §B7 retest) are still to come, and any resulting flips will be logged in a dated follow-up note. Three records were reviewed against the full text or abstract on 2026-10-06 and changed or confirmed: 570552580 (Wada test) flipped to Include; 570550007 and 570560429 confirmed Exclude with corrected notes.

Exclusion reasons (one primary category per record, assigned by the lead author's reading of the Rayyan notes):

| Category | n |
|---|---:|
| Tool/monitor/classifier/clinical-application aim, not a consciousness investigation | 407 |
| Not a mechanistic consciousness investigation (no operational consciousness measure, state characterization, or other topic) | 261 |
| Non-approved or no complexity metric | 72 |
| Review, thesis, book, retracted or other non-primary publication | 34 |
| Non-approved neural data modality | 6 |
| Not in English | 2 |
| Duplicate | 1 |
| **Total excluded** | **783** |

Decisions and notes: `full_text_screening_decisions_2026-10-05.csv` (columns `exclusion_category` = reviewer's own note; `exclusion_category_short` = category above). Authoritative export: `rayyan_full_text_screening_all_decisions_2026-10-05_articles.csv` and `_customizations_log.csv`.

**Pending.** Intra-rater test-retest on a 10% sample (§B7; ≥1 month after screening, earliest ~2026-11-05; κ ≥ 0.8). Methodology-only seeds (§B9b: Tononi 1994, Oizumi 2014, Chis-Ciure 2024) to be added after full-text screening is verified. PRISMA flow diagram to be updated with the numbers above.

## 7h. Full-text test-retest sample drawn (2026-10-07)

> *Note (2026-11-10): the full-text figures in this section (530 / 783) are superseded by §7n–§7o (529 / 784) after the retest adjudication. Kept as the record of what was true on the date written.*

**Why.** Protocol v0.5.1 §B7 specifies a 10 % random within-person re-screen (κ ≥ 0.8) for the calibration set and extraction/appraisal, plus a 1 % periodic check during bulk title/abstract screening, but gives no sampling plan for the full-text tier. A plan was therefore defined here and is recorded as an operational detail (no protocol change). A search of `protocol/`, `admin/`, `calibration/` and `code/` found no existing full-text sampling plan.

**Design.** 10 % of all 1,313 full-text decisions, proportionally stratified by original decision (53 of 530 Include; 78 of 783 Exclude; n = 131). Stratification guarantees both classes are present (κ computable) and that about 10 % of the includes are re-checked. Seeded draw (seed 20261007) with `code/full_text_retest_sample.py`; re-running reproduces the identical sample.

**Files.** `screening/full_text_retest_BLIND_rescreen_2026-10-07.csv` (blind: ID, DOI, title, year, journal, empty `retest_decision` / `retest_reason` / `retest_date` columns); `screening/full_text_retest_KEY_original_decisions_2026-10-07.csv` (original decisions; not to be opened before re-screening).

**Procedure.** Re-screen the 131 records blind from the full text against §B4, no earlier than 2026-11-05 (≥ 1 month after screening concluded 2026-10-05). Compute Cohen's κ (target ≥ 0.8) and list disagreements. Every disagreement is resolved by re-reading the source; flips update the Rayyan decision, `full_text_screening_decisions_2026-10-05.csv`, and the counts, and are logged in a dated note here. The 530 / 783 figures remain provisional until then. If κ < 0.8, the rubric is reviewed and the screening of the affected category is re-checked.

**Note.** Any additional informal checks of the includes before 2026-11-05 are outside this sample and are logged separately as spot checks, not as the §B7 retest.

## 7i. Papers to be added after screening (2026-10-07)

> *Note (2026-11-10): the additions listed here were later completed and entered; see §7p (Starkey replaced by Muñoz), §7q (final included set) and §7r. Counts here are superseded by §7n-§7o.*

Records added outside the screening pipeline are tracked in `screening/post_screening_additions_2026-10-07.csv` and reported separately in the PRISMA flow diagram (not mixed into the 1,313 → 530 / 783 counts). Current list: Carhart-Harris 2014 and Luppi 2022 (foundational papers, agreed by the supervisors after the screening exclusions; see addendum in `admin/seed_exclusion_review_2026-09-10.md`); the three §B9b methodology-only seeds; two further papers proposed by Adam after the test-retest sample was drawn (details to be entered). None of these is in the 131-record retest sample. Adding the two foundational papers is a deviation from §B4 as written and should be recorded in the amendments log and Methods.

## 7j. Title/abstract test-retest sample received (2026-10-07)

An 86-record sample of the title/abstract tier (about 1 % of the 8,581 screened records) was supplied by the lead reviewer as a Rayyan RIS export (`articles.ris`, 86 unique IDs). Original decisions in the export: 76 Excluded, 8 Included, 2 Maybe. Ten of the 86 are also in the 1,313 full-text set; none is in the 131-record full-text retest sample (§7h). 53 of the 86 have an abstract in the export; the other 33 were screened on title and metadata only.

The sample was drawn by random sampling in Covidence (per the lead reviewer, 2026-10-07); Covidence does not expose a seed, so the draw is documented by the resulting list of 86 IDs (the key file) rather than by a reproducible seed. Covidence was used only for drawing the sample, not for screening. For the blind re-screen, `screening/title_abstract_retest_BLIND_rescreen_2026-10-07.csv` lists the 86 records in shuffled order without the original decisions, with empty `retest_decision`, `retest_reason` and `retest_date` columns; `screening/title_abstract_retest_KEY_original_decisions_2026-10-07.csv` holds the original decisions (not to be opened before re-screening). Because the sample is dominated by Excludes (76 of 86), κ will be sensitive to a few disagreements, so raw agreement and the disagreeing records are reported alongside κ. Disagreements are resolved by re-reading the record; flips update Rayyan and are logged here. This sample is separate from the earlier periodic 1 % checks (§B7 step 4), which were performed before full-text screening without a saved record.

The Rayyan export of the 86-record sample is archived as `screening/rayyan_title_abstract_retest_sample_2026-10-07_articles.ris` and `..._customizations_log.csv`. Note: this export contains the original decisions, so it is not to be used for the blind re-screen.

### 7k. Checklist 1.3 - spot-check of the unexplained coverage-gap records (2026-10-07)

- **Population.** Records with no Elicit verdict and not in `elicit_unassessable_no_abstract_manifest.csv`: **1,027** in `elicit_vs_human_production_2026-09-10.csv` (811 human-Exclude, 195 human-Include, 21 human-Maybe). The 1,034 in the checklist and the 1,027 in the production report were earlier tallies; 1,027 is the figure recomputed from the reconciliation file. All 195 Include and 21 Maybe records went to full text, so the gap only means the 811 human-Excludes had no AI second screen.
- **Sample.** 20 records, random (seed 20261007, IDs sorted before shuffling; first 20 drawn).
- **Pattern check.** The "workspace-library dedup casualty" hypothesis is **not supported**: all 1,027 records have an abstract in the RIS, only 1 has a twin with an Elicit verdict (matched by title/DOI), and 1,019 sit in part 1. The cause of the missing verdicts remains unexplained (Elicit returned no verdict for records that had abstracts).
- **Human decisions in the sample.** The 13 human-Exclude sample records were read against their abstracts where borderline: 12 are clearly out of scope (BCI/seizure/sleep-staging classifiers, connectivity-only, a systematic review, a null-model method paper). **One borderline record, 570554060** (algorithmic-information/complexity quantification of neurophysiological recordings across sleep, task and action), was excluded at title/abstract and might meet the criteria at full text; flagged for the reviewer to decide. No re-screening of the gap was done, in line with the checklist.
- **Decision (2026-10-07, lead reviewer):** 570554060 stays excluded. No change to the screening set.

- **File renaming (2026-11-10).** To avoid confusing the blind files with the original decisions, the four retest CSVs were renamed (contents unchanged): `*_retest_BLIND_rescreen_2026-10-07.csv` (to screen from) and `*_retest_KEY_original_decisions_2026-10-07.csv` (original decisions; do not open before re-screening), for both the title/abstract and full-text samples. References in the checklist, protocol, run log and `code/full_text_retest_sample.py` were updated.

## 7l. Title/abstract re-screen sample: results (2026-11-10)

**Design.** 86 records (about 1% of 8,581), drawn at random in Covidence, re-screened blind by the lead reviewer in `title_abstract_retest_BLIND_rescreen_2026-10-07.csv` (file saved 2026-11-10; original decisions held in the KEY file). Intra-rater test-retest, about 5 weeks after the original screening. Scored by joining on `rayyan_article_id`; all 86 IDs matched.

| Measure | Value |
|---|---:|
| Raw agreement, three categories (Include / Maybe / Exclude) | 83/86 = **96.5%** |
| Cohen's κ, three categories | **0.836** |
| Raw agreement and κ, binary with Maybe counted as Include (the §B7 / calibration collapse) | 100% / **1.00** |
| Raw agreement and κ, binary with Maybe counted as Exclude (sensitivity) | 96.5% / 0.751 |

**Cross-tab (original -> retest).** Exclude -> Exclude 76; Include -> Include 5; Maybe -> Maybe 2; Include -> Maybe 3; no record moved to or from Exclude.

**Disagreements (all Include -> Maybe).** 570551323 (sleep-arousal PNN-GBMO classifier; possible consciousness context), 570558695 (brain-state classification with sparse PDC features; approved metrics inside a hybrid pipeline), 570562950 (depth of anaesthesia with Higuchi fractal dimension). All three are the classifier/monitoring grey-zone type and all three go to full text either way (Include and Maybe both do).

**Interpretation.** No Exclude was reversed, so the exclusion decisions behind the 7,268 records not sent to full text were stable in this sample (0 of 76 changed); with 76 Exclude records, the sample cannot rule out a low rate of unstable excludes. The only drift was Include -> Maybe on grey-zone records. κ at the collapse used for screening is 1.00 (target >= 0.8); three-way κ 0.836 also meets the target. No change to the screening set follows from this check.

## 7m. Full-text re-screen sample: results (2026-11-10)

**Design.** 131 records (10% per class, seeded script `code/full_text_retest_sample.py`, seed 20261007), re-screened blind by the lead reviewer in `full_text_retest_BLIND_rescreen_2026-10-07.csv` (saved 2026-11-10; see timing note) against the KEY file. All 131 IDs matched.

*Note on timing:* the original screening was concluded 2026-10-05 and the sample was drawn 2026-10-07, so the re-screen took place 36 days after the end of the original screening, which meets the >= 1 month rule in §B7.

| Measure | Value |
|---|---:|
| Raw agreement, three categories | 126/131 = **96.2%** |
| Cohen's κ, three categories | **0.922** |
| Raw agreement / κ, Maybe counted as Include | 97.7% / **0.952** |
| Raw agreement / κ, Maybe counted as Exclude | 96.2% / 0.920 |

Target (§B7): κ >= 0.8. **Met** under every collapse.

**Cross-tab (original -> retest).** Exclude -> Exclude 77; Include -> Include 49; Include -> Exclude 2; Include -> Maybe 2; Exclude -> Include 1.

**Disagreements (5), for the reviewer to adjudicate (no change made to the screening set yet).**
| ID | Original -> retest | Paper (short) | Retest reason / note |
|---|---|---|---|
| 570549751 | Include -> Exclude | Self and prolonged intrinsic neural timescale in schizophrenia | No consciousness claims; timescale relates to self-disorder rather than an operational consciousness measure |
| 570551510 | Include -> Exclude | Nasal air puff, DMN activity in comatose patients | Complexity and connectivity changes without independently demonstrating increased consciousness |
| 570551020 | Include -> Maybe | Sleep stage scoring with multiscale permutation entropy | Automatic sleep classification study |
| 570561796 | Include -> Maybe | Depth-of-anaesthesia indexes vs MAC | Uses MAC as reference; no behavioural responsiveness assessed |
| 570552845 | Exclude -> Include | Measures of entropy and complexity in altered states of consciousness | (no reason given) Original note says it tests whether permutation entropy and PLZC differentiate conscious from unconscious states, which reads as meeting the criteria; the original Exclude may be the error |

**Pattern.** Four of five differences are on classifier/monitoring or "does it demonstrate a consciousness claim" grey-zone records (§B4 grey zone); one is a likely original Exclude error. Net effect if all five retest decisions were adopted: Included 530 -> 527 (or 529 counting the two Include -> Maybe as Include).

**Status.** Retest passes. The 530/783 counts remain provisional until the five disagreements are adjudicated and the pending additions are added.

## 7n. Adjudication of the five full-text retest disagreements (2026-11-10)

The lead reviewer re-read the five records and kept the **retest decision** in each case. `full_text_screening_decisions_2026-10-05.csv` was updated (backup of the pre-change file not kept in the project; each change is recorded in the row's `screening_stage_note`).

| ID | Decision change |
|---|---|
| 570549751 | Include -> Exclude (category O) |
| 570551510 | Include -> Exclude (category O) |
| 570552845 | Exclude -> Include |
| 570551020 | Include -> **Maybe** |
| 570561796 | Include -> **Maybe** |

**Updated full-text counts (provisional until the two Maybe records are resolved and additions are added):** Include **527**, Exclude **784**, Maybe **2** (total 1,313). Exclusion categories: T 407, O 262, C 72, R 34, M 6, L 2, D 1 (= 784).

**Open:** a full-text outcome of Maybe is not a final state. The two Maybe records (570551020, 570561796) need a final Include/Exclude call (or a stated rule, e.g. grey-zone supervisor decision per §B4) before extraction. Rayyan must be updated by the reviewer to match.

## 7o. Resolution of the two full-text Maybe records (2026-11-10)

The lead reviewer judged 570551020 and 570561796 as **Include**. Final full-text outcome after the retest: **529 Include, 784 Exclude, 0 Maybe** (total 1,313). Net change from the 2026-10-05 figures (530 / 783): 2 Include -> Exclude, 1 Exclude -> Include (§7n). Still provisional only in the sense that the seven additions are reported separately and Rayyan must be kept in sync.

## 7p. Replacement of one of Adam's proposed additions (2026-11-10)

The lead reviewer replaced the proposed addition Starkey et al. 2023 (bioRxiv preprint, "Statistical diversity distinguishes global states of consciousness") with **Muñoz et al. 2020**, "General anesthesia reduces complexity and temporal asymmetry of the informational structures derived from neural recordings in Drosophila", Phys. Rev. Research 2, 023219, DOI 10.1103/PhysRevResearch.2.023219 (peer-reviewed; Drosophila LFP, statistical complexity, general anaesthesia). Not in the 8,581 screened records (checked by DOI/title). Register `post_screening_additions_2026-10-07.csv` updated; Starkey is not included.

## 7q. Rayyan sync and final included set (2026-11-10)

**Rayyan.** The lead reviewer confirmed Rayyan matches the retest adjudications: 570549751 and 570551510 Exclude; 570552845, 570551020 and 570561796 Include. Rayyan, `full_text_screening_decisions_2026-10-05.csv` (529 Include / 784 Exclude) and this log now agree.

**Additions.** Seven papers cannot be added to existing Rayyan records, so they were added outside Rayyan, by DOI, to the new file `screening/final_included_set_with_additions_2026-11-10.csv` (536 rows: 529 from screening + 7 additions, with a `source` column). The decisions CSV was deliberately left at 1,313 rows so that it keeps matching Rayyan. The seven: Carhart-Harris 2014 and Luppi 2022 (foundational-paper exception); Tononi-Sporns-Edelman 1994, Oizumi 2014 and Chis-Ciure 2024 (§B9b methodology-only seeds, DOIs from the protocol table; the Chis-Ciure DOI was confirmed against PubMed, PMID 38615851, by the lead reviewer on 2026-11-10); Mediano 2023 (eLife reviewed preprint, DOI 10.7554/eLife.88683.1) and Muñoz 2020 (replacing Starkey 2023). Register updated.

**IEEE count.** The IEEE Xplore total (1,209) was verified against `search/search_execution/IEEE/search_log.md`.

## 7r. Final PRISMA counts, frozen included set and extraction pilot sample (2026-11-10)

- **PRISMA.** Final counts and diagram written: `screening/prisma_flow_counts_FINAL_2026-11-10.md`, `prisma_flow_diagram_2026-11-10.png/.svg`. The 2026-10-07 DRAFT file is marked superseded.
- **Frozen included set.** `screening/final_included_set_with_additions_2026-11-10.csv` (536 records: 529 from screening + 7 additions) is frozen as the input to extraction: made read-only, SHA-256 hashes in `screening/FROZEN_included_set_2026-11-10.sha256` (also covers `full_text_screening_decisions_2026-10-05.csv`). Any later change needs a logged reason and a new dated file. Checks: 536 unique record IDs, no duplicate DOIs, 3 records without a DOI.
- **Extraction pilot sample (§B8).** 10 papers drawn by `code/extraction_pilot_sample.py`: simple random sample, seed 20261110, from the 529 screened-in records (the seven additions excluded), IDs sorted before sampling; reproducibility verified. Output: `extraction/pilot_sample_2026-11-10.csv`. The same 10 papers are used to pilot the §B10 appraisal checklist.


## 7s. Protocol v0.5.2 consistency audit (2026-11-10)

`protocol/prisma_protocol_v0.5.2.md` was checked for stale statements and updated: version date (now 2026-11-10); milestone status; §B6.2 search execution (now past tense with the total); §B7 steps 4 and 6 (retests done); §B8 (pilot sample drawn); §B11 citation-network count (529 + 7 = 536); amendments log (final 529 / 784 counts, retest results, additions added, frozen set, extraction pilot sample). `README.md` status table updated (protocol version, screening status, next phase). §7g and §7h of this log carry a pointer to the superseding §7n-§7o. Collaborator names (header, §B1, §B4-4/§C4, expert-elicitation line, amendment entries) were made generic in v0.5.2 on the lead reviewer's instruction 2026-11-10: collaborators are named only after substantial contribution. The registered v0.5.1 in `protocol/archive/` is unchanged. README, data management plan and `github_zenodo_setup.md` were aligned.

## 7t. Correction of who reviewed the seeds (2026-11-10)

The lead reviewer clarified that only the supervisors (Jurgen Jost, Lucia Melloni, Andrej Bicanski) reviewed the seed exclusions and agreed to add the two foundational papers; the collaborators did not. `admin/seed_exclusion_review_2026-09-10.md` (reviewer line, addendum, and the clarification paragraph, now removed as no collaborators are named), protocol v0.5.2 (foundational-paper bullet), the additions register and §7 references were corrected. A note-only wording change was also made to two rows of the frozen `final_included_set_with_additions_2026-11-10.csv` (records unchanged; hashes in `FROZEN_included_set_2026-11-10.sha256` regenerated).

## 7u. Pre-push sweep (2026-11-10)

Whole-folder check for stale statements before the GitHub push. Fixed: `admin/next_phase_checklist_2026-09-10.md` header (last-updated line); `protocol/prisma_checklist_mapping.md` (ASReview wording in item 9, PRISMA item 14 now complete, Zenodo note now points to the v0.5.2 release); `search/corpus_construction/log.md` ("Next step (Phase 2)" given a status note); README protocol-line date; pointer note added to run log §7i. Deliberately left as dated historical records (not edited): `admin/rayyan_reevaluation.md`, `admin/embase_removal_audit_2026-06.md`, `admin/github_zenodo_setup.md`, `calibration/*.md`, `search/pilot_search_notes.md`, earlier run log sections. No occurrence of the removed name anywhere in our own files. `.gitignore` excludes `.venv/`, PDFs and scratch folders. **Before the release:** `CITATION.cff` still says version 0.5.1 (date-released 2026-06-09) and must be changed to 0.5.2 with the release date at release time; the v0.5.2 Zenodo DOI must be added to §B6.3 afterwards.


## 7v. Post-retest Rayyan full-text export (2026-11-10)

The lead reviewer exported the full-text Rayyan project after the retest adjudications; the folder (originally named `2026-11-10_20-26-31`) was renamed `screening/rayyan_full_text_screening_all_decisions_2026-11-10/` (`articles.csv`, `customizations_log.csv`). Check against `full_text_screening_decisions_2026-10-05.csv`: 1,313 records in each, identical ID sets, **0 decision mismatches**; Rayyan counts 529 Included / 784 Excluded / 0 Maybe. This export is now the authoritative Rayyan record of the final full-text decisions. The earlier export `rayyan_full_text_screening_all_decisions_2026-10-05_articles.csv` and `_customizations_log.csv` (530 / 783) is kept unchanged as the record of the pre-retest state.

## 7w. Flattening of `screening/` (2026-11-10)

All files that sat in subfolders of `screening/` were moved to the folder root (contents unchanged: SHA-256 of the 39 real files matches before and after). Files with generic names were prefixed with their former folder to avoid clashes (e.g. `rayyan_full_text_screening_all_decisions_2026-11-10_articles.csv`, `elicit_input_part_1_of_2_2026-09-10.ris`, `rayyan_title_abstract_include_maybe_2026-09-11.ris`). This log was moved from `elicit_deployment_2026-09-10/run_log.md` to **`screening/screening_run_log.md`**; its earlier sections are otherwise unchanged and may name the old folders. Empty folders and `.DS_Store` files were put in `screening/to_be_deleted/` for the lead reviewer to review and delete. Path references were updated in the protocol, checklist, calibration results, PRISMA counts file, Elicit prompt audit and `code/reconcile_elicit_vs_human_production.py` (which now reads from `screening/`; it compiles, but was not re-run).

