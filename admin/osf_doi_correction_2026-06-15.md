# OSF Registration DOI Correction — Audit Note

**Date:** 2026-06-15

**Corrected OSF registration DOI from:** `10.17605/OSF.IO/FUX2J`
**To:** `10.17605/OSF.IO/FU82J`

This was a **documentation-only correction**. The OSF registration record itself is unchanged; the corrected DOI above is the canonical identifier as issued by OSF Registries. The incorrect string `FUX2J` was a transcription error introduced in some project documents when the registration record was first recorded.

The correction does **not** affect the protocol, the registration record on OSF, or the multi-database search execution.

## Files modified

| File | Occurrences of `FUX2J` replaced | Occurrences of `fux2j` URL form replaced |
|---|---:|---:|
| `README.md` | 4 | 4 |
| `protocol/prisma_protocol_v0.5.1.md` | 9 | 8 |
| `protocol/prisma_checklist_mapping.md` | 2 | 2 |
| `search/search execution/search_execution_report.md` | 3 | 2 |
| `search/search execution copy/search_execution_report.md` | 3 | 2 |

All occurrences were replaced repository-wide; a full-tree grep for the incorrect identifier returns zero results post-correction.

## Replacements applied

| Old | New |
|---|---|
| `10.17605/OSF.IO/FUX2J` | `10.17605/OSF.IO/FU82J` |
| `FUX2J` (bare identifier) | `FU82J` |
| `https://osf.io/fux2j` | `https://osf.io/fu82j/` |

## Not affected

- **Protocol methodology, eligibility criteria, search strategy, screening procedures, extraction fields, taxonomy, version history, amendments log.** No substantive content was changed; only the OSF identifier string and URL.
- **Zenodo archive.** All three Zenodo DOIs (`10.5281/zenodo.20140262` v0.4.1 historical; `10.5281/zenodo.20140263` concept; `10.5281/zenodo.20609130` v0.5.1 specific-release) preserved unchanged at every occurrence.
- **OSF registration record itself.** The registration on OSF Registries was issued with DOI `10.17605/OSF.IO/FU82J` and has always been correct on OSF's side; only the in-repository transcription was wrong.
- **GitHub release information.** Unchanged.
- **Search execution outputs.** The 2026-06-10 multi-database search and its 14,866-record raw retrieval are unaffected.
