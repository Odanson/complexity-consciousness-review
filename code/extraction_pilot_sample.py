"""Draw the 10-paper pilot sample for the extraction form (protocol §B8) and the
critical-appraisal checklist (§B10 uses the same 10 papers).

Input : screening/final_included_set_with_additions_2026-11-10.csv
Rule  : simple random sample of 10 from the 529 records whose source is
        'database search + full-text screening' (the seven additions are excluded
        so foundational/methods papers do not skew the pilot).
Seed  : 20261110. IDs are sorted before sampling so the draw is reproducible.
Output: extraction/pilot_sample_2026-11-10.csv
Run from the project root.
"""
import csv, random
SEED = 20261110
SRC = 'screening/final_included_set_with_additions_2026-11-10.csv'
rows = [r for r in csv.DictReader(open(SRC, encoding='utf-8'))
        if r['source'] == 'database search + full-text screening']
assert len(rows) == 529
ids = sorted(r['record_id'] for r in rows)
picked = random.Random(SEED).sample(ids, 10)
by = {r['record_id']: r for r in rows}
with open('extraction/pilot_sample_2026-11-10.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['pilot_no', 'record_id', 'rayyan_article_id', 'doi', 'title', 'year', 'journal'])
    for n, i in enumerate(picked, 1):
        r = by[i]
        w.writerow([n, i, r['rayyan_article_id'], r['doi'], r['title'], r['year'], r['journal']])
