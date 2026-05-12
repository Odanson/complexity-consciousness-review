# Complexity Measures of Consciousness — PRISMA Protocol & 3-Month Action Plan

**Working document — v0.1 — drafted 2026-04-22**
**Lead:** Samson Odan | **Co-supervisors (provisional):** Jurgen (primary), Andrej, Lucia
**Planned external collaborators (later phase):** Adam, Anil Seth

> Purpose of this document. Serve as (a) a pre-registrable **PRISMA-P systematic review protocol** and (b) a **week-by-week action plan** for the next three months. It assumes nothing about which complexity measures are "right"; the review's job is to catalogue what is being used, what each measure actually computes, and where it is misapplied.

---

## Part A — Scientific framing

### A1. Problem statement
"Complexity" has become a load-bearing word in consciousness science without a shared referent. Different authors mean: entropy of a signal, compressibility of a binary pattern, integration of information across a partition, criticality of dynamics, richness of a graph, dimensionality of a manifold, or the geometry of a conceptual "qualia space." These measures are not interchangeable. They quantify **different mathematical primitives** and therefore can only license **different claims** about consciousness. A neuroscientist or psychologist reading the literature today has no clean map from *measure → what it computes → what it can warrant about consciousness*. This review will produce that map.

### A2. Review aims
1. **Catalogue** all quantitative complexity measures that have been applied to neural data in consciousness research.
2. **Classify** them along orthogonal axes — mathematical primitive, data requirements, temporal granularity, aspect of consciousness addressed.
3. **Audit** the fit between each measure's mathematical content and the claims made with it (misuse, overreach, hidden assumptions — e.g., Granger causality as directionality in a densely interconnected system; IIT proxies that use amplitude only and ignore effective connectivity).
4. **Map** measures to aspects of consciousness: level, content, differentiation, integration, structural geometry of experience, temporal flow.
5. **Guide** future use: produce a decision tree / table for "if your question is X, consider measures Y; avoid Z because…".

### A3. Out of scope (explicit)
- Philosophical debates about the meaning of consciousness, except where they constrain measurement.
- Purely theoretical complexity papers with no neural data application (included only if cited as a methodological reference by an empirical paper already in the pool).
- Non-neural complexity (cardiac, metabolic, behavioral) unless used as a control variable in a consciousness study.
- Theory advocacy (IIT vs GNW vs HOT debates) beyond what is needed to understand a given measure.

### A4. Review type and registration
- **Review type:** Systematic review (methodological / measurement-focused). PRISMA 2020 reporting. PRISMA-P 2015 for protocol. Consider **PRISMA-ScR** (scoping review extension, Tricco 2018) if the methodological focus means we are mapping rather than synthesising effect sizes — likely the better fit. **Decision point before Week 2.**
- **Pre-registration:** PROSPERO *or* OSF Registries (PROSPERO has historically rejected methodological scoping reviews; OSF is safer). Target registration end of Week 2.

---

## Part B — PRISMA-P Protocol (draft)

### B1. Administrative
| Field | Value |
|---|---|
| Working title | Complexity measures of consciousness: a systematic methodological review of what they compute and what they can warrant |
| Protocol version / date | v0.1 / 2026-04-22 |
| Registry | OSF Registries (target) — PROSPERO fallback |
| Lead reviewer | Samson Odan |
| Second reviewer | TBD (candidate: a senior lab member or PhD student; required for double-screening) |
| Arbiter | Jurgen or Lucia |
| Funding | Max Planck Institute (confirm) |
| Amendments log | To be maintained in this file |

### B2. Review question
> **PQ1 (primary):** Which quantitative complexity measures have been applied to neural recordings in consciousness research, and what does each measure mathematically compute?
>
> **PQ2:** For each measure, what aspect of consciousness (level, content, differentiation, integration, structure, temporal flow) has been claimed, and is that claim warranted by the measure's mathematical content and by the study's data/design?
>
> **PQ3:** Where are measures being misapplied (e.g., directional inference from correlational measures, effective-connectivity claims from amplitude-only metrics)?
>
> **PQ4:** What are systematic gaps — aspects of consciousness for which no fit-for-purpose complexity measure exists (candidate: structural geometry of experience; subjective temporal flow)?

