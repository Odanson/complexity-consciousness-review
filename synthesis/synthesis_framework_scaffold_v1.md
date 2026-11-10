# Synthesis framework — scaffold (v1)

**Companion to:** `protocol/prisma_protocol_v0.5.1.md` §B2 (review questions PQ1–PQ7), §B10 (critical appraisal), §B11 (synthesis plan), §B12 (eight-axis taxonomy)
**Version:** 1 · 2026-09-10 · Samson Odan
**Status:** *Scaffold only.* All tables, figures, and narrative slots are empty — they will be populated after extraction completes. This document exists so the extraction form (`extraction/pq1_measure_extraction_form_v1.xlsx`) and the eventual synthesis manuscript are structurally aligned before any data are entered.

---

## 1. Design principle

The synthesis has **two levels** and one **cross-cutting register**:

1. **Level 1 — descriptive map (PQ1).** For every measure in the corpus: name, mathematical primitive, data requirement, spatial/temporal scale, theory anchoring, inferential status, validation evidence. This is a structured enumeration and is where the four §B11 summary tables live.
2. **Level 2 — warrant analysis (PQ2–PQ3, PQ5–PQ7).** For each measure–claim pairing: is the consciousness claim commensurate with what the measure computes and with the study's design? This is where the §B10 appraisal checklist and the §B11 misapplication register do their work.
3. **Cross-cutting register — gaps (PQ4).** Aspects of consciousness for which no fit-for-purpose measure exists. Fed by the coverage heatmap in §5 below.

Every synthesis component below is tagged with the axis (§B12), the PQ (§B2), and the §B11 artefact it fills. Nothing is invented outside those anchors.

---

## 2. Manuscript-level section outline

| Section | Purpose | Backing |
|---|---|---|
| **Introduction** | Problem: "complexity" is a load-bearing term with heterogeneous mathematical content (§A1). | §A1 · §A2 |
| **Methods** | PRISMA-ScR reporting; corpus, screening, extraction, appraisal. | §B1–§B10 |
| **Results — Level 1 (descriptive map)** | The four §B11 summary tables + coverage heatmap. | §B11 (i)–(iv) + heatmap |
| **Results — Level 2 (warrant analysis)** | §B10 appraisal summary + misapplication register + PQ5/PQ6/PQ7 sub-analyses. | §B10 · §B11 (misapplication register) · PQ5–PQ7 |
| **Results — gaps (PQ4)** | Under-addressed aspects (structural geometry; temporal phenomenology). | PQ4 |
| **Results — citation-network analysis** | Within-corpus citation graph; parallel-independent vs sequential-variation lines. | §B11 (added v0.4.2) |
| **Discussion** | Implications for measure choice; measure–theory pairings; open methodological problems. | PQ2–PQ7 |
| **Appendix — decision-support guide** | "If your question is X, these measures are plausibly warranted; these are not, because…" | §B11 decision-support appendix |

---

## 3. Four registered summary tables (§B11 (i)–(iv))

Each table below has its header row fixed by the extraction form (`pq1_measure_extraction_form_v1.xlsx`). Row-level population happens after extraction. Empty placeholder CSVs are pre-created in this folder so the fill-in step is a straight append, not a schema decision.

### Table 1 — measure × mathematical primitive (§B11 (i); axis §B12 Axis 1)

Purpose: for every distinct measure in the corpus, record its mathematical primitive family and the papers reporting it.

Columns: `measure_name`, `measure_family_axis1`, `n_papers`, `representative_citations`, `notes_on_variants`.
Placeholder file: `table_1_measure_x_primitive.csv`.

### Table 2 — measure × data requirement (§B11 (ii); axis §B12 Axis 2)

Purpose: which measures need which kind of data (amplitude only vs amplitude+connectivity vs phase-based vs perturbation vs multi-scale). Directly informs the decision-support appendix.

Columns: `measure_name`, `data_requirement_axis2`, `modalities_used`, `n_papers`, `notes`.
Placeholder file: `table_2_measure_x_data_requirement.csv`.

### Table 3 — measure × consciousness aspect claimed (§B11 (iii); axis §B12 Axis 4)

Purpose: which aspect of consciousness (level, content, integration, differentiation, structure, temporal flow) each measure has been used to claim. This is the direct evidence base for PQ2.

Columns: `measure_name`, `aspect_of_consciousness_axis4`, `claim_direction`, `n_papers`, `representative_citations`, `notes`.
Placeholder file: `table_3_measure_x_aspect.csv`.

