# IEEE Xplore — Search Execution Log

**Database:** IEEE Xplore
**Date searched:** 2026-06-10
**Query source:** Protocol v0.5.1 (`database_queries.md`)
**Search interface:** IEEE Xplore Advanced Search (Command Search)

## Search field

- All Metadata

## Limits applied

- Publication year: 1990–2026

## Records retrieved

**Total:** 1,209

## Query adaptation

IEEE Xplore imposes a maximum limit of **10 wildcard expressions (`*`) within a single query**. The registered protocol query exceeded this limit because several terms used wildcard expansion (e.g., `unconscious*`, `psychedelic*`, `dream*`, `neuroimag*`, `neural recording*`, `long-range temporal correlation*`, `temporal receptive window*`, `complexity measure*`, `complexity marker*`, `neural avalanche*`, and others).

To comply with IEEE Xplore's query parser while preserving conceptual coverage, wildcard expressions were replaced with explicit lexical variants where necessary. Examples:

| Wildcard form | Explicit replacement |
|---|---|
| `unconscious*` | `unconscious OR unconsciousness` |
| `psychedelic*` | `psychedelic OR psychedelics` |
| `dream*` | `dream OR dreams OR dreaming` |
| `neural avalanche*` | `"neural avalanche" OR "neural avalanches"` |
| `long-range temporal correlation*` | `"long-range temporal correlation" OR "long-range temporal correlations"` |
| `temporal receptive window*` | `"temporal receptive window" OR "temporal receptive windows"` |
| `complexity measure*` | `"complexity measure" OR "complexity measures"` |
| `complexity marker*` | `"complexity marker" OR "complexity markers"` |
| `neural recording*` | `"neural recording" OR "neural recordings"` |
| `neuroimag*` | `neuroimaging OR neuroimage OR neuroimages` |

**Database-specific term expansions retained (the four productive wildcards kept):**

- `anesthesi*` (covers anesthesia / anesthetic / anesthetics / anesthetized / anesthesiology / anesthesiologist)
- `anaesthesi*` (British spelling, same range)
- `electroencephalograph*` (covers electroencephalography / electroencephalographic / electroencephalographically)
- `magnetoencephalograph*` (same range)

These changes were made solely to satisfy IEEE Xplore query constraints and maintain semantic equivalence with the registered search strategy. They are implementation-level adaptations of the registered Boolean query for a database-platform technical limit, not a methodological narrowing of review scope.

## Export

### Primary export format

- **CSV**

### Export issue

- RIS export functionality was unavailable through the institutional IEEE Xplore interface.
- Attempted RIS exports opened a blank browser tab and did not generate a downloadable file.

### Export workaround

Because IEEE Xplore limits CSV exports to **1,000 records per operation**, records were exported separately by document type:

| Document type | Records exported |
|---|---:|
| Conferences | 931 |
| Journals | 256 |
| Early Access Articles | 12 |
| Magazines | 6 |
| Books | 4 |
| **Total** | **1,209** |

### Metadata fields exported in CSV

- Title
- Authors
- Affiliations
- Abstract
- DOI
- Keywords
- IEEE indexing terms
- MeSH terms
- Publication information
- Citation counts
- Funding information

## Archived files

- Search results screenshots — `IEEE_advanced_search_results_ 2026-06-10.png`, `IEEE_command_search_results_ 2026-06-10.png`
- IEEE journal export CSV — `IEEE_journal_results_2026-06-10.csv`
- IEEE consolidated other-types CSV — `IEEE_others_results_2026-06-10.csv` (conferences + early-access + magazines + books, combined to 953 records)

## Notes

- Search executed successfully after query adaptation.
- The database-specific modifications were implementation changes only and did not alter the conceptual eligibility framework defined in the protocol.
- IEEE retrievals will be merged with the other four database exports during deduplication.
