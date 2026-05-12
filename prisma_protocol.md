# Complexity Measures of Consciousness — PRISMA Review Protocol

**Version 0.4.1 — 2026-05-11**

**Lead reviewer:** Samson Odan
**Supervisors:** Jurgen Jost (primary), Lucia Melloni, Andrej Bicanski
**Planned external collaborators (later phase):** Adam Barrett, Anil Seth
**Provisional authorship (in order):** Samson Odan, Lucia Melloni, Andrej Bicanski, Jurgen Jost. May extend on contribution to include Adam Barrett and Anil Seth.

> **For supervisor review.** A pre-registrable PRISMA protocol for a methodological systematic review of complexity measures applied to neural data in consciousness research. Input is invited on the protocol substance (Part B) and on the open decisions in Part C.

---

## Executive summary

"Complexity" is used in consciousness science to refer to fundamentally different mathematical objects — entropy of a signal, compressibility of a binary string, integration of information across a partition, criticality of dynamics, graph topology, manifold dimension, the geometry of a "qualia space." These are not interchangeable. A reader of the literature today has no clean map from *measure → what it computes → what it can warrant about consciousness*.

This review will produce that map. It will (i) catalogue every quantitative complexity measure that has been applied to neural data in a consciousness context, (ii) classify the corpus along four orthogonal axes (mathematical primitive, data requirement, temporal granularity, aspect of consciousness), (iii) audit the fit between each measure's mathematical content and the claims made with it, and (iv) flag systematic gaps — in particular the structural geometry of experience and the experience of time.

The deliverable is a manuscript targeted at *Nature Human Behaviour* (primary; following the Yaron, Melloni, Pitts & Mudrik 2022 scoping-review precedent) or *Neuroscience & Biobehavioral Reviews*, with *Neuroscience of Consciousness* as a fallback. The manuscript will be accompanied by an open companion resource — extraction spreadsheet and taxonomy table on OSF, and an interactive website providing measure-by-measure look-up for the field.

---

## Part A — Scientific framing

### A1. Problem statement
"Complexity" has become a load-bearing word in consciousness science without a shared referent. Different authors mean: entropy of a signal, compressibility of a binary pattern, integration of information across a partition, criticality of dynamics, richness of a graph, dimensionality of a manifold, or the geometry of a conceptual "qualia space." These measures are not interchangeable. They quantify **different mathematical primitives** and therefore can only license **different claims** about consciousness. A neuroscientist or psychologist reading the literature today has no clean map from *measure → what it computes → what it can and cannot warrant about consciousness → how the measure relates to a given theoretical construct or theory*. This review will produce that map.

### A2. Review aims
1. **Catalogue** every quantitative complexity measure that has been applied to neural data — invasive or non-invasive, in humans or non-human animals — in consciousness research.
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
| Protocol version / date | v0.4.1 / 2026-05-11 |
| Registry | OSF Registries (target) |
| Lead reviewer | Samson Odan |
| Provisional authorship (in order) | Samson Odan; Lucia Melloni; Andrej Bicanski; Jurgen Jost. Adam Barrett and Anil Seth to be added on contribution. |
| Screening model | Calibrated single-reviewer + ASReview active-learning prioritisation (see §B7); precedent: Yaron, Melloni, Pitts & Mudrik 2022, *Nat Hum Behav* |
| Arbiter | Any two of Jurgen Jost, Lucia Melloni, Andrej Bicanski |
| Funding | Max Planck School of Cognition (to confirm) |
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
- **Embase** — Emtree-based pharmacology coverage finer than MeSH; relevant because anaesthesia is one of our central consciousness-state contrasts.

**Preprints.** bioRxiv, **medRxiv** (clinical / DOC / anaesthesia preprints land here, not bioRxiv), arXiv (q-bio.NC, cs.IT), PsyArXiv — inclusion per the revised §B4 criterion 1 (no citation threshold).

**Hand-search.** *Neuroscience of Consciousness*; *Consciousness and Cognition*; *NeuroImage*; *PLoS Computational Biology*; *Journal of Neuroscience*; *Cerebral Cortex*; *Brain*; *Current Biology*; *Nature Communications*; *eLife*; *PNAS* (key venue for seed-list papers — Tononi-Sporns-Edelman 1994, Toker 2022); *Anesthesiology* or *British Journal of Anaesthesia* (broad-scope venues where complexity-of-consciousness work currently lands but our previous list missed).

**Backward / forward citation tracking.** Performed using **Citationchaser** (free, reproducible, Zotero-integrated) — named here per PRISMA-S item 3 (citation-tracking is not reproducible without a named tool). Seed set in §B9.

**Expert elicitation.** Suggestions solicited from Jurgen, Lucia, Andrej, Anil Seth, and Adam Barrett; every suggestion logged together with whether the database search already captured it (this gives a sensitivity estimate).

