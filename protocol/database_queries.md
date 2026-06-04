# Locked search strategy — six database queries

**Companion to:** `prisma_protocol.md` §B6
**Status:** Locked v1.0
**Pilot date:** 2026-05-07
**Reference hit count (PubMed):** 4,580 records

> Each query below preserves the same three-block Boolean structure (Block 1 = consciousness / state, Block 2 = complexity / information / dynamics, Block 3 = neural data) and translates only the field-tag syntax, phrase quoting, and date / language filters to the database's native query language. The PubMed query in §0 is the canonical reference; if any term needs to change, change it there first, then re-derive the others.

---

## §0. PubMed / MEDLINE — canonical

Run via PubMed Advanced Search or NCBI E-utilities. No field tags are used — PubMed's automatic term mapping handles MeSH expansion for unscoped terms.

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
OR "perturbational complexity" OR PCI OR "PCI-state"
OR "integrated information" OR IIT OR phi
OR "causal density" OR "causal emergence" OR "phi-ID"
OR "information decomposition"
OR entropy OR "sample entropy" OR "approximate entropy"
OR "permutation entropy" OR "multiscale entropy" OR "spectral entropy"
OR "transfer entropy" OR "mutual information" OR "Granger causality"
OR "neural complexity" OR "matching complexity"
OR "neural avalanche*" OR criticality OR "branching parameter"
OR "long-range temporal correlation*" OR "detrended fluctuation analysis" OR DFA
OR "fractal dimension" OR "correlation dimension" OR "Hurst exponent"
OR Lyapunov OR chaos
OR "intrinsic dimensionality" OR "participation ratio" OR manifold
OR "small-world" OR modularity OR "rich-club" OR "hierarchical complexity"
OR "signal complexity" OR "signal diversity" OR "EEG complexity"
OR "complexity measure*" OR "complexity marker*")
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

**Final.** `Block 1 AND Block 2 AND Block 3`. Filters: English; 1990-01-01 to search date. Hit count on 2026-05-07: **4,580**.

---

## §1. Scopus

Run via the Scopus Advanced Search box. `TITLE-ABS-KEY()` searches title, abstract, author keywords, and indexed keywords — the closest analogue to PubMed's automatic term-mapping behaviour.

```
TITLE-ABS-KEY(
  ((consciousness OR "state of consciousness" OR "levels of consciousness"
    OR "loss of consciousness" OR unconscious* OR wakefulness OR arousal
    OR anesthesi* OR anaesthesi* OR sedation OR propofol OR sevoflurane
    OR ketamine OR xenon OR sleep OR NREM OR REM OR "slow wave sleep"
    OR "vegetative state" OR "unresponsive wakefulness syndrome" OR UWS
    OR "minimally conscious state" OR MCS OR coma OR "locked-in syndrome"
    OR LIS OR psychedelic* OR psilocybin OR LSD OR DMT OR ayahuasca
    OR meditation OR mindfulness OR dream* OR lucid)
  AND
   ("Lempel-Ziv" OR LZc OR LZ76 OR LZW OR compressibility
    OR "perturbational complexity" OR PCI OR "PCI-state"
    OR "integrated information" OR IIT OR phi
    OR "causal density" OR "causal emergence" OR "phi-ID"
    OR "information decomposition"
    OR entropy OR "sample entropy" OR "approximate entropy"
    OR "permutation entropy" OR "multiscale entropy" OR "spectral entropy"
    OR "transfer entropy" OR "mutual information" OR "Granger causality"
    OR "neural complexity" OR "matching complexity"
    OR "neural avalanche*" OR criticality OR "branching parameter"
    OR "long-range temporal correlation*" OR "detrended fluctuation analysis" OR DFA
    OR "fractal dimension" OR "correlation dimension" OR "Hurst exponent"
    OR Lyapunov OR chaos
    OR "intrinsic dimensionality" OR "participation ratio" OR manifold
    OR "small-world" OR modularity OR "rich-club" OR "hierarchical complexity"
    OR "signal complexity" OR "signal diversity" OR "EEG complexity"
    OR "complexity measure*" OR "complexity marker*")
  AND
   (EEG OR electroencephalograph* OR MEG OR magnetoencephalograph*
    OR iEEG OR ECoG OR intracranial OR "local field potential*" OR LFP
    OR fMRI OR BOLD OR "functional magnetic resonance"
    OR "single-unit" OR "multi-unit" OR "two-photon" OR "calcium imaging"
    OR "wide-field" OR neuroimag* OR "brain activity" OR "neural recording*"
    OR TMS OR "TMS-EEG" OR "TMS-evoked" OR "TMS evoked"
    OR "transcranial magnetic stimulation")
  )
)
AND PUBYEAR > 1989
AND LANGUAGE(english)
```

