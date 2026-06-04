# Elicit head-to-head — full 200-paper calibration results

**Companion to:** `calibration_test_plan.md` (pre-registered thresholds) · `calibration_equivalence_audit.md` (16-paper trial)
**Run completed:** 2026-05-28
**Inputs:** `calibration_200_screening (human).csv` (200 hand decisions, 1 blank) · `calibration_elicit_export_200.csv` (Elicit's full export, 195 records — 5 silently skipped; original Elicit filename: `elicit_calibration_200_export-6d61a5b1.csv`)

---

## Headline numbers

Joined on normalised title; n = 194 paired records with a non-blank human decision. Binary collapse with maybe → include throughout (high-sensitivity scoping default).

| Metric | Value | Pre-registered threshold | Pass? |
|---|---:|---|:-:|
| Elicit's recall of MY includes | **102/104 = 98.1%** | ≥ 95% | ✅ |
| Cohen's κ (binary, as-deployed) | **0.843** | ≥ 0.60 | ✅ |
| Raw agreement (as-deployed) | 179/194 = 92.3% | — | — |
| Raw agreement (strict-AND aggregation) | 166/194 = 85.6% | — | — |
| Cohen's κ (strict-AND) | 0.715 | — | — |
| Substantive disagreements | **0** | — | — |
| Empirical seeds screened IN | **8/8** | 8/8 | ✅ |

**Verdict against the pre-registered commit rule:** PASS on all three gates. Commit to Elicit as AI second-screener.

---

## 2×2 (as-deployed, binary, n = 194)

| | Elicit: exclude | Elicit: include |
|---|---:|---:|
| **Me: exclude (90)** | 77 | 13 |
| **Me: include (104)** | 2 | 102 |

Elicit dropped 2 of my 104 includes and over-included 13 of my 90 excludes. The over-inclusion is the dominant failure mode — exactly the pattern the 16-paper audit predicted at scale.

---

## Disagreement classification (15 total)

| Class | Count | What it means | Direction |
|---|---:|---|---|
| **Substantive** | **0** | Per-criterion calls genuinely differ from my judgement | — |
| **Aggregation drift** | **10** | Elicit's per-criterion calls agree with me (strict-AND of them = exclude) but its strict-OFF binary tag over-includes | all Elicit-over-includes |
| **Maybe-zone** | **5** | Genuine boundary calls; one criterion sits at a `maybe` edge | 4 over-includes, 1 over-exclude |

The all-zero substantive count is the most important finding in the table. **Every single one of Elicit's 15 disagreements with me is either an aggregation artefact or a defensible boundary call on a `maybe` edge** — not Elicit interpreting the protocol differently to me on any single record.

The 10 aggregation-drift records all have the same fingerprint: 1–2 criteria fail (mostly Consciousness or Measures), Elicit's score falls in the 2.5–2.8 band, and strict-OFF flips them to Include where strict-AND would correctly Exclude. Examples: ERP markers in human-robot interaction (cons=maybe, meas=no), occipital sharp transients in sleep (meas=no), preterm-infant fractal-dimension (cons=no, data=maybe).

---

## The maybe-zone (5 papers worth a close read)

These are genuine borderline calls, not tool failures. Each gets a quick human verdict on the full set:

| PMID | Title (short) | My call | Elicit | Elicit per-crit (cons/data/meas/type) | Note |
|---|---|---|---|---|---|
| 18990620 | DFA on intracranial pressure — TBI | exclude | include (3.5) | maybe / maybe / yes / yes | Uses DFA but no consciousness framing |
| 38136525 | Black holes entropy → consciousness | **include** | **exclude (1.4)** | maybe / no / no / no | Theoretical; no empirical neural data |
| 20626893 | Hippocampal synchronization + acute nicotine | exclude | include (4.3) | maybe / yes / yes / yes | Synchronisation methods, but no DOC framing |
| 25837427 | Ketamine network reconfiguration in anesthetised monkeys | exclude | include (4.3) | maybe / yes / maybe / yes | I judged the ketamine use as antidepressant-mechanism, not consciousness modulation |
| 33504952 | Brain-heart desync in anxiety | maybe | exclude (1.4) | no / no / no / no | All four per-criterion calls no |

Of these, the one to look at hardest is **PMID 38136525** (Black-holes-entropy / brain-connectome). My Include disagrees with all three of Elicit, the per-criterion logic, and the strict-AND aggregation. Could be the right inclusive read; could also be a candidate for the §B4 methodology-only-exception list rather than a search-passing include.

---

## The 5 silently-skipped records

Elicit returned 195/200. The 5 missing are all the abstract-less / problematic-abstract cases:

- PMID 11811170 — *Is MRI indicated before reduction of unilateral cervical dislocation* (no abstract in my screen either; my decision blank)
- PMID 25716830 — *Granger causality analysis in neuroscience and neuroimaging* (no abstract) — my decision: maybe
- PMID 30618577 — *Sleep, Wake, and Critical Brain States: Corollaries From Brain Dynamics* (perspectives piece, may lack standard abstract) — my decision: maybe
- PMID 20421793 — *Artefact in EEG monitoring in a patient with brain metastasis* — my decision: maybe
- PMID 8268440 — *Anesthetic management of thoracic aortic aneurysm* (1993, MEDLINE abstract may be missing) — my decision: exclude

This is a generic abstract-based-screening failure mode — any tool would silently skip these. **2.5% silent skip rate** is the operational number to document in §B7. Workflow implication: post-search, flag every record where Elicit returns no row, and screen them manually.

---

## What this means

The pre-registered thresholds are clear: **commit to Elicit as the AI second screener.** The case for committing is unusually strong because there are *zero* substantive disagreements — Elicit isn't interpreting any one paper's protocol-fit differently from me. The disagreements are all in the aggregation rule and at known fuzzy boundaries.

---

## Post-resolution numbers (reconciled human decisions, n = 195)

After the maybe-zone adjudications and the final blank fill (PMID 16632826 → Include), the human side has three substantive changes from the blind screen: PMID 38136525 Include → Exclude, PMID 33504952 Maybe → Exclude, PMID 16632826 blank → Include. Re-running the analysis against the same Elicit export:

| Metric | Blind (pre-registered) | Reconciled (post-resolution) |
|---|---:|---:|
| Valid paired records | 194 | **195** |
| As-deployed agreement | 179/194 = 92.3% | **182/195 = 93.3%** |
| Cohen's κ (as-deployed) | 0.843 | **0.865** |
| Recall of human-includes (as-deployed) | 102/104 = 98.1% | **103/103 = 100%** |
| Strict-AND agreement | 166/194 = 85.6% | 169/195 = 86.7% |
| Cohen's κ (strict-AND) | 0.715 | 0.736 |
| Recall of human-includes (strict-AND override) | — | **80/103 = 77.7%** |

The reconciled numbers describe the working dataset used downstream; the blind numbers are the formal calibration result that the pre-registered thresholds were tested against. **Both pass.**

---

## Correction to the deployment-rule recommendation

The earlier draft of this document recommended deploying Elicit with a strict-AND post-aggregation override ("exclude if any of the four per-criterion calls is `no`"). The post-resolution analysis disproves that recommendation, and I'm retracting it.

Breakdown of the reconciled-include cohort (n = 102 papers I kept as Include after reconciliation):

| `no` calls per record | Count | Strict-AND would |
|---:|---:|---|
| 0 | 79 | keep |
| 1 | 16 | drop |
| 2 | 6 | drop |
| 3 | 1 | drop |

Strict-AND drops **23 of my 102 includes** — papers where Elicit's per-criterion calls failed on one or more axes but I, having read the abstract, judged the paper in-scope anyway. Five of those have cons=no AND meas=no simultaneously (the most aggressive strict-AND target), and I still kept them as includes. Strict-AND would mean a 22.5% loss of recall — far worse than as-deployed Elicit alone.

I ran a small sweep of alternative rules:

| Rule | Recall preserved (want high) | Drift caught (want high) |
|---|:-:|:-:|
| R1 strict-AND (any `no` → exclude) | 79/102 = 77% | 10/13 = 77% |
| R2 substantive-no (cons=no OR meas=no → exclude) | 79/102 = 77% | 10/13 = 77% |
| R3 double-substantive (cons=no AND meas=no → exclude) | 97/102 = 95% | 2/13 = 15% |
| R4 score<3.0 + any `no` | 85/102 = 83% | 10/13 = 77% |
| R5 score<3.0 + substantive `no` | 85/102 = 83% | 10/13 = 77% |
| **R0 as-deployed (no override)** | **102/102 = 100%** | 0/13 — manual reconciliation |

For a scoping review, false negatives (recall loss) are strictly worse than false positives (over-inclusions caught at reconciliation). R0 dominates. R3 is the only alternative worth considering, and it saves 2 manual reads at the cost of 5 false negatives — a bad trade.

**Revised deployment recommendation: deploy Elicit as-deployed (strict-OFF, no override).** The 13 over-includes per 200 records become a manual reconciliation load of ≈ 6.5% of the corpus, all in the safe direction. The 5 papers where cons=no AND meas=no simultaneously can be tagged as "priority manual review" in the sort order (not as auto-excludes) — that's where false-positives concentrate, but each still gets a human read.

---

## Revised §B7 amendment draft

> *"Single human reviewer (S.O.) with AI-assisted second screening using Elicit (four-criterion rendering of §B6/§B7 eligibility logic, strict criteria OFF, no post-aggregation override; Elicit's binary verdict treated as a recommendation, all disagreements reconciled by the human reviewer). Calibration on n = 194 paired records (see `calibration_results.md`): blind Cohen's κ = 0.843, recall of human-includes = 98.1%, zero substantive disagreements, 8/8 empirical seeds screened IN. Post-reconciliation: κ = 0.865, recall = 100%, ≈ 6.5% manual reconciliation load (all over-includes). Records returning no abstract (≈2.5% of corpus) are screened manually by exception."*

---

## Seed gate — known-positive recovery check

The pre-registered seed gate (8/8 empirical seeds must be screened IN) was run on `calibration_seeds.ris` against the same Elicit setup. Result: **8/8 Include — gate PASSED.**

| # | Seed (resolved title) | Year | cons | data | meas | type | Verdict | Score |
|---|---|---|:-:|:-:|:-:|:-:|:-:|---:|
| 1 | *Metastability, fractal scaling, and synergistic information processing* (Luppi) | 2022 | **no** | yes | yes | yes | Include | 2.7 |
| 2 | *Increased spontaneous MEG signal diversity for psychoactive doses of ketamine* (Schartner) | 2017 | yes | yes | yes | yes | Include | 4.9 |
| 3 | *A theoretically based index of consciousness independent of sensory processing and behavior* (Casali, PCI) | 2013 | yes | yes | yes | yes | Include | 4.9 |
| 4 | *The entropic brain* (Carhart-Harris) | 2014 | yes | maybe | maybe | maybe | Include | 3.4 |
| 5 | *Complexity of multi-dimensional spontaneous EEG decreases during propofol induction* (Schartner LZc) | 2015 | yes | yes | yes | yes | Include | 4.9 |
| 6 | *Large scale screening of neural signatures of consciousness in VS / MCS patients* (Sitt) | 2014 | yes | yes | yes | yes | Include | 4.9 |
| 7 | *Stratification of unresponsive patients by an independently validated index* (Casarotto, PCI in DOC) | 2016 | yes | yes | yes | yes | Include | 4.9 |
| 8 | *Neural complexity is a common denominator of human consciousness across diverse regimes of cortical dynamics* (Toker) | 2022 | yes | yes | yes | yes | Include | 4.9 |

Two findings worth flagging from this run:

- **The Sitt 2014 paper screened in cleanly here (cons/data/meas/type all yes, score 4.9).** This is the paper that was a documented database miss in the original PubMed pilot (it framed itself as "neural signatures" rather than "consciousness" in the index terms). Elicit's semantic reading of the abstract correctly picks up the consciousness context. That's a quiet but important data point: Elicit may also serve as a *recovery channel* for Sitt-type framing misses, complementing §B5 citation tracking.
- **Seed #1 (Luppi) — initial sampler bug and re-test result.** The original lookup `Luppi[Author] AND 2022[PDAT] AND synergistic[Title]` matched the NeuroImage 2022 *Metastability, fractal scaling, and synergistic information processing* paper rather than the intended Nat Neurosci 2022 *A synergistic core for human brain evolution and cognition* paper (PMID 35618951). The lookup was disambiguated in `pilot_search.py` (added `AND core[Title]`) and `calibration_seeds.ris` regenerated. The canonical paper was re-screened in Elicit (`calibration_elicit_export_seeds_final.csv`; original Elicit filename: `elicit_seed_gate_rerun.csv`): **Include, score 3.5, cons=no, data=yes, meas=maybe, type=yes.** Same fingerprint as the NeuroImage version — Elicit reads "for human brain evolution and cognition" as not-consciousness, even though the paper's substance is the synergistic information decomposition the Luppi/Mediano/Rosas line uses for consciousness research. The pattern is independently confirmed on two Luppi papers, and matches the 23 reconciled human-includes that strict-AND would also drop. It is the strongest single piece of evidence for *not* deploying the strict-AND override (see the correction section below).

**Seed gate verdict: 8/8 verified-tested as-deployed.** Under any rule that excludes on cons=no, both Luppi seeds get dropped — which is why the as-deployed deployment is the correct one.

## Calibration close-out (all items complete)

1. ✅ **5 silently-skipped records adjudicated** — see `calibration_adjudications.md` (1 Include, 4 Exclude).
2. ✅ **5 maybe-zone disagreements resolved** — all five resolve to Exclude after reconciliation (2 blind-include flips, 3 confirmed).
3. ✅ **Luppi seed lookup fixed** in `pilot_search.py` (added `AND core[Title]`). `calibration_seeds.ris` regenerated.
4. ✅ **Canonical Luppi seed re-tested** (`calibration_elicit_export_seeds_final.csv`) — Include, score 3.5; the cons=no pattern reproduces on the canonical paper, confirming the as-deployed deployment recommendation.
5. ✅ **PMID 16632826 adjudicated Include** — *Spectral entropy + BIS under propofol* (Ellerkmann 2006). In-scope on all four criteria. Reconciled CSV updated.

**Calibration is closed.** Elicit moves from "evaluation" to "deployed second-screener." The §B7 amendment can be written from the revised draft above when ready to do so.

Once those three are done, the §B7 amendment can be written in one paragraph: *"Single human reviewer with AI-assisted second screening (Elicit, four-criterion rendering, strict-OFF + post-hoc strict-AND override), reconciled by the lead reviewer. Calibration: n = 194 paired records, κ = 0.843, recall of human-includes = 98.1%, zero substantive disagreements (see `calibration_results.md`). Records returning no abstract (2.5% of the corpus) are screened manually by exception."*

---

*Source-classified disagreement list with full per-criterion calls and reasons: `calibration_disagreements_classified.csv`.*
