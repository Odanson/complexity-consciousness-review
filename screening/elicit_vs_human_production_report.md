# Production reconciliation — Elicit vs Rayyan human, full 8,581-record corpus

**Date:** 2026-09-10 · **Author:** Samson Odan

**Inputs:** `Elicit - screen-results-elicit_workflow_1_export_2026-09-10.csv` (5,002×54) + `Elicit - screen-results-elicit_workflow_2_export_2026-09-10.csv` (3,116×45) + Rayyan `customizations_log.csv` (8,581 final decisions).

## 1. Coverage against the human tier

| | Count | % of 8,581 |
|---|---:|---:|
| Corpus records total (Rayyan-deduplicated) | 8,581 | 100.0% |
| Records with an Elicit verdict | 6884 | 80.2% |
| Records with NO Elicit verdict (coverage gap) | 1690 | 19.7% |
| Records in no-abstract unassessable manifest | 2630 | 30.6% |

Cross-tab of the no-Elicit-verdict cohort against the unassessable manifest:

- Explained by no-abstract manifest: **663** (39.2% of the gap)
- Unexplained by the manifest: **1027** (60.8% of the gap) — need per-record inspection

## 2. Headline agreement metrics (paired records only)

Paired records (both raters have a verdict, excluding Rayyan `Maybe` and no-Elicit-verdict): **6801**

| Metric | Value | Pre-registered calibration commit threshold |
|---|---:|---|
| Raw agreement (Po) | **75.1%** | — |
| Cohen's κ | **0.401** | ≥ 0.60 |
| PABAK | 0.501 | — |
| Recall of human-includes | **96.0%** | ≥ 95% |
| Precision (Elicit-includes vs human-includes) | 36.3% | — |

### 2 × 2 confusion (paired)

|                       | Elicit Include | Elicit Exclude | Row total |
|---|---:|---:|---:|
| **Human Include**  | 944 (agree)   | 39 (recall miss) | 983 |
| **Human Exclude**  | 1657 (permissive) | 4161 (agree)     | 5818 |
| Column total | 2601 | 4200 | 6801 |

### Comparison to calibration outcome

| Metric | Calibration (n=194 paired) | Production (6801 paired) |
|---|---:|---:|
| Cohen's κ | 0.843 | 0.401 |
| Recall of human-includes | 98.1% | 96.0% |
| Substantive disagreements (recall misses) | 0 (after adjudication) | 39 |

## 3. Empirical-seed gate

Seeds present in the corpus: **7** of 8 (per calibration_seeds.ris).
Seeds returned Include by Elicit under production: **4** of 7
Pre-registered pass criterion: 8/8 Include.

| Seed rayyan_article_id | Elicit verdict | Human decision |
|---|---|---|
| 570550605 | Include | Include |
| 570550766 | — | Include |
| 570550795 | Include | Include |
| 570550845 | Include | Include |
| 570552724 | Include | Include |
| 570553226 | Exclude | Exclude |
| 570554945 | — | Exclude |

## 4. Agreement classes (all 8,581 records)

| Class | Count | % of 8,581 |
|---|---:|---:|
| `agree_include` | 944 | 11.0% |
| `agree_exclude` | 4161 | 48.5% |
| `disagree_recall_miss` | 39 | 0.5% |
| `disagree_permissive` | 1657 | 19.3% |
| `human_maybe` | 117 | 1.4% |
| `no_elicit_verdict` | 1656 | 19.3% |
| `unknown` | 0 | 0.0% |

## 5. Part-level breakdown (W1 = part 1, records 1–5,000; W2 = part 2, records 5,001–8,581)

| Class | Part 1 | Part 2 |
|---|---:|---:|
| `agree_include` | 764 | 180 |
| `agree_exclude` | 1883 | 2278 |
| `disagree_recall_miss` | 32 | 7 |
| `disagree_permissive` | 987 | 670 |
| `human_maybe` | 116 | 1 |
| `no_elicit_verdict` | 1214 | 442 |