### B3. Eligibility — PECO framing

We adapt PICO/PECO to a methodological review:

- **P (Population / data):** Human or non-human animal neural recordings, any modality (EEG, MEG, iEEG/ECoG, fMRI, LFP, single-unit, two-photon calcium, wide-field optical).
- **E (Exposure / Index):** Application of at least one quantitative complexity measure (defined broadly — see taxonomy in §B8) to those recordings.
- **C (Comparator):** Either (i) a different state of consciousness (awake vs. sleep / anaesthesia / DOC / psychedelic / meditation / coma / LIS), (ii) a different measure on the same data, or (iii) a within-state correlation with a subjective / behavioural read-out.
- **O (Outcome):** Any claim linking the measure's values to an aspect of consciousness (discrimination, correlation, prediction, mechanistic explanation, negative result).

### B4. Inclusion / exclusion criteria

**Include** if all of:
1. Peer-reviewed journal article, or a clearly citable preprint that has been widely used (≥50 citations as a proxy; reviewed case-by-case).
2. Applies at least one quantitative complexity measure to neural data.
3. Makes or tests a claim relevant to consciousness (level, content, state discrimination, structure).
4. Published 1990-01-01 to search date (allow earlier *only* for seminal methodological papers, e.g., Tononi-Sporns-Edelman 1994 neural complexity).
5. English full text available.

**Exclude** if any of:
1. No neural data (pure theory, simulation-only without a stated empirical extension).
2. Consciousness is mentioned but not measured or manipulated (e.g., a paper about sleep staging that never frames any claim about consciousness).
3. Complexity is mentioned in prose but not quantified.
4. Conference abstract, editorial, commentary without original analysis.
5. Non-English without available translation.
6. Duplicate reports of the same dataset/analysis (keep the most complete).

**Grey zone — flag and decide with supervisor:**
- Simulation studies that propose a measure and validate against a neural-like model (include if widely used on real data elsewhere).
- Pharmaco-EEG studies where the consciousness framing is post-hoc.
- Anaesthesia monitoring papers (BIS-style) — include only if they analyse complexity as such, not if complexity is a black-box component of a proprietary index.

### B5. Information sources
- **Databases:** PubMed/MEDLINE, Scopus, Web of Science (Core Collection), PsycINFO, IEEE Xplore, Embase.
- **Preprints:** bioRxiv, arXiv (q-bio.NC, cs.IT), PsyArXiv — cautious inclusion, see B4.1.
- **Hand-search:** Neuroscience of Consciousness; Consciousness and Cognition; NeuroImage; PLoS Computational Biology; Journal of Neuroscience; Cerebral Cortex; Brain; Current Biology.
- **Backward/forward citation tracking** on a seed set (see B9).
- **Expert elicitation:** solicit suggestions from Juergen, Lucia, Andrew, Anil Seth, Adam; log all suggestions and whether they were already captured by the database search (provides sensitivity estimate).

### B6. Search strategy

Three concept blocks, ANDed. Each block is an OR of synonyms, with MeSH where available (PubMed) and field tags (`tiab` or equivalent per database).

**Block 1 — Consciousness / state**
```
(consciousness OR "state of consciousness" OR "levels of consciousness" OR
"loss of consciousness" OR unconscious* OR wakefulness OR arousal OR
anesthesi* OR anaesthesi* OR sedation OR propofol OR sevoflurane OR
ketamine OR xenon OR
sleep OR NREM OR REM OR "slow wave sleep" OR
"disorder* of consciousness" OR "vegetative state" OR
"unresponsive wakefulness syndrome" OR UWS OR
"minimally conscious state" OR MCS OR coma OR
"locked-in syndrome" OR LIS OR
psychedelic* OR psilocybin OR LSD OR DMT OR ayahuasca OR
meditation OR mindfulness OR
dream* OR lucid)
```

