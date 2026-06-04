[![DOI](https://zenodo.org/badge/1236657777.svg)](https://doi.org/10.5281/zenodo.20140262)

# Complexity Measures of Consciousness — PRISMA-ScR Review

Protocol, search strategy, and pilot code for a methodological scoping review of complexity measures applied to neural data in consciousness research.

The review systematically maps quantitative complexity measures applied to neural recordings in consciousness research, classifies included measures along eight orthogonal axes (mathematical primitive, data requirement, spatial scale, temporal granularity, theory anchoring, inferential status, validation evidence, aspect of consciousness), audits the fit between each included measure's mathematical content and the claims made with it, and identifies conceptual and methodological gaps. Reporting follows **PRISMA-ScR** (Tricco et al. 2018) and **PRISMA-S** (Rethlefsen et al. 2021); methodology follows **JBI** scoping-review guidance (Peters et al. 2020; Pollock et al. 2023).

## Status

| Item | Status |
|---|---|
| Protocol version | **v0.5** (2026-05-29, draft — holding for supervisor sign-off before OSF registration) |
| Search strategy | Locked in PubMed; five other database translations drafted |
| Search execution | Manual via each database's authenticated UI (institutional MPI/CBS login); code restricted to downstream QC, parsing, and analysis |
| PubMed hit count | 5,267 records (pilot, 2026-05-12) |
| Empirical seeds captured | 7 / 8 (Sitt 2014 = documented DB miss, recovered via citation tracking) |
| Screening model | Single human reviewer + Elicit AI second screening (calibrated 2026-05-28; κ = 0.843, recall 98.1 %, seeds 8/8) |
| Database access | Confirmed via MPI/CBS login: Scopus, Web of Science, PsycINFO (EBSCO), IEEE Xplore. Embase: confirmation pending |
| OSF workspace | Private workspace created 2026-05-29 (ORCID-linked, EU-Frankfurt storage); deliberately *unregistered*, *non-public*, and *unpopulated* pending v0.5 sign-off + change-audit clearance |
| Code archive | Zenodo, see DOI badge above |
| OSF registration | Pending v0.5 supervisor sign-off |

## Authors

Samson Odan (lead) · Lucia Melloni · Andrej Bicanski · Jurgen Jost.
External collaborators (to be added on contribution): Adam Barrett, Anil Seth.

## Files

- **`prisma_protocol.md`** and **`prisma_protocol_v0.4.1.md` / `.docx`** — current protocol, including locked search strategy, PECO criteria, eight-axis taxonomy, screening model, and amendments log. (`prisma_protocol.md` tracks the latest in-progress version; the `_v0.4.1` files are the stable snapshot archived on Zenodo.)
- **`database_queries.md`** — locked PubMed query plus equivalent translations for Scopus, Web of Science, PsycINFO, IEEE Xplore, and Embase.
- **`prisma_checklist_mapping.md` / `.docx`** — PRISMA-ScR (22-item) and PRISMA-S (16-item) compliance mapping against the protocol.
- **`pilot_search.py`** — pilot-search and seed-validation script (Python, stdlib only; queries PubMed E-utilities).
- **`pilot_search_report.md`** — most recent pilot output (hit counts + seed-paper per-block diagnosis).
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

- **OSF Registries:** pending — link will appear here on registration.
- **Zenodo (this repository, v0.4.1):** [10.5281/zenodo.20140262](https://doi.org/10.5281/zenodo.20140262)
- **Zenodo concept DOI** (always resolves to the latest released version): [10.5281/zenodo.20140263](https://doi.org/10.5281/zenodo.20140263)

## Citing this work

> Odan, S., Melloni, L., Bicanski, A., & Jost, J. (2026). *Complexity measures of consciousness: a PRISMA-ScR methodological review (v0.4.1)* [Protocol]. Zenodo. https://doi.org/10.5281/zenodo.20140262

## Licence

- Protocol document and methodological materials: **CC-BY 4.0**.
- Code (`pilot_search.py` and any later scripts): **MIT**.
