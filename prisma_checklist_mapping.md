# PRISMA-ScR + PRISMA-S checklist mapping

**Companion to:** `prisma_protocol.md` v0.4.1 (2026-05-11)
**Purpose.** One-page mapping showing where each PRISMA-ScR (Tricco et al. 2018, *Ann Intern Med*) and PRISMA-S (Rethlefsen et al. 2021, *Syst Rev*) item is addressed in the protocol. To be uploaded to OSF alongside the protocol at registration so reviewers can verify compliance without hunting.

---

## PRISMA-ScR (22 items)

| # | Section | Item | Where addressed in protocol |
|---:|---|---|---|
| 1 | Title | Identify report as scoping review | Title line ("PRISMA Review Protocol") + §A4 (review type locked to PRISMA-ScR) |
| 2 | Abstract | Structured summary | Executive summary (top of document) |
| 3 | Introduction | Rationale | §A1 problem statement |
| 4 | Introduction | Objectives | §A2 review aims (5 aims) + §B2 review questions (PQ1–PQ7) |
| 5 | Methods | Protocol and registration | §A4 (PRISMA-ScR + OSF); §B1 administrative; this protocol = the registerable document |
| 6 | Methods | Eligibility criteria | §B3 PECO + §B4 inclusion / exclusion / grey-zone criteria |
| 7 | Methods | Information sources | §B5 (six databases with per-database rationale; preprints; hand-search; Citationchaser; expert elicitation) |
| 8 | Methods | Search | §B6 (locked Block 1 / Block 2 / Block 3 PubMed string + companion `database_queries.md` with five translations) |
| 9 | Methods | Selection of sources of evidence | §B7 (Rayyan + ASReview workflow; calibrated single-reviewer + active-learning model; Yaron 2022 NHB precedent) |
| 10 | Methods | Data charting process | §B7 data extraction paragraph + §B8 extraction-fields list; pilot on 10 studies, 20 % quality-control re-extraction |
| 11 | Methods | Data items | §B8 extraction fields (12 categories) |
| 12 | Methods | Critical appraisal of individual sources of evidence (*optional*) | §B10 (we elect to apply a measurement-methodology checklist; six items rated low / some concern / high) |
| 13 | Methods | Synthesis of results | §B11 narrative-synthesis plan + §B12 taxonomy (eight axes) |
| 14 | Results | Selection of sources of evidence | Pending — will be populated post-multi-database run (PRISMA flow diagram from Rayyan exports, §B7) |
| 15 | Results | Characteristics of sources of evidence | Pending — extraction output |
| 16 | Results | Critical appraisal within sources of evidence | Pending — §B10 checklist outputs |
| 17 | Results | Results of individual sources of evidence | Pending — per-paper extraction outputs |
| 18 | Results | Synthesis of results | Pending — §B11 tables + heatmap + misapplication register |
| 19 | Discussion | Summary of evidence | Pending — manuscript draft |
| 20 | Discussion | Limitations | Pending; will include the documented Sitt 2014 database miss (§B6.2), single-reviewer screening deviation (§B7), and scope decisions in §A3 |
| 21 | Discussion | Conclusions | Pending — manuscript draft |
| 22 | Funding | Funding | §B14 (Max Planck School of Cognition) |

Items 14–21 are Results / Discussion items and are not part of the protocol *per se* — they are populated during execution. PRISMA-ScR expects them to be addressed in the manuscript, not in the protocol. Their slots are reserved here for traceability.

---

## PRISMA-S (16 items — search reporting)

| # | Block | Item | Where addressed in protocol |
|---:|---|---|---|
| 1 | Information sources & methods | Database name | §B5 + `database_queries.md` (PubMed/MEDLINE, Scopus, Web of Science Core Collection, PsycINFO, IEEE Xplore, Embase) |
| 2 | Information sources & methods | Multi-database searching | §B5 (six databases; rationale per database); §B6.3 audit-trail policy (24-hour multi-database window) |
| 3 | Information sources & methods | Study registries | Not applicable for this scoping review (we do not search trial registries; no clinical trials are in scope). Documented as N/A. |
| 4 | Information sources & methods | Online resources and browsing | §B5 hand-search list (12 journals); preprint sources (bioRxiv, medRxiv, arXiv, PsyArXiv) |
| 5 | Information sources & methods | Citation searching | §B5 (Citationchaser, named per PRISMA-S requirement) + §B9 seed set |
| 6 | Information sources & methods | Contacts | §B5 expert elicitation (Jurgen, Lucia, Andrej, Anil Seth, Adam Barrett); each suggestion logged with capture-vs-miss status |
| 7 | Information sources & methods | Other methods | None used beyond items 1–6 |
| 8 | Information sources & methods | Inclusion and exclusion criteria | §B4 (replicated here for cross-reference to the search) |
| 9 | Search strategies | Full search strategies | §B6 (PubMed canonical, in full); `database_queries.md` (five database translations, in full) |
| 10 | Search strategies | Limits and restrictions | §B6 (English; 1990-01-01 to search date); §B4 inclusion criterion 5 |
| 11 | Search strategies | Search filters | None applied (we do not use validated filters such as Cochrane Highly Sensitive Search Strategy) |
| 12 | Search strategies | Prior work | §B6.1 pilot results table (v0.3 → 4,580; v0.4.1 → 5,267) and §B6.2 seed-paper validation |
| 13 | Peer review | Search peer review | Internal peer review by Lucia Melloni and Andrej Bicanski (docx markup 2026-05-10 + email 2026-05-10); changes recorded in amendments log v0.4 / v0.4.1 |
| 14 | Managing records | Total records identified | §B6.1 (PubMed = 5,267 as of 2026-05-12; multi-database total pending) |
| 15 | Managing records | Deduplication | §B7 (Bramer method in Zotero + Rayyan deduplicator + manual spot-check) |
| 16 | Reporting | Date of search | §B6.1 (pilot dates); locked-search date to be recorded as `search_log_YYYY-MM-DD.txt` per §B6.3 |

---

## Compliance summary

**PRISMA-ScR:** 13 of 22 items addressed in the protocol (the remaining 8 are Results / Discussion items that populate during execution). Of the protocol items, all are addressed.

**PRISMA-S:** 14 of 16 items addressed in the protocol. Item 3 (study registries) is N/A and documented; item 11 (search filters) is N/A.

**Items pending registration-time entries:** authorship ORCIDs (§B1); estimated milestone dates (§B1); Zenodo DOI for the code archive (§B6.3).

---

*End of mapping document.*
