# Elicit calibration — metric calculations (working notes)

*Personal notes. Not for the audit trail; not referenced from protocol or tracking files. Shows the actual arithmetic behind every headline number in `calibration_results.md` so the verdict is reconstructible from first principles.*

---

## 1. What we're measuring, and why

Two raters — me, screening blind against §B6/§B7; Elicit, screening the same 200 RIS records against the four-criterion rendering with strict criteria OFF and no overrides. Neither rater is ground truth. The calibration question is **how often do we agree, and how often does Elicit drop a paper I would keep**.

I pre-registered (in `calibration_test_plan.md`) three thresholds for committing to Elicit as an AI second-screener:

| Threshold | Required | Why this metric |
|---|---|---|
| **Recall of my includes** | ≥ 95 % | A scoping review treats false negatives as the dominant error mode — a paper I would have kept that Elicit drops, never gets read. |
| **Cohen's κ (binary, as-deployed)** | ≥ 0.60 | "Substantial" agreement on the Landis-Koch scale; corrects raw agreement for the agreement-by-chance that prevalence inflates. |
| **All 8 empirical seeds screened IN** | 8/8 | Known-positive sanity check; the calibration uses agreement, but the seeds are the one place I do have correct answers. |

The decision rule was: commit if all three pass; fall back to decision-support if recall is 90–95 % or κ is 0.40–0.60; reject if anything is worse.

The rest of this doc shows the arithmetic on the **blind** dataset (what the pre-registration was tested against) and on the **reconciled** dataset (what the working corpus actually looks like after I read the disagreements). Both pass; the reconciled numbers are stronger.

---

## 2. The blind dataset (the formal calibration)

After dropping the 1 blank human decision among the 195 paired records, n = 194. Binary collapse: maybe → include throughout (high-sensitivity scoping default).

Confusion table (rows = me, columns = Elicit):

|               | Elicit: exclude | Elicit: include | Row total |
|---|---:|---:|---:|
| **Me: exclude** | 77 | 13 | **90** |
| **Me: include** | 2  | 102 | **104** |
| **Column total** | **79** | **115** | **194** |

The four cells are the things I'll be computing with.

---

## 3. Raw agreement

The simplest metric: fraction of records where Elicit and I gave the same binary verdict.

$$p_o = \frac{\text{diagonal}}{n} = \frac{77 + 102}{194} = \frac{179}{194} = 0.9227 \approx 92.3\%$$

This is what most people mean when they say "we agreed on 92 %." It's necessary but not sufficient — agreement could be high just because most papers are easy excludes.

---

## 4. Cohen's κ (binary, as-deployed)

κ adjusts raw agreement for the agreement two raters would get by chance, given their marginal rates of using each label. Formula:

$$\kappa = \frac{p_o - p_e}{1 - p_e}$$

I already have *p₀* = 179/194. I need *pₑ*, the expected agreement under independence.

Marginal probabilities (from the row/column totals above):

| | exclude | include |
|---|---:|---:|
| **Me** | 90 / 194 = 0.4639 | 104 / 194 = 0.5361 |
| **Elicit** | 79 / 194 = 0.4072 | 115 / 194 = 0.5928 |

Expected agreement = chance of both saying exclude + chance of both saying include, under independence:

$$p_e = (0.4639)(0.4072) + (0.5361)(0.5928) = 0.1889 + 0.3178 = 0.5067$$

Plug in:

$$\kappa = \frac{0.9227 - 0.5067}{1 - 0.5067} = \frac{0.4160}{0.4933} = 0.8434 \approx 0.843$$

On the Landis-Koch interpretation banding:

| κ range | Interpretation |
|---|---|
| < 0.00 | poor (worse than chance) |
| 0.00 – 0.20 | slight |
| 0.20 – 0.40 | fair |
| 0.40 – 0.60 | moderate |
| 0.60 – 0.80 | substantial |
| **0.80 – 1.00** | **almost perfect** |

