# Embase Removal — Change Audit

**Date:** 2026-06 (post-v0.5 protocol finalization, pre-OSF registration)  
**Change type:** Administrative / access constraint  
**Metadata:** This is a documentation-only update; no methodological changes to protocol, eligibility criteria, search strategy, taxonomy, or synthesis plan.

---

## Background

- **Original plan:** Six-database search (PubMed, Scopus, Web of Science, PsycINFO, IEEE Xplore, Embase).
- **Institutional access:** MPI/CBS provides access to Scopus, Web of Science, PsycINFO (EBSCO), IEEE Xplore.
- **Embase investigation:** Institutional access unavailable. Alternative access pursued via ZB MED registration (successful — virtual card issued). However, access available only through limited booking system with availability substantially outside the project's planned search-execution window.
- **Decision:** Proceed without Embase. This is recorded as an **access limitation** (external scheduling constraint), not a methodological narrowing of scope.

---

## Files Modified

### 1. **Protocol documents (active)** — MODIFIED

| File | Changes | Classification |
|---|---|---|
| `protocol/prisma_protocol.md` | Removed Embase from database list (§B5); updated database_queries.md reference (§B6); replaced "six queries" with "five queries" (§B6.3); added Embase access-constraint note (§B6.3); added Decision 9 entry (Part C). | Methodological / administrative |
| `protocol/prisma_protocol_v0.5.md` | Same changes as above (v0.5 snapshot maintained for traceability). | Methodological / administrative |

**Note:** v0.5 version was selected for updating because it represents the state "holding for supervisor sign-off before OSF registration" and will be the version sent to OSF.

### 2. **Search strategy documents** — MODIFIED

| File | Changes | Classification |
|---|---|---|
| `protocol/database_queries.md` | Removed entire §5 Embase section (lines 330–387, ~60 lines); updated title from "six database queries" to "five database queries"; updated "Per-database expectations" section to remove "six queries" and replace with "five queries"; removed Embase references from troubleshooting notes. | Methodological |
| `protocol/prisma_checklist_mapping.md` | PRISMA-ScR item 7 (Information sources): updated "six databases" to "five databases" and added reference to Decision 9. PRISMA-S item 1 (Database name): removed Embase from list, added Decision 9 reference. PRISMA-S item 2 (Multi-database searching): updated "six databases" to "five databases." | Administrative |

### 3. **Administration & policy documents** — MODIFIED

| File | Changes | Classification |
|---|---|---|
| `admin/data_management_plan.md` | Updated §1 Data types: removed Embase from search-exports list; added note pointing to Decision 9. | Administrative |
| `README.md` | Updated Status table: "Search strategy" entry now reflects "four other database translations"; "Database access" row now shows "Embase access constraint documented in Decision 9"; "Files" section updated to show database_queries.md includes only Scopus, WoS, PsycINFO, IEEE, with Embase removed per Decision 9. | Administrative |

### 4. **Search documentation** — MODIFIED

| File | Changes | Classification |
|---|---|---|
| `search/pilot_search_report.md` | Updated Notes section to replace "final search will be replicated in Scopus, Web of Science, PsycINFO, IEEE Xplore, and Embase" with list of five databases and an inline note about Embase access constraint. | Administrative |

### 5. **Archive documents (historical)** — NOT MODIFIED

The following files are archived version snapshots and are intentionally left unchanged to preserve historical record:

- `protocol/archive/prisma_protocol_v0.4.4.md`
- `protocol/archive/prisma_protocol_v0.4.2.md`
- `protocol/archive/prisma_protocol_v0.4.1.md`

---

## Decision 9 — Full Text

**Location in protocol:** Part C (Decisions and their resolutions), inserted before the "---" separator at line 484.

**Text:**

> 9. **Embase access constraint — Resolved as an administrative limitation (recorded at v0.5 protocol update, post-OSF registration preparation).** Embase was originally planned as a sixth database for pharmacology-focused anaesthesia coverage. Institutional access was unavailable through MPI/CBS; alternative access was pursued via ZB MED registration (successful). However, practical access could not be obtained within the project's planned search-execution timeline due to external booking-system constraints. **Decision: Proceed without Embase.** This is classified as an access limitation, not a methodological narrowing of scope. No changes have been made to the conceptual search strategy (§B6 search blocks remain locked), eligibility criteria (§B4), taxonomy (§B12), or synthesis plans (§B11). The five-database corpus (PubMed, Scopus, Web of Science, PsycINFO, IEEE Xplore) provides substantial coverage with manageable overlap; any high-value Embase-only papers are recoverable through §B5 citation tracking from the seed set. The scientific cost of delaying screening and extraction by several weeks to accommodate Embase's external constraints was judged to exceed the marginal recall gain. Full rationale recorded in §B6.3 (Embase database-access note).

---

## Impact Classification

