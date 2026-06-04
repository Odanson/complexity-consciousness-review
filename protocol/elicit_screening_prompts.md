# Elicit screening prompts — verbatim record (deployed 2026-05-28)

**Companion to:** `prisma_protocol.md` §B7 step 5 (v0.5 — Elicit deployment introduced at v0.4.4, carried unchanged into v0.5) · `calibration_test_plan.md` · `calibration_results.md`
**Recorded:** 2026-05-29

This document is the canonical, **verbatim** record of the prompts used to configure Elicit's systematic-review workflow for (a) the pre-registered calibration on the 200-record PubMed subsample and (b) the planned bulk pass on the deduplicated multi-database corpus (Phase 3 Weeks 6–7 of the rotation). It exists so any third party can reproduce the configuration exactly, and so the protocol's named criteria are anchored to the actual text Elicit received.

---

## Research question (Elicit protocol setup)

> Which quantitative complexity, information-theoretic, dynamical, perturbational, or related measures have been applied to empirical neural data in consciousness research, and what aspects of consciousness are those measures used to investigate or explain?

---

## Four-criterion screening prompts (deployed verbatim)

### 1. Consciousness Research Context

> Does this study investigate consciousness, states of consciousness, or transitions between conscious states (e.g., wakefulness, sleep, anaesthesia, disorders of consciousness, psychedelics, meditation, dreaming, conscious perception), OR explicitly interpret findings in relation to consciousness or neural signatures/mechanisms of consciousness?

### 2. Empirical Neural Data Application

> Does this study analyse empirical neural data (e.g., EEG, MEG, fMRI/BOLD, ECoG/iEEG, LFP, single-unit or multi-unit recordings, calcium imaging, TMS-EEG, or other neural recordings), OR systematically review/meta-analyse studies that analyse such neural data?

### 3. Quantitative Complexity-Family Measures Applied

> Does this study apply — or systematically review studies that apply — one or more quantitative complexity-family measures as a primary analysis (e.g., entropy family, Lempel-Ziv complexity, Kolmogorov measures, PCI/ST-PCI, mutual information, transfer entropy, Granger causality, wSMI, DFA, multifractal measures, neural avalanches, metastability, PLV/wPLI, criticality, integrated information/φ-family, ACW, PLE, TRW, dimensionality/manifold measures), rather than only proposing or theoretically discussing such measures?

### 4. Eligible Study Type

> Is this an empirical research article, systematic review, or meta-analysis — not solely a conference abstract, editorial, commentary, opinion piece, narrative perspective, or theoretical/simulation-only paper without empirical results?

---

## Deployment configuration

- **Strict criteria:** OFF (scoping-review default; retains borderline papers).
- **Post-aggregation override:** none. Elicit's binary verdict is treated as a recommendation; the human reviewer reconciles disagreements per §B7. (Rationale for *no* override: see `calibration_results.md` §"Correction to the deployment-rule recommendation" — strict-AND would drop 23/103 reconciled human-includes, recall 77.7 %, far below the pre-registered ≥ 95 % floor.)
- **No-abstract records:** Elicit silently omits records without an abstract (≈ 2.5 % of the calibration corpus). These are flagged for manual exception screening.
- **Per-criterion exports:** every paper's per-criterion yes/no/maybe call, the corresponding rationale, and the source quote highlighted in the abstract are exported to CSV and retained as part of the audit trail.
- **Elicit version + run date:** recorded at each run (the protocol notes Elicit's accuracy moves between releases, so the version is part of reproducibility).

---

## Provenance — how these prompts came to be

- **First version (six overlapping criteria).** Initial Elicit-internal suggestions from the systematic-review workflow's auto-suggest, lightly edited to fit our PECO. Six columns with overlaps across topic / data-type / methodology / publication-type.
- **Refined to four orthogonal criteria (pre-calibration).** Reorganised into the four current orthogonal columns — Topic, Data, Method, Article-kind — to make disagreement analysis cleaner. Three substantive wording corrections applied: (i) added a reviews-of-empirical-work clause to C2 (`OR systematically review/meta-analyse studies that analyse...`); (ii) added the parallel reviews clause and the *primary analysis* guard to C3 (`apply — or systematically review studies that apply — ... as a primary analysis ... rather than only proposing or theoretically discussing`); (iii) stripped C4 down to the publication-type filter only, removing the empirical/theoretical clause that duplicated C3 and the data-type clause that duplicated C2.
- **Decision-equivalence audit on 16-paper trial** (`calibration_equivalence_audit.md`, 2026-05-27): confirmed the four-criterion rendering is decision-equivalent to §B6/§B7 at the criterion level (PASS). The one paper-level disagreement was diagnosed as Elicit's strict-OFF aggregation drift, not a criterion-rendering problem.
- **Pre-registered calibration on 200-paper subsample** (`calibration_results.md`, 2026-05-28): blind n = 194, Cohen's κ = 0.843, recall of human-includes = 98.1 %, substantive disagreements = 0, seeds 8/8 Include. All three pre-registered commit thresholds cleared.
- **Re-confirmed on seed-gate re-run** with the canonical Luppi *synergistic core* paper after the `pilot_search.py` lookup fix (`calibration_elicit_export_seeds_final.csv`; original Elicit filename: `elicit_seed_gate_rerun.csv`, 2026-05-29): same prompts, same configuration, 8/8 Include.

---

## How the criteria map to protocol §B6 / §B7

| Elicit criterion | Backing protocol section |
|---|---|
| 1. Consciousness Research Context | §B6 Block 1 (consciousness / state); §B3 PECO Population/context; §B4 inclusion criterion (consciousness claim) |
| 2. Empirical Neural Data Application | §B6 Block 3 (neural data); §B4 inclusion criterion (applied to neural data) |
| 3. Quantitative Complexity-Family Measures Applied | §B6 Block 2 (complexity-variant terms — the substantive content filter); §B4 inclusion criterion (applies a quantitative complexity measure); §B12 Axis 1 (mathematical primitive families) |
| 4. Eligible Study Type | §B4 publication-type exclusions (no editorials, commentaries, opinion pieces, theoretical-only / simulation-only papers, conference abstracts without full data) |

The four criteria are an English-language rendering of the same eligibility logic that the locked Boolean search operationalises programmatically. Equivalence was tested in the 16-paper audit and confirmed at the criterion level; remaining paper-level disagreements during the calibration were all aggregation-rule or maybe-zone artefacts (see `calibration_results.md`).

---

## Change control

Any change to these prompts requires (a) a re-calibration round on a fresh seeded random sample using the procedure in `calibration_test_plan.md`, (b) an entry in this document's *Provenance* section, and (c) an amendments-log entry in `prisma_protocol.md`. The deployment configuration above (strict OFF, no override) is justified by the calibration outcome and should not be changed without re-running that calibration.