**Notes.** Scopus uses `*` as a multi-character wildcard. Hyphenated phrases (`"Lempel-Ziv"`, `"TMS-EEG"`) are treated as exact phrases. `PUBYEAR > 1989` excludes 1989 and earlier.

---

## §2. Web of Science (Core Collection)

Run via Advanced Search; `TS=` is "Topic" — searches title, abstract, author keywords, and Keywords Plus.

```
TS=(
  ((consciousness OR "state of consciousness" OR "levels of consciousness"
    OR "loss of consciousness" OR unconscious* OR wakefulness OR arousal
    OR anesthesi* OR anaesthesi* OR sedation OR propofol OR sevoflurane
    OR ketamine OR xenon OR sleep OR NREM OR REM OR "slow wave sleep"
    OR "vegetative state" OR "unresponsive wakefulness syndrome" OR UWS
    OR "minimally conscious state" OR MCS OR coma OR "locked-in syndrome"
    OR LIS OR psychedelic* OR psilocybin OR LSD OR DMT OR ayahuasca
    OR meditation OR mindfulness OR dream* OR lucid)
  AND
   ("Lempel-Ziv" OR LZc OR LZ76 OR LZW OR compressibility
    OR "perturbational complexity" OR PCI OR "PCI-state"
    OR "integrated information" OR IIT OR phi
    OR "causal density" OR "causal emergence" OR "phi-ID"
    OR "information decomposition"
    OR entropy OR "sample entropy" OR "approximate entropy"
    OR "permutation entropy" OR "multiscale entropy" OR "spectral entropy"
    OR "transfer entropy" OR "mutual information" OR "Granger causality"
    OR "neural complexity" OR "matching complexity"
    OR "neural avalanche*" OR criticality OR "branching parameter"
    OR "long-range temporal correlation*" OR "detrended fluctuation analysis" OR DFA
    OR "fractal dimension" OR "correlation dimension" OR "Hurst exponent"
    OR Lyapunov OR chaos
    OR "intrinsic dimensionality" OR "participation ratio" OR manifold
    OR "small-world" OR modularity OR "rich-club" OR "hierarchical complexity"
    OR "signal complexity" OR "signal diversity" OR "EEG complexity"
    OR "complexity measure*" OR "complexity marker*")
  AND
   (EEG OR electroencephalograph* OR MEG OR magnetoencephalograph*
    OR iEEG OR ECoG OR intracranial OR "local field potential*" OR LFP
    OR fMRI OR BOLD OR "functional magnetic resonance"
    OR "single-unit" OR "multi-unit" OR "two-photon" OR "calcium imaging"
    OR "wide-field" OR neuroimag* OR "brain activity" OR "neural recording*"
    OR TMS OR "TMS-EEG" OR "TMS-evoked" OR "TMS evoked"
    OR "transcranial magnetic stimulation")
  )
)
AND LA=(English)
AND PY=(1990-2026)
```

**Notes.** WoS treats hyphenated terms as separate words inside `TS=`; the quoted-phrase form (`"Lempel-Ziv"`) is necessary. Wildcards: `*` (multi-char), `?` (single-char), `$` (zero-or-one). Update `PY=` upper bound to the actual search year on each rerun.

---

## §3. PsycINFO (EBSCOhost interface)

Run via the EBSCOhost Advanced Search builder, three rows (one per block), default field "Select a Field (optional)" which searches title, abstract, author keywords, and subject headings. Combine with AND.

**Row 1 — Block 1 (paste into search box, no field tag)**
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

**Row 2 — Block 2**
```
("Lempel-Ziv" OR LZc OR LZ76 OR LZW OR compressibility
OR "perturbational complexity" OR PCI OR "PCI-state"
OR "integrated information" OR IIT OR phi
OR "causal density" OR "causal emergence" OR "phi-ID"
OR "information decomposition"
OR entropy OR "sample entropy" OR "approximate entropy"
OR "permutation entropy" OR "multiscale entropy" OR "spectral entropy"
OR "transfer entropy" OR "mutual information" OR "Granger causality"
OR "neural complexity" OR "matching complexity"
OR "neural avalanche*" OR criticality OR "branching parameter"
OR "long-range temporal correlation*" OR "detrended fluctuation analysis" OR DFA
OR "fractal dimension" OR "correlation dimension" OR "Hurst exponent"
OR Lyapunov OR chaos
OR "intrinsic dimensionality" OR "participation ratio" OR manifold
OR "small-world" OR modularity OR "rich-club" OR "hierarchical complexity"
OR "signal complexity" OR "signal diversity" OR "EEG complexity"
OR "complexity measure*" OR "complexity marker*")
```