κ = 0.843 sits in *almost perfect* and clears the pre-registered ≥ 0.60 threshold comfortably. Note that with n = 194 the standard error on κ is roughly 0.05, so the confidence interval is something like [0.74, 0.94] — solidly in the substantial-to-almost-perfect range no matter how the wobble lands.

---

## 5. Why κ rather than raw agreement

If 90 % of records are excludes (lopsided prevalence), even two random raters who always picked the majority label would hit ~81 % raw agreement just by guessing the modal answer. κ explicitly subtracts that chance baseline out:

- Blind raw agreement: 92.3 %
- Blind chance agreement (pₑ): 50.7 % (less lopsided than I assumed because Elicit and I both use include for ~55–60 %)
- Excess over chance: 92.3 % − 50.7 % = 41.6 percentage points
- κ scales that excess against the maximum possible excess (100 % − 50.7 % = 49.3 points): 41.6 / 49.3 = 0.843

So κ says: of the agreement we *could* have shown on top of pure chance, we achieved 84 % of it.

---

## 6. Recall of my includes (the most important number for a scoping review)

In the language of the 2×2:

$$\text{Recall} = \frac{\text{Elicit-include AND I-include}}{\text{Total I-include}} = \frac{TP}{TP + FN} = \frac{102}{102 + 2} = \frac{102}{104} = 0.9808 \approx 98.1\%$$

That is, of the 104 papers I would have kept, Elicit dropped 2.

For a scoping review this is the single most consequential metric, and it's why I weighted it as the first pre-registered threshold. The other failure direction — Elicit *over-includes* 13 papers I'd exclude — gets caught at manual reconciliation. The 2 papers Elicit drops would never be read.

Recall ≥ 95 % was the threshold. 98.1 % passes.

---

## 7. Strict-AND aggregation — and why I rejected it as a deployment rule

After the calibration, I considered overriding Elicit's binary verdict with the protocol's own strict-AND logic: *exclude if any of the four per-criterion calls is `no`*. The idea was to catch the 10 over-includes where Elicit's per-criterion analysis itself said the paper failed but its strict-OFF score-threshold kept it as Include.

To test this honestly, I had to run the rule against the **reconciled** dataset (n = 195 — see §9 below) and check both directions, not just the ones I was hoping to catch.

The 2×2 under strict-AND override:

|               | E-strict: exclude | E-strict: include | Row total |
|---|---:|---:|---:|
| **Me: exclude** | 89 | 3 | **92** |
| **Me: include** | 23 | 80 | **103** |
| **Column total** | **112** | **83** | **195** |

The strict-AND override drops **23 of my 103 includes** — papers where Elicit's per-criterion call failed on one or more axes but where, having read the abstract myself, I judged the paper in-scope. Recall under this rule:

$$\text{Recall}_{\text{strict-AND}} = \frac{80}{103} = 0.7767 \approx 77.7\%$$

That's a 22.5-point recall hit, far below the pre-registered ≥ 95 % floor and unacceptable for a scoping review. I swept the rule space:

| Rule | Recall preserved | Drift caught |
|---|:-:|:-:|
| R1 strict-AND (any `no` → exclude) | 77 % | 77 % |
| R2 substantive-no (cons=no OR meas=no → exclude) | 77 % | 77 % |
| R3 double-substantive (cons=no AND meas=no → exclude) | 95 % | 15 % |
| R4 score < 3.0 + any `no` | 83 % | 77 % |
| R5 score < 3.0 + substantive `no` | 83 % | 77 % |
| **R0 as-deployed (no override)** | **100 %** | 0 % (manual reconciliation handles drift) |

R3 is the least bad of the override rules: 95 % recall preserved, but it catches only 2 of 13 drift cases. The trade is *drop 5 real includes to save 2 manual reads*. That's a clearly bad trade for a scoping review.

R0 (as-deployed, no override) dominates. The 13 over-includes per 200 records become a manual reconciliation load of ≈ 6.5 % of the corpus, all in the safe direction.