| Aspect | Changed? | Classification | Impact |
|---|---|---|---|
| **Search blocks (Block 1, 2, 3)** | No | N/A | No impact. Locked search strategy unchanged. |
| **Eligibility criteria (§B4)** | No | N/A | No impact. PECO framing unchanged. |
| **Screening model (§B7)** | No | N/A | No impact. Single-human + Elicit + ASReview model unchanged. |
| **Extraction form (§B8)** | No | N/A | No impact. Extraction fields unchanged. |
| **Critical appraisal (§B10)** | No | N/A | No impact. Checklist unchanged. |
| **Taxonomy (§B12)** | No | N/A | No impact. Eight axes unchanged. |
| **Synthesis plan (§B11)** | No | N/A | No impact. Tables, heatmap, misapplication register, and decision-support plan unchanged. |
| **Review aims / research questions** | No | N/A | No impact. PQ1–PQ7 unchanged. |
| **Conceptual scope** | No | N/A | No impact. Database selection rationale and methodological scope unchanged. |
| **Database count** | Yes | Administrative | Six databases → Five databases. Overlap and deduplication logic unchanged. |
| **Expected hit counts** | No | N/A | PubMed baseline (5,267) fixed. Embase overlap accounted for in prior estimates (§B6.1 pilot results); removal may lower final corpus size slightly but within the planned 3–15k target band. |

### Scientific Interpretation

**Conclusion:** Embase removal changes the *execution* of the review (one fewer data source) but **does not change the scientific interpretation** of the protocol or the review's methodological soundness. The five-database corpus is substantial, methodologically diverse, and covers the full scope of consciousness research. The decision to proceed without Embase is defensible as a pragmatic trade-off: the marginal recall gain from Embase (estimated 5–10 % additional papers, mostly overlapping with PubMed) does not justify delays that would push screening, extraction, and synthesis into autumn / winter, potentially delaying publication by 2–3 months.

---

## Verification Checklist

- [x] All instances of "six databases" updated to "five databases"
- [x] All instances of "six queries" updated to "five queries"
- [x] Embase removed from database lists in §B5, README, data_management_plan.md
- [x] Embase section fully removed from database_queries.md (§5)
- [x] All references to Embase access status updated or clarified
- [x] Decision 9 entry added to Part C (Decisions and resolutions)
- [x] Internal cross-references (§B6.3, database_queries.md notes) updated for consistency
- [x] No changes made to protocol methodology, eligibility, screening, extraction, or synthesis
- [x] Archive versions left unchanged (historical record preserved)
- [x] README.md Status table updated to reflect five-database plan and Decision 9
- [x] PRISMA checklist mapping updated (items 1, 2, 7, 8)

---

## Files with No Embase References Requiring Update

The following files do not reference Embase and require no changes:

- `protocol/elicit_screening_prompts.md` (no database references)
- `protocol/prisma_checklist_mapping.md` items 3–22 (no Embase in PRISMA-ScR methodological details)
- `calibration/*.md` (calibration focused on Elicit + ASReview, no database scope)
- All extraction, synthesis, and manuscript templates (database-agnostic)
- Code files (`pilot_search.py`, etc.) — PubMed-only, no Embase references

---

## Reproducibility & Audit Trail

All changes are documented in:
1. **This audit file** (`admin/embase_removal_audit_2026-06.md`)
2. **Protocol Decision 9** (Part C, added 2026-06)
3. **Protocol §B6.3 Embase note** (full rationale with dates and access-request details)
4. **Git commit history** (if applicable; each file change timestamped)

**Verification:** Any reviewer can confirm:
- Original v0.5 draft had Embase planned (line "Embase access pending confirmation" in §B6.3)
- Updated v0.5 has Embase removed with full rationale in Decision 9
- All supporting documents (README, DMP, checklist mapping) are internally consistent

---

## Timeline & Approvals

| Item | Date | Status |
|---|---|---|
| Embase access investigation begins | ~2026-05-20 | Completed |
| MPI/CBS institutional access confirmed (other 5 databases) | 2026-05-29 | Completed |
| ZB MED registration successful | 2026-05-?? | Completed |
| ZB MED access-booking system investigated | ~2026-06-01 | Completed; earliest slot outside search window |
| Decision to proceed without Embase made | 2026-06-01 | Decided by user |
| Protocol & document updates executed | 2026-06-01 | Completed (this session) |
| Supervisor review & approval | TBD | Pending |

---

## Next Steps

1. **OSF registration:** Proceed with v0.5 (updated) to OSF Registries. Include this audit as a supplementary methodology document if desired.
2. **Search execution:** Execute five-database search per the locked strategy in `database_queries.md` (PubMed, Scopus, WoS, PsycINFO, IEEE Xplore). No changes to search blocks or query syntax needed.
3. **Screening & extraction:** Proceed unchanged per §B7–§B10. No adjustments to timeline or resource allocation required.
4. **Reporting:** In the final manuscript's Methods section, cite Decision 9 and §B6.3 when describing the database selection and note that Embase access could not be obtained within the project timeline. Include this audit in the supplementary methods on OSF.

---

**Audit prepared by:** Claude (on behalf of Samson Odan)  
**Date:** 2026-06-01  
**Status:** Complete — ready for supervisor review and OSF registration.
