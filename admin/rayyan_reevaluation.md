# Rayyan re-evaluation — do we still need it?

**Date:** 2026-05-29
**Context:** v0.5 protocol; Elicit is now the formal AI second-screener under §B7 step 5; ASReview handles active-learning prioritisation. Rayyan was originally named as the calibration-phase screening UI in §B7. With Elicit's UI covering per-criterion screening, per-record rationale, source quotes, and CSV export, *does Rayyan still earn its place in the pipeline?*

## What Rayyan was originally going to do

The v0.4.3 §B7 had two screening-phase tools: **Rayyan** for the calibrated single-reviewer phase (paper-by-paper screening with documented rationale per decision) and **ASReview** for the active-learning bulk pass. Rayyan was paired with the calibration set; ASReview took over for the long tail.

## What Elicit now covers

Elicit's PRISMA-2020 systematic-review workflow already provides:

- Per-record screening UI with the four protocol criteria as named columns.
- Per-criterion yes / no / maybe with rationale and source-quote highlighting in the abstract.
- Overall include / exclude verdict + score.
- CSV / Excel export of every decision (used as the audit trail in §B7).
- Manual override for any individual record (used during reconciliation).
- A PRISMA flow diagram auto-generated at the end.

This functionally covers what Rayyan offered for the calibration phase, with the bonus that the same tool runs the bulk pass.

## What Rayyan still uniquely offers

- **Deduplication.** Rayyan's deduplicator is the second of three layers in §B7's dedup pipeline (Bramer in Zotero + Rayyan + manual spot-check). This step is independent of screening and is genuinely useful.
- **Free, well-documented, robust.** No downside to running a project on it as a backup.

## Recommendation (conservative)

**Keep Rayyan in the protocol lightly.** The protocol-facing framing should remain something like:

> "Rayyan used for deduplication and screening management where appropriate."

Operationally — i.e., in how the work actually runs day-to-day — the division of labour is likely to converge to:

- **Elicit** as the screening engine (per-criterion screening with rationale + source-quote audit trail).
- **ASReview** as the prioritisation engine (active-learning queue ordering during the bulk pass).
- **Rayyan** as the corpus-management layer (deduplication as one of three dedup tools per §B7; conflict-tracking / project-state if needed during calibration / reconciliation).

The reason for keeping Rayyan in the protocol *lightly* rather than removing it: methodological legitimacy. PRISMA-ScR reviewers expect Rayyan or an equivalent screening-management tool to be named; removing it for purely operational reasons would invite questions that have no scientific payoff to litigate. The conservative position is to keep it cited, use it where it earns its place (dedup is the clearest case), and let operational practice converge without forcing protocol-level surgery.

## Protocol implications

**No protocol edit recommended at v0.5.** The current §B7 "Screening platform" line — *"Rayyan (free, conflict-tracked) for the calibration phase; ASReview ... for the active-learning prioritised screening of the bulk corpus"* — is conservative enough as written; it does not preclude Elicit's role (described separately in §B7 step 5), nor does it overcommit to Rayyan beyond what we will actually use. If a tightening edit lands later, it should be a soft replacement along the lines of *"Rayyan for deduplication and screening management where appropriate; ASReview ..."*, not a removal.

## Operational note

Whoever runs Phase 2 deduplication should treat Rayyan's deduplicator as one of three independent dedup passes per §B7 (Bramer-in-Zotero + Rayyan + manual spot-check). Whether to also use Rayyan's UI during reconciliation is a personal-preference call; Elicit's export covers the audit-trail requirement either way.