**Block 2 — Complexity / information / dynamics**
```
("Lempel-Ziv" OR LZc OR LZ76 OR LZW OR compressibility OR
"perturbational complexity" OR PCI OR "PCI-state" OR
"integrated information" OR IIT OR "phi" OR
"causal density" OR "causal emergence" OR "phi-ID" OR
"information decomposition" OR
entropy OR "sample entropy" OR "approximate entropy" OR
"permutation entropy" OR "multiscale entropy" OR "spectral entropy" OR
"transfer entropy" OR "mutual information" OR
"Granger causality" OR
"neural complexity" OR "matching complexity" OR
"neural avalanche*" OR "criticality" OR "branching parameter" OR
"long-range temporal correlation*" OR "detrended fluctuation analysis" OR DFA OR
"fractal dimension" OR "correlation dimension" OR "Hurst exponent" OR
"Lyapunov" OR "chaos" OR
"intrinsic dimensionality" OR "participation ratio" OR "manifold" OR
"small-world" OR "modularity" OR "rich-club" OR "hierarchical complexity")
```

**Block 3 — Neural data**
```
(EEG OR electroencephalograph* OR
MEG OR magnetoencephalograph* OR
iEEG OR ECoG OR intracranial OR "local field potential*" OR LFP OR
fMRI OR BOLD OR "functional magnetic resonance" OR
"single-unit" OR "multi-unit" OR
"two-photon" OR "calcium imaging" OR "wide-field" OR
neuroimag* OR "brain activity" OR "neural recording*")
```

**Final query:** `#1 AND #2 AND #3`, with date limit 1990-present, English.

> **Pilot this search before locking it.** Run in PubMed first, sanity-check against the seed list (B9). If any seed paper is not captured, diagnose and revise. Target hit count 3k–15k records; tighten or loosen accordingly.

### B7. Study records — management, selection, extraction

**Reference management:** Zotero group library (shared with supervisors). Export to RIS.

**Deduplication:** Bramer method in Zotero + Rayyan's dedup; manual spot-check.

**Screening platform:** Rayyan (free, dual-blind, conflict tracking). Fallback: Covidence.

**Screening stages:**
1. **Title/abstract** — two reviewers, blinded, independent. **Calibration** on first 100 records, compute Cohen's κ; target κ ≥ 0.7 before proceeding. Recalibrate if drift.
2. **Full text** — two reviewers, independent; reasons for exclusion logged.
3. **Conflict resolution** — arbiter (Juergen / Lucia).

**PRISMA flow diagram** maintained live from Rayyan exports.

**Data extraction:** Piloted form (Google Sheet or Airtable). Pilot on 10 studies, revise. Extracted by one reviewer, 20 % random sample independently re-extracted by second reviewer for quality control. Disagreement → arbiter.

### B8. Data items (extraction fields)

For each included study:

- **Bibliographic:** authors, year, journal, DOI.
- **Design:** species, N, age, population (healthy / DOC / anaesthetised / etc.), state contrast, paradigm.
- **Recording:** modality, channels/voxels, sampling rate, reference, preprocessing pipeline (cite a clear description).
- **Measure(s):** name, exact mathematical variant, formula reference, implementation (toolbox / code / language), parameters (window, embedding dim, etc.).
- **Pre-processing assumptions:** stationarity, normalisation, binarisation, surrogate method.
- **Data requirement:** amplitude only / amplitude + connectivity / perturbation-based / multi-scale.
- **Claim(s):** what is inferred about consciousness; what aspect (level / content / integration / differentiation / structure / temporal flow).
- **Validation:** ground truth used (behavioural report, clinical diagnosis, pharmacological manipulation, etc.); classification accuracy / effect size / CI.
- **Statistical rigor:** multiple-comparison correction, surrogate controls, cross-validation.
- **Reproducibility:** code available (Y/N), data available (Y/N), parameters fully reported (Y/N).
- **Reported limitations / caveats** (verbatim quote).
- **Our flagged misapplications:** a free-text field where reviewers note concerns (e.g., "GC used for directionality on densely coupled system").

