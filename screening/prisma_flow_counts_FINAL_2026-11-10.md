# PRISMA-ScR flow counts - FINAL (2026-11-10)

Supersedes `prisma_flow_counts_DRAFT_2026-10-07.md`. Diagram: `prisma_flow_diagram_2026-11-10.png` / `.svg`. Counts final after both retests (run log §7l-§7q). Source files: `full_text_screening_decisions_2026-10-05.csv` (1,313 rows; verified against the Rayyan export `rayyan_full_text_screening_all_decisions_2026-11-10_articles.csv` and `_customizations_log.csv`, 0 mismatches) and `final_included_set_with_additions_2026-11-10.csv` (536 rows).

## Identification
| Step | Records |
|---|---:|
| PubMed | 4,912 |
| Scopus | 4,212 |
| Web of Science | 3,750 |
| IEEE Xplore | 1,209 |
| APA PsycINFO | 783 |
| **Total identified (2026-06-10)** | **14,866** |
| Duplicates removed (Rayyan, 2026-06-15 to 06-16) | 6,285 |
| **Records screened (title/abstract)** | **8,581** |

## Screening and eligibility
| Step | Records |
|---|---:|
| Excluded at title/abstract | 7,268 |
| Sought and assessed at full text (full text available for all) | 1,313 |
| Excluded at full text | 784 |
| **Included from the search** | **529** |
| Added outside the search | 7 |
| **Studies in the review** | **536** |

## Full-text exclusion reasons (one primary reason per record)
| Reason (code) | n |
|---|---:|
| Tool/monitor/classifier/clinical-application aim, not a consciousness investigation (T) | 407 |
| Not a mechanistic consciousness investigation, no operational consciousness measure (O) | 262 |
| Non-approved or no complexity metric (C) | 72 |
| Review, thesis, book, retracted or other non-primary publication (R) | 34 |
| Non-approved neural data modality (M) | 6 |
| Not in English (L) | 2 |
| Duplicate (D) | 1 |
| **Total** | **784** |

## Additions outside the search (n = 7; `post_screening_additions_2026-10-07.csv`)
- Foundational-paper exception (2): Carhart-Harris 2014; Luppi 2022.
- Methodology-only seeds, §B9b (3): Tononi-Sporns-Edelman 1994; Oizumi 2014; Chis-Ciure 2024.
- Proposed by a collaborator, treated as foundational (2): Mediano 2023 (eLife reviewed preprint); Muñoz 2020 (Phys. Rev. Research), which replaced Starkey 2023.

## Reliability checks
| Check | n | Raw agreement | κ |
|---|---:|---:|---:|
| Title/abstract blind re-screen (§7l) | 86 | 96.5% | 0.836 (1.00 with Maybe = Include) |
| Full-text blind re-screen (§7m) | 131 | 96.2% | 0.922 |
| Elicit vs human, production (8,574 IDs; 6,801 paired) | 6,801 | 75.1% | 0.401 (recall 96.0%, PABAK 0.501) |

## Notes
- Full-text changes after the retest: 530/783 became 529/784 (run log §7n, §7o).
- Three records in the included set have no DOI.
- Mediano 2023 is cited by its reviewed-preprint DOI; check for a Version of Record before submission.
