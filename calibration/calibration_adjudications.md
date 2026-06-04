# Calibration adjudications — silently-skipped records and maybe-zone disagreements

**Companion to:** `calibration_results.md`
**Adjudicated by:** Samson Odan (lead reviewer)
**Date:** 2026-05-28

This document records the human-reconciliation decisions for the two classes of records flagged by the 200-paper calibration:

- **5 silently-skipped records** — abstract-less or problematic-abstract papers that Elicit's pipeline silently omitted. These were screened manually by exception (§B7).
- **5 maybe-zone disagreements** — paired records where Elicit and the blind human screen produced different binary verdicts because one or more criterion calls sat at a fuzzy boundary. These were re-read with both Elicit's per-criterion rationale and the blind human notes in view.

Decisions here are reconciled (post-Elicit-reading), not blind. The blind decisions live in `calibration_200_screening (human).csv`; the reconciled versions are mirrored into `calibration_200_screening_reconciled.csv`.

---

## 1. Silently-skipped records (n = 5)

### PMID 11811170 — *Is MRI indicated before reduction of a unilateral cervical facet dislocation?* (Hart, Vaccaro & Nachwalter, 2002)

**Decision: EXCLUDE.** Clinical controversy / opinion article on MRI use in cervical spine trauma management. The paper concerns neurologic injury risk and treatment decisions after spinal trauma, not consciousness or consciousness-related neural dynamics, and does not apply a complexity measure to neural data. Falls outside the review's eligibility criteria.

### PMID 25716830 — *Granger causality analysis in neuroscience and neuroimaging* (Seth et al., 2015)

**Decision: EXCLUDE (retained as methodological background reference).**

- Consciousness: maybe/no
- Neural data: maybe
- Complexity / information dynamics: yes (Granger causality; directed functional connectivity; information-flow measure)
- Study type: methodological toolbox / review

Methodological overview/tutorial of Granger causality for neuroscience and neuroimaging. Although consciousness is mentioned as one possible application domain, the paper does not investigate consciousness, does not analyse a consciousness-related empirical neural dataset, and does not make a consciousness claim. Retained as a methodological background reference and taxonomy source for Granger causality, but excluded from the review corpus.

### PMID 30618577 — *Sleep, Wake, and Critical Brain States: Corollaries From Brain Dynamics* (Iyer, 2018)

**Decision: INCLUDE.**

- Consciousness: yes/maybe
- Neural data: maybe
- Complexity / information dynamics: yes (criticality, scale-free dynamics, long-range temporal correlations, neuronal avalanches, EEG/LFP dynamics)
- Study type: yes/maybe (opinion / theoretical synthesis)

Opinion / synthesis article reviewing criticality-based brain dynamics across sleep–wake states using neural complexity-related metrics (LRTC, neuronal avalanches, scale-free dynamics, EEG/LFP temporal structure). Although not an original empirical study, the article is directly relevant to the mapping of complexity measures and their interpretation in consciousness-related neural states (sleep, wakefulness, vigilance, arousal). Included as a conceptual / methodological synthesis within the criticality lineage.

### PMID 20421793 — *Artefact in the EEG monitoring in a patient with brain metastasis* (Faraoni et al., 2010)

**Decision: EXCLUDE.** Clinical correspondence / case report on artefacts in EEG-based anaesthesia monitoring (entropy and bispectral index) in a patient with brain metastases. Although EEG-derived entropy measures are discussed, the scientific aim is monitoring artefact and interpretation of anaesthetic depth indices in the context of cerebral pathology, not the study of consciousness or consciousness-related neural complexity.

### PMID 8268440 — *The anesthetic management of a patient with a thoracic aortic aneurysm...* (Mori et al., 1993)

**Decision: EXCLUDE.** Clinical anaesthesia case report describing airway management and cardiopulmonary complications during thoracic aortic aneurysm surgery. Although EEG monitoring is briefly used intraoperatively, the study concerns anaesthetic management and respiratory/hemodynamic stabilisation rather than consciousness or complexity measures applied to neural data.

**Silently-skipped summary: 1 INCLUDE · 4 EXCLUDE.**

---

## 2. Maybe-zone disagreements (n = 5)

### PMID 38136525 — *From Black Holes Entropy to Consciousness: The Dimensions of the Brain Connectome* (Le Bihan, 2023)

- Blind: Human = **Include** | Elicit = **Exclude** (score 1.4; per-criterion cons=maybe / data=no / meas=no / type=no)
- **Reconciled: EXCLUDE (retain as B4 background / theoretical context).**

