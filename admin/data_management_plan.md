# Data Management Plan

**Project:** Complexity Measures of Consciousness — PRISMA-ScR Methodological Review
**Lead:** Samson Odan (Max Planck School of Cognition)
**Protocol companion:** `prisma_protocol_v0.5.md` (v0.5, signed off by all four lead authors)
**Date:** 2026-05-29 (refreshed at OSF-upload review)

This is a half-page operational DMP for the OSF registration form. The review uses **no primary human-subjects data**; all material is drawn from the published peer-reviewed literature plus auditable workflow artefacts.

## 1. Data types

- **Search exports.** RIS / CSV files exported from PubMed, Scopus, Web of Science, PsycINFO, IEEE Xplore (one per database, archived with timestamp + query string). Note: Embase was originally planned but access could not be obtained within the project timeline; see Decision 9 in the protocol.
- **Deduplicated corpus.** Single RIS / CSV combining the per-database exports after Bramer + Rayyan dedup + manual spot-check.
- **Screening decisions.** Per-record include / maybe / exclude calls with rationale, exported from Elicit and ASReview (Phase 3) and from the human-reconciliation log.
- **Extraction tables.** Per-included-paper structured extraction (§B8 form) capturing eight-axis taxonomy tags, methodological details, claim → evidence mapping, and validation evidence.
- **Synthesis artefacts.** §B11 measure × axis tables, the misapplication register, the decision-support appendix, and the gap heatmap.
- **Code.** Python scripts in this repository (search pilot, calibration sampler, analysis script).
- **Calibration artefacts.** Two pre-registered calibration rounds: the 16-paper decision-equivalence audit (`calibration_16paper_trial_human_decisions.xlsx`, `calibration_elicit_export_16paper_trial.csv`, `calibration_equivalence_audit.md`) and the 200-record head-to-head calibration (`calibration_200_screening (human).csv`, `calibration_200_screening_reconciled.csv`, `calibration_200.ris`, `calibration_elicit_export_200.csv`, `calibration_disagreements_classified.csv`, `calibration_adjudications.md`, `calibration_200_provenance.txt`, `calibration_results.md`); plus the seed-gate check (`calibration_seeds.ris`, `calibration_elicit_export_seeds_final.csv`) and the verbatim Elicit prompts (`elicit_screening_prompts.md`). The arithmetic walkthrough underlying every headline number in `calibration_results.md` is in `elicit_metric_calculations.md` (working notes).

## 2. Storage and access during the project

- **Working copy.** Samson's MacBook (encrypted disk) + Max Planck School of Cognition institutional cloud backup.
- **Version control.** GitHub repository (private during pre-registration, public from OSF registration onward).
- **Shared workspace.** Private OSF project space (supervisors invited as read-only contributors via ORCID). Mirrors the GitHub structure.
- **No PII or sensitive data.** The project does not store identifiable information about human subjects; all source material is already-published peer-reviewed research.

## 3. Versioning, audit trail, and reproducibility

- Every Python script, document, and data artefact is committed to GitHub with a meaningful commit message; no `git add -A` against untracked sensitive files.
- Each protocol version is tagged on GitHub; Zenodo auto-archives each release and mints a versioned DOI. Concept DOI: 10.5281/zenodo.20140263.
- Screening, extraction, and reconciliation decisions are logged at the per-record level with rationale + source-quote where applicable.
- The Elicit deployment configuration is recorded verbatim in `elicit_screening_prompts.md`; the locked PubMed search is in `database_queries.md` and reproducible from `pilot_search.py`.

## 4. Sharing and publication

- **Protocol + methodology** licensed under **CC-BY 4.0** (see `LICENSE-PROTOCOL.txt`).
- **Code** licensed under **MIT** (see `LICENSE`).
- **Registered protocol** registered on OSF Registries prior to the locked multi-database search execution; the OSF registration link is added to the README and §B6.3 once minted.
- **Included-set dataset** (RIS + extraction tables) released on OSF with the manuscript, under CC-BY 4.0.
- **Manuscript** will be submitted to an appropriate journal for the review’s scope and contribution, with candidate venues including *Nature Human Behaviour*, *Neuroscience & Biobehavioral Reviews*, and *Neuroscience of Consciousness*.
- **Companion website** (Yaron NHB style) planned post-publication for measure-by-measure look-up.

## 5. Retention

- All artefacts retained for at least ten years on Zenodo (institutional repository with long-term preservation) and on the OSF project page.
- GitHub repository retained indefinitely.
- Local working copies migrated as Samson's institution changes.

## 6. Responsibilities

- **Samson Odan (lead):** day-to-day data management, code, documentation, audit trail.
- **Lucia Melloni, Andrej Biçanski, Jürgen Jost (supervisors):** review at month-end milestones; final approval of the registered protocol and the manuscript.
- **Adam Barrett, Anil Seth (planned external collaborators):** to be added on contribution.

## 7. Costs

No budget required. All tools used are free at the level we need (PubMed, GitHub, Zenodo, OSF, Citationchaser, Zotero, ASReview). Access to required software and services (including Elicit's Scale-tier systematic-review workflow) will be maintained for the duration of screening.