**Row 3 — Block 3**
```
(EEG OR electroencephalograph* OR MEG OR magnetoencephalograph*
OR iEEG OR ECoG OR intracranial OR "local field potential*" OR LFP
OR fMRI OR BOLD OR "functional magnetic resonance"
OR "single-unit" OR "multi-unit" OR "two-photon" OR "calcium imaging"
OR "wide-field" OR neuroimag* OR "brain activity" OR "neural recording*"
OR TMS OR "TMS-EEG" OR "TMS-evoked" OR "TMS evoked"
OR "transcranial magnetic stimulation")
```

**Combine** all three rows with AND. Apply EBSCO limits: language = English; date 1990–present; document type = Peer-reviewed journals (initially leave open — narrow during screening, not at search).

**Notes.** EBSCO's `*` wildcard requires at least three leading characters and must not appear inside a phrase. If `criticality` returns too many hits in PsycINFO due to the philosophy literature, narrow to `"neural criticality" OR "critical brain"`.

---

## §4. IEEE Xplore

Run via Advanced Search → Command Search. IEEE's `("All Metadata":term)` searches title, abstract, indexing terms, and full-text excerpts.

```
("All Metadata":(consciousness OR "state of consciousness" OR "levels of consciousness"
  OR "loss of consciousness" OR unconscious* OR wakefulness OR arousal
  OR anesthesi* OR anaesthesi* OR sedation OR propofol OR sevoflurane
  OR ketamine OR xenon OR sleep OR NREM OR REM OR "slow wave sleep"
  OR "vegetative state" OR "unresponsive wakefulness syndrome" OR UWS
  OR "minimally conscious state" OR MCS OR coma OR "locked-in syndrome"
  OR LIS OR psychedelic* OR psilocybin OR LSD OR DMT OR ayahuasca
  OR meditation OR mindfulness OR dream* OR lucid))
AND
("All Metadata":("Lempel-Ziv" OR LZc OR LZ76 OR LZW OR compressibility
  OR "perturbational complexity" OR PCI OR "PCI-state"
  OR "integrated information" OR IIT OR phi
  OR "causal density" OR "causal emergence" OR "phi-ID"
  OR "information decomposition"
  OR entropy OR "sample entropy" OR "approximate entropy"
  OR "permutation entropy" OR "multiscale entropy" OR "spectral entropy"
  OR "transfer entropy" OR "mutual information" OR "Granger causality"
  OR "neural complexity" OR "matching complexity"
  OR "neural avalanche*" OR criticality OR "branching parameter"
  OR "long-range temporal correlation*" OR "detrended fluctuation analysis" OR DFA
  OR "fractal dimension" OR "correlation dimension" OR "Hurst exponent"
  OR Lyapunov OR chaos
  OR "intrinsic dimensionality" OR "participation ratio" OR manifold
  OR "small-world" OR modularity OR "rich-club" OR "hierarchical complexity"
  OR "signal complexity" OR "signal diversity" OR "EEG complexity"
  OR "complexity measure*" OR "complexity marker*"))
AND
("All Metadata":(EEG OR electroencephalograph* OR MEG OR magnetoencephalograph*
  OR iEEG OR ECoG OR intracranial OR "local field potential*" OR LFP
  OR fMRI OR BOLD OR "functional magnetic resonance"
  OR "single-unit" OR "multi-unit" OR "two-photon" OR "calcium imaging"
  OR "wide-field" OR neuroimag* OR "brain activity" OR "neural recording*"
  OR TMS OR "TMS-EEG" OR "TMS-evoked" OR "TMS evoked"
  OR "transcranial magnetic stimulation"))
```

**Filters.** Year range 1990–present; content type "Conferences" + "Journals" + "Magazines" + "Early Access Articles". Keep all four — the engineering literature uses conference papers heavily and excluding them at search time loses real signal.

