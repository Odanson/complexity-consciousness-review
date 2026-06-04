# Decision-equivalence audit — 16-paper trial

**Companion to:** `calibration_test_plan.md`
**Anchor question:** Are Elicit's four-criterion prompts a faithful operational rendering of the §B6/§B7 eligibility logic, such that the existing human screen can stand as the calibration baseline?
**Verdict — short version:** **PASS at the criterion level.** Proceed with the full 200-paper run using option A (keep the existing human screen as fixed baseline). One disagreement on 15 paired papers, diagnosed as a documented Elicit *aggregation* artefact, not a criterion-drift problem. Two methodological refinements recommended for the full run.

---

## What was paired

The human file (`calibration_16paper_trial_human_decisions.xlsx`; original filename: `Human Decision_1.xlsx`) carries 16 decisions. The Elicit export (`calibration_elicit_export_16paper_trial.csv`; original Elicit filename: `Elicit - screen-results-review-audit.csv`) carries 15. The one record only in the human file is **PMID 25716830 — *Granger causality analysis in neuroscience and neuroimaging*** (no abstract; Elicit can't screen an abstract-less record). The audit is over the 15 paired records.

---

## Headline numbers

| Metric | Value | Read |
|---|---:|---|
| Raw agreement, as-deployed (Elicit's own Include/Exclude tag) | **14/15 = 93.3%** | "almost perfect" zone |
| Cohen's κ, as-deployed | **0.842** | almost perfect (Landis-Koch) |
| Elicit's recall of MY includes | **10/10 = 100%** | the number that matters most — zero false-negatives against my judgement |
| Raw agreement, strict-AND of Elicit's per-criterion calls | 12/15 = 80.0% | substantial |
| Cohen's κ, strict-AND | 0.609 | substantial |

κ on 15 observations is statistically unstable (the test plan flags κ as unreliable under ~50–100), so treat these as directional. The picture is unambiguously strong agreement, and the divergence between the two κ values is itself informative — that's the diagnostic the audit was designed to surface.

---

## The single binary disagreement (and what it's actually about)

**PMID 15134712 — *Pathological theta oscillations in idiopathic generalised epilepsy* (2004)**

- **Me:** EXCLUDE, reason "No consciousness relevance"
- **Elicit's per-criterion calls:** cons=**no**, data=yes, measures=**no**, study-type=yes
- **Elicit's binary tag:** Include (score 2.5)

The crucial observation: **Elicit and I agree at the criterion level**. Both call it `no` on consciousness context. Both call it `no` on complexity-family measures (spectral power + coherence aren't complexity-family). The strict-AND of Elicit's own per-criterion calls is **exclude** — same as my verdict.

So the disagreement does not come from the four-criterion rendering being unfaithful to the protocol. It comes from **Elicit's strict-OFF binary tag**, which appears to be a score-thresholded aggregation (score ≥ ~2.0 → Include) rather than a protocol-style strict-AND. Two of four criteria failing isn't enough to push the binary tag to Exclude under strict-OFF.

This is the most important finding in the audit — and it has a clean fix.

---

## A second pattern at the maybe edges

The strict-AND aggregation flips three records the OTHER way relative to my screening:

| PMID | Title | Elicit per-criterion (cons/data/meas/type) | Strict-AND | My call |
|---|---|---|---|---|
| 42109925 | Acas-eer EEG emotion recognition | maybe / yes / **no** / yes | exclude | maybe |
| 29363595 | Basal forebrain contributes to DMN | maybe / yes / **no** / yes | exclude | maybe |
| 40272770 | Topological reorganisation in functional dyspepsia | **no** / yes / maybe / yes | exclude | maybe |

In each case Elicit's `no` on C3 (complexity-family measures applied as the primary analysis) is *substantively defensible* — Acas-eer uses differential entropy as a feature for a classifier rather than as the analysis; Basal-forebrain studies gamma oscillations without an explicit complexity measure; Functional-dyspepsia uses graph-theoretic network metrics that sit on the edge of "complexity-family." My `maybe` is the inclusive scoping-review default at the boundary. Both are defensible readings.

This is **not** criterion drift — it's the irreducible fuzziness of "as the primary analysis" and "complexity-family" at the edges. We *want* this surfaced; resolving each is a reading-level judgement.

---

## What this means for the calibration

The audit confirms what we needed it to confirm: **the four-criterion rendering is decision-equivalent to the protocol at the criterion level.** The one binary disagreement is Elicit's aggregation rule, not my re-translation of the eligibility logic. **Option A stands.**

Two refinements to fold into the full 200-paper run:

**1. Report both κ values, not one.** Add to `calibration_analysis.py`: alongside the as-deployed κ, compute a **strict-AND κ** by aggregating Elicit's per-criterion calls with the protocol's actual logic (include iff none of the four are `no`). The pair of numbers separates two questions:

- *κ(as-deployed)* — "is Elicit, as it would be deployed, a useful second screener?"
- *κ(strict-AND)* — "is Elicit, as a per-criterion renderer of the protocol, faithful?"

The gap between them quantifies how much of the disagreement is Elicit's aggregation vs Elicit's criterion judgement. On these 15 records the gap is 0.23 κ-points, all in the aggregation direction.

**2. Classify each disagreement by source.** When reading the disagreement list on the full set, tag each as:

- **Substantive** — per-criterion calls genuinely differ between Elicit and me.
- **Aggregation** — per-criterion calls agree but Elicit's binary tag over-includes (paper #9 here).
- **Maybe-zone** — per-criterion calls agree at the boundary of one criterion's wording (papers #1, #3, #15 here, all on C3).

This converts the κ from a single summary into something the methods section can actually use: "of N disagreements, S were substantive, A aggregation, M maybe-zone — the commit decision rests on the substantive subset."

---

## Two operational notes

- **The no-abstract case (Granger causality, PMID 25716830).** Elicit's full pipeline silently skips records without an abstract. This is a generic abstract-based-screening failure mode that any tool would share. For the full run: either drop no-abstract records from the calibration (cleaner), or upload the full text into Elicit on those rows (recovers them but adds manual work). I'd drop them and document the count.
- **Elicit's column ordering vs the criterion list I registered.** Elicit's export orders the four as Consciousness / Study-Type / Empirical-Data / Measures, not my registered Cons / Empirical-Data / Measures / Study-Type. Substantively identical; only matters when reading the CSV. No action needed.

---

## Verdict and next step

**Equivalence verdict — PASS.** Keep my existing 200-paper human screen. Proceed with the full Elicit run under the four-criterion setup, strict-OFF, no overrides, identical 200-paper RIS upload. When the export is back, compute both κ values and classify disagreements by source.

If Elicit's aggregation drift turns out to be a recurring pattern at scale (i.e. on the full 200 we see meaningful numbers of "both criteria fail but score-threshold keeps it in" papers), the deployment recommendation isn't "don't use Elicit" — it's "deploy Elicit with a thin post-aggregation rule (e.g. exclude any paper with `no` on cons or on measures, regardless of score)." That's a one-line addition to the production workflow and it eliminates the only error mode the audit found.
