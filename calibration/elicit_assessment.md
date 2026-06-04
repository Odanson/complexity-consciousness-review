# Elicit for the Complexity-Measures Scoping Review — An Objective Assessment

**Companion to:** `prisma_protocol.md` v0.5 · *(this is the pre-decision assessment from before the Elicit calibration was run; the rotation framing referenced below was the operative project framing at the time and has since been superseded by Lucia's "full Chapter-1 project" framing — the substantive Elicit analysis remains current)*
**Prepared:** 2026-05-25
**Prompted by:** Lucia's suggestion to use [Elicit](https://elicit.com/) to speed up the work.
**Scope of this note:** (1) where Elicit genuinely helps across our pipeline, and (2) whether using it as a "second reviewer" is a good move. Based on the Elicit systematic-review webinar (the GLP-1 / type-2-diabetes demo) plus what our own protocol actually requires.

---

## Bottom line up front

Elicit is worth adopting, but as a **screening-and-extraction accelerator and an AI second-screener — not as a replacement for the parts of this review that carry the intellectual weight** (the eight-axis taxonomy attribution, the math-vs-claims misapplication audit, the clustering / citation-network landscape).

Two things to hold onto before reading further:

1. **The demo is a clinical effect-size SLR; ours is a methodological scoping review.** Almost every feature shown — strict eligibility criteria, Kaplan-Meier curve digitisation, meta-analysis, effect-size extraction, narrative synthesis of "does the drug work" — is built for the Cochrane clinical world. Our outcome is not an effect size; it is *which complexity measure is used, on what data, with what mathematical content, and whether the claim attached to it is justified*. The overlap with Elicit is real but partial, and the partial bits matter.

2. **Elicit-as-"second reviewer" is not the same as a second independent human.** It is one automated system. For a solo reviewer (us) it is strictly better than nothing and genuinely strengthens the protocol — but it must be framed honestly as *AI-assisted second screening*, not *dual independent review*. More on this below; it is the most consequential decision in this note.

---

## The mismatch to keep in front of mind

| Dimension | Elicit demo (GLP-1 SLR) | Our review |
|---|---|---|
| Review type | Clinical systematic review | Methodological **scoping** review |
| Outcome of interest | Persistence/adherence rates, effect sizes | Systematic mapping + critique of complexity *measures* |
| "Strict criteria" toggle | **On** (fail one criterion → exclude) | **Off** — scoping reviews keep borderline papers (presenter said this explicitly) |
| Extraction targets | Sample size, dosing, KM curves, RCT vs cohort | Mathematical primitive, data requirement, inferential status, validation evidence (Axes 1–8) |
| Synthesis | Meta-analysis / narrative effect summary | Gap map + misapplication register + decision-support appendix |
| Validation evidence cited | 108/74/28 **Cochrane** reviews | None of Elicit's published accuracy numbers are on methodological reviews |

The headline accuracy figures from the webinar — title/abstract screening 96.9% sensitivity / 92.5% specificity; full-text 99.5% / 70.1%; extraction 95.6% — are all measured against **Cochrane clinical reviews**. They are encouraging, but we should not assume they transfer cleanly to "does this paper apply a quantitative complexity measure to neural data in a consciousness context." Our screening question is actually fairly clean and Elicit will likely do well on it; our *extraction* question is abstract and methodological, and that is where Elicit's numbers are least likely to hold.

---

## Where Elicit genuinely helps (stage by stage against our protocol)

**§B6 / Phase 2 — Source gathering.** Our PubMed search is locked at 5,267 records and translated to six databases. Elicit's PubMed tab runs raw Boolean queries: paste our locked string and it returns the same record set as PubMed itself (the presenter demonstrated 984 in Elicit ≈ 985 in PubMed). So Elicit does **not** force us off our reproducible search — we can keep the locked Boolean query as the source of record and just run it *inside* Elicit. Secondary benefit: Elicit's 138M-paper semantic corpus could serve as an **additional recovery channel** for database-missed papers (the Sitt-2014 problem), complementing — not replacing — our §B5 citation tracking.

**Phase 3 — Title/abstract screening. This is the single biggest time win.** Screening ~8–12k deduplicated records is where solo-reviewer hours disappear. Elicit screens against named eligibility-criterion questions, returns yes/no/maybe per criterion with a source quote highlighted in the abstract, and exports the full per-paper / per-criterion / rationale / quote table as CSV. With strict criteria **off** (correct for a scoping review) and Elicit's deliberate bias toward high sensitivity, it errs toward keeping papers — exactly the failure mode we want. This is a credible alternative or complement to the ASReview active-learning step in our current plan.

**Phase 4 — Full-text screening.** Elicit auto-fetches open-access full texts and, via its Chrome extension, can use **institutional credentials** to pull subscription papers (relevant once our library access is confirmed — see Phase 0). It screens full text the same way and shows exactly where in the PDF (including tables/figures) each judgment came from.

**§B8 — Data extraction (with an important boundary).** Elicit extracts user-defined columns from each included paper, with quotes and "not mentioned" handling. The right division of labour for us: let Elicit **pull the relevant methods text** into columns (what measure, what signal type, what recording modality, what the authors claim) — this saves real reading time — but **we assign the Axis 1–8 tags ourselves**. Elicit can quote "they computed Lempel-Ziv complexity on resting EEG"; it cannot reliably decide that this is Axis-1 *information-theoretic*, Axis-7 *inferential-status: descriptive*, Axis-8 *validation: pharmacological dissociation only*. Those are the judgments the whole review exists to make.

**PRISMA-S reporting / audit trail.** Every decision is exportable with rationale and source quote, and Elicit auto-generates a PRISMA flow diagram with per-criterion exclusion counts. That maps directly onto our `prisma_checklist_mapping.md` obligations and the flow diagram in the rotation deliverables list.

---

## Where Elicit does *not* help (and where it could quietly hurt)

- **The rotation landscape itself.** Topic clustering (BERTopic/LDA) and the citation-network analysis (Citationchaser → Louvain/Leiden) are the actual rotation deliverable. Elicit does none of this — it has no citation-graph or community-detection capability. Elicit accelerates the screening→extraction pipeline that *feeds* the landscape; it does not produce the landscape.
- **§B10 critical appraisal and meta-analysis.** Both are explicitly on Elicit's *roadmap* and not yet shipped. We can hand-build risk-of-bias columns in extraction, but there is no dedicated appraisal stage today.
- **§B11 synthesis.** Elicit's auto-generated narrative report is, by the presenter's own words, "a first pass" — and it is shaped like a clinical review (characteristics-of-included-studies tables, effect summaries). It will not write our gap map, misapplication register, or decision-support appendix. Treat any Elicit report as raw material at most.
- **KM-curve / figure digitisation.** Impressive, but irrelevant to us — we are not extracting survival curves. (Noted only so we don't over-value the demo's flashiest feature.)
- **Reproducibility drift if we lean on semantic search.** Elicit's semantic corpus search is *not* reproducible the way a Boolean PubMed query is, and the underlying ranking logic isn't fully transparent (a webinar attendee raised exactly this). If we ever let semantic search become a *primary* identification source, we compromise the audit trail we have carefully built for OSF. Keep semantic search supplementary and logged.

---

## The second-reviewer question (the crux)

Our protocol is deliberately a **solo-reviewer** design, justified by Yaron/Melloni 2022 (NHB) precedent and shored up with three reliability mechanisms: within-person test-retest (κ ≥ 0.8 on a 10% re-screen after a 2-week gap), periodic blind test-retest every 1,000 records, and an optional LLM-assisted verification pass on a 5–10% sub-sample (log disagreements, no override). Andrej's standing worry — and the field's — is the missing second human.

Elicit offers two relevant modes: **decision support** (humans review Elicit's recommendations, blinded from each other, then reconcile) and **Elicit as second screener** (run Elicit independently, export, compare to the human's decisions, reconcile, and compute agreement-rate + Cohen's κ). The review-stats panel gives a quantified calibration: our agreement with Elicit, and the same exclusion-reason rate (κ becomes stable above ~50–100 papers).

**My recommendation: adopt Elicit as an AI second-screener / decision-support layer, as a *complement* to — not a replacement for — the within-person test-retest. And do not call it dual independent review.**

The reasoning, honestly stated:

- These measure *different* things. Test-retest measures **our internal consistency** over time. Elicit-agreement measures **our calibration against an external benchmark**. Both add value; reporting both is stronger than either alone, and arguably stronger than the bare single-reviewer design in Yaron 2022.
- Elicit's high sensitivity means it is good at flagging papers we may have wrongly *excluded* — the single-reviewer failure mode that actually threatens a scoping review's completeness. That is precisely the gap a solo reviewer needs covered.
- But it is one automated system, not an independent mind. Current guidance (Cochrane's RAISE recommendations; the presenter's own concession that "we cannot just trust yet a system to do all of it by itself") treats AI as oversight-supported assistance, not as a substitute reviewer. Claiming "two independent reviewers" when one is Elicit would be a misrepresentation a reviewer could rightly challenge.
- The defensible framing for our methods section and the OSF registration: *"Single human reviewer (S.O.) with AI-assisted second screening (Elicit, PRISMA-2020 workflow), reconciled by the human reviewer; reviewer reliability assessed by within-person test-retest (κ ≥ 0.8) and human–AI agreement statistics."* That is accurate, it upgrades what we already planned (it effectively replaces the "optional LLM verification" line with something more rigorous and auditable), and it concedes nothing we cannot back up.

---

## Reproducibility & OSF implications (do these or don't bother)

1. **Run the locked Boolean query in Elicit's PubMed tab**, not semantic search, for the primary identification set. Keep semantic-corpus search as a supplementary recovery channel only, clearly labelled as such.
2. **Record the Elicit version and the date/time of every run** in the search/screening log — the AI behaves like a moving target between releases (the webinar itself noted error rates fell from ~20% to ~4–5% across versions), so the version is part of reproducibility.
3. **Export the per-paper criteria / rationale / quote CSVs** at each stage into the OSF data folder — this is the audit trail PRISMA-S asks for, and it is the thing that lets a third party check Elicit's decisions.
4. **State plainly in the protocol amendment** that screening was AI-assisted (Elicit), with human reconciliation, and that no decision was delegated to the tool without human review.

---

## Fit with the existing toolchain

Elicit overlaps with **Rayyan + ASReview** (screening) and with the manual **Zotero/spreadsheet extraction** for §B8 — it could substitute for, or run alongside, both. It does **not** replace **Citationchaser** (citation graph), **BERTopic** (topic clustering), or **Zotero** as a reference manager, and it does not touch the eight-axis attribution or the synthesis. The cleanest consolidation would be: Elicit for screening + first-pass extraction; keep Citationchaser + BERTopic + the manual axis-tagging and synthesis exactly as planned. Decide deliberately whether Elicit *replaces* ASReview or *runs as a parallel check* against it — running both once on the calibration set would itself be a useful validation.

---

## Practical prerequisites before committing

- **Plan tier / cost.** The rigorous SR features shown (strict-criteria toggle, dual review, review stats, PRISMA report, API) live on Elicit's **Scale / Enterprise** plans, not the free tier. Worth checking with Lucia whether her group or the institution already has access before we build a workflow around it.
- **Institutional full-text access.** The Chrome-extension full-text fetch depends on the library credentials we are already chasing in Phase 0 — so that prerequisite now does double duty.
- **A small head-to-head before trusting it.** Run Elicit on the same 200-abstract calibration set we screen by hand (Phase 3, Week 5), compute the agreement and κ, and only then decide how much of the bulk screen to lean on it for. That is one afternoon and it converts "Lucia says it's fast" into our own validation number.

---

## One-paragraph recommendation to take to Lucia

Elicit looks like a real speed win for the screening and first-pass extraction stages, and using it as an AI second-screener meaningfully strengthens our solo-reviewer design — I'd adopt it for those, run the locked PubMed Boolean query *inside* Elicit so we keep our reproducible search, and validate it against our own 200-abstract calibration set before relying on it. I would *not* present it as a second independent human reviewer, and I would keep the taxonomy attribution, the misapplication audit, the clustering, and the citation-network landscape in our own hands, since those are the parts of the review that actually constitute the contribution.

---

*Assessment only — no protocol changes made. If we proceed, the changes land as a §B7 amendment ("AI-assisted second screening") plus the four reproducibility items above, and the "optional LLM verification" line in the screening plan is upgraded to the Elicit second-screener workflow.*