**Reference paper for measure-to-NCC mapping.** Yaron, Pitts, Mudrik & Melloni 2024, *Neurosci & Biobehav Rev* (PII: S0149763424001398) — used as a measure-mapping precedent. The Block 2 term list and §B12 taxonomy are cross-checked against the measures catalogued there.

### B6. Search strategy — locked v1.0

Three concept blocks, ANDed. Each block is an OR of synonyms. The PubMed string below is the canonical reference; equivalent translations for Scopus, Web of Science, PsycINFO, IEEE Xplore, and Embase are in the companion document **`database_queries.md`** and use the same blocks with database-specific field tags.

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

The single remaining miss — Sitt et al. 2014, *Brain* (PMID 24919971) — is a **confirmed** database miss. Block 2 was deliberately broadened in v0.4.1 to include **wSMI** (weighted symbolic mutual information) specifically as a recovery attempt for Sitt 2014, since the paper uses wSMI prominently in its 92-marker battery. The v0.4.1 re-pilot showed `B2:–` for Sitt 2014 PMID despite the wSMI term being in the search — the paper's published abstract genuinely contains none of the technical measure names, only the title-level "neural signatures of consciousness" framing. Further broadening (e.g., adding `"neural signature*"`) was rejected on noise grounds across all six databases.

Sitt 2014 is therefore recovered through §B5 backward / forward citation tracking on the seed set, which it satisfies via virtually every captured DOC / EEG paper. This recovery path is documented in §B9a and the **confirmed** miss status was carried over from a provisional flag in v0.3 to a confirmed entry in v0.4.1.

The three methodology-only seeds (§B9b — Tononi-Sporns-Edelman 1994; Oizumi-Albantakis-Tononi 2014; Chis-Ciure, Melloni & Northoff 2024) are correctly **not** captured by the database search; all three are theoretical / derivation / framework papers without neural-data application. They enter the review via the §B4 seminal-methodological-paper exception, not via search, and are validated only by PMID resolution.

#### B6.3 Search audit trail

On the day of the locked multi-database search (TBD, before OSF registration), all six queries will be run within a 24-hour window. Raw query strings, date / time of execution, per-database hit counts, and exported result files will be archived as `search_log_YYYY-MM-DD.txt` plus per-database RIS exports in the OSF project. This file forms the audit trail PRISMA-ScR / JBI methodology requires.

### B7. Study records — management, selection, extraction

**Reference management.** Zotero group library (shared with supervisors); export to RIS.

**Deduplication.** Bramer method in Zotero plus Rayyan's deduplicator; manual spot-check.

**Screening platform.** Rayyan (free, conflict-tracked) for the calibration phase; **ASReview** (van de Schoot et al. 2021, *Nat Mach Intell*) for the active-learning prioritised screening of the bulk corpus.

**Screening model — calibrated single-reviewer + active-learning prioritisation.**

The lab does not have personnel capacity for a full dual-screening pass. Following the JBI scoping-review methodology (Peters et al. 2020; Pollock et al. 2023) — which explicitly does not mandate strict dual independent screening — and following the precedent of **Yaron, Melloni, Pitts & Mudrik 2022, *Nature Human Behaviour***, which published a scoping review in this exact field without an ideal dual-reviewer setup, the screening proceeds as follows:

1. **Calibration (dual-screen).** Two reviewers — Samson plus a rotating supervisor (Jurgen / Lucia / Andrej, the precise pairing logged) — independently screen the first 200 title / abstract records. Cohen's κ is computed; target κ ≥ 0.7. Disagreements are resolved with the third supervisor as arbiter. If κ < 0.7 the inclusion criteria are clarified and calibration is repeated on the next 200 records.
2. **Bulk title / abstract screening (single-reviewer + ASReview).** Samson screens the remainder with ASReview's active-learning prioritisation, which reorders records by inclusion probability after each labelling decision. Screening proceeds until the inclusion rate drops below an a-priori stopping criterion (≤ 5 inclusions in the last 100 screened) — the standard ASReview saturation heuristic — at which point the unscreened tail is sampled and audited rather than fully screened.
3. **Full-text screening (dual-screen).** Two reviewers (Samson + rotating supervisor) independently screen every full-text retrieval; reasons for exclusion logged. The full-text count is small enough that full dual screening is feasible.
4. **Conflict resolution.** Arbiter — any two of Jurgen, Lucia, Andrej.
5. **Supervisor spot-checks.** A 10 % random sample of single-reviewer title / abstract decisions is re-screened by a supervisor; disagreements trigger re-screening of adjacent records and an update to the inclusion rubric.

**Transparency.** The deviation from PRISMA's default dual independent title / abstract screening is documented here, in §C, and in the OSF registration. The Yaron et al. 2022 NHB review is cited as published precedent.

