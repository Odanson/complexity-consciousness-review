# Complexity Measures of Consciousness — PRISMA Review Protocol

**Version 0.5.1 — 2026-06-04 (registration-ready)**

**Lead reviewer:** Samson Odan
**Supervisors:** Jurgen Jost, Lucia Melloni, Andrej Bicanski
**Planned external collaborators (later phase):** Adam Barrett, Anil Seth
**Provisional authorship (in order):** Samson Odan, Lucia Melloni, Andrej Bicanski, Jurgen Jost. May extend on contribution to include Adam Barrett and Anil Seth.

---

## Executive summary

"Complexity" is used in consciousness science to refer to fundamentally different mathematical objects — entropy of a signal, compressibility of a binary string, integration of information across a partition, criticality of dynamics, graph topology, manifold dimension, the geometry of a "qualia space." These are not interchangeable. A reader of the literature today has no clean map from *measure → what it computes → what it can warrant about consciousness*.

This review will produce that map. It will (i) systematically map and characterise quantitative complexity measures applied to neural data in consciousness research, (ii) classify the included corpus along eight orthogonal axes (mathematical primitive, data requirement, temporal granularity, aspect of consciousness, spatial scale, theory anchoring, inferential status, validation evidence), (iii) audit the fit between each included measure's mathematical content and the claims made with it, and (iv) identify conceptual and methodological gaps, including potential gaps relating to the structural geometry of experience and the representation of temporal experience.

The primary deliverable is a peer-reviewed review manuscript. It will be accompanied by an open companion resource consisting of the extraction dataset and taxonomy tables hosted on OSF. An interactive web resource may be developed subsequently as a dissemination layer for the field.

---

## Part A — Scientific framing

### A1. Problem statement
"Complexity" has become a load-bearing word in consciousness science without a shared referent. Different authors mean: entropy of a signal, compressibility of a binary pattern, integration of information across a partition, criticality of dynamics, richness of a graph, dimensionality of a manifold, or the geometry of a conceptual "qualia space." These measures are not interchangeable. They quantify **different mathematical primitives** and therefore can only license **different claims** about consciousness. A neuroscientist or psychologist reading the literature today has no clean map from *measure → what it computes → what it can and cannot warrant about consciousness → how the measure relates to a given theoretical construct or theory*. This review will produce that map.

### A2. Review aims
1. **Systematically identify and catalogue** quantitative complexity measures applied to neural data — invasive or non-invasive, in humans or non-human animals — in consciousness research.
2. **Classify** the corpus along orthogonal axes — mathematical primitive, data requirements, spatial scale, temporal granularity, theory anchoring, inferential status (causal vs descriptive), validation evidence, aspect of consciousness addressed.
3. **Audit** the fit between each measure's mathematical content and the claims made with it (misuse, overreach, hidden assumptions — e.g., Granger causality as directionality in a densely interconnected system; IIT proxies that use amplitude only and ignore effective connectivity; descriptive measures interpreted post-hoc as theory-confirming).
4. **Map** measures to aspects of consciousness: level, content, integration, differentiation, structural geometry of experience, temporal flow.
5. **Guide** future use: produce a decision table of the form "if your question is X, consider measures Y; if your theory is X, consider measure Y; avoid Z because…".

### A3. Out of scope
- Philosophical debates about the meaning of consciousness, except where they constrain measurement.
- Purely theoretical complexity papers with no neural-data application (included only if cited as a methodological reference by an empirical paper already in the pool).
- Non-neural complexity (cardiac, metabolic, behavioural) unless used as a control variable in a consciousness study.
- **Theory adjudication** — we do not arbitrate between IIT, GNW, HOT or other theories. We *do* catalogue each measure's theoretical provenance (PQ5, Axis 6 — theory anchoring) and surface post-hoc theoretical re-interpretation where it occurs (PQ7); we do not score theories against one another on the back of this review.

> **Note on the memory–consciousness interface.** Memory-derived complexity measures (replay complexity, memory-state entropy, engram-related metrics) are *deliberately out of scope*. Consciousness and memory dissociate (amnesiacs are conscious), so the review can scope consciousness cleanly without them. The interface is flagged here as a candidate for a follow-on paper, not as an appendix to this review.

> **Note on cross-species data.** Non-human animal data is in primary scope (several core measure families — neural avalanches, single-unit-derived entropies, dense-array criticality — are only tractable in animal data). Findings are reported with explicit interpretive care about translation to human consciousness; this caveat is enforced in the §B8 extraction form (Design: species + translation-caveat field) and in the §B11 synthesis tables.

### A4. Review type and registration
- **Review type.** Methodological / measurement-focused. PRISMA 2020 reporting; PRISMA-P 2015 for the protocol. Because the goal is to map measures rather than synthesise effect sizes, **PRISMA-ScR** (scoping-review extension, Tricco et al. 2018) is likely the better fit — to be confirmed under §C1.
- **Pre-registration.** OSF Registries (target). PROSPERO is a fallback but has historically rejected purely methodological scoping reviews.

---

## Part B — Protocol

### B1. Administrative

| Field | Value |
|---|---|
| Working title | Complexity measures of consciousness: a methodological review of what they compute and what they can warrant |
| Protocol version / date | v0.5.1 / 2026-06-04 (registration-ready; supervisor sign-off complete) |
| Registry | OSF Registries (target) |
| Lead reviewer | Samson Odan |
| Provisional authorship (in order) | Samson Odan; Lucia Melloni; Andrej Bicanski; Jurgen Jost. Adam Barrett and Anil Seth to be added on contribution. |
| Screening model | Single human reviewer with AI-assisted second screening (Elicit, calibrated 2026-05-28) + ASReview active-learning prioritisation; within-person test-retest for self-consistency (see §B7). Precedent: Yaron, Melloni, Pitts & Mudrik 2022, *Nat Hum Behav* |
| Arbiter | Any two of Jurgen Jost, Lucia Melloni, Andrej Bicanski |
| Funding | Max Planck School of Cognition |
| Progress-review cadence | Monthly. |
| Milestone schedule | **Late June 2026 — operational checkpoint** (multi-database search executed and locked; deduplicated corpus available; Elicit + ASReview screening pipeline operational on the dedup corpus; database access fully confirmed). **Late July 2026 — substantive scientific checkpoint** (bulk screening progressing; preliminary corpus characterisation; early Axis-1 mapping on includes-so-far). **August–September 2026 → synthesis and manuscript trajectory** (extraction underway; gap heatmap emerging; manuscript outline). |

#### B1.2 Author ORCIDs and affiliations

| Author | ORCID | Affiliations |
|---|---|---|
| Samson Odan | 0009-0002-2909-0831 | (1) Max Planck Institute for Human Cognitive and Brain Sciences, Dept. of Psychology; (2) Max Planck Institute for Mathematics in the Sciences; (3) ScaDS.AI Dresden/Leipzig; (4) Max Planck School of Cognition; (5) Predictive Brain Department, University Alliance Ruhr, Faculty of Psychology, Ruhr-University Bochum |
| Lucia Melloni | 0000-0001-8743-5071 | (1) Predictive Brain Department, University Alliance Ruhr, Faculty of Psychology, Ruhr-University Bochum; (2) Department of Neurology, NYU Grossman School of Medicine; (3) Canadian Institute for Advanced Research (CIFAR), Brain, Mind, and Consciousness Program |
| Andrej Biçanski | 0000-0003-3356-1034 | (1) Max Planck Institute for Human Cognitive and Brain Sciences, Dept. of Psychology; (2) ScaDS.AI Dresden/Leipzig |
| Jürgen Jost | 0000-0001-5258-6590 | (1) Max Planck Institute for Mathematics in the Sciences; (2) Max Planck Institute for Human Cognitive and Brain Sciences, Dept. of Psychology; (3) ScaDS.AI Dresden/Leipzig; (4) Santa Fe Institute Santa 1399 Hyde Park Road, Santa Fe, New Mexico 87501, United States of America |
| Amendments log | Maintained at the end of this document |

### B2. Review questions

**PQ1 (primary).** Which quantitative complexity measures have been applied to neural recordings in consciousness research, and what does each measure mathematically compute?

**PQ2.** For each measure, what aspect of consciousness (level, content, integration, differentiation, structure, temporal flow) has been claimed, and is that claim warranted by the measure's mathematical content and by the study's data and design?

**PQ3.** Where are measures being misapplied — for example, directional inference from correlational measures; effective-connectivity claims from amplitude-only metrics?

**PQ4.** What are the systematic gaps — aspects of consciousness for which no fit-for-purpose complexity measure currently exists? Candidates: structural geometry of experience; subjective temporal flow.

**PQ5 — Theory provenance.** For each measure, what theoretical framework (if any) does it derive from, and is the measure (a) the canonical operationalisation of that theory, (b) one of several non-equivalent proxies for it, or (c) theory-agnostic in origin and adopted post-hoc?

**PQ6 — Within-theory operationalisation drift.** For theories with multiple empirical proxies (IIT: φ, φ*, geometric φ, whole-minus-sum, φ-ID; GNW: ignition / global-broadcast indices / late-P3 surrogates; predictive processing: entropy-rate variants), do the proxies converge on the same data and the same rank-ordering of states? Where they diverge, is the divergence acknowledged in the source paper?

**PQ7 — Post-hoc theoretical re-interpretation.** Are descriptively-derived measures (LZc, sample entropy, DFA) being interpreted as evidence for specific theories they were not built to test, and on what justification?

> *Optional — PQ8 (Theory-discriminating power)* — deferred to v1.1 or a follow-on paper. Considered for inclusion but parked on scope grounds: would require committing up front to a fixed list of ≤ 5 competing theory predictions, and risks turning a methodological review into a theory-comparison paper.

### B3. Eligibility — PECO framing

We adapt PICO/PECO to a methodological review:

- **P (Population / data).** Human or non-human animal neural recordings, any modality (EEG, MEG, iEEG / ECoG, fMRI, LFP, single-unit, two-photon calcium, wide-field optical).
- **E (Exposure / Index).** Application of at least one quantitative complexity measure (defined broadly — see §B12) to those recordings.
- **C (Comparator).** Either (i) a different state of consciousness (awake vs. sleep / anaesthesia / DOC / psychedelic / meditation / coma / LIS), (ii) a different measure on the same data, or (iii) a within-state correlation with a subjective or behavioural read-out.
- **O (Outcome).** Any claim linking the measure's values to an aspect of consciousness — discrimination, correlation, prediction, mechanistic explanation, or negative result.

### B4. Inclusion / exclusion criteria