### B9. Seed set (backward/forward citation scaffold — tentative, to verify)

*These are starting points, not included-by-default. Listed to (a) pilot the search and (b) seed snowballing. Any that slip through the database search indicate a search-strategy problem.*

- Tononi, Sporns, Edelman 1994 *PNAS* — neural complexity (Cn).
- Tononi & Edelman 1998 *Science* — consciousness and complexity.
- Casali et al. 2013 *Sci Transl Med* — PCI introduction.
- Casarotto et al. 2016 *Ann Neurol* — PCI in DOC.
- Schartner et al. 2015 *PLoS ONE*; 2017 *Neurosci Conscious* — LZc in anaesthesia / psychedelics.
- Sitt et al. 2014 *Brain* — EEG markers in DOC.
- Oizumi, Albantakis, Tononi 2014 *PLoS Comput Biol* — IIT 3.0.
- Mediano, Seth, Barrett et al. — φ-ID, integrated information decomposition.
- Seth 2010 — causal density.
- Luppi et al. 2020–2024 — integrated information in anaesthesia / DOC.
- Toker et al. 2022 *PNAS* — chaos and consciousness.
- Shew & Plenz 2013 — criticality.
- Palva et al. — long-range temporal correlations.
- Carhart-Harris et al. 2014 — entropic brain.
- Varley et al. — redundancy/synergy decompositions.
- Northoff & Lamme reviews — markers of consciousness.
- Julio's qualia-structure / unfolding work (verify citation with Lucia).
- Kiefer, Chang, Anil Seth reviews on complexity measures.

> **Action for Week 1:** build this seed set to ~30 papers with full references and verify with Lucia/Juergen.

### B10. Risk of bias / methodological quality
Classical RoB tools (ROBINS-I, QUADAS-2) do not map neatly onto methodological reviews. We will develop a **measurement-methodology checklist** inspired by QUADAS-2 and the TRIPOD statement, covering:

1. Measure specification (formula unambiguous? parameters reported?).
2. Data suitability (sufficient channels/length for the measure?).
3. Validation (ground truth? cross-validated?).
4. Control for confounds (SNR, sample-rate differences, muscle artefact, state dependence of measure at zero-information limit).
5. Reproducibility (code + data + params).
6. Interpretation (claims commensurate with what the measure computes?).

Each item rated low / some concern / high. Piloted on 10 studies; revised.

### B11. Synthesis plan
- **Narrative synthesis**, organised by the taxonomy in §B12.
- **Summary tables:** (i) measure × mathematical primitive; (ii) measure × data requirement; (iii) measure × consciousness aspect claimed; (iv) measure × validation evidence.
- **Heatmap** of measure × consciousness-state coverage (to identify gaps).
- **Misapplication register** — a structured list of recurring misuses with representative citations.
- **Decision-support appendix** — "if your question is X, these measures are plausibly warranted; these are not, because…".
- **No meta-analysis** of effect sizes is planned (too heterogeneous). If a sub-family (e.g., LZc in DOC) has enough comparable studies, consider a mini meta-analysis.

### B12. Taxonomy (working draft — will be revised after extraction)