**PRISMA flow diagram** maintained live from Rayyan / ASReview exports.

**Data extraction.** Piloted form (Google Sheet or Airtable). Pilot on 10 studies, then revise. Extracted by Samson; a 20 % random sample independently re-extracted by a supervisor for quality control. Disagreement → arbiter.

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

To be added on completion of the seed-elicitation pass with supervisors:

- Tononi & Edelman 1998 *Science* — consciousness and complexity (verify whether empirical or methodology-only).
- Mediano, Seth, Barrett et al. 2021 — φ-ID, integrated-information decomposition.
- Seth, Barrett, Barnett 2011 — *Causal density and integrated information as measures of conscious level*.
- Luppi et al. 2020–2024 — integrated information in anaesthesia / DOC (additional papers).
- Shew & Plenz 2013, *The Neuroscientist* — functional benefits of criticality in the cortex.
- Palva et al. 2001–2013 — long-range temporal correlations.
- Varley et al. 2021–2023 — redundancy / synergy decompositions.
- Northoff & Lamme 2006–2020 — reviews on markers of consciousness.
- Kiefer, Chang, Anil Seth — reviews on complexity measures (verify).

> **Footnote on Sitt 2014.** This paper is retained on the empirical seed list as a transparency anchor: it is one of the most cited DOC-EEG complexity papers and any reviewer reproducing the search will need to see why it appears as missed. Its abstract uses the title-level "neural signatures of consciousness" framing without naming any specific complexity measure (although the paper computes 92 markers including permutation entropy and weighted symbolic mutual information). Block 2 broadening to `"neural signature*"` was considered and rejected on noise grounds. The paper is recovered through backward / forward citation tracking from any captured paper that cites it (§B5).

#### B9b — Methodology-only seeds (included by exception, not via search)

Theoretical / derivation papers grounding the measurement framework. They have no empirical neural-data application and therefore correctly fail Block 3 of the search. Included via §B4 inclusion criterion 4 (seminal methodological papers).

| # | Citation | PMID | DOI |
|---|---|---|---|
| 1 | Tononi, Sporns, Edelman 1994, *PNAS* — *A measure for brain complexity: relating functional segregation and integration in the nervous system* | 8197179 | 10.1073/pnas.91.11.5033 |
| 2 | Oizumi, Albantakis, Tononi 2014, *PLoS Comput Biol* — *From the phenomenology to the mechanisms of consciousness: Integrated Information Theory 3.0* | 24811198 | 10.1371/journal.pcbi.1003588 |
| 3 | Chis-Ciure, Melloni & Northoff 2024, *Neurosci & Biobehav Rev* — *A measure centrality index for systematic empirical comparison of consciousness theories* (the "Yaron paper") | 38615851 | 10.1016/j.neubiorev.2024.105670 |

Additional methodology-only papers may be added as the seed-elicitation pass proceeds (candidates: Tononi 2008 *Biol Bull* on consciousness as integrated information; theoretical IIT 4.0 papers if relevant).

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

Each item rated *low concern / some concern / high concern*. Pilot the checklist on 10 studies, revise, then apply to the full corpus. **Items 1, 5, and 6 feed the §B11 misapplication register directly.**

This is a deliberate departure from the typical scoping-review default of skipping appraisal: it is justified by the review's specific aim of producing usage guidance, not just a map.

### B11. Synthesis plan
- **Narrative synthesis**, organised by the taxonomy in §B12.
- **Summary tables:** (i) measure × mathematical primitive; (ii) measure × data requirement; (iii) measure × consciousness aspect claimed; (iv) measure × validation evidence.
- **Heatmap** of measure × consciousness-state coverage to identify gaps.
- **Misapplication register** — a structured list of recurring misuses with representative citations.
- **Decision-support appendix** — "if your question is X, these measures are plausibly warranted; these are not, because…".
- **No meta-analysis** of effect sizes is planned (heterogeneity is too high). If a sub-family (e.g., LZc in DOC) has enough comparable studies, a mini meta-analysis may be added.

### B12. Taxonomy (working draft — will be revised after extraction)

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

> **Coverage check.** Lucia flagged that the measures inventory must be demonstrably complete — "if the set isn't complete then the review is not either." The Block 2 term list and Axis 1 family list have been cross-checked against (a) the Yaron, Pitts, Mudrik & Melloni 2024 *NBR* mapping of measures to candidate NCCs, (b) the wSMI / Dehaene-King line, and (c) the phase / dynamical-systems family (Varela, Kelso, Le Van Quyen). The taxonomy is open to further additions during the seed-elicitation pass; any addition triggers a Block 2 re-pilot.

