# OSF project setup — step-by-step

**Goal:** Create the **private** OSF project workspace now (no registration yet — registration waits for the four supervisor sign-offs on v0.5).

**Time:** ~30 minutes the first time.

**Prerequisite:** ORCID account. Yours is recorded in the protocol as 0009-0002-2909-0831.

---

## Stage 1 — OSF account + project (10 minutes)

1. Go to **osf.io**.
2. Sign in with ORCID (top-right → *Sign in* → *Sign in with ORCID*). This links the project to your ORCID automatically — important for the eventual Zenodo / Crossref handshake at publication.
3. Once signed in: *Create new project*.
4. Project title: **Complexity Measures of Consciousness — PRISMA-ScR Methodological Review**
5. Project description (paste this):
   > Pre-registrable PRISMA-ScR scoping review cataloguing quantitative complexity measures applied to neural data in consciousness research. Systematically maps measures along eight orthogonal axes (mathematical primitive, data requirement, spatial scale, temporal granularity, theory anchoring, inferential status, validation evidence, aspect of consciousness), audits the fit between each measure's mathematical content and the claims made with it, and identifies conceptual and methodological gaps. Methods follow PRISMA-ScR (Tricco et al. 2018), PRISMA-S (Rethlefsen et al. 2021), and JBI scoping-review guidance (Peters et al. 2020; Pollock et al. 2023). Screening uses a single human reviewer with AI-assisted second screening (Elicit, pre-registered calibration: κ = 0.843, recall 98.1 %, seeds 8/8) + ASReview active-learning prioritisation + within-person test-retest.
6. *Storage location*: pick your closest region (EU-Frankfurt for Max Planck).
7. **Privacy: Private** (this is the workspace, not the registration).
8. Create.

## Stage 2 — Folder structure (5 minutes)

Create these folders under the project root (via OSF's *Files* tab → *+* on the OSF Storage component):

```
/protocol/
/code/
/search/
/calibration/
/screening/
/extraction/
/synthesis/
/manuscripts/
/admin/
```

## Stage 3 — Upload v0.5 artefacts (10 minutes)

Upload the following from this repo into the matching folders:

- `/protocol/` ← `prisma_protocol.md`, `prisma_checklist_mapping.md`, `database_queries.md`, `elicit_screening_prompts.md`, all `prisma_protocol_v0.4.*.md` snapshots, `LICENSE-PROTOCOL.txt`
- `/code/` ← `pilot_search.py`, `calibration_sample.py`, `calibration_analysis.py`, `requirements.txt`, `LICENSE`
- `/search/` ← `pilot_search_report.md`, `pilot_search_notes.md`
- `/calibration/` ← `calibration_test_plan.md`, `calibration_equivalence_audit.md`, `calibration_results.md`, `calibration_adjudications.md`, `calibration_200_screening (human).csv`, `calibration_200_screening_reconciled.csv`, `calibration_disagreements_classified.csv`, `calibration_200_provenance.txt`, `calibration_200.ris`, `calibration_seeds.ris`, `elicit_assessment.md`
- `/admin/` ← `rotation_milestone.md`, `rotation_checklist.md`, `github_zenodo_setup.md`, `docs/data_management_plan.md`, `wording_audit_2026-05-29.md`

## Stage 4 — Invite supervisors as contributors (5 minutes)

Once Lucia and Andrej have replied with their ORCIDs (you have Jürgen's already at 0000-0001-5258-6590):

- Project → *Contributors* → *Add*.
- Search by ORCID for each. Set permission: **Read + write** (so they can leave inline comments / upload extraction tables if they ever want to).
- Bibliographic contributor: **yes** (appears as a contributor in the OSF citation).
- Send.

## Stage 5 — Link GitHub repo (optional but recommended)

If you have the GitHub repo public-ready: project → *Add-ons* → enable **GitHub** → authorise → select `complexity-consciousness-review` → enable as a component. This mirrors your GitHub commits into the OSF project as an audit trail.

## What NOT to do yet

- **Do not register the project.** Registration is the irreversible pre-registration step and waits for the four sign-offs on v0.5. The private workspace and the registration are separate operations on OSF.
- **Do not flip privacy to public** until the day you register.

## When to register

The decision (§C remaining open item) is *before vs after the multi-database run.* Lucia's earlier guidance was lean toward *before* (PRISMA-ScR convention is to register the protocol before search execution). When the four sign-offs are in:

1. Tag `v0.5` on GitHub → Zenodo auto-archives → mints a new specific-release DOI.
2. Update protocol §B6.3 with the new DOI; commit + push.
3. On OSF: *Registrations* → *Create new registration* → fill the OSF-Standard form → attach the v0.5 snapshot → submit.
4. The OSF registration link goes into the README and §B1, replacing the "(target)" / "(pending)" placeholders.