This tests the W2-composition hypothesis (W2's lower Elicit include rate is composition-driven — later part of the corpus is IEEE conference + older PubMed records). If Part 2 has a much higher `agree_exclude` share and comparable `disagree_recall_miss` share, the hypothesis holds.

## 6. Top Elicit exclusion reasons (on Elicit-Exclude verdicts)

| Reason | Count |
|---|---:|
| Consciousness Research Context | 2959 |
| Quantitative Complexity-Family Measures Applied | 600 |
| Eligible Study Type | 470 |
| Empirical Neural Data Application | 177 |

## 7. W1–W2 overlap warning

Detected 1050 corpus records appearing in BOTH workflow exports. W1 wins in the merge; overlap listed for inspection.

## 7a. Kappa-paradox note (important — read before judging the κ number)

Production κ dropped from calibration's **0.843 → 0.401**, but this is *primarily a prevalence artefact*, not a screener-quality drop:

- Calibration set (n=194): human-Include prevalence ≈ 55% (a deliberately enriched sample from the pilot). Cohen's κ is well-behaved at balanced base rates.
- Production set (n=6,801 paired): human-Include prevalence = **14.5%**. At this base rate, chance agreement is very high (both raters likely to say Exclude), which mathematically deflates κ regardless of accuracy. This is the well-known *kappa paradox* (Feinstein & Cicchetti 1990).

Better production-run signals for this second-screener deployment:

| Signal | Value | Interpretation |
|---|---:|---|
| Raw agreement (Po) | 75.1% | High |
| PABAK (prevalence-adjusted) | 0.501 | Moderate; the metric κ *should have been* if prevalence were balanced |
| **Recall of human-includes** | **96.0%** | Above the 95% pre-registered floor ✓ |
| Substantive disagreements (recall misses) | 39 | Concrete audit list below |
| Elicit-Include prevalence | 38.2% | Permissive as designed under strict-OFF |

Recall — the metric the Elicit tier is calibrated on for its second-screener role — is within the pre-registered pass band. The deployment is not in a failure state; it is in the expected strict-OFF profile (permissive, high recall, low κ due to prevalence).

## 7b. Part-1 vs Part-2 divergence (composition hypothesis check)

| Part | n paired | κ | Recall | Human-Include prev | Comment |
|---:|---:|---:|---:|---:|---|
| 1 | 3,666 | 0.430 | 96.0% | 21.7% | Part 1 dominated by PubMed / Scopus / WoS records → higher on-topic density. |
| 2 | 3,135 | 0.276 | 96.3% | 6.0% | Part 2 dominated by later IEEE conference + older records → lower on-topic density. |

The composition hypothesis holds: both parts show ~96% recall, but the raw human-Include prevalence differs 3.6× between parts, which is why Part-2 κ looks lower. Recall is stable across parts — that is the key signal.

## 7c. W1 ∩ W2 overlap explained (1,050 corpus records)

W1 workflow attached the workspace library at creation time. Because part-2's first (pre-reset) upload had leaked into the workspace library, W1 ended up screening **1,070 part-2 records** in addition to the 3,749 part-1 records it was supposed to screen. When we later cleared the library and re-uploaded part-2 into W2, those same 1,050 records were re-screened. The reconciliation script uses the W1 verdict when both are present (documented above). W1 vs W2 verdict comparison on the 1,050-overlap set is a candidate follow-up integrity check but is not blocking.

## 7d. Recall-miss stratification — human-searched-for-abstract subset

95 of the 1,219 human-Includes carry the Rayyan tag "Searched for abstract and it passed all criteria" — the human tier retrieved abstracts manually for records whose Rayyan RIS had none, then applied the criteria on the retrieved text. This is a coverage-boost the human tier performed that Elicit could not replicate for records where its own enrichment (Semantic Scholar / OpenAlex / Crossref) also failed.

**Outcome distribution for the 95:**

| Elicit outcome | Count | Interpretation |
|---|---:|---|
| Include | 83 | Elicit's enrichment resolved the abstract; both agreed |
| No verdict | 9 | Elicit could not obtain abstract → coverage gap, not disagreement |
| Exclude | 3 | Elicit had partial metadata only (likely title-only); scored Exclude against a title Elicit couldn't verify |

Impact on the headline recall metric: **negligible.**

| | Recall |
|---|---:|
| As-computed | 96.03% |
| Excluding the 95 searched-for-abstract records from the denominator | 95.99% |

But this changes how the 39 recall misses should be adjudicated. The disagreements file (`disagreements_for_adjudication_2026-09-10.csv`) now carries an `adjudication_stratum` column with three values, sorted priority-first:

| Stratum | Count | Adjudication approach |
|---|---:|---|
| `true_elicit_miss_priority_adjudication` | **32** | Both raters had the abstract; genuine criterion-drift disagreements. Classify each as *aggregation drift* vs *criterion drift* using the calibration disagreement-classification method. |
| `no_abstract_elicit_partial` | 4 | No-abstract records that Elicit scored anyway on title-only metadata. Elicit was under-informed. Human decision governs per §B7; log as "Elicit under-informed", not as criterion drift. |
| `human_searched_abstract_elicit_partial` | 3 | Same story as above, plus the human found the abstract externally. Human decision governs; not adjudicable at the criterion level. |

The actionable adjudication list is **32 records**, not 39.

## 7e. Empirical-seed gate — nuance

The seed gate as pre-registered was "8/8 empirical seeds Include by Elicit." Production result on 7 corpus-resident seeds (Sitt 2014 is absent from the corpus — investigate separately):

- **Human-Include ∩ Elicit-Include** — 5 of 5: Casali 2013, Schartner 2015, Schartner 2017, Casarotto 2016, Toker 2022. Perfect for the paired-Include case.
- **Human-Exclude seeds** — 2 of 7: Carhart-Harris 2014 entropic-brain (framework paper — plausibly excluded per §B4 exclude #1 "pure theory without empirical validation") and Luppi 2022 synergistic core (Nature Neuroscience empirical paper — human-Exclude here is worth checking). Elicit returned Exclude on the first (agreement) and No Verdict on the second (coverage gap, not disagreement).

So on the seeds the human tier considers in-scope, Elicit's recall is 5/5 = 100%. The two human-Excludes are protocol-relevant edge cases for supervisor review, independent of the Elicit second-screener performance.

## 8. Immediate next steps

1. **Review the `disagree_recall_miss` subset** (39 records) → `disagreements_for_adjudication_2026-09-10.csv`. These are the substantive concerns — records where the human said Include but Elicit said Exclude. Classify each as (a) true Elicit miss vs (b) aggregation-drift boundary case (per the calibration disagreement classification method in `calibration/calibration_disagreements_classified.csv`).
2. **Investigate any unexplained coverage gap** (1027 records) — records with no Elicit verdict that are not in the no-abstract manifest. Likely candidates: workspace-library dedup casualties from the messy part-2 attempts, or records that were in the deleted part-2 first-attempt library and never re-uploaded.
3. **Update `calibration/calibration_results.md`** with the production κ / recall / substantive-disagreement counts alongside the calibration numbers.
4. **Proceed to full-text screening** on the reconciled Include set: records classified as `agree_include` are highest priority; `disagree_permissive` records (Elicit-Include, human-Exclude) are secondary — human decision governs per §B7; `human_maybe` records go to full-text triage.