**Include** if all of:
1. Peer-reviewed journal article, *or* a preprint that (a) applies a quantitative complexity measure to neural data, (b) makes a consciousness claim, (c) is not retracted, and (d) has an openly available full text. No minimum citation count is required — a numeric threshold would be age-biased against recent strong work and is not earned by the rest of the criteria, which already enforce quality (no abstracts/editorials, quantitative measure required, consciousness claim required).
2. Applies at least one quantitative complexity measure to neural data.
3. Makes or tests a claim relevant to consciousness (level, content, state discrimination, structure).
4. Published 1990-01-01 to search date — earlier only for seminal methodological papers (e.g., Tononi-Sporns-Edelman 1994 neural complexity).
5. English full text available.

> **English-only framing — decision recorded v0.4.3 (Lucia, 2026-05-14).** Jurgen suggested (2026-05-12) tentatively extending the search to include French- and German-language abstracts. After consultation with Lucia, this is declined: (a) the highest-impact consciousness-neuroscience publications — including those originating in francophone and germanophone research groups — are overwhelmingly published in English; (b) extending coverage to non-English literature would impose a screening burden disproportionate to the marginal coverage gain, particularly under the solo-reviewer screening model adopted in §B7; (c) any high-value non-English paper not captured by the English-language search is recoverable through §B5 backward / forward citation tracking on the seed set. The English-language inclusion criterion is therefore retained as in v0.1 and acknowledged as a documented scoping decision.

**Exclude** if any of:
1. No neural data (pure theory, or simulation-only without a stated empirical extension).
2. Consciousness is mentioned but not measured or manipulated (e.g., a sleep-staging paper that frames no claim about consciousness).
3. Complexity is mentioned in prose but not quantified.
4. Conference abstract, editorial, or commentary without original analysis.
5. Non-English without available translation.
6. Duplicate report of the same dataset and analysis (keep the most complete).

**Grey zone — flag for supervisor decision:**
- Simulation studies that propose a measure and validate against a neural-like model (include if the measure is widely used on real data elsewhere).
- Pharmaco-EEG studies where the consciousness framing is post-hoc.
- Anaesthesia-monitoring papers (BIS-style) — include only if they analyse complexity as such, not where complexity is a black-box component of a proprietary index.

### B5. Information sources

Each database is justified per PRISMA-S item 3 (one-line rationale).

**Databases.**
- **PubMed / MEDLINE** — primary biomedical index; canonical for the consciousness-neuroscience corpus.
- **Scopus** — broader interdisciplinary coverage including engineering and computational venues that PubMed under-indexes; strong for methods papers.
- **Web of Science (Core Collection)** — independent indexing path; Keywords-Plus expansion catches papers PubMed misses on text alone.
- **PsycINFO** — psychology / cognitive-science journals (some not in MEDLINE) and the behavioural-paradigm literature that anchors consciousness claims.
- **IEEE Xplore** — engineering and signal-processing venues where novel measure proposals first appear; conference papers carry real signal in this literature.

**Preprints.** bioRxiv, **medRxiv** (clinical / DOC / anaesthesia preprints land here, not bioRxiv), arXiv (q-bio.NC, cs.IT), PsyArXiv — inclusion per the revised §B4 criterion 1 (no citation threshold).

**Hand-search.** *Neuroscience of Consciousness*; *Consciousness and Cognition*; *NeuroImage*; *PLoS Computational Biology*; *Journal of Neuroscience*; *Cerebral Cortex*; *Brain*; *Current Biology*; *Nature Communications*; *eLife*; *PNAS* (key venue for seed-list papers — Tononi-Sporns-Edelman 1994, Toker 2022); *Anesthesiology* or *British Journal of Anaesthesia* (broad-scope venues where complexity-of-consciousness work currently lands but our previous list missed).

**Backward / forward citation tracking.** Performed using **Citationchaser** (free, reproducible, Zotero-integrated) — named here per PRISMA-S item 3 (citation-tracking is not reproducible without a named tool). Seed set in §B9.

**Expert elicitation.** Suggestions solicited from Jurgen, Lucia, Andrej, Anil Seth, and Adam Barrett; every suggestion logged together with whether the database search already captured it (this gives a sensitivity estimate).

**Reference paper for measure-to-NCC mapping.** Yaron, Pitts, Mudrik & Melloni 2024, *Neurosci & Biobehav Rev* (PII: S0149763424001398) — used as a measure-mapping precedent. The Block 2 term list and §B12 taxonomy are cross-checked against the measures catalogued there.

### B6. Search strategy — locked v1.0

Three concept blocks, ANDed. Each block is an OR of synonyms. The PubMed string below is the canonical reference; equivalent translations for Scopus, Web of Science, PsycINFO, and IEEE Xplore are in the companion document **`database_queries.md`** and use the same blocks with database-specific field tags.

