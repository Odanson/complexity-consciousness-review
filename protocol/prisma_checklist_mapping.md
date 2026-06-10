# PRISMA-ScR + PRISMA-S checklist mapping

**Companion to:** `prisma_protocol.md` (Version 0.5.1, 2026-06-04)
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
| 7 | Methods | Information sources | §B5 (five databases with per-database rationale; preprints; hand-search; Citationchaser; expert elicitation; Decision 9 documents Embase access constraint) |
| 8 | Methods | Search | §B6 (locked Block 1 / Block 2 / Block 3 PubMed string + companion `database_queries.md` with four translations) |
| 9 | Methods | Selection of sources of evidence | §B7 (single human reviewer + Elicit AI second-screening + ASReview active-learning prioritisation; within-person test-retest; pre-registered Elicit calibration documented in `calibration_results.md`; Yaron 2022 *Nat Hum Behav* precedent for the single-human-reviewer baseline) |
| 10 | Methods | Data charting process | §B7 data extraction paragraph + §B8 extraction-fields list; piloted structured extraction form on 10 studies, then revised before bulk extraction; 10 % intra-rater re-extraction after ≥ 1-month delay |
| 11 | Methods | Data items | §B8 extraction fields (12 categories) |
| 12 | Methods | Critical appraisal of individual sources of evidence (*optional*) | §B10 (we elect to apply a measurement-methodology checklist; six items rated low / some concern / high; piloted on the same 10-study set used for §B8 extraction-form pilot) |
| 13 | Methods | Synthesis of results | §B11 narrative-synthesis plan + §B12 taxonomy (eight axes) |
| 14 | Results | Selection of sources of evidence | Pending — populated post-multi-database run (PRISMA flow diagram from Elicit + ASReview exports, §B7) |
| 15 | Results | Characteristics of sources of evidence | Pending — extraction output |
| 16 | Results | Critical appraisal within sources of evidence | Pending — §B10 checklist outputs |
| 17 | Results | Results of individual sources of evidence | Pending — per-paper extraction outputs |
| 18 | Results | Synthesis of results | Pending — §B11 tables + heatmap + misapplication register |
| 19 | Discussion | Summary of evidence | Pending — manuscript draft |
| 20 | Discussion | Limitations | Pending; will include the documented Sitt 2014 database miss (§B6.2), the single-human-reviewer with AI-assisted second-screening model (§B7), and scope decisions in §A3 |
| 21 | Discussion | Conclusions | Pending — manuscript draft |
| 22 | Funding | Funding | §B14 (Max Planck School of Cognition; lead reviewer's PhD-track funding line) |

Items 14–21 are Results / Discussion items and are not part of the protocol *per se* — they are populated during execution. PRISMA-ScR expects them to be addressed in the manuscript, not in the protocol. Their slots are reserved here for traceability.

---

## PRISMA-S (16 items — search reporting)

| # | Block | Item | Where addressed in protocol |
|---:|---|---|---|
| 1 | Information sources & methods | Database name | §B5 + `database_queries.md` (PubMed/MEDLINE, Scopus, Web of Science Core Collection, PsycINFO, IEEE Xplore); Decision 9 documents Embase access constraint |
| 2 | Information sources & methods | Multi-database searching | §B5 (five databases; rationale per database); §B6.3 audit-trail policy (24-hour multi-database window) |
| 3 | Information sources & methods | Study registries | Not applicable for this scoping review (we do not search trial registries; no clinical trials are in scope). Documented as N/A. |
| 4 | Information sources & methods | Online resources and browsing | §B5 hand-search list (12 journals); preprint sources (bioRxiv, medRxiv, arXiv, PsyArXiv) |
| 5 | Information sources & methods | Citation searching | §B5 (Citationchaser, named per PRISMA-S requirement) + §B9 seed set |
| 6 | Information sources & methods | Contacts | §B5 expert elicitation (Jürgen Jost, Lucia Melloni, Andrej Biçanski; planned external collaborators Anil Seth and Adam Barrett); each suggestion logged with capture-vs-miss status |
| 7 | Information sources & methods | Other methods | None used beyond items 1–6 |
| 8 | Information sources & methods | Inclusion and exclusion criteria | §B4 (replicated here for cross-reference to the search) |
| 9 | Search strategies | Full search strategies | §B6 (PubMed canonical, in full); `database_queries.md` (five database translations, in full) |
| 10 | Search strategies | Limits and restrictions | §B6 (English; 1990-01-01 to search date); §B4 inclusion criterion 5 |
| 11 | Search strategies | Search filters | None applied (we do not use validated filters such as Cochrane Highly Sensitive Search Strategy) |
| 12 | Search strategies | Prior work | §B6.1 pilot results table (v0.3 → 4,580; v0.4.1 → 5,267) and §B6.2 seed-paper validation |
| 13 | Peer review | Search peer review | Internal peer review by Lucia Melloni and Andrej Biçanski (docx markup 2026-05-10 + email 2026-05-10) and by Jürgen Jost (2026-05-29 reply); changes recorded in amendments log v0.4 / v0.4.1 / v0.5 |
| 14 | Managing records | Total records identified | §B6.1 (PubMed = 5,267 as of 2026-05-12; multi-database total pending) |
| 15 | Managing records | Deduplication | §B7 (Bramer method in Zotero + Rayyan deduplicator + manual spot-check) |
| 16 | Reporting | Date of search | §B6.1 (pilot dates); locked-search date to be recorded as `search_log_YYYY-MM-DD.txt` per §B6.3 |

---

## Compliance summary

**PRISMA-ScR:** 13 of 22 items addressed in the protocol (the remaining 8 are Results / Discussion items that populate during execution). Of the protocol items, all are addressed.

**PRISMA-S:** 14 of 16 items addressed in the protocol. Item 3 (study registries) is N/A and documented; item 11 (search filters) is N/A.

**OSF Registries registration completed:** DOI [10.17605/OSF.IO/FUX2J](https://doi.org/10.17605/OSF.IO/FUX2J); registration record at [https://osf.io/fux2j](https://osf.io/fux2j).

**Items still pending:** final multi-database record totals (populated after the locked multi-database run).

The Zenodo concept DOI (10.5281/zenodo.20140263) and v0.5.1 specific-release DOI (10.5281/zenodo.20609130) are recorded in §B6.3 and will be updated only if a new GitHub/Zenodo release is created for v0.5.1.

---

*End of mapping document.*
