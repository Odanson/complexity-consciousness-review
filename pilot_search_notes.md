# Pilot search — pre-flight notes

A live PubMed run from this session is blocked at the network proxy. The pilot script `pilot_pubmed_search.py` will execute the protocol's §B6 search end-to-end on your machine in well under a minute and write three artefacts (`pilot_report.md`, `pilot_sample.csv`, `pilot_pmid_list.txt`).

Before running it, three observations are worth recording — they do not need PubMed to verify, and they will materially change the hit count.

## Predictable noise sources in Block 2 (current v0.2 protocol)

**1. Bare `"phi"` is a disaster.** PubMed will match this token in dozens of unrelated contexts: φ-coefficient (statistics), phi-29 polymerase, Bacteriophage φX174, phi-related angles in protein crystallography, CD279 (PD-1 has the symbol PHI in some annotations), and so on. Replace with explicit phrases only:
- `"integrated information"` — already in.
- `"phi value"`, `"phi metric"`, `"phi*"`, `"empirical phi"`, `"geometric phi"`, `"whole-minus-sum phi"` — add as quoted phrases.
- Drop the bare `"phi"` token.

**2. `"manifold"` and `"chaos"` will pull massive volumes of off-topic physics and pure-maths.** Tighten to neural-context phrasings:
- Replace `"manifold"` with `"neural manifold"` OR `"low-dimensional manifold"` OR `"manifold learning"`.
- Replace `"chaos"` with `"deterministic chaos"` OR `"chaotic dynamics"` OR `"edge of chaos"`.

**3. `"modularity"`, `"small-world"`, `"rich-club"`, `"hierarchical complexity"` are graph-theory terms used widely outside neuroscience.** They survive Block 3 (which forces a neural-data context), but inside the AND they will still inflate hit counts via review papers about graph theory in general that happen to mention EEG once. Treat them as on-watch and decide after the pilot whether to require `[tiab]` field tags.

## Refined Block 2 (v2 — proposed)

```
("Lempel-Ziv" OR LZc OR LZ76 OR LZW OR compressibility OR
 "perturbational complexity" OR PCI OR "PCI-state" OR
 "integrated information" OR IIT OR
 "phi value" OR "phi metric" OR "phi*" OR "empirical phi" OR
 "geometric phi" OR "whole-minus-sum phi" OR
 "causal density" OR "causal emergence" OR "phi-ID" OR
 "information decomposition" OR
 entropy OR "sample entropy" OR "approximate entropy" OR
 "permutation entropy" OR "multiscale entropy" OR "spectral entropy" OR
 "transfer entropy" OR "mutual information" OR "Granger causality" OR
 "neural complexity" OR "matching complexity" OR
 "neural avalanche*" OR "criticality" OR "branching parameter" OR
 "long-range temporal correlation*" OR "detrended fluctuation analysis" OR DFA OR
 "fractal dimension" OR "correlation dimension" OR "Hurst exponent" OR
 "Lyapunov exponent" OR "deterministic chaos" OR "chaotic dynamics" OR "edge of chaos" OR
 "intrinsic dimensionality" OR "participation ratio" OR
 "neural manifold" OR "low-dimensional manifold" OR "manifold learning" OR
 "small-world network" OR "modularity" OR "rich-club" OR "hierarchical complexity")
```

This should cut the noise floor by an order of magnitude without dropping any genuine hit.

## Recommended run sequence

1. Run `pilot_pubmed_search.py` once with the **current Block 2** (already in the script).
2. Skim `pilot_sample.csv` for the noise types listed above.
3. If the count is > 15 000 or noise dominates the sample, swap in the **refined Block 2** above and re-run.
4. Diff the two PMID lists (`comm -3 list_v1.sorted list_v2.sorted`) to confirm v2 only drops papers we agree are off-topic.

## Field tags worth piloting if the count is still too large

PubMed's default search expands many terms into MeSH and full-text. Force explicit title/abstract matching by appending `[tiab]` to weakening terms. For example, a v3 with `entropy[tiab]` rather than bare `entropy` will be more precise but may miss MeSH-only matches. Use this only if v2 still over-collects.

## What I cannot verify from this environment

- Whether the eight seed PMIDs in the script are correct. The script will tell you on first run; any seed marked **NO** is a script-correction issue, not a search-strategy issue.
- Whether the title `Toker et al. 2022 PNAS — chaos and consciousness` resolves to PMID `35914187`. Treat this one as provisional until the script confirms.

## Time and cost

Whole pilot, including v1 and v2 runs and sample inspection, is about 30 minutes of human time. No cost. No NCBI API key required, but a free key (registration takes 2 minutes) raises the rate limit from 3 to 10 requests per second.