> **What counts as "complexity" in this review (added v0.4.2 on Jurgen's request).** Block 2 is the **agreed-upon, explicit set of complexity-variant terms** for this review — it converts an otherwise diffuse concept ("complexity") into a reviewable inclusion criterion. A paper is retrieved by the search only if it matches at least one Block 2 term in its title, abstract, MeSH headings, or indexed keywords. The list was iteratively constructed and expanded through pilot rounds: initial draft in v0.1; expanded in v0.3 to recover Schartner / Casarotto framings; expanded in v0.4 with the phase / dynamical-systems family (PLV, wPLI, metastability, chimera-state, phase coherence) after Lucia's review (2026-05-10); expanded in v0.4.1 to incorporate the GNW / IIT / TTC measure families catalogued by Chis-Ciure, Melloni & Northoff 2024 *NBR* (wSMI, ACW, PLE, TRW, ST-PCI, multifractal DFA, state differentiation, scale-free, GS-topography). Any further expansion triggers a re-pilot and a new version of the protocol; see the amendments log.

**Block 1 — Consciousness / state**
```
(consciousness OR "state of consciousness" OR "levels of consciousness"
OR "loss of consciousness" OR unconscious* OR wakefulness OR arousal
OR anesthesi* OR anaesthesi* OR sedation OR propofol OR sevoflurane
OR ketamine OR xenon OR sleep OR NREM OR REM OR "slow wave sleep"
OR "vegetative state" OR "unresponsive wakefulness syndrome" OR UWS
OR "minimally conscious state" OR MCS OR coma OR "locked-in syndrome"
OR LIS OR psychedelic* OR psilocybin OR LSD OR DMT OR ayahuasca
OR meditation OR mindfulness OR dream* OR lucid)
```

**Block 2 — Complexity / information / dynamics**
```
("Lempel-Ziv" OR LZc OR LZ76 OR LZW OR compressibility
OR "Kolmogorov complexity" OR "Kolmogorov signal complexity" OR KSC
OR "perturbational complexity" OR PCI OR "PCI-state" OR "ST-PCI"
OR "state transitions complexity index"
OR "integrated information" OR IIT OR phi
OR "causal density" OR "causal emergence" OR "phi-ID"
OR "information decomposition" OR "state differentiation"
OR entropy OR "sample entropy" OR "approximate entropy"
OR "permutation entropy" OR "multiscale entropy" OR "spectral entropy"
OR "transfer entropy" OR "mutual information" OR "Granger causality"
OR "weighted symbolic mutual information" OR wSMI
OR "neural complexity" OR "matching complexity"
OR "neural avalanche*" OR criticality OR "branching parameter"
OR "long-range temporal correlation*" OR "detrended fluctuation analysis" OR DFA
OR "multifractal" OR "MF-DFA"
OR "fractal dimension" OR "correlation dimension" OR "Hurst exponent"
OR Lyapunov OR chaos
OR "intrinsic dimensionality" OR "participation ratio" OR manifold
OR "small-world" OR modularity OR "rich-club" OR "hierarchical complexity"
OR "signal complexity" OR "signal diversity" OR "EEG complexity"
OR "complexity measure*" OR "complexity marker*"
OR "phase-locking value" OR PLV OR "phase locking value"
OR "weighted phase-lag index" OR wPLI
OR metastability OR "chimera state*" OR "chimera-state*"
OR "phase coherence" OR "phase synchron*"
OR "autocorrelation window" OR ACW
OR "power-law exponent" OR PLE
OR "temporal receptive window*" OR TRW
OR "scale-free" OR "scale free"
OR "global signal topography" OR "GS-topography")
```

**Block 3 — Neural data**
```
(EEG OR electroencephalograph* OR MEG OR magnetoencephalograph*
OR iEEG OR ECoG OR intracranial OR "local field potential*" OR LFP
OR fMRI OR BOLD OR "functional magnetic resonance"
OR "single-unit" OR "multi-unit" OR "two-photon" OR "calcium imaging"
OR "wide-field" OR neuroimag* OR "brain activity" OR "neural recording*"
OR TMS OR "TMS-EEG" OR "TMS-evoked" OR "TMS evoked"
OR "transcranial magnetic stimulation")
```

**Final query.** `Block 1 AND Block 2 AND Block 3`. Filters: English; date 1990-01-01 to search date.

#### B6.1 Pilot results

| Pilot date | Block 2 spec | Block 1 | Block 2 | Block 3 | B1 ∧ B2 ∧ B3 |
|---|---|---:|---:|---:|---:|
| 2026-05-07 (v0.3 search) | original + signal-complexity additions | 1,550,317 | 524,399 | 1,356,030 | **4,580** |
| 2026-05-12 (v0.4.1 search) | + wSMI, phase / dynamical-systems family, ACW, PLE, TRW, KSC, MF-DFA, state differentiation, ST-PCI, scale-free, GS-topography | 1,551,682 | 559,496 | 1,357,089 | **5,267** |

The v0.4.1 Block 2 was extended after Lucia's docx review (2026-05-10) and after cross-checking Chis-Ciure, Melloni & Northoff 2024 *NBR* (the "Yaron paper"; PII S0149763424001398), which catalogues measure families associated with GNW, IIT, and the Temporospatial Theory of Consciousness (TTC). The TTC family in particular (ACW, PLE, TRW, scale-free measures) was absent from the v0.3 Block 2 and is now included.

The v0.4.1 expansion grew the intersection from 4,580 to 5,267 records (+15 %) — the new measure families brought ~700 additional papers into scope. The full intersection remains comfortably inside the target band of 3,000–15,000 and supports calibrated single-reviewer screening with active-learning prioritisation (per §B7). No further Block-2 narrowing is required.

#### B6.2 Seed-paper validation

As of the v0.4.1 pilot (2026-05-12), eight empirical seeds (§B9a) were checked against the locked search; **seven of eight are captured**.

The single remaining miss — Sitt et al. 2014, *Brain* (PMID 24919971) — is a **confirmed** database miss. Block 2 was deliberately broadened in v0.4.1 to include **wSMI** (weighted symbolic mutual information) specifically as a recovery attempt for Sitt 2014, since the paper uses wSMI prominently in its 92-marker battery. The v0.4.1 re-pilot showed `B2:–` for Sitt 2014 PMID despite the wSMI term being in the search — the paper's published abstract genuinely contains none of the technical measure names, only the title-level "neural signatures of consciousness" framing. Further broadening (e.g., adding `"neural signature*"`) was rejected on noise grounds across the planned multi-database search.

Sitt 2014 is therefore recovered through §B5 backward / forward citation tracking on the seed set, which it satisfies via virtually every captured DOC / EEG paper. This recovery path is documented in §B9a and the **confirmed** miss status was carried over from a provisional flag in v0.3 to a confirmed entry in v0.4.1.

The three methodology-only seeds (§B9b — Tononi-Sporns-Edelman 1994; Oizumi-Albantakis-Tononi 2014; Chis-Ciure, Melloni & Northoff 2024) are correctly **not** captured by the database search; all three are theoretical / derivation / framework papers without neural-data application. They enter the review via the §B4 seminal-methodological-paper exception, not via search, and are validated only by PMID resolution.

#### B6.3 Search audit trail

On the day of the locked multi-database search (after OSF registration), all five queries will be run within a 24-hour window. Raw query strings, date / time of execution, per-database hit counts, and exported result files will be archived as `search_log_YYYY-MM-DD.txt` plus per-database RIS exports in the OSF project. This file forms the audit trail PRISMA-ScR / JBI methodology requires.

**Execution model (recorded v0.5; Embase access constraint documented in Decision 9).** Search execution is **manual via each database's authenticated web interface** (institutional MPI/CBS login: Scopus, Web of Science, PsycINFO via EBSCO, IEEE Xplore confirmed working 2026-05-29; PubMed open-access). The locked conceptual query is translated into each database's specific syntax in `database_queries.md`, executed via the database's UI, and exported (RIS / CSV) with the verbatim query string and execution timestamp logged. *Code and automation are deliberately restricted to downstream stages* — deduplication QC, RIS parsing, provenance checks, corpus statistics, clustering, citation-network analysis, and taxonomy / gap analyses — and are not used to issue search queries. This separation keeps the search step auditable by hand at PRISMA-S level while reserving programmatic work for the parts of the pipeline where reproducibility and scale make code preferable.

**Database access: Embase.** Embase was originally planned as a sixth database to provide Emtree-based pharmacology coverage (relevant to anaesthesia-related consciousness research). Institutional access was investigated through MPI/CBS library services (unavailable) and alternative routes through ZB MED registration (successful, virtual card issued). However, Embase access is available only through a limited booking system with slots substantially outside the project's planned search-execution timeline. The scientific cost of delaying search execution, screening, and extraction by several weeks to accommodate external Embase access constraints was judged to exceed the expected marginal recall gain, particularly given the substantial redundancy with PubMed/MEDLINE and the breadth of the five-database corpus. The review therefore proceeds without Embase. This is recorded as an access limitation (external scheduling constraint), not as a methodological narrowing of review scope. No changes have been made to eligibility criteria, database-selection rationale, search strategy, or synthesis plans.

**Code and protocol archive.** The pilot-search script (`pilot_search.py`), the locked database queries (`database_queries.md`), the PRISMA-ScR / PRISMA-S checklist mapping (`prisma_checklist_mapping.md`), and this protocol are archived on Zenodo with a permanent DOI:

- **v0.5.1 (this version):** [10.5281/zenodo.20609130](https://doi.org/10.5281/zenodo.20609130)
- **Concept DOI** (always resolves to the latest released version): [10.5281/zenodo.20140263](https://doi.org/10.5281/zenodo.20140263)

The GitHub source repository linked by Zenodo will be made public on the day of OSF registration; the link will be added here at that time.

### B7. Study records — management, selection, extraction

**Reference management.** Zotero group library (shared with supervisors); export to RIS.

**Deduplication.** Bramer method in Zotero plus Rayyan's deduplicator; manual spot-check.

**Screening platform.** Rayyan (free, conflict-tracked) for calibration and screening management where appropriate; **ASReview** (van de Schoot et al. 2021, *Nat Mach Intell*) for active-learning prioritised bulk screening.

**Screening model — single human reviewer with AI-assisted second screening (Elicit) + ASReview active learning + within-person test-retest (revised v0.4.4).**

The lab has no available personnel capacity for a second *human* reviewer in any role. Supervisors will give feedback on completed work at progress milestones but will not perform screening, calibration, or quality-control re-screening. The protocol must therefore be feasible for a single human reviewer (Samson) operating alone. Following the JBI scoping-review methodology (Peters et al. 2020; Pollock et al. 2023) — which explicitly does not mandate dual independent screening — and following the published precedent of **Yaron, Melloni, Pitts & Mudrik 2022, *Nature Human Behaviour***, which published a scoping review in this exact field without dual independent screening, screening proceeds as follows. **Elicit (PRISMA-2020-compliant systematic-review workflow) serves as a formal AI second-screener; this is documented as an explicit deviation from PRISMA's default dual *independent human* screening, with the calibration outcome reported alongside (v0.4.4).**

1. **Self-calibration pass (solo reviewer).** Samson screens the first 200 title / abstract records in Rayyan with documented rationale per inclusion / exclusion decision. The inclusion rubric is revised iteratively where ambiguities surface. No second reviewer is involved at this stage.

2. **Within-person test-retest (after a 2-week gap).** Samson re-screens a 10 % random sub-sample of the calibration set (20 abstracts) blind to his original decisions; computes Cohen's κ for self-agreement; target κ ≥ 0.8. If lower, the rubric is refined further and the calibration set is re-screened in full. This step provides a documented self-consistency check in lieu of inter-rater reliability.

3. **Bulk title / abstract screening (ASReview active learning).** Samson runs ASReview on the full deduplicated corpus with active-learning prioritisation. Records are reordered by inclusion probability after each labelling decision. Stopping criterion: ≤ 5 inclusions in the last 100 records screened (the standard ASReview saturation heuristic). The unscreened tail is then sampled and audited rather than fully screened.

4. **Periodic test-retest during bulk screening.** Every 1,000 records, a 1 % random sample of recently-screened records is re-screened blind; drift in κ is logged. If drift becomes substantive (κ < 0.7 across consecutive checks), screening is paused and the rubric reviewed.

5. **AI-assisted second screening (Elicit, revised v0.4.4).** Every record is independently screened by Elicit's systematic-review workflow against a four-criterion rendering of §B6/§B7 eligibility (consciousness research context; empirical neural data application; quantitative complexity-family measures applied; eligible study type). **The verbatim research question and the four criterion prompts as deployed are recorded in `elicit_screening_prompts.md` (canonical reference for reproducibility).** Configuration: strict criteria OFF (scoping-review default), Elicit's binary verdict treated as a *recommendation*, all human–Elicit disagreements reconciled by Samson. No automated post-aggregation override is applied (the as-deployed configuration was shown to dominate any strict-AND alternative on the calibration set — see paragraph below). Elicit's per-criterion calls, rationales, and source quotes are exported (CSV / Excel) and retained as part of the audit trail; screening exports are archived in the OSF project and repository alongside the human reconciliation logs. Records returning no abstract (Elicit silently omits these — ≈ 2.5 % of the calibration set) are flagged and screened manually by exception. The deployment was calibrated against Samson's blind screening on a seeded random 200-record subsample of the PubMed-locked corpus (`calibration_test_plan.md`; calibration outcome reported below).

6. **Full-text screening (solo reviewer).** Samson performs full-text screening alone; reasons for exclusion logged. Volume at this stage is small (estimated 200–500 papers), making single-pass screening tractable.

7. **Supervisor consultation at month-end milestones.** Jurgen, Lucia, and Andrej review aggregated progress at the end of each month — included-set characteristics, inclusion-rate trajectory, edge cases flagged by Samson — and provide feedback that shapes the next month's rubric. Supervisor input is at the *protocol-revision* level, not at the per-paper screening level.

**Transparency.** The deviation from PRISMA's default dual *independent human* screening is documented here, in §C, in the OSF registration, and in the manuscript's *Limitations* section. The Yaron et al. 2022 NHB review is cited as published precedent for a single-human-reviewer scoping review in the same field; the Elicit AI-second-screening layer is documented as an additional reliability safeguard, not as a substitute for a second human reviewer.

**Calibration outcome (Elicit AI second-screener, recorded v0.4.4).** A pre-registered calibration was run on a seeded random 200-record subsample (`calibration_test_plan.md` registered three commit thresholds before any analysis). Outcome on the blind 194 paired records: Cohen's κ (binary, as-deployed) = **0.843** ("almost perfect"); raw agreement = 92.3 %; **recall of human-includes = 102/104 = 98.1 %**; **substantive disagreements = 0** (all 15 paired disagreements diagnosed as either Elicit's strict-OFF aggregation drift or boundary calls at fuzzy criterion edges); empirical-seeds gate = **8/8 Include**. All three pre-registered thresholds (recall ≥ 95 %; κ ≥ 0.60; 8/8 seeds) passed. After human reconciliation of the 15 disagreements (`calibration_adjudications.md`), the working-corpus values are κ = 0.865 and recall = 103/103 = 100 % on n = 195. Known limitation: Elicit's per-criterion call on the consciousness-context axis may return `no` for substantively in-scope information-theoretic / synergistic-information papers whose abstracts do not frame the consciousness link explicitly (reproduced on both Luppi 2022 seed papers — NeuroImage and Nat Neurosci); under the as-deployed rule these still pass Elicit's binary verdict via score, and any residual misses are recoverable through §B5 citation tracking. Full numbers, computations, and the disagreement classification are in `calibration_results.md`; arithmetic walkthroughs are in `elicit_metric_calculations.md` (working notes).

**PRISMA flow diagram** maintained from Rayyan / ASReview exports.

**Data extraction.** A piloted structured extraction form will be implemented in a version-controlled tabular environment and piloted on 10 studies, then revised if needed before bulk extraction begins. Samson extracts every included paper. A 10 % random sample is re-extracted by Samson after a ≥ 1-month delay (intra-rater test-retest); deviations are logged and resolved by re-reading the source. Supervisors review extraction outputs at month-end milestones but are not part of the extraction pipeline.

### B8. Data items (extraction fields)

For each included study:

- **Bibliographic:** authors, year, journal, DOI.
- **Design:** species, N, age, population (healthy / DOC / anaesthetised / etc.), state contrast, paradigm.
- **Recording:** modality, channels / voxels, sampling rate, reference, pre-processing pipeline (cite a clear description).
- **Measure(s):** name, exact mathematical variant, formula reference, implementation (toolbox / code / language), parameters (window, embedding dim., etc.).
- **Pre-processing assumptions:** stationarity, normalisation, binarisation, surrogate method.
- **Data requirement:** amplitude only / amplitude + connectivity / perturbation-based / multi-scale.
- **Claim(s):** what is inferred about consciousness; what aspect (level / content / integration / differentiation / structure / temporal flow).
- **Validation:** ground truth used (behavioural report, clinical diagnosis, pharmacological manipulation, etc.); classification accuracy / effect size / CI.
- **Statistical rigor:** multiple-comparison correction, surrogate controls, cross-validation.
- **Reproducibility:** code available (Y/N), data available (Y/N), parameters fully reported (Y/N).
- **Reported limitations / caveats** (verbatim quote).
- **Reviewer-flagged misapplications:** free-text field for concerns (e.g., "GC used for directionality on a densely coupled system").

### B9. Seed set

The seed set has two roles, separated below. **B9a (empirical seeds)** are used to validate that the locked database search captures the field's central empirical papers; any miss must be diagnosed and either fixed (by broadening the search) or documented (and recovered via §B5 citation tracking). **B9b (methodology-only seeds)** are theoretical / derivation papers that enter the review only via the §B4 seminal-methodological-paper exception and are therefore *not* expected to satisfy Block 3 of the search.

#### B9a — Empirical seeds (validate the locked search)

Status as of 2026-05-07 (pilot run against the locked PubMed string):

| # | Citation | PMID | DOI | Search status |
|---|---|---|---|---|
| 1 | Casali et al. 2013, *Sci Transl Med* — *A theoretically based index of consciousness independent of sensory processing and behavior* (PCI introduction) | 23946194 | 10.1126/scitranslmed.3006294 | Captured |
| 2 | Casarotto et al. 2016, *Ann Neurol* — PCI in DOC | 27717082 | — | Captured |
| 3 | Schartner et al. 2015, *PLoS ONE* — LZc in anaesthesia | 26252378 | — | Captured |
| 4 | Schartner et al. 2017, *Neurosci Conscious* — signal diversity in psychedelics | 28422113 | — | Captured |
| 5 | Sitt et al. 2014, *Brain* — *Large-scale screening of neural signatures of consciousness in patients in a vegetative or minimally conscious state* | 24919971 | 10.1093/brain/awu141 | **Known DB miss — recovered via §B5 citation tracking** |
| 6 | Carhart-Harris et al. 2014, *Front Hum Neurosci* — *The entropic brain* | 24550805 | — | Captured |
| 7 | Toker et al. 2022, *PNAS* — *Consciousness is supported by near-critical slow cortical electrodynamics* | 36522453 | — | Captured |
| 8 | Luppi et al. 2022, *Nat Neurosci* — synergistic core for human cognition | 35781077 | — | Captured |

Additional candidate seed papers identified during supervisor consultation:

- Tononi & Edelman (1998), Science (PMID: 9836629). Neural Complexity and the Dynamic Core hypothesis.
- Mediano et al. (2025) — Toward a unified taxonomy of information dynamics via Integrated Information Decomposition (φ-ID). Foundational framework integrating Partial Information Decomposition and Integrated Information theory to characterise synergistic, redundant, and unique information dynamics in complex systems. DOI: 10.1073/pnas.2423297122.
- Seth, Barrett & Barnett (2011) (PMID: 21893526). Causal density and integrated information as measures of conscious level. Foundational methodological paper comparing causal density and integrated information as candidate measures of conscious level and discussing their theoretical and practical application to neural data..
- Luppi et al. (2022). Integrated information in disorders of consciousness and anaesthesia; representative empirical anchor for the contemporary integrated-information consciousness literature.
- Shew & Plenz 2013. Functional benefits of criticality in the cortex; canonical review of the criticality framework.
- Palva et al. (2013). Long-range temporal correlations in large-scale brain activity; representative anchor for the LRTC literature.
- Northoff & Lamme (2020). Review of consciousness theories and neural markers, emphasizing convergence through temporo-spatial brain dynamics; included as a consciousness-theory anchor.

> **Footnote on Sitt 2014.** This paper is retained on the empirical seed list as a transparency anchor: it is one of the most cited DOC-EEG complexity papers and any reviewer reproducing the search will need to see why it appears as missed. Its abstract uses the title-level "neural signatures of consciousness" framing without naming any specific complexity measure (although the paper computes 92 markers including permutation entropy and weighted symbolic mutual information). Block 2 broadening to `"neural signature*"` was considered and rejected on noise grounds. The paper is recovered through backward / forward citation tracking from any captured paper that cites it (§B5).

#### B9b — Methodology-only seeds (included by exception, not via search)

Theoretical / derivation papers grounding the measurement framework. They have no empirical neural-data application and therefore correctly fail Block 3 of the search. Included via §B4 inclusion criterion 4 (seminal methodological papers).

| # | Citation | PMID | DOI |
|---|---|---|---|
| 1 | Tononi, Sporns, Edelman 1994, *PNAS* — *A measure for brain complexity: relating functional segregation and integration in the nervous system* | 8197179 | 10.1073/pnas.91.11.5033 |
| 2 | Oizumi, Albantakis, Tononi 2014, *PLoS Comput Biol* — *From the phenomenology to the mechanisms of consciousness: Integrated Information Theory 3.0* | 24811198 | 10.1371/journal.pcbi.1003588 |
| 3 | Chis-Ciure, Melloni & Northoff 2024, *Neurosci & Biobehav Rev* — *A measure centrality index for systematic empirical comparison of consciousness theories* (the "Yaron paper") | 38615851 | 10.1016/j.neubiorev.2024.105670 |

Additional methodology-only papers may be identified through the registered search, citation-tracking procedures, or extraction process.

> **Why Chis-Ciure et al. 2024 is in B9b.** The v0.4.1 pilot run (2026-05-12) confirmed the paper fails Block 3 (`B1:+ B2:+ B3:– full: MISSED`) — correctly, because it proposes the Measure Centrality Index framework and reviews measures rather than analysing neural recordings. It functions in this protocol as a measure-mapping reference (§B5; §B12 Axis 1 family 12 derived from it) and as a methodology precedent for cross-theory comparison, not as an empirical input. Included via §B4 exception.

---

> **Maintenance.** Whenever a paper is moved between B9a and B9b, or whenever the locked search is amended, re-run `pilot_search.py` and update both the §B6 pilot results and the B9a status column. The amendments log records each such change.

### B10. Critical appraisal (PRISMA-ScR — optional, elected)

Under the JBI scoping-review methodology (Peters et al. 2020; Pollock et al. 2023) and PRISMA-ScR (Tricco et al. 2018), critical appraisal of methodological quality is *optional* — not mandated as in a full systematic review. Classical risk-of-bias tools (ROBINS-I, QUADAS-2) target effect-size-synthesis reviews and do not map cleanly onto a methodological mapping review such as this one.

We *elect* to apply a critical-appraisal step for one specific reason: the review's deliverable is a guidance map of "which measure can warrant which kind of consciousness claim" (§A2, aim 5), and the §B11 misapplication register depends on a consistent, paper-by-paper appraisal of methodological quality. Without that appraisal, the misapplication claims would be impressionistic rather than auditable.

The appraisal is therefore a **measurement-methodology checklist**, not a risk-of-bias instrument. It is inspired by QUADAS-2 and the TRIPOD statement but tailored to consciousness-complexity measures:

1. **Measure specification.** Is the mathematical formula unambiguous? Are parameters (m, r, τ, window length, embedding dimension, normalisation, surrogate procedure) fully reported?
2. **Data suitability.** Sufficient channels / record length / sampling rate for the measure as specified? Stationarity assumptions met where the measure requires them?
3. **Validation.** Is there a ground truth (behavioural report, clinical diagnosis, pharmacological manipulation, perturbation)? Are claims cross-validated against an independent dataset or another measure?
4. **Confound control.** Are confounds reported and controlled — SNR, sampling-rate heterogeneity, muscle artefact, drug-state vs sleep-state confounds, age, recording-duration differences, surrogate / shuffled controls?
5. **Reproducibility.** Are code, data, and exact parameter settings reported (Y / N / partial)?
6. **Interpretation–warrant fit.** Is the consciousness claim commensurate with what the measure mathematically computes (e.g., a correlational measure not claimed as directional; an amplitude-only proxy not claimed as effective connectivity)?

Each item rated *low concern / some concern / high concern*. Pilot the checklist on the same 10-study set used for the §B8 extraction-form pilot, revise if needed, then apply to the full corpus. **Items 1, 5, and 6 feed the §B11 misapplication register directly.**

Under the solo-reviewer model (§B7), Samson applies the checklist alone. A 10 % random sample is re-appraised by Samson after a ≥ 1-month delay (intra-rater test-retest); persistent deviations trigger review of the checklist rubric. Supervisors review the appraisal outputs at month-end milestones.

This is a deliberate departure from the typical scoping-review default of skipping appraisal: it is justified by the review's specific aim of producing usage guidance, not just a map.

### B11. Synthesis plan
- **Narrative synthesis**, organised by the taxonomy in §B12.
- **Summary tables:** (i) measure × mathematical primitive; (ii) measure × data requirement; (iii) measure × consciousness aspect claimed; (iv) measure × validation evidence.
- **Heatmap** of measure × consciousness-state coverage to identify gaps.
- **Misapplication register** — a structured list of recurring misuses with representative citations.
- **Decision-support appendix** — "if your question is X, these measures are plausibly warranted; these are not, because…".
- **Citation-network analysis on the included set (added v0.4.2 on Jurgen's request).** Using Citationchaser exports of the included papers (estimated 100–300 post-screening), build the *within-corpus* citation graph — which included papers cite which, identify clusters and cite-trees, and distinguish *parallel independent developments* (multiple lines starting from different seed papers) from *sequential variations* on the same key paper (e.g., the Tononi-Sporns-Edelman 1994 line of descendants). Reported as a network figure plus a short narrative. Note: scope is restricted to the included set, not the full 5,267-record search corpus; full-corpus citation analysis would inflate the work materially and is parked as a candidate Phase-2 study.
- **No meta-analysis** of effect sizes is planned (heterogeneity is too high). If a sub-family (e.g., LZc in DOC) has enough comparable studies, a mini meta-analysis may be added.

### B12. Taxonomy

> **Mathematical taxonomy versus consciousness-research taxonomy — decision recorded v0.4.3 (Lucia, 2026-05-14).** The formal mathematical taxonomy of complexity measures — partitioning them by their abstract mathematical home (algorithmic information theory; classical Shannon information theory; causal information theory; dynamical-systems theory; statistical-physics critical phenomena; algebraic-graph and topological theory; differential geometry and manifold methods; applied time-series statistics; perturbational experimental design; statistical-learning theory) — is conceptually distinct from the consciousness-research taxonomy in which these measures are deployed. We acknowledge this distinction (Jurgen, 2026-05-12). Nevertheless, the complexity measures included in this review have been selected, adapted, and operationalised specifically for the neuroscientific context: their mathematical lineage is intellectually relevant but is already documented in each measure's canonical reference (see §B9 and §F glossary). Operationalising mathematical lineage as a separate taxonomic axis would (a) duplicate information available in those canonical references, (b) risk fragmenting the taxonomy across two dimensions that mostly co-vary in practice, and (c) extend the operational scope of the review beyond what is feasible under the solo-reviewer model (§B7). Accordingly, we elect to confine the taxonomy to the eight axes below — which classify measures along the dimensions that matter for *how the measure is used in consciousness research and what it can warrant about consciousness*. The mathematical-lineage distinction is recorded narratively in the manuscript's Methods section and in the §F glossary entries, but not as a separate axis.

**Axis 1 — Mathematical primitive**
1. Entropy family: Shannon, differential, approximate, sample, permutation, spectral, multiscale.
2. Compressibility: Lempel-Ziv (LZ76, LZc, LZW), Kolmogorov signal complexity (KSC).
3. Information flow: mutual information, transfer entropy, Granger causality, partial directed coherence, φ-ID, **weighted symbolic mutual information (wSMI; Dehaene-King line)**.
4. Integrated information: φ, φ*, geometric φ, whole-minus-sum φ, φ-AR (autoregressive), φ-SI (stochastic interaction), φ-CII (causal-information integration), φ-C (compression-complexity), φ-atomic, state differentiation (D), empirical φ surrogates.
5. Dynamical / criticality: neural avalanches, branching parameter, DFA / LRTCs, **multifractal DFA**, Hurst, Lyapunov exponents, correlation dimension, edge-of-chaos.
6. Structural / graph-theoretic: small-worldness, modularity, rich-club, hierarchical complexity, Tononi-Sporns-Edelman neural complexity.
7. Dimensionality / manifold: intrinsic dimensionality, participation ratio, embedding dimension.
8. Perturbational: PCI, PCI-state (ST-PCI), PCI-LZW.
9. Structure-of-experience: qualia-space unfolding, optimal-transport distances between state representations.
10. Hybrid / composite: supervised ML classifiers whose features are any of the above.
11. **Phase / dynamical-systems coupling (Varela / Kelso / Le Van Quyen line):** phase-locking value (PLV), weighted phase-lag index (wPLI), phase coherence, metastability, chimera-state indices, dynamical-systems synchrony measures.
12. **Temporospatial / scale-free measures (TTC line; from Chis-Ciure-Melloni-Northoff 2024 NBR):** autocorrelation window (ACW), power-law exponent (PLE), temporal receptive windows (TRW), scale-free topology measures, global signal (GS) + GS-topography.

**Axis 2 — Data requirement**
- Amplitude only.
- Amplitude + functional connectivity.
- Amplitude + effective connectivity.
- Phase only / phase + amplitude (added in v0.4 — dynamical-systems-theory measures are largely phase-based).
- Requires external perturbation.
- Requires simultaneous multi-scale recording.

**Axis 3 — Temporal granularity**
- Event-level (single-trial, sub-second).
- Windowed / epoch-level.
- Long-range / scaling (seconds to hours).
- State-level (one number per session).

**Axis 4 — Aspect of consciousness claimed**
- Level / wakefulness.
- Content / what is experienced.
- Integration (across regions / networks).
- Differentiation (richness of repertoire).
- Structure (geometry of experience — under-represented).
- Temporal flow (experience of time — under-represented; planned focus of follow-on work).

**Axis 5 — Spatial scale (added in v0.4 on Lucia's recommendation)**
- Single-unit / multi-unit (microelectrode-scale).
- Laminar / columnar (cortical-microcircuit scale).
- Area-level (cortical-area or ROI).
- Whole-brain network (sensor-/voxel-level coverage).

The same measure can behave very differently across these scales — for example, avalanche statistics depend on sampling density; LZc on EEG vs on multi-unit spike trains is essentially a different measurement. Recording this axis explicitly is required for honest cross-paper comparison.

**Axis 6 — Theory anchoring (added in v0.4 on Lucia's recommendation)**
- Theory-derived (φ ← IIT; ignition / global-broadcast indices ← GNW; entropy-rate variants ← predictive processing / entropic brain; etc.).
- Theory-agnostic (LZc, sample entropy, DFA — descriptive measures of signal structure, theory-neutral in origin).
- Theory-agnostic-but-interpreted-post-hoc — a descriptively-derived measure being read as evidence for a specific theory it was not built to test (the PQ7 case).

**Axis 7 — Inferential status (added in v0.4)**
- Causal (perturbation-based: PCI, TMS-EEG protocols).
- Correlational / descriptive (transfer entropy, Granger causality, LZc on resting data).

Currently bundled into "data requirement," but this is an inferential property — a measure that requires perturbation makes a different kind of claim than a correlational one — and worth pulling out.

**Axis 8 — Validation evidence type (lifted from §B8 in v0.4)**
- Behavioural report.
- Clinical diagnosis (e.g., DOC classification).
- Pharmacological manipulation.
- Cross-measure agreement only.
- None / no validation against an external criterion.

This axis is already an extraction field (§B8); promoting it into the taxonomy spine lets the §B11 gap-heatmap be diagnostic.

This taxonomy is the review's **conceptual spine**. It is expected to shift after extraction; revisions will be tracked in the amendments log.

> **Coverage check.** Lucia flagged that the measure-family inventory must adequately cover the major measure families used in the field — "if the set isn't complete then the review is not either." *Coverage* is operationalised here as cross-checking against established measure-family reference lines rather than as exhaustive enumeration of every measure ever published; the Block 2 term list and Axis 1 family list have been cross-checked against (a) the Yaron, Pitts, Mudrik & Melloni 2024 *NBR* mapping of measures to candidate NCCs, (b) the wSMI / Dehaene-King line, and (c) the phase / dynamical-systems family (Varela, Kelso, Le Van Quyen). The taxonomy was initially developed through literature review, supervisor consultation, and the seed-identification process. If previously unrepresented measure families are identified during the registered search, citation-tracking, or extraction phases, they will be incorporated into the taxonomy and documented in the amendments log; any such addition will trigger a Block 2 re-pilot.

### B13. Dissemination
- **Target journals.** *Nature Human Behaviour* (primary — Yaron, Melloni, Pitts & Mudrik 2022 precedent in the same field); *Neuroscience & Biobehavioral Reviews* (strong fallback — Yaron, Pitts, Mudrik & Melloni 2024 precedent). *Neuroscience of Consciousness* as third option. *Nature Reviews Neuroscience* and *Trends in Cognitive Sciences* have been removed from the target list — they rarely publish systematic / scoping reviews of this kind (Lucia, 2026-05-10).
- **Preprint** on bioRxiv concurrent with submission.
- **Companion open resource.** Extraction spreadsheet + taxonomy table on OSF; **interactive companion website** providing measure-by-measure look-up keyed by Axis 1–8 (cf. the Yaron-Melloni NHB companion site as a precedent).
- **Conference.** ASSC 2026 (if timing permits).

### B14. Ethics & funding
- No primary data collection; no ethics approval required.
- Author affiliations are recorded in §B1.2.
- Funding: Max Planck School of Cognition (lead reviewer's PhD-track funding line; confirmed via Samson's affiliation in §B1.2). No additional external funding for this protocol.
- The review concerns a field containing competing theoretical frameworks. To minimise interpretive bias, the protocol explicitly restricts scope to methodological mapping and does not adjudicate among theories (§A3).

---

## Part C — Decisions and their resolutions

Status of all nine protocol decisions: Decisions 1–7 raised in v0.2 / v0.3 (after supervisor review pass 2026-05-10), Decision 8 documented in v0.5 (2026-05-29), Decision 9 documented in v0.5.1 (2026-06-04).

1. **Review type — Resolved.** Locked to **PRISMA-ScR scoping review**. Endorsed by Lucia ("yes, PRISMA-ScR is the right call") and Andrej ("I tend to agree").
2. **Scope commitment — Resolved.** Neural signal complexity, both invasive and non-invasive, in humans and non-human animals. Tightening to human-only was considered and rejected (would structurally exclude measure families that depend on dense sampling — avalanche statistics, single-unit-derived entropies); cross-species interpretive caveat added to §A3 and §B8 instead.
3. **Screening model — Resolved (revised v0.4.4 to add formal Elicit AI second-screening).** **Single human reviewer + Elicit AI second screening + ASReview active-learning prioritisation + within-person test-retest** (see §B7). The lab has no available personnel for a second *human* reviewer in any role; supervisors give feedback on completed work at month-end milestones but do not screen, calibrate, or perform quality-control re-screening. The v0.4.3 "optional LLM-assisted verification (transparency, not arbitration)" step has been upgraded to a formal AI-assisted second-screening layer after a pre-registered calibration on 200 records cleared all three commit thresholds (κ = 0.843, recall of human-includes = 98.1 %, seeds 8/8; full numbers in §B7 calibration paragraph and `calibration_results.md`). Yaron, Melloni, Pitts & Mudrik 2022 *Nat Hum Behav* remains cited as published precedent for single-human-reviewer scoping reviews in this field; the Elicit layer is documented as an additional safeguard, not as a substitute for a second independent human reviewer.
4. **Authorship policy and order.** To settle before Adam Barrett and Anil Seth are formally invited; provisional order Samson (lead) → Jurgen → Lucia → Andrej, with Adam Barrett and Anil Seth added on contribution.
5. **Taxonomy sign-off — Resolved.** Lucia endorsed the four-axis spine and proposed two further axes (spatial scale, theory anchoring); both adopted in §B12 plus two further axes (causal vs descriptive; validation evidence type). Axis 1 expanded with wSMI and a phase / dynamical-systems family.
6. **Registration venue — Resolved.** **OSF Registries.**
7. **Grey-zone calls — Status: agreed.** Anaesthesia-monitoring papers, pharmaco-EEG, simulation-only papers retained as flag-and-decide grey-zone items in §B4.
8. **Block-2 keyword breadth (Jürgen, 2026-05-29) — Considered; not implemented as a v0.5 protocol change; to be evaluated empirically post-search.** Jürgen raised that Block 2 may be overly broad / heterogeneous and suggested estimating retrieval volume using a narrower term set first (e.g., omitting terms such as “scale-free”). The concern is methodologically legitimate and will be evaluated empirically post-search. v0.5 does not implement pre-registration narrowing of Block 2 because pilot retrieval remains within the planned target band (§B6.1; 5,267 records), the present breadth reflects supervisor-guided expansion aligned with the review taxonomy, and recall is prioritised for methodological mapping. For a scoping review, over-search is recoverable through screening whereas under-search risks omission of relevant measure families. No pre-registration change is therefore implemented. Instead, during the bulk screening phase, Block 2 sub-families will be tracked against the measure families they populate. After the included set is locked, a term-level contribution analysis may be conducted to assess which Block 2 terms contributed meaningfully to included studies and which yielded negligible signal. Terms with minimal contribution may become candidates for refinement in a future protocol version or follow-on review. This converts the concern from a pre-registration trade-off into an empirical question answered using the included corpus.

9. **Embase access constraint — Resolved as an administrative limitation (recorded in v0.5.1 post-registration-preparation update, 2026-06-04).** Embase was originally planned as a sixth database to provide Emtree-based pharmacology coverage (relevant to anaesthesia-related consciousness research). Institutional access was investigated through MPI/CBS library services (unavailable) and alternative routes through ZB MED registration (successful — virtual library card issued). However, practical Embase access depended on a limited booking system with available slots substantially outside the project's planned search-execution timeline. The scientific cost of delaying search execution, screening, and extraction by several weeks to accommodate external Embase access constraints was judged to exceed the expected marginal recall gain, particularly given the substantial redundancy with PubMed/MEDLINE and the breadth of the five-database corpus (PubMed, Scopus, Web of Science, PsycINFO, IEEE Xplore). **Decision: Proceed without Embase.** This is classified as an access limitation (external scheduling constraint), not as a methodological narrowing of review scope. No changes have been made to eligibility criteria (§B4), search strategy (§B6 search blocks remain locked), taxonomy (§B12), screening plan (§B7), extraction plan (§B8), or synthesis plan (§B11). The five-database corpus provides substantial coverage; any high-value Embase-only papers are recoverable through §B5 citation tracking from the seed set. Full rationale and access-investigation details documented in §B6.3 (Embase database-access note).

---

## Part D — Risk register

| Risk | Likelihood | Mitigation |
|---|---|---|
| Hit count too large (> 20 k) | Medium | Tighten Block 1 to explicit state-change contexts; drop non-specific "wakefulness". |
| Hit count too small (< 1 k) | Low | Relax Block 3 to include non-neural recording modalities used as consciousness proxies. |
| No second *human* reviewer available | Medium-high (mitigated v0.4.4) | Elicit AI second screening deployed and calibrated against blind human decisions (κ = 0.843, recall 98.1 %, seeds 8/8 on n = 194; see §B7 and `calibration_results.md`); within-person test-retest provides self-consistency; deviation from PRISMA's default dual *independent human* screening disclosed transparently. |
| "Complexity" keyword noise (complexity theory, software complexity, etc.) | High | Block 2 is deliberately specific. Run a noise audit on the first 500 records. |
| Qualia-structure / optimal-transport line under-cited in databases | Medium | Backward-citation scaffold; expert elicitation. |
| Scope creep into measure design before the review is complete | High | Hard line: no new-measure development inside the review window. |
| Cross-institute / part-time supervisor availability | Medium | Stand-in coverage between Lucia and Andrej; weekly written updates regardless of meeting cadence. |
| PRISMA prefers dual independent screening; single-human-reviewer reviews exist but are weaker | Certain (mitigated v0.4.4) | See second-reviewer row; Elicit AI second-screening layer adds an independent, traceable, per-criterion screening pass with calibration evidence; deviation from dual independent *human* screening disclosed transparently in §C, in the OSF registration, and in the manuscript's *Limitations*. |

---

## Part E — Future extensions beyond the current protocol

1. **Replication audit.** A potential extension of the review would be a targeted replication audit of a small number of influential studies (for example, recomputing measures such as Lempel–Ziv complexity from publicly available datasets where feasible). Such an exercise could provide an additional methodological perspective on reproducibility and implementation variability, but is outside the scope of the present review.
2. **Visualisation of theory–measure relationships.** The review will catalogue the theoretical provenance of included measures and their relationship to different consciousness frameworks. Depending on the structure of the extracted corpus, a future extension may develop a dedicated visual representation of these relationships (for example, summary tables, network diagrams, or layered maps) as a companion resource.
3. **Complexity and the temporal structure of experience.**     One anticipated outcome of the review is a clearer assessment of whether existing complexity measures adequately address the temporal structure of conscious experience. If substantial gaps are identified, this may motivate a dedicated follow-on review or conceptual paper focused specifically on temporal experience and its possible quantitative characterisation.

---

## Part F — Glossary of measures

*Each entry to be expanded with: one-line definition, mathematical core, data requirements, canonical reference, typical implementation, known failure modes.*

- **LZc / Lempel-Ziv complexity** — binarised-signal compressibility; distinguishes states but is driven by spectral content as much as by richness; normalisation choice matters.
- **PCI** — TMS-EEG perturbational integration × differentiation; gold standard for level; requires perturbation, so not a pure read-out.
- **Sample / permutation / multiscale entropy** — windowed dynamical complexity; parameter-sensitive (m, r, τ); stationarity assumed.
- **Transfer entropy / Granger causality** — information-flow proxies; **widely misused to claim directionality in densely coupled systems**; surrogate controls and effective-connectivity models are needed.
- **φ and variants** — integrated information; the canonical form is intractable; empirical variants (φ*, geometric φ, whole-minus-sum) are not equivalent.
- **Neural complexity (Tononi-Sporns-Edelman 1994)** — balance of integration and segregation across subsets; N² combinatorics; largely superseded in practice.
- **DFA / LRTCs** — long-range temporal correlations; level of consciousness tracks the Hurst exponent in several datasets; sensitive to stationarity and detrending.
- **Neural avalanches / branching parameter** — criticality signatures; depend on spatial sampling and thresholding.
- **φ-ID (synergy / redundancy decomposition)** — decomposes integrated information into interpretable atoms; promising for differentiating level vs. content claims.
- **Causal emergence / causal density** — macro-scale effective information vs. micro.
- **Intrinsic dimensionality / manifold measures** — dimensionality of the neural state space; underused for consciousness specifically.
- **Optimal-transport / qualia-unfolding** — structural geometry of experience; few empirical applications; *candidate gap*.

---

## Amendments log

- **v0.1 — 2026-04-22.** Initial draft (protocol + 3-month action plan).
- **v0.2 — 2026-04-27.** Executive summary added.
- **v0.3 — 2026-05-07.** Search strategy locked. PubMed pilot returned 4,580 records (Block 1 ∧ Block 2 ∧ Block 3) on the canonical query. Block 2 broadened to include `"signal complexity"`, `"signal diversity"`, `"EEG complexity"`, `"complexity measure*"`, `"complexity marker*"` (added during pilot to recover Casarotto/Schartner-style framing). Block 3 broadened to include `TMS`, `"TMS-EEG"`, `"TMS-evoked"`, `"TMS evoked"`, `"transcranial magnetic stimulation"` (added to recover Casali 2013 PCI line). §B6 rewritten with locked queries and pilot results. §B6.1–B6.3 added (pilot results, seed validation, audit-trail policy). §B9 split into B9a (empirical seeds — must pass search) and B9b (methodology-only seeds — included by exception). Companion document `database_queries.md` added with translations of the locked PubMed query into Scopus, Web of Science, PsycINFO (EBSCOhost), IEEE Xplore, and Embase syntax. Sitt et al. 2014 (PMID 24919971) documented as a known database miss recovered via §B5 citation tracking; rationale recorded in §B6.2 and §B9a footnote.
- **v0.4 — 2026-05-11.** Supervisor review pass incorporated. All changes carry attribution to Lucia (docx markup 2026-05-10 + email 2026-05-10) or Andrej (docx markup 2026-05-10) or both. Detail:
  - *Administrative.* External collaborator "Adam" corrected to "Adam Barrett" (Lucia). Funding line updated from "Max Planck Institute" to "Max Planck School of Cognition" (Lucia). §B1 "Second reviewer" row replaced with "Screening model" entry naming the calibrated single-reviewer + ASReview plan, citing the Yaron et al. 2022 NHB precedent.
  - *Framing (§A1 / §A2 / §A3).* §A1 problem statement extended with "and cannot warrant" and "how the measure relates to a given theoretical construct or theory" (Andrej + Lucia). §A2 aim 1 reframed to be explicit about invasive and non-invasive techniques in humans and non-human animals (Lucia: do not appear to exclude fMRI / fNIRS / PET). §A2 aim 2 listed all eight taxonomy axes (was four). §A2 aim 5 extended with the "if your theory is X" decision-table form (Lucia). §A3 "Theory advocacy" bullet replaced with the cleaner "Theory adjudication" formulation (we do not adjudicate between theories; we do catalogue theoretical provenance — Lucia + Andrej). Memory–consciousness interface explicitly placed out of scope (Lucia; Andrej note "amnesiacs are conscious"). Cross-species interpretive caveat added (Andrej scope flag).
  - *Review questions (§B2).* Three new questions added — **PQ5 (Theory provenance)**, **PQ6 (Within-theory operationalisation drift)**, **PQ7 (Post-hoc theoretical re-interpretation)** (all Lucia). Optional **PQ8 (Theory-discriminating power)** deferred to v1.1 / a follow-on paper (Lucia flagged as scope risk).
  - *Eligibility (§B4).* The ≥ 50-citation preprint threshold dropped (both Andrej and Lucia flagged it as undefendable). Replaced with explicit content criteria: applies a quantitative complexity measure to neural data, makes a consciousness claim, not retracted, openly available full text.
  - *Information sources (§B5).* Rewritten with a one-line rationale per database (PRISMA-S item 3, Lucia). **medRxiv** added to preprint sources (Lucia: clinical / DOC / anaesthesia preprints land there). Hand-search list extended with *Nature Communications*, *eLife*, *PNAS*, *Anesthesiology* / *British Journal of Anaesthesia* (Lucia). Citation-tracking tool named: **Citationchaser** (Lucia — PRISMA-S item 3 requires a named tool). Yaron et al. 2024 *NBR* added as reference for measure-to-NCC mapping (Lucia link).
  - *Screening (§B7).* Rewritten around the calibrated single-reviewer + ASReview plan, with Yaron, Melloni, Pitts & Mudrik 2022 NHB as published precedent for scoping reviews without dual independent title / abstract screening. Lucia's email (2026-05-10): "I am not convinced [a second reviewer] will realistically work, mainly because of time and resources… We did publish a scoping review in NHB without the ideal dual-reviewer setup." JBI methodology cited.
  - *Taxonomy (§B12).* Axis 1 expanded with **weighted symbolic mutual information (wSMI; Dehaene-King line)** and a new **family 11 — Phase / dynamical-systems coupling** (PLV, wPLI, metastability, chimera-states; Varela / Kelso / Le Van Quyen line) — Lucia flagged the original Axis 1 as missing these. Four new axes added: **Axis 5 — Spatial scale** (single-unit / laminar / area / whole-brain network; Lucia); **Axis 6 — Theory anchoring** (theory-derived / theory-agnostic / theory-agnostic-but-interpreted-post-hoc; Lucia); **Axis 7 — Inferential status** (causal vs descriptive; Lucia); **Axis 8 — Validation evidence type** (lifted from §B8 extraction-only into the taxonomy spine to make the §B11 gap-heatmap diagnostic; Lucia). Axis 2 (data requirement) extended with a phase-only / phase + amplitude entry. Coverage-check note added at end of §B12 (Lucia: "if the set isn't complete then the review is not either").
  - *Dissemination (§B13).* Target journals reordered: primary now **Nature Human Behaviour** (Yaron et al. 2022 precedent), fallback **Neuroscience & Biobehavioral Reviews** (Yaron et al. 2024 precedent). *NRN* and *TICS* removed — Lucia: "aren't that much into systematic reviews." **Companion website** added as a deliverable alongside the OSF spreadsheet (Lucia: "more impactful is a website. See what we did in Yaron NHB").
  - *Ethics & funding (§B14).* "Max Planck affiliation" updated to "Max Planck School of Cognition" (Lucia).
  - *Part C.* Rewritten as "Decisions and their resolutions" — each of the seven v0.3 decisions marked resolved with attribution. Single remaining open item: OSF registration timing.
  - *Part E.* Reframed methodological question 2 around theory-anchoring display rather than theory–measure asymmetry (Lucia: "frame it as whether a measure relates to a theory or whether it is theory agnostic"). Memory–consciousness question removed and consolidated into §A3 out-of-scope note (Lucia + Andrej).
  - *Block 2 / search re-pilot pending.* The Block 2 additions in this version (wSMI, phase-locking, dynamical-systems family) materially expand the search; a re-pilot of `pilot_search.py` is required and the §B6 hit-count table will be updated in v0.4.1.
  - *Items pending clarification from Samson.* (i) Identity of the "Julio" reference in §B9a (Giulio Tononi? Julio Hidalgo? other?); (ii) any further measures from the Yaron 2024 NBR paper to add to Axis 1 / Block 2 once Samson has retrieved the PDF.
- **v0.4.1 — 2026-05-11.** Follow-up patches after the Yaron paper (Chis-Ciure, Melloni & Northoff 2024, *Neurosci & Biobehav Rev*, PII S0149763424001398) was attached, plus three direct decisions from Samson.
  - *Julio reference dropped (§B9a).* Per Samson — the "Julio" placeholder referred to discussion notes about an unfolding-qualia-structure idea floated by Lucia, not a specific cited paper; removed from the seed-elicitation list.
  - *§B10 reframed as PRISMA-ScR critical appraisal (Item 5 on the OSF-readiness list).* The section is now framed as an *optional* JBI critical-appraisal step that we *elect* to perform because the §B11 misapplication register depends on it; the checklist items are the same but the methodological framing is now correct for a scoping review rather than a full systematic review.
  - *Block 2 expanded with Yaron-paper measure families (§B6 + script + §B12 Axis 1).* Added: **Kolmogorov complexity / KSC**, **ST-PCI**, **state differentiation**, **wSMI**, **multifractal / MF-DFA**, **autocorrelation window (ACW)**, **power-law exponent (PLE)**, **temporal receptive window(s) / TRW**, **scale-free** terms, **global signal topography / GS-topography**. The TTC measure family (ACW, PLE, TRW, GS-topography) was absent from v0.4 and is the Yaron paper's central contribution to our taxonomy. Axis 1 in §B12 now lists 12 families (added family 12 — Temporospatial / scale-free) and family 4 (Integrated information) expanded with the φ-variants explicitly catalogued by Chis-Ciure et al. (φ-AR, φ-SI, φ-CII, φ-C, φ-atomic, state differentiation).
  - *Yaron 2024 added to §B9a seed-elicitation list* as a measure-mapping reference.
  - *Search re-pilot completed (2026-05-12).* v0.4.1 PubMed pilot returned **5,267 records** (+15 % from v0.3's 4,580). §B6.1 hit-count table populated. Seven of eight empirical seeds captured. **Sitt 2014 confirmed as a database miss after wSMI expansion** — the paper's published abstract contains none of the specific complexity-measure names; recovery path via §B5 citation tracking now confirmed rather than provisional. **Chis-Ciure, Melloni & Northoff 2024 reclassified from B9a (empirical) to B9b (methodology-only)** — the pilot showed B3:– (correctly, since it is a methodology / review paper, not an empirical study). §B6.2 narrative updated to reflect both results.
  - *Authorship and full names recorded.* Provisional authorship locked (in §B1 and the header): Samson Odan, Lucia Melloni, Andrej Bicanski, Jurgen Jost — Adam Barrett and Anil Seth to be added on contribution. Supervisor surnames expanded throughout to full names. **Adam Barnett → Adam Barrett** corrected (Lucia's docx insertion had a typo; Adam B. Barrett at Sussex, Anil Seth's collaborator on causal density and integrated information, is the intended person).
  - *Companion documents added.* `prisma_checklist_mapping.md` (PRISMA-ScR 22-item + PRISMA-S 16-item mapping, one-page) and `github_zenodo_setup.md` (step-by-step instructions for putting the repo on GitHub and producing a Zenodo DOI for v0.4.1).
  - *Zenodo archive created (2026-05-12).* v0.4.1 of the protocol and companion files archived on Zenodo. Specific-release DOI: **10.5281/zenodo.20140262**. Concept (latest) DOI: **10.5281/zenodo.20140263**. §B6.3 (Search audit trail) updated to record both DOIs. `README.md` populated with the badge, file index, citation, and licence (CC-BY 4.0 for the protocol; MIT for the code).
- **v0.4.2 — 2026-05-12.** Three substantive additions following Jurgen's review of v0.2 (received 2026-05-12). Jurgen's first two comments (timeline; non-English publications) are parked for the next supervisor meeting per Samson's instruction and are not implemented here.
  - *§B6 preamble on systematic complexity-variant criteria (Jurgen comment 3).* Added an explicit framing block above the locked queries: Block 2 is the *agreed-upon set of complexity-variant terms* for this review, iteratively constructed and expanded through pilot rounds. Converts what looked like an ad-hoc list into a justified inclusion criterion. Documents the four expansion rounds (v0.1 → v0.3 → v0.4 → v0.4.1) with attribution.
  - *§B11 citation-network analysis on the included set (Jurgen comment 4, mid-tier).* Added as a synthesis bullet. Post-screening, build the within-corpus citation graph (via Citationchaser) on the included papers (estimated 100–300), identify clusters and cite-trees, and distinguish parallel independent developments from sequential variations on the same key paper (e.g., the Tononi-Sporns-Edelman 1994 line). Full-corpus citation analysis on 5,267 raw records is parked as a candidate Phase-2 study.
  - *§B12 Axis 0 — Mathematical lineage (Jurgen comment 5, heavier).* New axis added prior to Axis 1, recording each measure family's formal mathematical home (algorithmic information theory; classical / Shannon information theory; causal information theory; dynamical-systems theory; statistical-physics critical phenomena; algebraic-graph / topological theory; differential geometry / manifolds; time-series statistics; experimental / perturbational design; hybrid statistical learning). Distinct from Axis 1, which records the consciousness-research family naming. Multi-rooted measures (e.g., φ-ID, wSMI) listed in more than one lineage. Total axis count: nine. Executive-summary axis list updated accordingly. §B11 synthesis tables now include measure × Axis 0 lineage.
  - *Pending from Jurgen, parked.* Items 1 (timeline) and 2 (French + German publications); the latter has real resource implications and is held for supervisor discussion.
- **v0.4.3 — 2026-05-14.** Three changes following meeting with Lucia (2026-05-14). All three simplify the protocol relative to v0.4.2.
  - *§B4 — English-only framing retained, with rationale recorded.* Jurgen's tentative-inclusion suggestion for French and German (2026-05-12) is declined on Lucia's advice (2026-05-14): the highest-impact consciousness-neuroscience work is overwhelmingly published in English, and the marginal coverage gain from non-English literature does not justify the screening burden under the solo-reviewer model. Any high-value non-English paper missed by the search is recoverable through §B5 citation tracking. The English-language inclusion criterion is therefore retained as in v0.1 and explicitly acknowledged as a documented scoping decision.
  - *§B12 — Axis 0 (Mathematical lineage) removed; eight-axis taxonomy restored (Lucia, 2026-05-14).* v0.4.2 added a separate Axis 0 in response to Jurgen's observation that mathematical and consciousness-research taxonomies differ (2026-05-12). v0.4.3 removes this axis and replaces it with a narrative acknowledgment at the top of §B12. Rationale: the mathematical lineage of each measure is already documented in its canonical reference (§B9, §F); operationalising lineage as a separate axis would duplicate that information, fragment the taxonomy across two co-varying dimensions, and extend the review's operational scope beyond what is feasible under the solo-reviewer model. The eight-axis taxonomy (Axes 1–8) is restored. Executive summary updated from "nine orthogonal axes" to "eight orthogonal axes." §B11 synthesis tables updated to remove the measure × Axis-0 lineage entry. Note: the Block 2 measure additions made in v0.4.2 (wSMI, phase / dynamical-systems family, ACW, PLE, TRW, KSC, multifractal DFA, state differentiation, ST-PCI, scale-free, GS-topography) are retained — these are legitimate measure families in the consciousness-research literature regardless of the meta-classification decision.
  - *§B7 / §B8 / §B10 — Screening, extraction, and critical appraisal made solo-reviewer realistic (Lucia, 2026-05-14; Samson, 2026-05-14).* None of the three supervisors will be available as a second reviewer in any role; supervisors will give feedback on completed work at month-end milestones but will not screen, calibrate, spot-check, or re-extract. §B7 rewritten: solo self-calibration on first 200 abstracts; within-person test-retest at 2-week gap (target κ ≥ 0.8 self-agreement); ASReview active-learning bulk screening with the standard saturation stopping criterion; periodic test-retest every 1,000 records during bulk screening; optional LLM-assisted verification on a sub-sample for transparency only (no override of Samson's decisions); solo full-text screening; supervisor consultation at month-end milestones at the protocol-revision level, not per-paper. §B8 extraction: 20 % supervisor re-extraction dropped, replaced with 10 % self re-extraction after ≥ 1-month delay. §B10 critical appraisal: 10 % self re-appraisal after ≥ 1-month delay. §C decision 3 amended to record the revised screening model. The deviation from PRISMA's default dual independent screening continues to be documented transparently in §C, in the OSF registration, and in the manuscript's *Limitations* section, citing Yaron et al. 2022 *Nature Human Behaviour* as a published precedent for single-reviewer scoping reviews in this field.
- **v0.4.4 — 2026-05-29.** Formal AI-assisted second-screening layer (Elicit) introduced after a pre-registered head-to-head calibration cleared all commit thresholds. Following Lucia's suggestion (2026-05-19) to consider Elicit for speed, an objective assessment (`elicit_assessment.md`) was prepared and a pre-registered test plan was written before any analysis (`calibration_test_plan.md`).
  - *§B7 step 5 — Optional LLM-assisted verification upgraded to formal AI second screening (Elicit).* The v0.4.3 line *"Optional LLM-assisted verification (transparency, not arbitration)"* is replaced by an explicit AI-second-screening step: every record is screened by Elicit against a four-criterion rendering of §B6/§B7 (consciousness research context; empirical neural data application; quantitative complexity-family measures applied; eligible study type) with strict criteria OFF, no automated post-aggregation override, all disagreements reconciled by the human reviewer. The rationale for *no* override — i.e., for deploying Elicit "as-deployed" rather than applying a strict-AND override on top of its per-criterion calls — is that the calibration showed strict-AND would drop 23/103 reconciled human-includes (recall 77.7 %), well below the pre-registered ≥ 95 % floor; full rule sweep in `calibration_results.md` §"Correction to the deployment-rule recommendation." Records returning no abstract (≈ 2.5 % of corpus) are flagged and screened manually by exception.
  - *§B7 calibration outcome paragraph added.* Blind values on n = 194 paired records: Cohen's κ = 0.843, raw agreement 92.3 %, recall of human-includes 102/104 = 98.1 %, substantive disagreements = 0, seeds gate 8/8 Include. All three pre-registered commit thresholds (recall ≥ 95 %; κ ≥ 0.60; 8/8 seeds) cleared. Post-reconciliation values on n = 195: κ = 0.865, recall = 100 %. Known limitation: Elicit's consciousness-context call returns `no` on substantively in-scope information-theoretic / synergistic-information work whose abstracts do not frame the consciousness link explicitly (reproduced on both Luppi 2022 seeds); under the as-deployed rule these still pass via score, and §B5 citation tracking catches any residual misses.
  - *§B1 screening-model row, §C decision 3, and §D risk register updated* to name Elicit explicitly as an AI second-screener and to record that the relevant risks (no second human reviewer; PRISMA dual-screening preference) are mitigated, not eliminated. The Yaron et al. 2022 NHB precedent for single-human-reviewer scoping reviews in this field remains the primary published precedent; the Elicit layer is documented as an additional reliability safeguard, not as a substitute for an independent second human reviewer.
  - *Companion documents added.* `elicit_assessment.md` (objective pre-decision assessment), `calibration_test_plan.md` (pre-registered design and commit thresholds), `calibration_equivalence_audit.md` (16-paper trial confirming decision-equivalence of the four-criterion rendering), `calibration_results.md` (full numbers, disagreement classification, deployment-rule correction), `calibration_adjudications.md` (resolutions for the 5 silently-skipped and 5 maybe-zone records), `calibration_200_screening_reconciled.csv` (working corpus with `post_resolution` audit column), `elicit_metric_calculations.md` (Samson's arithmetic walkthrough, working notes — not part of the formal trail).
  - *`pilot_search.py` — Luppi seed lookup disambiguated.* The bare `Luppi[Author] AND 2022[PDAT] AND synergistic[Title]` lookup matched the NeuroImage 2022 *Metastability, fractal scaling, and synergistic information processing* paper instead of the intended Nat Neurosci 2022 *A synergistic core for human brain evolution and cognition* paper (PMID 35618951). Lookup tightened with `AND core[Title]`; `calibration_seeds.ris` regenerated; canonical seed re-tested in Elicit (Include, score 3.5).
- **v0.5 — 2026-05-29. Administrative and decision-record update incorporating Jürgen’s 2026-05-29 feedback and the v0.4.4 Elicit calibration results. Added author ORCIDs and affiliations (§B1.2), revised milestone scheduling and progress-review cadence (§B1), documented Decision 8 (Block-2 keyword breadth) in Part C, and clarified the manual search-execution model (§B6.3). A protocol-wide change audit was completed on 2026-05-29 (v0.5_change_audit_2026-05-29.md) and identified no methodological drift. No changes were made to eligibility criteria, search strategy, screening procedures, extraction fields, synthesis plans, or taxonomy structure relative to v0.4.4.
  - *§B1 + new §B1.2 — author ORCIDs and affiliations.* ORCIDs recorded for all four lead authors (Samson 0009-0002-2909-0831; Lucia 0000-0001-8743-5071; Andrej 0000-0003-3356-1034; Jürgen 0000-0001-5258-6590). Affiliations recorded for all four (institution-level only — street addresses omitted; the "Neural Computation Group" sub-unit label dropped from Samson and Andrej's MPI CBS line for consistency with Jürgen's, normalised as "Max Planck Institute for Human Cognitive and Brain Sciences, Dept. of Psychology"): Samson (MPI CBS / MPI MIS / ScaDS.AI Dresden-Leipzig / Max Planck School of Cognition / Ruhr-University Bochum); Lucia (Ruhr-University Bochum / NYU Grossman / CIFAR); Andrej (MPI CBS / ScaDS.AI Dresden-Leipzig); Jürgen (MPI MIS / MPI CBS / ScaDS.AI Dresden-Leipzig / Santa Fe Institute).
  - *§B1 — cadence and three-stage milestone schedule.* Progress-review cadence: monthly. Milestone schedule revised (2026-05-29 PM) from a single end-of-July milestone to three checkpoints: late June 2026 (operational checkpoint), late July 2026 (substantive scientific checkpoint), August–September 2026 (synthesis and manuscript trajectory). Adopted in response to Jürgen's 2026-05-29 cadence / first-milestone questions.
  - *§C decision 8 (new) — Block-2 keyword breadth: considered; not implemented as a v0.5 protocol change; to be evaluated empirically post-search.* Jürgen's 2026-05-29 suggestion to estimate retrieval volume with fewer keywords first (citing "scale-free" as a candidate for removal) is acknowledged as methodologically legitimate but not implemented as a pre-registration change: the v0.3 → v0.4.1 pilot rounds executed the "estimate first" procedure and returned 5,267 PubMed records — well inside the 3–15 k target band registered in v0.3; the current breadth is Lucia-driven and mirrors the Chis-Ciure / Melloni / Northoff 2024 *NBR* authoritative measure mapping; the locked search is on Zenodo, and pre-emptively unlocking it forces re-pilot with seed-miss risk on the Toker / Luppi / Schartner lines. **Monitoring plan**: during the bulk pass we track which Block 2 sub-families populate which Axis 1 families, and after the included set is locked a term-level contribution analysis on the included set will be conducted empirically and reported in the methods writeup. The concern is therefore *acknowledged → monitored → empirically assessed*, not declined.
  - *§B6.3 — manual search-execution clause (new).* The protocol now explicitly states that search execution is manual via each database's authenticated web interface, with code restricted to downstream QC / parsing / analysis. This documents the existing execution model after librarian confirmation (Scopus / Web of Science / PsycINFO via EBSCO / IEEE Xplore via MPI/CBS login) and is a clarification of the execution model, not a methodology change.
  - *§B14 — affiliations cross-reference + funding confirmation.* Affiliations live in §B1.2; §B14 funding line confirmed as Max Planck School of Cognition (via Samson's affiliation entry); placeholder framing removed.
  - *Editorial wording sweep (2026-05-29 morning, no separate version bump).* `wording_audit_2026-05-29.md` documents three precision edits to §Executive summary, §A2 review aim 1, and §B12 Coverage check — all wording-only, no scientific or methodological drift. Captured here so the v0.4.4 → v0.5 diff has full attribution.
  - *No §B6 / §B7 / §B12 substantive changes.* All search blocks, screening pipeline (including the v0.4.4 Elicit deployment), and taxonomy axes / family lists are unchanged from v0.4.4.

- **v0.5.1 — 2026-06-04 (registration-ready).** Post-supervisor sign-off administration. No methodological changes from v0.5. Changes:
  - *Header and B1 metadata updated.* Version bumped from v0.5 to v0.5.1; date updated from 2026-05-29 to 2026-06-04; status changed from "draft, holding for supervisor sign-off" to "registration-ready, supervisor sign-off complete."
  - *Embase removal documented (Decision 9).* Embase was originally planned as a sixth database but institutional access could not be obtained within the project timeline (external booking-system constraint). Decision to proceed with five-database search recorded as Decision 9 in Part C and documented in §B6.3. Classification: access limitation, not methodological narrowing. All associated documents (database_queries.md, README, PRISMA checklist mapping, data management plan, pilot search report) updated for consistency. Comprehensive audit trail created in admin/embase_removal_audit_2026-06.md.
  - *Rationale for v0.5.1 version bump.* The protocol status changed materially (draft → registration-ready), supervisor sign-off was obtained, Decision 9 was documented, and seven active documents were updated. This constitutes a discrete checkpoint appropriate for a point-release version number. The protocol is now ready for OSF registration.

---

*End of document.*
