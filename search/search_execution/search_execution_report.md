# Multi-Database Search Execution — Summary Report

**Project:** Complexity Measures of Consciousness — PRISMA-ScR Methodological Review
**Search execution date:** 2026-06-10
**Query source:** Protocol v0.5.1 (`database_queries.md`)
**Protocol registration:** OSF Registries — DOI [10.17605/OSF.IO/FU82J](https://doi.org/10.17605/OSF.IO/FU82J); record at [https://osf.io/fu82j/](https://osf.io/fu82j/)

---

## Headline retrieval

| Database | Records retrieved | Per-database log |
|---|---:|---|
| PubMed (NLM) | 4,912 | [`pubmed/search_log.md`](pubmed/search_log.md) |
| Scopus (Elsevier) | 4,212 | [`scopus/search_log.md`](scopus/search_log.md) |
| Web of Science Core Collection (Clarivate) | 3,750 | [`Web_of_Science/search_log.md`](Web_of_Science/search_log.md) |
| APA PsycINFO (via Ovid) | 783 | [`PsycInfo/search_log.md`](PsycInfo/search_log.md) |
| IEEE Xplore | 1,209 | [`IEEE/search_log.md`](IEEE/search_log.md) |
| **Total retrieved before deduplication** | **14,866** | — |

The raw five-database total sits comfortably inside the **3,000–15,000 target band** registered in protocol v0.3 §B6 and carried forward unchanged through v0.5.1. The post-deduplication unique-record count will be recorded after the Phase-2 dedup step.

## Five-database (not six) execution

Embase was originally planned as a sixth database to provide Emtree-based pharmacology coverage. Institutional access was investigated through MPI/CBS library services (unavailable) and alternative routes through ZB MED registration (successful — virtual library card issued). However, practical Embase access depended on a limited booking system with available slots substantially outside the project's planned search-execution timeline. The decision to proceed without Embase is documented in protocol v0.5.1 §C decision 9 (2026-06-04) as an **access limitation** (external scheduling constraint), not a methodological narrowing of review scope. The five-database corpus provides substantial coverage; any high-value Embase-only papers are recoverable through §B5 citation tracking from the seed set.

## Per-database notes (executive level)

- **PubMed (4,912).** Phrase-index warnings raised for `"Kolmogorov signal complexity"`, `"PCI-state"`, `"ST-PCI"`, and `"state transitions complexity index"` — did not prevent execution. Retrieval differs from the v0.4.1 pilot (5,267 on 2026-05-12) consistent with PubMed indexing / ATM drift between pilot and final-execution dates. No modification to the registered search strategy.
- **Scopus (4,212).** Executed without warnings via Advanced Document Search using `TITLE-ABS-KEY`. RIS export complete.
- **Web of Science Core Collection (3,750).** Executed via Topic Search (`TS=`); the registered query was translated to WoS syntax with no substantive change. RIS exported in four chunks (`savedrecs.ris`, `savedrecs(1).ris`, `savedrecs(2).ris`, `savedrecs(3).ris`) per WoS export limits.
- **APA PsycINFO (783).** Final retrieval obtained through the Ovid search-history workflow: each concept block run separately (consciousness 341,828 / complexity 28,180 / neural-recording 213,821) and combined to set 4 (`1 AND 2 AND 3` = 796), then limited to English + 1990–Current (set 5 = 783).
- **IEEE Xplore (1,209).** Query adapted to satisfy IEEE Xplore's **10-wildcard maximum**: explicit lexical expansions replaced 14 of the 18 registered wildcards; the four productive wildcards (`anesthesi*`, `anaesthesi*`, `electroencephalograph*`, `magnetoencephalograph*`) were preserved. Adaptation documented in IEEE log §"Query adaptation" as an **implementation change for a database technical limit**, not a methodological narrowing. CSV exports were partitioned by document type (Conferences 931 / Journals 256 / Early-Access 12 / Magazines 6 / Books 4) because IEEE Xplore caps single-export CSVs at 1,000 records.

## Archived files (per database)

Each database folder contains the database-specific `search_log.md` plus the raw export files and execution screenshots used to validate the run.

```
search/search execution/
├── search_execution_report.md              ← this document
├── pubmed/
│   ├── search_log.md
│   ├── pubmed_2026-06-10_4912.nbib
│   ├── pubmed_results_2026-06-10.png
│   └── pubmed_search_history_2026-06-10.png
├── scopus/
│   ├── search_log.md
│   ├── scopus_2026-06-10_4212.ris
│   └── scopus_results_2026-06-10.png
├── Web_of_Science/
│   ├── search_log.md
│   ├── WoS_results_2026-06-10.png
│   └── savedrecs*.ris (4 RIS files combined to 3,750 records)
├── PsycInfo/
│   ├── search_log.md
│   └── PsychInfo/PsyChInfo_results_2026-06-10.ris (+ .odt)
└── IEEE/
    ├── search_log.md
    ├── IEEE_advanced_search_results_ 2026-06-10.png
    ├── IEEE_command_search_results_ 2026-06-10.png
    ├── IEEE_journal_results_2026-06-10.csv
    └── IEEE_others_results_2026-06-10.csv
```

## Audit trail compliance

This report and the five per-database logs together satisfy **PRISMA-S** reporting items 1, 2, 9, 14, and 16 (database names; multi-database searching; full search strategies; total records identified; date of search). The registered conceptual query, its per-database syntactic translations, and the documented IEEE adaptation are recorded in `database_queries.md`; the protocol's amendments-log entry for v0.5.1 documents the execution-day commit, with the OSF registration DOI ([10.17605/OSF.IO/FU82J](https://doi.org/10.17605/OSF.IO/FU82J)) as the public pre-registration anchor.