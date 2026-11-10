# PQ1 measure-level extraction form — codebook (v1)

**Companion to:** `protocol/prisma_protocol_v0.5.1.md` §B8 (data items), §B12 (eight-axis taxonomy) · **Version 1** · 2026-09-10 · Samson Odan

**Deliverables:**

- `pq1_measure_extraction_form_v1.xlsx` — the form itself, with data-validation dropdowns on every controlled-vocabulary column.
- `pq1_measure_extraction_form_v1.csv` — same columns, no validations (git-friendly diff surface).
- `pq1_measure_extraction_codebook.md` — this file.

## Unit of extraction

One row per **(paper, measure)**. If a paper reports LZc + PCI, that's two rows sharing paper-identity fields but with distinct `measure_*` and axis-tag columns. This is the granularity PQ1 requires: *what does each measure mathematically compute*, not *what does each paper conclude*.

## Field groups and columns

| Column | Group | Controlled vocab | Guidance |
|---|---|---|---|
| `row_id` | A. Extraction meta | — | Unique ID for this (paper, measure) row. Format: <rayyan_article_id>-M<measure_index>. |
| `extractor` | A. Extraction meta | — | Initials or name of the person extracting this row. |
| `extraction_date` | A. Extraction meta | — | YYYY-MM-DD. |
| `extraction_status` | A. Extraction meta | `extraction_status` | Workflow status. |
| `extraction_confidence` | A. Extraction meta | `extraction_confidence` | Extractor's confidence in the row overall. |
| `needs_full_text_recheck` | A. Extraction meta | `needs_full_text_recheck` | Flag if the row needs a second look at the source PDF. |
| `awaiting_supervisor_input` | A. Extraction meta | `yes_no_unclear` | Y if row is blocked on supervisor decision. |
| `rayyan_article_id` | B. Paper identity | — | From Rayyan customizations_log (numeric, no 'rayyan-' prefix). |
| `doi` | B. Paper identity | — | DOI, lowercase, no URL prefix. |
| `pubmed_id` | B. Paper identity | — | PubMed ID if present. |
| `first_author` | B. Paper identity | — | Family name of first author. |
| `year` | B. Paper identity | — | Publication year (YYYY). |
| `journal` | B. Paper identity | — | Journal or venue name. |
| `title` | B. Paper identity | — | Full title (verbatim). |
| `human_screening_decision` | B. Paper identity | — | Rayyan human decision at title/abstract tier: Include / Maybe / Exclude. |
| `elicit_verdict` | B. Paper identity | — | Elicit aggregated Include/Exclude verdict (may be blank for no-abstract records). |
| `species` | C. Study design | — | Homo sapiens / Macaca mulatta / etc. If multiple, list all. |
| `N` | C. Study design | — | Sample size (per group, or total). |
| `age_range` | C. Study design | — | Mean ± SD or range if reported. |
| `population` | C. Study design | `population` | Choose from controlled list; use 'Mixed / other' if none fits. |
| `state_contrast` | C. Study design | — | The states compared, e.g., 'awake vs. propofol-anaesthesia', 'placebo vs. LSD'. |
| `paradigm_or_task` | C. Study design | — | Resting / task / stimulus / TMS-EEG protocol / etc. |
| `modality` | D. Recording | `modality` | Primary recording modality. Use 'Multimodal' if the study combines two or more. |
| `channels_or_voxels` | D. Recording | — | Number of channels / sensors / voxels / units used in the reported analysis. |
| `sampling_rate_hz` | D. Recording | — | Hz. If downsampled, report the sampling rate at which the measure was computed. |
| `reference` | D. Recording | — | Reference / re-referencing scheme (e.g., average, mastoid, CSD, source-reconstructed). |
| `preprocessing_pipeline_cite` | D. Recording | — | Cite the specific pipeline description (e.g., 'FieldTrip default, Oostenveld 2011'; 'as in Schartner 2015'). |
| `measure_name` | E. Measure identity | — | The measure as named by the authors, e.g., 'LZc', 'CSER', 'wSMI', 'PCI'. |
| `measure_variant` | E. Measure identity | — | Exact mathematical variant, e.g., 'LZ76 on binarised amplitude', 'permutation entropy m=3 tau=1'. |
| `measure_family_axis1` | E. Measure identity | `measure_family_axis1` | §B12 Axis 1 — mathematical primitive family. Choose one; if the measure is composite, choose 'Hybrid / composite'. |
| `formula_reference` | E. Measure identity | — | Citation for the canonical formula used (author, year, section/equation number). |
| `implementation_toolbox_or_code` | E. Measure identity | — | Toolbox / package / repo / language, and version if reported. |
| `parameters` | E. Measure identity | — | All hyperparameters: window length, embedding dim, binarisation threshold, coarse-graining, k-nearest-neighbours, etc. |
| `stationarity_assumption` | F. Assumptions | `yes_no_unclear` | Does the measure assume stationarity or is a stationarity check reported? |
| `normalisation` | F. Assumptions | — | Amplitude normalisation, z-scoring, unit-variance, per-channel vs global — describe briefly. |
| `binarisation` | F. Assumptions | — | If the measure operates on binarised signals, describe the binarisation rule. |
| `surrogate_method` | F. Assumptions | — | Surrogate/null model used to build a reference (phase-shuffle, IAAFT, permutation, etc.). |
| `data_requirement_axis2` | F. Assumptions | `data_requirement_axis2` | §B12 Axis 2 — what the measure needs from the data. |
| `aspect_of_consciousness_axis4` | G. Consciousness claim | `aspect_of_consciousness_axis4` | §B12 Axis 4 — which aspect the study links the measure to. |
| `claim_direction` | G. Consciousness claim | `claim_direction` | Direction of the reported effect on the primary contrast. |
| `verbatim_claim` | G. Consciousness claim | — | One or two sentences quoted verbatim from the paper that state the consciousness-linked finding. |
| `spatial_scale_axis5` | H. Cross-cutting axes | `spatial_scale_axis5` | §B12 Axis 5. |
| `temporal_granularity_axis3` | H. Cross-cutting axes | `temporal_granularity_axis3` | §B12 Axis 3. |
| `theory_anchoring_axis6` | H. Cross-cutting axes | `theory_anchoring_axis6` | §B12 Axis 6. |
| `inferential_status_axis7` | H. Cross-cutting axes | `inferential_status_axis7` | §B12 Axis 7. |
| `validation_type_axis8` | I. Validation | `validation_type_axis8` | §B12 Axis 8. |
| `ground_truth` | I. Validation | — | Specific criterion used, e.g., 'CRS-R score', 'plasma propofol concentration', 'behavioural response'. |
| `accuracy_or_effect` | I. Validation | — | Reported classification accuracy, effect size (d, r), AUC — with units. |
| `ci_or_p` | I. Validation | — | Confidence interval or p-value as reported. |
| `multiple_comparison_correction` | J. Statistical rigor | — | FDR / Bonferroni / cluster-based / none — describe. |
| `surrogate_controls` | J. Statistical rigor | `yes_no_unclear` | Are surrogate/null controls reported? |
| `cross_validation` | J. Statistical rigor | — | K-fold, LOO, split-half, held-out — describe. |
| `sample_size_justification` | J. Statistical rigor | — | Power calculation? Prior effect-size reference? None? |
| `code_available` | K. Reproducibility | `yes_no_unclear` | Is analysis code publicly available? |
| `code_url` | K. Reproducibility | — | URL if available. |
| `data_available` | K. Reproducibility | `yes_no_unclear` | Is data publicly available? |
| `data_url` | K. Reproducibility | — | URL if available. |
| `params_fully_reported` | K. Reproducibility | `yes_no_unclear` | Are all hyperparameters and preprocessing steps fully reported? |
| `reported_limitations_verbatim` | L. Limitations | — | Verbatim quote from the paper's limitations / caveats section. |
| `reviewer_flagged_misapplication` | L. Limitations | — | Extractor's concern, e.g., 'GC applied to a densely coupled system without partialling', 'LZ interpreted as Kolmogorov complexity'. Free text. |
| `free_text_notes` | M. Notes | — | Anything else the extractor wants to record for supervisor review. |