The decisive piece of evidence — independently of the rule sweep — is that **both Luppi seed papers (NeuroImage 2022 *metastability/fractal* and Nat Neurosci 2022 *synergistic core*) get cons=no from Elicit**, even though both are substantively in-scope. Any rule that excludes on cons=no drops a known-positive seed. The Luppi case is the third independent confirmation that strict-AND override would harm recall on real consciousness work.

---

## 8. Seeds — the known-positive sanity check

Eight empirical seeds, all included by exception under the search-recovery mechanism, were run through the same Elicit setup as `calibration_seeds.ris`. All 8 came back Include (as-deployed). The canonical Luppi paper was re-tested after the seed-lookup bug fix in `pilot_search.py`; same Include verdict, same cons=no pattern.

**8/8 — gate passes.** Combined with recall 98.1 % and κ 0.843, all three pre-registered thresholds clear.

---

## 9. Reconciled dataset (working corpus, n = 195)

After reading the 15 disagreements with both Elicit's per-criterion rationale and my blind notes in view, I made the following changes:

- **2 maybe-zone flips:** PMID 38136525 (Black-holes-entropy) Include → Exclude; PMID 33504952 (brain-heart desync) Maybe → Exclude.
- **3 maybe-zone confirmations:** PMID 18990620, 20626893, 25837427 stay Exclude.
- **10 aggregation-drift confirmations:** my original blind Excludes confirmed on re-read.
- **1 blank filled:** PMID 16632826 (Ellerkmann 2006, spectral entropy + BIS under propofol) → Include.

That gives n = 195 valid paired records. Reconciled 2×2:

|               | Elicit: exclude | Elicit: include | Row total |
|---|---:|---:|---:|
| **Me: exclude** | 79 | 13 | **92** |
| **Me: include** | 0  | 103 | **103** |
| **Column total** | **79** | **116** | **195** |

Quick recompute, same formulas as §3–6:

- Raw agreement: (79 + 103) / 195 = 182/195 = **93.3 %**
- Marginals: me-exc = 92/195 = 0.4718; me-inc = 103/195 = 0.5282; elicit-exc = 79/195 = 0.4051; elicit-inc = 116/195 = 0.5949
- *pₑ* = (0.4718)(0.4051) + (0.5282)(0.5949) = 0.1911 + 0.3143 = 0.5054
- κ = (0.9333 − 0.5054) / (1 − 0.5054) = 0.4279 / 0.4946 = **0.865**
- Recall = 103 / (103 + 0) = **100 %**

The reconciled κ is slightly higher (0.865 vs 0.843) and recall is perfect — both because the 2 blind Includes that flipped to Exclude were exactly the H-include / E-exclude cells (the dangerous direction), and reconciliation moved them into agreement.

---

## 10. Verdict

| Pre-registered threshold | Required | Blind value | Reconciled value | Verdict |
|---|---:|---:|---:|:-:|
| Recall of my includes | ≥ 95 % | 98.1 % | 100 % | ✅ pass |
| Cohen's κ (as-deployed) | ≥ 0.60 | 0.843 | 0.865 | ✅ pass |
| Seeds screened IN | 8/8 | 8/8 | — | ✅ pass |

All three thresholds clear comfortably. Substantive disagreements after diagnosis: zero. **Commit to Elicit as AI second-screener under the as-deployed rule (strict criteria OFF, no override, manual reconciliation of disagreements).**

The κ I'd report in a methods paper is the **blind** value (0.843), because that's the calibration as the protocol pre-registered it; the reconciled value (0.865) describes the working corpus but was computed after I read Elicit, so it's not a clean rater-agreement measure.

---

*All numbers in this doc can be reproduced from `calibration_200_screening (human).csv` (blind) or `calibration_200_screening_reconciled.csv` (reconciled) and `elicit_calibration_200_export-6d61a5b1.csv`, using the join logic in `calibration_analysis.py`.*