**Axis 1 — Mathematical primitive**
1. Entropy family: Shannon, differential, approximate, sample, permutation, spectral, multiscale entropy.
2. Compressibility: Lempel-Ziv (LZ76, LZc, LZW).
3. Information flow: mutual information, transfer entropy, Granger causality, partial directed coherence, phi-ID.
4. Integrated information: φ, φ*, geometric φ, whole-minus-sum φ, empirical φ surrogates.
5. Dynamical / criticality: neural avalanches, branching parameter, DFA / LRTCs, Hurst, Lyapunov exponents, correlation dimension, edge-of-chaos.
6. Structural / graph-theoretic: small-worldness, modularity, rich-club, hierarchical complexity, Tononi-Sporns-Edelman neural complexity.
7. Dimensionality / manifold: intrinsic dimensionality, participation ratio, embedding dimension.
8. Perturbational: PCI, PCI-state, PCI-LZW.
9. Structure-of-experience: qualia-space unfolding, optimal-transport distances between state representations.
10. Hybrid / composite: supervised ML classifiers whose features are any of the above.

**Axis 2 — Data requirement**
- Amplitude only.
- Amplitude + functional connectivity.
- Amplitude + effective connectivity.
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
- Temporal flow (experience of time — under-represented; Samson's interest).

This taxonomy is the review's **conceptual spine**. It will likely shift after extraction; we version it in the amendments log.

### B13. Dissemination
- Target journals: *Nature Reviews Neuroscience*, *Trends in Cognitive Sciences*, *Neuroscience of Consciousness*, *Neuroscience & Biobehavioral Reviews*.
- Preprint on bioRxiv concurrent with submission.
- Companion open resource: extraction spreadsheet + taxonomy table on OSF for community use.
- Conference: ASSC 2026 (if timing permits).

### B14. Ethics & funding
- No primary data collection; no ethics approval required.
- Declare Max Planck affiliation and any other funding.
- Conflict-of-interest: none anticipated.

---

## Part C — 3-month action plan

Calendar-anchored; dates assume start-of-week Monday, Week 1 = 2026-04-20 (current week). Adjust if follow-up with Juergen/Lucia shifts scope.

### Week 1 — 2026-04-20 → 04-26 (THIS WEEK)
**Theme:** Foundations, supervisor alignment, Friday follow-up.

- [ ] Read, in order:
  - **PRISMA 2020** (Page et al., *BMJ* 2021) — reporting checklist.
  - **PRISMA-P 2015** (Moher et al., *BMJ* 2015) — protocol standard.
  - **PRISMA-ScR** (Tricco et al., *Ann Intern Med* 2018) — scoping extension.
  - **Cochrane Handbook** ch. 2–4 (selection and bias).
  - Two exemplar reviews in neuroscience methodology for style: Luppi et al. 2023 review of integrated-information measures; Bayne et al. reviews of markers of consciousness.
- [ ] Draft v0.2 of this document after reading, incorporating PRISMA-P field completeness check.
- [ ] Finalise the **seed paper list** (target 30 papers, full citations, all retrievable). Verify with Lucia.
- [ ] Send a short briefing (≤ 1 page) to Juergen, Lucia, Andrew ahead of Friday's meeting with: (i) proposed review question, (ii) scope boundaries, (iii) top three decisions needed from them (see §D).
- [ ] **Friday follow-up meeting** — lock scope decisions; identify second reviewer.
- [ ] Email Xi Yuan (time/event segmentation) — 10-minute-ask on whether there is an existing catalogue of temporal segmentation methods used in neural data that bears on how temporal complexity is measured.
- [ ] Email Stefan (feature filtering, consciousness → memory) — ask which filtering frameworks he treats as information-theoretic; relevant for any consciousness measure that depends on selecting "relevant" signal dimensions.
- [ ] Email Adam and Anil Seth — *not yet inviting formally*; introduce the project and ask whether they are open to being consulted on scope / expert sift at month 2.
- [ ] Ask Lucia to pass the hello to Christian (as noted).
- [ ] Set up Zotero group library + OSF project page (private for now).

### Week 2 — 04-27 → 05-03
**Theme:** Lock protocol, register, pilot search.

- [ ] Incorporate Friday feedback → v1.0 protocol.
- [ ] Decide systematic review vs. PRISMA-ScR (expect: scoping, given methodological focus).
- [ ] Register on OSF Registries with v1.0 protocol.
- [ ] Pilot Block 1 / Block 2 / Block 3 searches in PubMed. Target 3k–15k hits after AND.
- [ ] Check seed papers are captured; diagnose misses.
- [ ] Meet with institute subject librarian — sanity-check search strings per database (PubMed MeSH ≠ Scopus).
- [ ] Build Rayyan project; invite second reviewer.
- [ ] Draft extraction form; internal review.

### Week 3 — 05-04 → 05-10
**Theme:** Run searches, deduplicate, pilot screening.

- [ ] Lock and run final searches across all databases on same day; archive outputs with query + date.
- [ ] Import to Zotero → Rayyan; deduplicate; record numbers for PRISMA flow.
- [ ] Calibration screen — both reviewers screen first 100 abstracts independently; compute κ; resolve conflicts; update decision rules; **repeat with next 100 if κ < 0.7**.
- [ ] Weekly standup with Juergen / Lucia.

### Weeks 4–6 — 05-11 → 05-31
**Theme:** Title/abstract screening at scale + start full-text.

- [ ] Screen ~1 000 abstracts/week per reviewer (2k pair-reviewed/week). Adjust to real throughput.
- [ ] Conflict log reviewed weekly with arbiter.
- [ ] Begin retrieving full texts of included abstracts.
- [ ] Pilot the extraction form on 10 full-text papers; iterate.
- [ ] Update living PRISMA flow diagram.

### Weeks 7–9 — 06-01 → 06-21
**Theme:** Full-text screening + extraction starts.

- [ ] Complete full-text screening; log exclusion reasons.
- [ ] Start extraction in parallel once form is stable.
- [ ] Backward/forward citation search from the seed set + any high-value included paper.
- [ ] Expert suggestions round — ask Juergen, Lucia, Andrew, Anil, Adam for any paper we missed. Log each; check whether the search retrieved it.
- [ ] Draft taxonomy v2 from what is accumulating in extraction.

### Weeks 10–12 — 06-22 → 07-12
**Theme:** Synthesis, writing, first draft.

- [ ] Complete extraction.
- [ ] Quality check: 20 % random re-extraction by second reviewer.
- [ ] Build synthesis tables and heatmap.
- [ ] Draft manuscript sections: Introduction, Methods (PRISMA), Results (taxonomy + tables + heatmap), Discussion (misapplication register + decision support + gaps → candidate for a new measure).
- [ ] Internal review with Juergen / Lucia / Andrew.
- [ ] Decide whether to formally invite Adam & Anil Seth as co-authors based on contribution level to date.

### Month 4+ (contingency and extension)
- Revisions, journal formatting, preprint.
- **Follow-on design work:** the gaps identified in §B12 Axis-4 (structure of experience; temporal flow) become the design brief for the new measure the lab wants to develop. Don't start this in parallel — it will distort the review.

---

## Part D — Decisions to bring to Friday's meeting

1. **Review type:** full systematic review vs. **PRISMA-ScR scoping review** (recommend the latter).
2. **Scope commitment:** neural signal complexity only (confirmed), or keep a small door open for computational-model papers used as primary methodology references?
3. **Second reviewer identity:** who will dual-screen and dual-extract? Essential PRISMA requirement; this is the main resource ask.
4. **Authorship policy and order** now (before inviting Adam / Anil) to avoid later friction.
5. **Measure taxonomy sign-off** — does §B12 look right to Juergen / Lucia at the level of spine? Anything we are obviously missing?
6. **Registration venue:** OSF vs PROSPERO.
7. **Grey-zone calls:** anaesthesia monitoring / BIS papers; pharmaco-EEG papers; simulation-only papers with widely used code.

---

## Part E — Standing risk register

| Risk | Likelihood | Mitigation |
|---|---|---|
| Hit count too large (>20k) | Medium | Tighten Block 1 to explicit state-change contexts; drop non-specific "wakefulness". |
| Hit count too small (<1k) | Low | Relax Block 3 to include non-neural recording modalities used as consciousness proxies. |
| No second reviewer available | Medium-high | Recruit a rotating pair (senior PhD + postdoc) and define minimum dual-screening (at least all full texts). Document deviation if dual title/abstract screening is not feasible. |
| "Complexity" keyword noise (complexity theory, complexity in software, etc.) | High | Block 2 is deliberately specific. Run noise-audit on first 500 records. |
| Julio's qualia-structure / optimal-transport line under-cited in databases | Medium | Backward-citation scaffold + expert elicitation with Lucia. |
| Scope creep into memory / temporal-flow measure design | High | Explicit hard line: *no new measure development until Month 4*. |
| Timezone / availability mismatch with retired Juergen | Medium | Andrej as stand-in; weekly written updates regardless of meeting cadence. |
| PRISMA requires dual screening throughout; single-reviewer PhD reviews exist but are weaker | Certain | See second-reviewer row; disclose any deviation transparently. |

---

## Part F — Open methodological questions to revisit with supervisors

1. Should the review report a **replication audit** on a small number of headline papers (e.g., re-compute LZc from published data) as a methodological case study? This is high-value but doubles the workload.
2. How to treat the **theory-measure asymmetry**: IIT has a canonical φ but many empirical "proxies"; GNW has no canonical measure; predictive-coding frameworks are typically operationalised via entropy. Do we taxonomise theories separately from measures, or map measures onto the theories that motivate them?
3. **Temporal-flow gap** (Samson's specific interest): if no existing complexity measure captures experienced time, is the review the right venue to say so, or is that a follow-on paper?
4. **Memory connection** (Lucia's prompt): include a short appendix on complexity measures at the consciousness–memory interface (e.g., replay complexity, memory-state entropy)? Keep or punt?

---

## Part G — Glossary of measures (to flesh out in Week 2 alongside seed set)

*Minimal scaffolding — each entry to include: one-line definition, mathematical core, data requirements, canonical reference, typical implementation, known failure modes.*

- LZc / Lempel-Ziv complexity — binarised-signal compressibility; distinguishes states but is driven by spectral content as much as richness; normalisation choice matters.
- PCI — TMS-EEG perturbational integration×differentiation; gold-standard for level; requires perturbation so not pure "read-out".
- Sample / permutation / multiscale entropy — windowed dynamical complexity; parameter-sensitive (m, r, τ); stationarity assumption.
- Transfer entropy / Granger causality — information-flow proxies; **widely misused to claim directionality in densely coupled systems**; surrogate controls and effective-connectivity models needed.
- φ and variants — integrated information; canonical form is intractable; empirical variants (φ*, geometric φ, whole-minus-sum) are not equivalent.
- Neural complexity (Tononi-Sporns-Edelman 1994) — balance of integration and segregation across subsets; N^2 combinatorics; largely superseded in practice.
- DFA / LRTCs — long-range temporal correlations; level of consciousness tracks the Hurst exponent in several datasets; stationarity and detrending sensitive.
- Neural avalanches / branching parameter — criticality signatures; depend on spatial sampling and thresholding.
- φ-ID (synergy / redundancy decomposition) — decomposes integrated information into interpretable atoms; promising for differentiating level vs. content claims.
- Causal emergence / causal density — macro-scale effective information vs. micro.
- Intrinsic dimensionality / manifold measures — dimensionality of neural state space; underused for consciousness specifically.
- Optimal-transport / qualia-unfolding — structural geometry of experience; few empirical applications; *candidate gap*.

---

## Amendments log
- **v0.1 — 2026-04-22** — initial draft.

---

*End of working document.*