## Controlled vocabularies

Every dropdown-backed column pulls from a single canonical list on the `Controlled_vocab` sheet in the XLSX. Adding a value requires updating that sheet **and** this codebook — no ad-hoc extensions during extraction.

### `measure_family_axis1`
- Entropy family
- Compressibility
- Information flow
- Integrated information
- Dynamical / criticality
- Structural / graph-theoretic
- Dimensionality / manifold
- Perturbational
- Structure-of-experience
- Hybrid / composite
- Phase / dynamical-systems coupling
- Temporospatial / scale-free

### `data_requirement_axis2`
- Amplitude only
- Amplitude + functional connectivity
- Amplitude + effective connectivity
- Phase only / phase + amplitude
- Requires external perturbation
- Requires simultaneous multi-scale recording

### `temporal_granularity_axis3`
- Event-level (single-trial, sub-second)
- Windowed / epoch-level
- Long-range / scaling (seconds to hours)
- State-level (one number per session)

### `aspect_of_consciousness_axis4`
- Level / wakefulness
- Content / what is experienced
- Integration (across regions / networks)
- Differentiation (richness of repertoire)
- Structure (geometry of experience)
- Temporal flow (experience of time)

### `spatial_scale_axis5`
- Single-unit / multi-unit
- Laminar / columnar
- Area-level / ROI
- Whole-brain network

### `theory_anchoring_axis6`
- Theory-derived
- Theory-agnostic
- Theory-agnostic-but-interpreted-post-hoc

### `inferential_status_axis7`
- Causal (perturbation-based)
- Correlational / descriptive

### `validation_type_axis8`
- Behavioural report
- Clinical diagnosis
- Pharmacological manipulation
- Cross-measure agreement only
- None / no external criterion

### `population`
- Healthy adult
- Healthy adolescent / child
- Anaesthetised
- Disorders of consciousness (DOC)
- Sleep / NREM / REM
- Psychedelic (report-capable)
- Meditator
- Neurological / psychiatric
- Non-human primate
- Rodent
- Other non-human animal
- Mixed / other

### `modality`
- EEG
- MEG
- fMRI / BOLD
- iEEG / ECoG
- LFP
- Single-unit
- Multi-unit
- Two-photon calcium
- Wide-field optical
- TMS-EEG
- Multimodal

### `claim_direction`
- Positive (measure tracks aspect)
- Null / no effect
- Negative (measure fails or opposite direction)
- Mixed

### `yes_no_unclear`
- Y
- N
- Unclear

### `extraction_confidence`
- High
- Medium
- Low

### `extraction_status`
- Not started
- In progress
- Awaiting supervisor
- Complete

### `needs_full_text_recheck`
- N
- Y — flag reason in notes

## Change control

Any change to columns, dropdown lists, or unit of extraction requires (a) an amendments-log entry in the protocol, (b) a version bump on this form (`v2`, `v3`, …) with the changelog documented at the top of this codebook, and (c) re-piloting on ≥ 5 already-extracted papers to confirm the new form still captures the previous fields losslessly.