### Table 4 — measure × validation evidence (§B11 (iv); axis §B12 Axis 8)

Purpose: for every measure, the strongest validation evidence in the corpus (behavioural report / clinical diagnosis / pharmacological manipulation / cross-measure agreement only / none). Feeds appraisal item 3.

Columns: `measure_name`, `validation_type_axis8`, `strongest_ground_truth`, `strongest_effect`, `n_papers_validated`, `n_papers_no_external_criterion`, `notes`.
Placeholder file: `table_4_measure_x_validation.csv`.

---

## 4. Cross-cutting descriptive tables (support tables — not §B11 registered, but expected in the manuscript)

Two additional tables the extraction schema supports, listed here so they are not surprises at write-up time:

- **Table S1 — measure × spatial scale (§B12 Axis 5).** Which measures have been deployed at which spatial scale.
- **Table S2 — measure × theory anchoring (§B12 Axis 6).** Direct input to PQ5.

Placeholder files: `table_s1_measure_x_spatial_scale.csv`, `table_s2_measure_x_theory.csv`.

---

## 5. Coverage heatmap (§B11 — "measure × consciousness-state coverage to identify gaps")

Axes: measures (rows) × consciousness states (columns; from the `state_contrast` extraction field, mapped to the §B3 comparator list — awake vs sleep / NREM / REM / anaesthesia / DOC / psychedelic / meditation / coma / LIS). Cell values: paper counts.

**Empty cells are the finding.** A measure × state cell with zero papers is a candidate PQ4 gap.

Deliverable slot: `figures/coverage_heatmap.png` (generated post-extraction from the four summary tables + the `state_contrast` column).

---

## 6. §B10 critical-appraisal summary (feeds Level 2)

Six-item checklist, three levels per item (`low concern` / `some concern` / `high concern`):

1. Measure specification (formula, parameters, surrogate)
2. Data suitability (channels, record length, stationarity)
3. Validation (external criterion, cross-validation)
4. Confound control (SNR, drug × state, artefacts)
5. Reproducibility (code, data, params)
6. Interpretation–warrant fit (claim vs mathematical content)

Deliverable slot: `table_5_critical_appraisal_summary.csv` — one row per (paper, measure), six item columns + narrative notes. Items 1, 5, 6 also flag rows for the misapplication register (§7 below).

---

## 7. Misapplication register (§B11)

Structured list of *recurring* misuses, each with representative citations. Rows are misapplication *patterns*, not individual papers. Extraction column `reviewer_flagged_misapplication` feeds this directly; §B10 items 1/5/6 also feed it.

Columns: `pattern_id`, `pattern_description`, `example_measures`, `mechanism_of_misapplication`, `representative_citations`, `severity` (low/medium/high — how far the claim outruns the measure), `frequency_in_corpus` (n papers exhibiting the pattern), `related_PQ`.

Deliverable slot: `misapplication_register.csv`.

Candidate seed patterns (to be validated against the corpus, *not* asserted a priori):

- P1: Directional inference from correlational measures (e.g., LZc, sample entropy interpreted as causal about integration).
- P2: Effective-connectivity claims from amplitude-only metrics.
- P3: LZc / signal diversity interpreted as Kolmogorov algorithmic complexity (the Mediano et al. 2023 caveat).
- P4: Scalar entropy read as multidimensional phenomenological richness without a phenomenological instrument (the Moses et al. 2026 caveat).
- P5: Descriptively-derived measures interpreted post-hoc as evidence for a specific theory (PQ7 pattern).
- P6: Non-hallucinogenic active-control absent when claiming psychedelic-specific entropy elevation (Moses et al. 2026 recommendation).

## 8. PQ5–PQ7 sub-analyses (Level 2)

### PQ5 — theory provenance

For each measure, code as (a) canonical operationalisation of a theory, (b) one of several non-equivalent proxies, or (c) theory-agnostic in origin. Sourced from `theory_anchoring_axis6`.

Deliverable slot: `pq5_theory_provenance.csv` (columns: `measure_name`, `provenance_class`, `parent_theory`, `alternative_proxies`, `notes`).

### PQ6 — within-theory operationalisation drift

For theories with multiple empirical proxies (IIT: φ / φ* / geometric φ / whole-minus-sum / φ-ID; GNW: ignition / global-broadcast / late-P3 surrogates; predictive processing: entropy-rate variants), tabulate proxy-vs-proxy convergence when reported on the same data and the same state ordering.

