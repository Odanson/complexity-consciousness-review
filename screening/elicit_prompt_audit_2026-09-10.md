# Audit — calibrated Elicit prompts against protocol v0.5.1

**Audit date:** 2026-09-10
**Auditor:** Samson Odan (with review-assistant cross-check)
**Purpose:** Before starting the production Elicit run on the 8,581-record corpus, re-verify that the four calibrated screening prompts in `protocol/elicit_screening_prompts.md` remain decision-equivalent to the frozen protocol §B3 (PECO), §B4 (include/exclude), §B6 (search-strategy concept blocks), and §B7 (screening model). No protocol changes have been made since v0.4.3 → v0.5.1; this audit re-runs the criterion-level equivalence check on the record.

**Result: PASS.** All four criteria remain a faithful English-language rendering of the frozen eligibility logic. No prompt edits required. One documentation note on grey-zone routing (see §3 below), no action.

---

## 1. Criterion-level mapping (re-verified)

| Elicit criterion | Frozen protocol backing | Equivalence status |
|---|---|---|
| **C1 Consciousness Research Context** — investigates consciousness, states / transitions, or interprets findings in relation to consciousness or its neural signatures. | §B3 P (consciousness / state list) + §B4 include #3 (consciousness claim) + §B6 Block 1 (consciousness / state term set). | Match. C1's example list (wakefulness, sleep, anaesthesia, DOC, psychedelics, meditation, dreaming, conscious perception) is a strict subset of §B6 Block 1's OR-list, and the "OR explicitly interpret findings in relation to consciousness or neural signatures / mechanisms of consciousness" clause is a direct rendering of §B4 include #3. |
| **C2 Empirical Neural Data Application** — analyses empirical neural recordings, OR systematically reviews studies that do. | §B3 P (modality list) + §B6 Block 3 (neural-data term set) + §B4 include #1 (peer-reviewed empirical / eligible preprint / systematic review). | Match. C2's modality enumeration (EEG, MEG, fMRI/BOLD, ECoG/iEEG, LFP, single/multi-unit, calcium imaging, TMS-EEG) is a strict subset of §B3 P; the "OR systematically review / meta-analyse" clause was added at v0.4.3 to keep decision-equivalence with §B4 include #1 (which now explicitly covers systematic reviews and meta-analyses of eligible empirical studies). |
| **C3 Quantitative Complexity-Family Measures Applied** — applies (or systematically reviews the application of) one or more quantitative complexity-family measures as a primary analysis, rather than only proposing or theoretically discussing them. | §B3 E (index broadly defined) + §B6 Block 2 (complexity-variant terms) + §B12 Axis 1 (mathematical primitive families) + §B4 exclude #3 (mentioned in prose but not quantified) + §B4 exclude #1 (pure theory / simulation-only). | Match. C3's enumerated list (entropy family, LZ, Kolmogorov, PCI/ST-PCI, MI, TE, GC, wSMI, DFA, multifractal, avalanches, metastability, PLV/wPLI, criticality, φ-family, ACW/PLE/TRW, dimensionality/manifold) is a strict subset of §B6 Block 2 and the §B12 Axis-1 catalogue. The "as a primary analysis... rather than only proposing or theoretically discussing" guard closes the loop against §B4 exclude #1 and #3. |
| **C4 Eligible Study Type** — empirical research article, systematic review, or meta-analysis; not solely conference abstract, editorial, commentary, opinion piece, narrative perspective, or theoretical / simulation-only. | §B4 include #1 (peer-reviewed article or eligible preprint; systematic reviews / meta-analyses now explicit) + §B4 exclude #4 (conference abstract / editorial / commentary without original analysis) + §B4 exclude #1 (pure theory / simulation-only). | Match. C4 is deliberately stripped of the data-type and empirical/theoretical clauses (those duplicated C2 and C3 pre-v0.4.3 and were removed to keep the four criteria orthogonal); the residual publication-type filter is exactly §B4 exclude #4 rewritten as an include prompt. |

## 2. Deployment configuration (re-verified)

| Configuration | Frozen setting | Backing |
|---|---|---|
| Strict criteria | **OFF** | §B7 step 5 (scoping-review default; strict-AND override was pre-registered as *rejected* — `calibration_results.md` §"Correction to the deployment-rule recommendation"). Strict-AND would have dropped 23/103 reconciled human-includes, recall 77.7%, below the pre-registered ≥ 95% floor. |
| Post-aggregation override rule | **none** | §B7 step 5 (Elicit's aggregated binary is a recommendation; human reviewer reconciles disagreements). |
| No-abstract records | Silently omitted by Elicit; flagged for manual exception documentation. | §B7 step 5. Updated coverage estimate for the production corpus: **2,632 / 8,581 (30.7%)** — much higher than the 2.5% seen on the PubMed-only calibration subsample. Manifest already written: `elicit_unassessable_no_abstract_manifest.csv`. |
| Per-criterion exports | yes/no/maybe + rationale + source-quote CSV per record. | §B7 step 5. |
| Elicit version + run date | Recorded at run start in `screening_run_log.md` §0. | §B7 step 5 (release-version reproducibility). |

## 3. Documentation note — grey-zone routing (no action)

The §B4 grey zones (simulation-that-validates-on-a-neural-like model; pharmaco-EEG post-hoc consciousness framing; anaesthesia-monitoring "BIS-style" black-box indices) are *not* rendered as explicit Elicit criteria. They are handled correctly by the layered pipeline:

- **Upstream (search).** §B6 Block 2 is the substantive content filter; a proprietary black-box index with no exposed complexity component will typically fail to match Block 2 and never reach Elicit.
- **In Elicit.** Under strict-OFF aggregation, borderline cases return `maybe` on the boundary criterion and pass through as low-confidence Include. This matches the calibrated behaviour: 15 paired disagreements on the 200-record subsample were all diagnosed as aggregation drift or boundary-criterion `maybe`, none as substantive misclassification.
- **In human reconciliation.** §B7 step 5 reconciles all human–Elicit disagreements; grey-zone routing is triggered there.

No prompt edit needed. The grey-zone handling is documented here for the audit trail and cross-referenced from the run log's §5 (reconciliation plan).

## 4. Non-rendered criteria — separation of concerns (no action)

Two frozen eligibility filters are **not** rendered as Elicit criteria, by design:

- **Date range (1990–present, pre-1990 seminal-methodological exception).** Enforced upstream by the search strings (`database_queries.md`); the corpus reaching Elicit is already date-filtered. Rendering this as an Elicit criterion would be redundant and add noise.
- **English full text available.** Same treatment — enforced upstream by database-level language filters (v0.4.3 decision, re-affirmed).

## 5. Amendments-log entry (proposed)

None required. This audit re-verifies the deployment configuration frozen at v0.4.4 and carried into v0.5.1; no prompt or configuration change is proposed. The audit itself is logged here and cross-referenced from `screening_run_log.md` §0 as a pre-flight artefact.

## 6. Cross-references

- Canonical prompts: `protocol/elicit_screening_prompts.md`
- Registered calibration: `calibration/calibration_test_plan.md`, `calibration/calibration_results.md`, `calibration/calibration_equivalence_audit.md`
- Deployment run log: `screening/screening_run_log.md`
- Unassessable-records manifest: `screening/elicit_unassessable_no_abstract_manifest.csv`
- Protocol (frozen): `protocol/prisma_protocol_v0.5.1.md` §B3 · §B4 · §B6 · §B7 · §B12
