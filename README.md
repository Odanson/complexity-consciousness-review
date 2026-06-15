[![DOI](https://zenodo.org/badge/1236657777.svg)](https://doi.org/10.5281/zenodo.20609130)

# Complexity Measures of Consciousness — PRISMA-ScR Review

Protocol, search strategy, and pilot code for a methodological scoping review of complexity measures applied to neural data in consciousness research.

The review systematically maps quantitative complexity measures applied to neural recordings in consciousness research, classifies included measures along eight orthogonal axes (mathematical primitive, data requirement, spatial scale, temporal granularity, theory anchoring, inferential status, validation evidence, aspect of consciousness), audits the fit between each included measure's mathematical content and the claims made with it, and identifies conceptual and methodological gaps. Reporting follows **PRISMA-ScR** (Tricco et al. 2018) and **PRISMA-S** (Rethlefsen et al. 2021); methodology follows **JBI** scoping-review guidance (Peters et al. 2020; Pollock et al. 2023).

## Status

| Item | Status |
|---|---|
| Protocol version | **v0.5.1** (2026-06-04) |
| Search strategy | Locked five-database strategy: PubMed, Scopus, Web of Science, PsycINFO, IEEE Xplore |
| Search execution | Manual via each database's authenticated UI (institutional MPI/CBS login); code restricted to downstream QC, parsing, and analysis |
| Multi-database search executed | **2026-06-10 — 14,866 records (raw, pre-dedup):** PubMed 4,912 · Scopus 4,212 · Web of Science 3,750 · PsycINFO 783 · IEEE Xplore 1,209. See [`search/search execution/search_execution_report.md`](search/search%20execution/search_execution_report.md). |
| PubMed pilot hit count | 5,267 records (v0.4.1 pilot, 2026-05-12; historical comparator) |
| Empirical seeds captured (v0.4.1 pilot) | 7 / 8 (Sitt 2014 = documented DB miss, recovered via citation tracking; full seed validation against the executed multi-database corpus to follow Phase 2 dedup) |
| Screening model | Single human reviewer + Elicit AI second screening (calibrated 2026-05-28; κ = 0.843, recall 98.1 %, seeds 8/8) |
| Database access | Confirmed via MPI/CBS login: Scopus, Web of Science, PsycINFO (EBSCO), IEEE Xplore. Embase access constraint documented in Decision 9. |
| OSF workspace | Private workspace created 2026-05-29 (ORCID-linked, EU-Frankfurt storage); populated with stable pre-registration files |
| Code archive | Zenodo, see DOI badge above |
| OSF registration | **Registered (v0.5.1):** [10.17605/OSF.IO/FU82J](https://doi.org/10.17605/OSF.IO/FU82J) · [view record](https://osf.io/fu82j/) |

## Authors

Samson Odan (lead) · Lucia Melloni · Andrej Bicanski · Jurgen Jost.
External collaborators (to be added on contribution): Adam Barrett, Anil Seth.

## Files

- **`prisma_protocol_v0.5.1.md`** — **registered protocol** archived on OSF Registries ([10.17605/OSF.IO/FU82J](https://doi.org/10.17605/OSF.IO/FU82J)) and Zenodo ([10.5281/zenodo.20609130](https://doi.org/10.5281/zenodo.20609130); concept DOI [10.5281/zenodo.20140263](https://doi.org/10.5281/zenodo.20140263)). Contains the locked search strategy, PECO criteria, eight-axis taxonomy, screening model (single human + Elicit AI second-screening + ASReview prioritisation), and amendments log used for the executed review.
- **Legacy protocol snapshots** (`prisma_protocol_v0.4.1.md` through `prisma_protocol_v0.5.md`) — archived historical versions retained for provenance and version history; each transition is recorded in the v0.5.1 amendments log.
- **`database_queries.md`** — locked PubMed query plus equivalent translations for Scopus, Web of Science, PsycINFO, and IEEE Xplore (Embase removed per Decision 9).
- **`prisma_checklist_mapping.md` / `.docx`** — PRISMA-ScR (22-item) and PRISMA-S (16-item) compliance mapping against the protocol.
- **`pilot_search.py`** — pilot-search and seed-validation script (Python, stdlib only; queries PubMed E-utilities).
- **`pilot_search_report.md`** — most recent pilot output (hit counts + seed-paper per-block diagnosis).
- **`search/search execution/`** — executed multi-database search artefacts (2026-06-10): per-database raw exports + screenshots + `search_log.md`, plus a `search_execution_report.md` summary at the folder root.
- **`github_zenodo_setup.md`** — instructions used to set up this repository and the Zenodo archive.

## Reproducing the pilot search

```bash
python3 pilot_search.py
```

No external dependencies — the script uses only the Python standard library and pings NCBI E-utilities. With an NCBI API key set in `NCBI_API_KEY`, the rate limit relaxes from 3 to 10 requests per second.

A clean Markdown report is written to `pilot_search_report.md` next to the script.

## Environment setup

The current repository is intentionally lightweight. The pilot-search script
(`pilot_search.py`) uses only the Python standard library and therefore has no
required third-party dependencies.

A minimal isolated environment can nevertheless be created as follows:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Optional but recommended:

```bash
pip install --upgrade pip setuptools wheel
```

The virtual environment directory (`.venv/`) is excluded from version control
via `.gitignore`.

If future analysis scripts introduce external dependencies, a `requirements.txt`
file will be added and versioned in the repository.

## Registration

- **OSF Registries (v0.5.1):** [10.17605/OSF.IO/FU82J](https://doi.org/10.17605/OSF.IO/FU82J) — registration record at [https://osf.io/fu82j/](https://osf.io/fu82j/)
- **Zenodo (this repository, v0.5.1):** [10.5281/zenodo.20609130](https://doi.org/10.5281/zenodo.20609130)
- **Zenodo concept DOI** (always resolves to the latest released version): [10.5281/zenodo.20140263](https://doi.org/10.5281/zenodo.20140263)

## Citing this work

> Odan, S., Melloni, L., Bicanski, A., & Jost, J. (2026). *Complexity measures of consciousness: a PRISMA-ScR methodological review (v0.5.1)* [Protocol]. Zenodo. https://doi.org/10.5281/zenodo.20609130

## Licence

- Protocol document and methodological materials: **CC-BY 4.0**.
- Code (`pilot_search.py` and any later scripts): **MIT**.
