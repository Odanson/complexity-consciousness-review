> **SUPERSEDED 2026-11-10 by `prisma_flow_counts_FINAL_2026-11-10.md`.** Kept for the record; do not use.

# PRISMA-ScR flow counts - DRAFT (2026-10-07)

**Status: PROVISIONAL.** Both retests are done (run log §7l, §7m); the final full-text counts are 529 Include / 784 Exclude after retest adjudication (run log §7n, §7o); only the additions remain to be added. Do not use in the manuscript until the final version replaces this file.

## Identification
| Step | Records | Source |
|---|---:|---|
| PubMed | 4,912 | `search/corpus_construction/log.md` |
| Scopus | 4,212 | same |
| Web of Science | 3,750 | same |
| APA PsycINFO | 783 | same |
| IEEE Xplore | 1,209 | `search/search_execution/IEEE/search_log.md` (verified 2026-11-10; matches 14,866 minus the other four) |
| **Total identified (2026-06-10)** | **14,866** | |
| Duplicates removed (Rayyan, 2026-06-15 to 06-16) | 6,285 | |
| **Records screened (title/abstract)** | **8,581** | |

## Title/abstract screening
| Step | Records |
|---|---:|
| Screened (single human reviewer in Rayyan; Elicit AI second screen, see calibration_results.md for coverage) | 8,581 |
| Human Include after adjudication of 39 disagreements (14 upheld, 25 flipped to Exclude) | 1,196 |
| Human Maybe | 117 |
| Excluded at title/abstract | 7,268 (8,581 - 1,313) |
| **Sought for full-text retrieval / assessed** | **1,313** |
| Full text not retrieved | 0 (all 1,313 available) |

Note: three of the 1,313 are resolved as Exclude for duplication/scope (570549920, 570552482, 570554409, see run log §7g); they are counted within the 783 below.

## Full-text assessment (1,313)
| Outcome | Records |
|---|---:|
| **Included** | **529** |
| **Excluded** | **784** |

Reasons for exclusion (one primary reason per record):

| Reason (short code) | n |
|---|---:|
| Tool/monitor/classifier/clinical-application aim, not a consciousness investigation (T) | 407 |
| Not a mechanistic consciousness investigation, no operational consciousness measure (O) | 262 |
| Non-approved or no complexity metric (C) | 72 |
| Review, thesis, book, retracted or other non-primary publication (R) | 34 |
| Non-approved neural data modality (M) | 6 |
| Not in English (L) | 2 |
| Duplicate (D) | 1 |
| **Total** | **784** |

Updated 2026-11-10 after the full-text retest (run log §7m, §7n): 5 decisions changed (originally 530 / 783). The retest reached κ = 0.922.

## Additions outside the search (reported separately, not yet in the 529)
Source: `post_screening_additions_2026-10-07.csv`. All seven were added on 2026-11-10 to `final_included_set_with_additions_2026-11-10.csv` (529 + 7 = **536**), outside Rayyan, by DOI.
- Foundational-paper exception (agreed by supervisors): Carhart-Harris 2014; Luppi 2022 (2).
- Methodology-only seeds, §B9b: Tononi-Sporns-Edelman 1994; Oizumi 2014; Chis-Ciure 2024 (3), pending.
- Proposed by Adam, added as foundational papers (decided 2026-10-07): Mediano et al. 2023 (eLife); Muñoz et al. 2020 (Phys. Rev. Research), which replaced the originally proposed Starkey et al. 2023 preprint on 2026-11-10 (2).
- Planned total if all agreed: 529 + 7 = 536 (to be finalised after retests).

## Open before finalising
1. Retest results (could move records between Included and Excluded).
2. (Done 2026-11-10) IEEE Xplore count verified against its search log.
3. Confirm the final additions count.  (570554060 stays excluded, decided 2026-10-07.)