### B13. Dissemination
- **Target journals.** *Nature Human Behaviour* (primary — Yaron, Melloni, Pitts & Mudrik 2022 precedent in the same field); *Neuroscience & Biobehavioral Reviews* (strong fallback — Yaron, Pitts, Mudrik & Melloni 2024 precedent). *Neuroscience of Consciousness* as third option. *Nature Reviews Neuroscience* and *Trends in Cognitive Sciences* have been removed from the target list — they rarely publish systematic / scoping reviews of this kind (Lucia, 2026-05-10).
- **Preprint** on bioRxiv concurrent with submission.
- **Companion open resource.** Extraction spreadsheet + taxonomy table on OSF; **interactive companion website** providing measure-by-measure look-up keyed by Axis 1–8 (cf. the Yaron-Melloni NHB companion site as a precedent).
- **Conference.** ASSC 2026 (if timing permits).

### B14. Ethics & funding
- No primary data collection; no ethics approval required.
- Declare Max Planck School of Cognition affiliation and any other funding.
- No conflicts of interest anticipated.

---

## Part C — Decisions and their resolutions

Status of the seven decisions raised in v0.2 / v0.3, after the supervisor review pass on 2026-05-10.

1. **Review type — Resolved.** Locked to **PRISMA-ScR scoping review**. Endorsed by Lucia ("yes, PRISMA-ScR is the right call") and Andrej ("I tend to agree").
2. **Scope commitment — Resolved.** Neural signal complexity, both invasive and non-invasive, in humans and non-human animals. Tightening to human-only was considered and rejected (would structurally exclude measure families that depend on dense sampling — avalanche statistics, single-unit-derived entropies); cross-species interpretive caveat added to §A3 and §B8 instead.
3. **Screening model — Resolved.** Calibrated single-reviewer + ASReview active-learning prioritisation (see §B7), citing Yaron, Melloni, Pitts & Mudrik 2022 *Nat Hum Behav* as published precedent. The lab does not have capacity for full dual independent title / abstract screening; this plan replaces the v0.3 "TBD second reviewer" entry.
4. **Authorship policy and order.** To settle before Adam Barrett and Anil Seth are formally invited; provisional order Samson (lead) → Jurgen → Lucia → Andrej, with Adam Barrett and Anil Seth added on contribution.
5. **Taxonomy sign-off — Resolved.** Lucia endorsed the four-axis spine and proposed two further axes (spatial scale, theory anchoring); both adopted in §B12 plus two further axes (causal vs descriptive; validation evidence type). Axis 1 expanded with wSMI and a phase / dynamical-systems family.
6. **Registration venue — Resolved.** **OSF Registries.**
7. **Grey-zone calls — Status: agreed.** Anaesthesia-monitoring papers, pharmaco-EEG, simulation-only papers retained as flag-and-decide grey-zone items in §B4.

> Remaining open item: **OSF registration timing** — before vs after the multi-database run. To be decided in the next supervisor meeting.

---

## Part D — Risk register

| Risk | Likelihood | Mitigation |
|---|---|---|
| Hit count too large (> 20 k) | Medium | Tighten Block 1 to explicit state-change contexts; drop non-specific "wakefulness". |
| Hit count too small (< 1 k) | Low | Relax Block 3 to include non-neural recording modalities used as consciousness proxies. |
| No second reviewer available | Medium-high | Recruit a rotating pair (senior PhD + postdoc); define a minimum dual-screening floor (at least all full texts). Document any deviation transparently. |
| "Complexity" keyword noise (complexity theory, software complexity, etc.) | High | Block 2 is deliberately specific. Run a noise audit on the first 500 records. |
| Qualia-structure / optimal-transport line under-cited in databases | Medium | Backward-citation scaffold; expert elicitation. |
| Scope creep into measure design before the review is complete | High | Hard line: no new-measure development inside the review window. |
| Cross-institute / part-time supervisor availability | Medium | Stand-in coverage between Lucia and Andrej; weekly written updates regardless of meeting cadence. |
| PRISMA requires dual screening; single-reviewer reviews exist but are weaker | Certain | See second-reviewer row; disclose any deviation transparently. |

---

## Part E — Open methodological questions

1. **Replication audit.** Should the review include a small replication audit on a handful of headline papers (e.g., re-compute LZc from published data) as a methodological case study? High-value but roughly doubles the workload.
2. **Theory-anchoring display (reframed in v0.4 per Lucia's email).** Now that PQ5 and the new Axis 6 carry the substantive work of cataloguing each measure's theory provenance, the open question is how to *display* the mapping — as one summary table of measures × theories, or as side-by-side per-theory tables, or as a layered map. To decide after first 30 extractions when the empirical density is visible.
3. **Temporal-flow gap.** If no existing complexity measure captures experienced time, is the review the right venue to say so, or is that better treated as a follow-on paper?

---

## Part F — Glossary of measures (working draft)

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

---

*End of document.*