**Notes.** IEEE's `*` wildcard must not be the first character of a term. Expect IEEE to return a much smaller corpus than PubMed/Scopus/WoS — most consciousness-complexity literature is not engineering-indexed. Treat IEEE as a *coverage check* rather than a primary corpus.

---

## §5. Embase (Embase.com / Elsevier interface)

Run via Embase Advanced Search. Field code `:ti,ab,kw` searches title, abstract, and Emtree author keywords.

```
((consciousness OR 'state of consciousness' OR 'levels of consciousness'
  OR 'loss of consciousness' OR unconscious* OR wakefulness OR arousal
  OR anesthesi* OR anaesthesi* OR sedation OR propofol OR sevoflurane
  OR ketamine OR xenon OR sleep OR NREM OR REM OR 'slow wave sleep'
  OR 'vegetative state' OR 'unresponsive wakefulness syndrome' OR UWS
  OR 'minimally conscious state' OR MCS OR coma OR 'locked-in syndrome'
  OR LIS OR psychedelic* OR psilocybin OR LSD OR DMT OR ayahuasca
  OR meditation OR mindfulness OR dream* OR lucid):ti,ab,kw)
AND
(('Lempel-Ziv' OR LZc OR LZ76 OR LZW OR compressibility
  OR 'perturbational complexity' OR PCI OR 'PCI-state'
  OR 'integrated information' OR IIT OR phi
  OR 'causal density' OR 'causal emergence' OR 'phi-ID'
  OR 'information decomposition'
  OR entropy OR 'sample entropy' OR 'approximate entropy'
  OR 'permutation entropy' OR 'multiscale entropy' OR 'spectral entropy'
  OR 'transfer entropy' OR 'mutual information' OR 'Granger causality'
  OR 'neural complexity' OR 'matching complexity'
  OR 'neural avalanche*' OR criticality OR 'branching parameter'
  OR 'long-range temporal correlation*' OR 'detrended fluctuation analysis' OR DFA
  OR 'fractal dimension' OR 'correlation dimension' OR 'Hurst exponent'
  OR Lyapunov OR chaos
  OR 'intrinsic dimensionality' OR 'participation ratio' OR manifold
  OR 'small-world' OR modularity OR 'rich-club' OR 'hierarchical complexity'
  OR 'signal complexity' OR 'signal diversity' OR 'EEG complexity'
  OR 'complexity measure*' OR 'complexity marker*'):ti,ab,kw)
AND
((EEG OR electroencephalograph* OR MEG OR magnetoencephalograph*
  OR iEEG OR ECoG OR intracranial OR 'local field potential*' OR LFP
  OR fMRI OR BOLD OR 'functional magnetic resonance'
  OR 'single-unit' OR 'multi-unit' OR 'two-photon' OR 'calcium imaging'
  OR 'wide-field' OR neuroimag* OR 'brain activity' OR 'neural recording*'
  OR TMS OR 'TMS-EEG' OR 'TMS-evoked' OR 'TMS evoked'
  OR 'transcranial magnetic stimulation'):ti,ab,kw)
AND [english]/lim
AND [1990-2026]/py
```

**Notes.** Embase uses single quotes for phrases; double quotes mean exact-text match (no Emtree expansion) and should be avoided here. The `[1990-2026]/py` filter must be updated to the actual search year on each rerun. Embase will overlap heavily with PubMed/MEDLINE — that overlap is captured in the PRISMA flow's deduplication step (§B7), not at search time.

---

## Per-database expectations & re-run protocol

The PubMed corpus (4,580) will overlap substantially with Scopus, WoS, and Embase. After deduplication (Bramer method in Zotero + Rayyan), the unique-record total typically lands at ~1.3–1.7× the largest single database. PsycINFO and IEEE Xplore are coverage checks rather than primary contributors.

**On the day of the locked search**, run all six queries within a 24-hour window so the date stamps are commensurable. Archive the raw query strings, the date/time, and the per-database hit counts in a single text file (`search_log_YYYY-MM-DD.txt`) and store it in the OSF project alongside this document. That file is part of the audit trail PRISMA-ScR expects.

**If any single database returns dramatically more or fewer records than expected** (e.g., Scopus > 30 000, IEEE > 5 000, or any database returning 0), do not export — instead, diagnose first by running each block individually in that database to identify which block is misbehaving in that platform's syntax. Common causes: hyphen handling in WoS, wildcard position rules in EBSCO and IEEE, and quote-vs-no-quote phrase semantics in Embase.

---

*End of document.*
