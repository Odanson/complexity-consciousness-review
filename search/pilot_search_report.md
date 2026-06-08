# Pilot PubMed search — report

Run: 2026-05-12T06:32:40+00:00 → 2026-05-12T06:33:25+00:00 UTC

## Hit counts

| Query | Count |
|---|---:|
| Block 1 (consciousness) | 1,551,682 |
| Block 2 (complexity) | 559,496 |
| Block 3 (neural data) | 1,357,089 |
| Block 1 AND Block 2 AND Block 3 | 5,267 |

## Empirical seeds — per-block diagnosis

| Seed paper | PMID | B1 | B2 | B3 | Full query |
|---|---|:-:|:-:|:-:|:-:|
| Casali et al. 2013 Sci Transl Med (PCI) | 23946194 | ✓ | ✓ | ✓ | ✓ |
| Casarotto et al. 2016 Ann Neurol (PCI in DOC) | 27717082 | ✓ | ✓ | ✓ | ✓ |
| Schartner et al. 2015 PLoS ONE (LZc anaesthesia) | 26252378 | ✓ | ✓ | ✓ | ✓ |
| Schartner et al. 2017 Neurosci Conscious (psychedelics) | 28422113 | ✓ | ✓ | ✓ | ✓ |
| Sitt et al. 2014 Brain (DOC EEG markers) | 24919971 | ✓ | ✗ | ✓ | **✗ — investigate** |
| Carhart-Harris et al. 2014 (entropic brain) | 24550805 | ✓ | ✓ | ✓ | ✓ |
| Toker et al. 2022 PNAS (consciousness and chaos) | 36522453 | ✓ | ✓ | ✓ | ✓ |
| Luppi et al. 2022 Nat Neurosci (synergistic core) | 35781077 | ✓ | ✓ | ✓ | ✓ |
| Chis-Ciure, Melloni & Northoff 2024 NBR (Measure Centrality Index) | 38615851 | ✓ | ✓ | ✗ | **✗ — investigate** |

## Methodology-only seeds (included by exception)

| Seed paper | PMID |
|---|---|
| Tononi-Sporns-Edelman 1994 PNAS (neural complexity) | 8197179 |
| Oizumi-Albantakis-Tononi 2014 PLoS Comput Biol (IIT 3.0) | 24811198 |

## Notes

- If Block 1 ∧ Block 2 ∧ Block 3 returns more than 20 000 records,
  tighten Block 1 to explicit state-change contexts (drop bare
  *wakefulness* / *arousal*).
- If any seed is **not captured**, diagnose and revise the
  search before locking the protocol. Common causes: term
  appears only in the body (need to broaden field tags) or a
  block synonym is missing.
- This is a PubMed-only pilot. The final search will be
  replicated in Scopus, Web of Science, PsycINFO, and IEEE Xplore per §B5 of the protocol.
  (Embase was originally planned but could not be accessed within the project timeline; see Decision 9 in the protocol.)
