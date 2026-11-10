#!/usr/bin/env python3
"""Draw the seeded random 10% test-retest sample for full-text screening (protocol §B7).

Input : screening/full_text_screening_decisions_2026-10-05.csv (1,313 records)
Design: proportional stratification by full_text_decision (Include / Exclude), so the
        sample is a random 10% of all records AND ~10% of the includes; both classes
        are present, so Cohen's kappa is computable.
Seed  : 20261007 (date drawn). Re-running reproduces the identical sample.
Output: screening/full_text_retest_BLIND_rescreen_2026-10-07.csv      (BLIND: no prior decision/notes)
        screening/full_text_retest_KEY_original_decisions_2026-10-07.csv  (original decisions; do not open before re-screening)
Usage : python3 code/full_text_retest_sample.py   (run from the repo root)
"""
import csv, random, math
SEED = 20261007; FRAC = 0.10
SRC = 'screening/full_text_screening_decisions_2026-10-05.csv'
rows = list(csv.DictReader(open(SRC, encoding='utf-8-sig')))
rng = random.Random(SEED)
picked = []
for cls in ('Include', 'Exclude'):
    ids = sorted(r['rayyan_article_id'] for r in rows if r['full_text_decision'] == cls)
    k = round(len(ids) * FRAC)
    picked += rng.sample(ids, k)
rng.shuffle(picked)
by = {r['rayyan_article_id']: r for r in rows}
with open('screening/full_text_retest_BLIND_rescreen_2026-10-07.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['rayyan_article_id', 'doi', 'title', 'year', 'journal', 'retest_decision', 'retest_reason', 'retest_date'])
    for i in picked:
        r = by[i]; w.writerow([i, r['doi'], r['title'], r['year'], r['journal'], '', '', ''])
with open('screening/full_text_retest_KEY_original_decisions_2026-10-07.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['rayyan_article_id', 'original_full_text_decision'])
    for i in sorted(picked): w.writerow([i, by[i]['full_text_decision']])
print(len(picked), 'records drawn; seed', SEED)