Deliverable slot: `pq6_proxy_convergence.csv` (columns: `theory`, `proxy_a`, `proxy_b`, `dataset_or_paradigm`, `agreement_direction`, `agreement_metric`, `citation`).

### PQ7 — post-hoc theoretical re-interpretation

Sub-set of the misapplication register (pattern P5), tabulated separately because it is a PQ in its own right.

Deliverable slot: `pq7_posthoc_reinterpretation.csv` (columns: `measure_name`, `origin` (descriptive / theory-derived), `theory_reinterpreted_as`, `justification_stated_in_paper`, `citation`, `appraiser_assessment`).

## 9. Citation-network analysis (§B11, added v0.4.2)

Within-corpus citation graph. Nodes: included papers. Edges: within-corpus citations extracted via Citationchaser (source: `code/citation_network/`).

Analysis: cluster into families (parallel independent lines vs sequential variations on the same seed), report densities, identify the seed papers each cluster descends from.

Deliverable slots:

- `citation_network_edges.csv` (columns: `citing_paper`, `cited_paper`, `year_citing`, `year_cited`, `cluster_id`).
- `figures/citation_network.png` — network figure.
- `citation_network_narrative.md` — 1–2 pages of narrative + cluster interpretation.

## 10. Decision-support appendix (§B11)

The synthesis's user-facing product. Format: for each `aspect_of_consciousness_axis4` value + each `state_contrast` cluster, a short recommendation of the form:

> **If you want to make a claim about {aspect} in {state paradigm}:**
> plausibly warranted measures: {…} — because {mathematical + validation reason} · corpus evidence: {n papers}
> not warranted: {…} — because {measure–claim mismatch reason} · corpus evidence: {n papers}
> insufficient evidence to judge: {…}

Deliverable slot: `decision_support_appendix.md`. Table-of-contents entries populate from the coverage heatmap; recommendations populate from the misapplication register plus the critical-appraisal summary.

## 11. PQ4 — gaps section

Cross-reference from the coverage heatmap: which (measure family × consciousness aspect) cells are empty, and which aspects (structural geometry of experience; subjective temporal flow) have thin measure coverage. Fed straight into the thesis's Q1/Q2/Q3 framing.

Deliverable slot: `pq4_gaps.md` — short narrative + a `gaps_table.csv` enumerating the empty cells.

## 12. No formal meta-analysis (§B11)

Heterogeneity is too high across the corpus for a pooled effect-size analysis. If a sub-family (e.g., LZc in DOC) has enough comparable studies at extraction, a mini meta-analysis may be added as a supplementary appendix; scope decision recorded here rather than assumed.

## 13. Deliverable inventory (post-extraction, all files in this folder)

| File | Purpose | Source data |
|---|---|---|
| `table_1_measure_x_primitive.csv` | §B11 (i) | Extraction form (§B12 Axis 1) |
| `table_2_measure_x_data_requirement.csv` | §B11 (ii) | Extraction form (Axis 2) |
| `table_3_measure_x_aspect.csv` | §B11 (iii) | Extraction form (Axis 4) |
| `table_4_measure_x_validation.csv` | §B11 (iv) | Extraction form (Axis 8) |
| `table_5_critical_appraisal_summary.csv` | §B10 | Appraisal checklist rows |
| `table_s1_measure_x_spatial_scale.csv` | Support | Extraction (Axis 5) |
| `table_s2_measure_x_theory.csv` | Support | Extraction (Axis 6) |
| `figures/coverage_heatmap.png` | §B11 gaps identification | Tables 1–4 + state_contrast |
| `misapplication_register.csv` | §B11 | Extraction + Appraisal items 1/5/6 |
| `pq5_theory_provenance.csv` | PQ5 | Extraction (Axis 6) |
| `pq6_proxy_convergence.csv` | PQ6 | Extraction + narrative pass |
| `pq7_posthoc_reinterpretation.csv` | PQ7 | Extraction (Axis 6 = c) |
| `citation_network_edges.csv` + `figures/citation_network.png` + `citation_network_narrative.md` | §B11 citation-network analysis | Citationchaser exports |
| `decision_support_appendix.md` | §B11 decision-support | All of the above |
| `pq4_gaps.md` + `gaps_table.csv` | PQ4 | Coverage heatmap |

## 14. Change control

This scaffold is version-controlled (`v1` → `v2` etc.). Any change to the manuscript outline, the deliverable inventory, or the mapping between §B11 artefacts and files here requires (a) a version bump on this document with the changelog appended, and (b) if the change adds or removes a §B11 artefact, an amendments-log entry in the protocol.