The paper is explicitly about consciousness and discusses entropy / information-theoretic ideas, but it does not analyse empirical neural data or operationally apply a complexity measure to neural recordings. It is a conceptual / theoretical framework paper and therefore fails the protocol's empirical eligibility criteria. Retained as background / theoretical context (§B4), not as an included study in the review corpus.

### PMID 33504952 — *Out-of-step: brain-heart desynchronisation in anxiety disorders* (Tumati et al., 2021)

- Blind: Human = **Maybe** | Elicit = **Exclude** (score 1.4; per-criterion all `no`)
- **Reconciled: EXCLUDE.**

Review / theoretical article on neuro-cardiac synchronisation and anxiety disorders. Although the paper discusses phase synchronisation, intertrial coherence, heartbeat-evoked potentials, and spatiotemporal neural dynamics, consciousness is not the primary research target and no complexity measure is operationally applied to consciousness-related neural data.

### PMID 18990620 — *Detrended fluctuation analysis of intracranial pressure predicts outcome following traumatic brain injury* (Burr et al., 2008)

- Blind: Human = **Exclude** | Elicit = **Include** (score 3.5; per-criterion cons=maybe / data=maybe / meas=yes / type=yes)
- **Reconciled: EXCLUDE (confirmed).**

The paper applies DFA to intracranial pressure recordings in TBI patients to predict neurological status, survival, and functional outcome. Although a consciousness-related clinical measure (Glasgow Coma Scale) appears as an outcome / covariate, consciousness is not the primary scientific target, and no complexity measure is operationally used to study consciousness or conscious state.

### PMID 20626893 — *Investigating the synchronisation of hippocampal neural network in response to acute nicotine exposure* (Akkurt et al., 2010)

- Blind: Human = **Exclude** | Elicit = **Include** (score 4.3; per-criterion cons=maybe / data=yes / meas=yes / type=yes)
- **Reconciled: EXCLUDE (confirmed).**

The paper applies approximate entropy to hippocampal gamma oscillations in rat slice recordings to study nicotine-induced neural synchronisation and cognition/memory-related dynamics. Although neural complexity is quantified, consciousness is not the scientific target and no complexity measure is used to study conscious state or consciousness-related neural dynamics.

### PMID 25837427 — *Large-scale persistent network reconfiguration induced by ketamine in anesthetised monkeys: relevance to mood disorders* (Lv et al., 2016)

- Blind: Human = **Exclude** | Elicit = **Include** (score 4.3; per-criterion cons=maybe / data=yes / meas=maybe / type=yes)
- **Reconciled: EXCLUDE (confirmed).**

The paper analyses whole-brain resting-state fMRI and graph-theoretic network properties following ketamine administration in anesthetised macaque monkeys. Although neural network complexity / connectivity measures are applied to neural data, the scientific target is antidepressant action and mood-disorder circuitry rather than consciousness or conscious state. Anaesthesia serves as an experimental imaging condition rather than a consciousness manipulation of interest.

**Maybe-zone summary: 5 EXCLUDE.** Two blind-human decisions flipped (PMID 38136525 Include → Exclude; PMID 33504952 Maybe → Exclude); three blind-human Excludes were confirmed.

---

## Subsequent adjudication (2026-05-29)

### PMID 16632826 — *Spectral entropy and bispectral index as measures of the electroencephalographic effects of propofol* (Ellerkmann et al., 2006, *Anesthesia & Analgesia*)

- Blind: Human = *(blank — not screened in the original pass)* | Elicit = **Include** (score 4.9; per-criterion cons=yes / data=yes / meas=yes / type=yes)
- **Reconciled: INCLUDE.**

Empirical EEG study examining depth of anaesthesia during propofol administration using entropy-based measures (state entropy, response entropy) alongside the bispectral index (BIS). The study directly investigates consciousness-related state changes (anaesthetic depth), applies complexity / information-theoretic measures to neural data, and satisfies all four §B7 eligibility criteria. The original blind blank was a screening omission rather than an undecided call; the reconciled CSV (`calibration_200_screening_reconciled.csv`) now records this decision with the `post_resolution` note.

**Updated reconciliation count:** 11 total post-resolution edits to the blind set — 2 maybe-zone flips, 3 maybe-zone confirmations, 5 silently-skipped fills (1 Include, 4 Exclude), and this 1 blank-fill (Include). All recorded in the reconciled CSV's `post_resolution` column for the OSF audit trail.
