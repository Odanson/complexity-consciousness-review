# Wording audit — overclaim sweep

**Date:** 2026-05-29
**Scope:** Repository-wide editorial pass before commit. Goal: remove unintended overclaims of exhaustiveness or certainty; bring wording in line with PRISMA-ScR / JBI scoping-review conventions ("systematically map," "identify and classify," "included measures," "characterise the literature," "identify gaps") without weakening scientific ambition.
**Not a methodological change.** No protocol version bump and no amendments-log entry — per the audit instruction this is an editorial precision pass only.

---

## Trigger terms searched

Across all live `.md` documents:

`every` · `all (when implying exhaustiveness)` · `exhaustive` · `complete(ness)` · `comprehensive` · `definitive (catalogue)` · `entire literature` · `universal` · `universe of` · `fully captures` · `perfect (recovery|capture)` · `all measures` · `all metrics` · `catalogues every` · `catalogues all` · `catalogues what`

Snapshots `prisma_protocol_v0.4.1.md`, `v0.4.2.md`, `v0.4.3.md` were **not** edited — see "Files intentionally left alone" below.

---

## Substantive edits (7)

### 1. `README.md` — landing-page description

Before:
> "The review **catalogues every** quantitative complexity measure that has been applied to neural recordings in a consciousness context, **classifies them** along eight orthogonal axes …, audits the fit …, and **flags systematic gaps**."

After:
> "The review **systematically maps** quantitative complexity measures applied to neural recordings in consciousness research, **classifies included measures** along eight orthogonal axes …, audits the fit between each **included measure's** mathematical content and the claims made with it, and **identifies conceptual and methodological gaps**."

Why: the landing-page sentence is the most-read piece of the repo and the one the original concern was raised about. Replaces three overclaim phrases at once.

### 2. `prisma_protocol.md` — Executive summary (line 18)

Before: *"It will (i) **catalogue every** quantitative complexity measure that has been applied to neural data in a consciousness context, (ii) **classify the corpus** along eight orthogonal axes …, (iii) audit the fit between **each measure's** mathematical content …, and (iv) **flag systematic gaps**."*

After: *"It will (i) **systematically identify and catalogue** quantitative complexity measures applied to neural data in consciousness research, (ii) classify the **included corpus** along eight orthogonal axes …, (iii) audit the fit between each **included measure's** mathematical content …, and (iv) **identify conceptual and methodological gaps**."*

Why: same overclaim pattern as the README, and the executive summary is the OSF-facing version of the same sentence.

### 3. `prisma_protocol.md` — §A2 review aim 1 (line 30)

Before: *"**Catalogue every** quantitative complexity measure **that has been applied** to neural data — invasive or non-invasive, in humans or non-human animals — in consciousness research."*

After: *"**Systematically identify and catalogue** quantitative complexity measures **applied** to neural data — invasive or non-invasive, in humans or non-human animals — in consciousness research."*

Why: aim 1 is the protocol's formal statement of scope. Drops the absolute "every"; preserves the substantive ambition (the full inclusive range of techniques and species).

### 4. `prisma_protocol.md` — §B12 Coverage check (line 440)

Before: *"Lucia flagged that the measures inventory must be **demonstrably complete** — 'if the set isn't complete then the review is not either.' The Block 2 term list and Axis 1 family list have been cross-checked against …"*

After: *"Lucia flagged that the **measure-family inventory must adequately cover the major measure families used in the field** — 'if the set isn't complete then the review is not either.' ***Coverage* is operationalised here as cross-checking against established measure-family reference lines rather than as exhaustive enumeration of every measure ever published;** the Block 2 term list and Axis 1 family list have been cross-checked against …"*

Why: this paragraph had the strongest absolute-completeness wording in the protocol. The fix preserves Lucia's verbatim quote (her words and concern are unchanged) but adds the explicit operationalisation — *complete* in our usage means *covers the major measure families*, established via cross-check, not *exhaustive enumeration*. The substantive methodology (cross-checking Block 2 against the Yaron 2024 / wSMI / phase-dynamics reference lines) is unchanged.

### 5. `prisma_protocol_action_plan.md` — purpose statement (line 7)

Before: *"the review's job is to **catalogue what is being used**, what **each measure** actually computes, and where it is misapplied."*

After: *"the review's job is to **systematically map what is being used**, what each **included measure** actually computes, and where it is misapplied."*

Why: same wording pattern as the live protocol's executive summary; kept consistent.

### 6. `prisma_protocol_action_plan.md` — §A2 aim 1 (line 17)

Before: *"**Catalogue all** quantitative complexity measures **that have been applied** to neural data in consciousness research."*

After: *"**Systematically identify and catalogue** quantitative complexity measures **applied** to neural data in consciousness research."*

Why: mirrors the §A2 fix in `prisma_protocol.md`.

### 7. `elicit_assessment.md` — clinical-vs-methodological comparison table (line 27)

Before: column cell "**Catalogue + critique** of complexity *measures*"

After: column cell "**Systematic mapping + critique** of complexity *measures*"

Why: an internal-comparison cell, but the wording mirrors the same pattern; kept consistent with the protocol's revised framing.

---

## Hits intentionally left alone (defensible bounded claims)

The trigger words also appear in many places where the surrounding context bounds the claim — these were inspected and retained.

- **Periodicity / cadence.** "Every 1,000 records" (test-retest cadence in protocol §B7 step 4, rotation milestone §Phase 3, rotation checklist Standing items, `elicit_assessment.md` §63) — a frequency, not an exhaustiveness claim.
- **Bounded internal sets.** "Every included paper" (protocol §B7 data-extraction sentence; rotation milestone §3 deliverable 8; rotation milestone §5; rotation checklist Phase 6), "every screening decision" (rotation milestone §5; rotation checklist Standing items), "every disagreement" (`calibration_test_plan.md` §4), "every single one of Elicit's 15 disagreements" (`calibration_results.md`), "every record" in Elicit screening (protocol §B7 step 5 — refers to records in our corpus that pass the search) — all bounded to the included or paired set, not the literature.
- **Methodological idioms.** "Most complete" (referring to which duplicate report to keep, protocol §B4 + action plan §6), "screening complete" / "abstract screening complete" / "Chapter 1 substantively complete" (rotation checklist gates) — these are aspect/progress markers ("we are done with this step"), not exhaustiveness claims.
- **"Theory adjudication" framing (§A3).** "We *do* catalogue each measure's theoretical provenance" — bounded to per-measure provenance recording, not a universe claim.
- **Citations to external catalogues.** "the measures catalogued there" / "catalogues measure families associated with GNW, IIT, and TTC" — referring to what the Chis-Ciure / Yaron 2024 paper catalogues, not what we claim. Defensible.
- **Sitt 2014 recovery sentence (§B6.2).** "recovered through §B5 citation tracking on the seed set, which it satisfies via virtually every captured DOC / EEG paper" — bounded to citation-tracking behaviour on the seed set; "virtually every" is a soft claim about citation graph density, not literature coverage. Defensible.
- **Expert elicitation (§B5).** "every suggestion logged together with whether the database search already captured it" — refers to suggestions received from supervisors / external collaborators (bounded set, used for a sensitivity estimate). Defensible.
- **Risk register (§D), scope-creep row.** "before the review is complete" — temporal completion, not coverage. Defensible.
- **PRISMA checklist mapping.** "Of the protocol items, all are addressed." — claims about checklist coverage of *the protocol*, not literature coverage. Defensible.
- **Elicit assessment §72.** "the single-reviewer failure mode that actually threatens a scoping review's completeness" — methodological term ("completeness" in PRISMA usage = recall of inclusions), not a claim of ontological completeness.

If a future reviewer flags any of these as still overclaiming, they're isolated single-word fixes — but I think each is defensible as it stands.

---

## Files intentionally left alone

- **`prisma_protocol_v0.4.1.md`, `v0.4.2.md`, `v0.4.3.md`** (and their `.docx` snapshots). These are *immutable historical snapshots* of what was the live protocol at each version. v0.4.1 is on Zenodo (DOI 10.5281/zenodo.20140262); editing the in-repo copy retroactively would corrupt the audit trail and create a mismatch between the in-repo and Zenodo-archived versions of the same DOI. The overclaim wording in these snapshots is what the protocol *said at the time*; the current and future versions carry the revised wording. If a future Zenodo release is cut from the live protocol post-audit, that future snapshot will carry the corrected language automatically.
- **`prisma_protocol_v0.4.4.md`** does not yet exist (v0.4.4 lives only in the live `prisma_protocol.md`). When a v0.4.4 snapshot is generated, it will already carry the corrected wording.
- **Code files** (`pilot_search.py`, `calibration_sample.py`, `calibration_analysis.py`). Comments and docstrings were not flagged by the trigger-term sweep.
- **Data artefacts** (`calibration_*.csv`, `.ris`, `_provenance.txt`). Tabular records; no narrative wording to revise.
- **Email draft** (`email_to_supervisors.md`). Pre-existing draft of an unsent supervisor email; the trigger-term sweep returned nothing concerning here.

---

## Files touched

`README.md` · `prisma_protocol.md` (3 edits) · `prisma_protocol_action_plan.md` (2 edits) · `elicit_assessment.md` (1 edit).
Plus this audit-log file itself (`wording_audit_2026-05-29.md`) added to the folder.

No code, no data, no snapshots, no protocol version change, no amendments-log entry.
