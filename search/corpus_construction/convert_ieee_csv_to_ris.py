#!/usr/bin/env python3
"""
Convert IEEE Xplore CSV exports to RIS.

Usage:
    python convert_ieee_csv_to_ris.py input1.csv input2.csv -o IEEE_2026-06-10.ris

If -o is omitted, each CSV is converted to a same-name .ris file.
"""

import argparse
import math
import re
from pathlib import Path

import pandas as pd


def clean_val(x):
    if pd.isna(x):
        return ""
    s = str(x).strip()
    if s.lower() in ("nan", "none", "nat"):
        return ""
    return re.sub(r"\s+", " ", s)


def escape_ris_text(s):
    return clean_val(s).replace("\r", " ").replace("\n", " ")


def split_authors(authors):
    s = clean_val(authors)
    if not s:
        return []
    return [p.strip() for p in s.split(";") if p.strip()]


def ris_type(row):
    ident = clean_val(row.get("Document Identifier", ""))
    pubtitle = clean_val(row.get("Publication Title", ""))
    if "conference" in ident.lower() or "conference" in pubtitle.lower() or "proceeding" in pubtitle.lower():
        return "CPAPER"
    if "book" in ident.lower():
        return "CHAP"
    if "magazine" in ident.lower():
        return "MGZN"
    return "JOUR"


def write_tag(f, tag, value):
    value = escape_ris_text(value)
    if value:
        f.write(f"{tag}  - {value}\n")


def row_to_ris(f, row):
    f.write(f"TY  - {ris_type(row)}\n")
    write_tag(f, "TI", row.get("Document Title", ""))
    for au in split_authors(row.get("Authors", "")):
        write_tag(f, "AU", au)

    write_tag(f, "T2", row.get("Publication Title", ""))
    write_tag(f, "JO", row.get("Publication Title", ""))
    write_tag(f, "PY", row.get("Publication Year", ""))
    write_tag(f, "VL", row.get("Volume", ""))
    write_tag(f, "IS", row.get("Issue", ""))
    write_tag(f, "SP", row.get("Start Page", ""))
    write_tag(f, "EP", row.get("End Page", ""))
    write_tag(f, "AB", row.get("Abstract", ""))
    write_tag(f, "SN", row.get("ISSN", ""))
    write_tag(f, "SN", row.get("ISBNs", ""))
    write_tag(f, "DO", row.get("DOI", ""))
    write_tag(f, "UR", row.get("PDF Link", ""))
    write_tag(f, "PB", row.get("Publisher", ""))

    for col in ["Author Keywords", "IEEE Terms", "Mesh_Terms"]:
        kws = clean_val(row.get(col, ""))
        if kws:
            for kw in [k.strip() for k in kws.split(";") if k.strip()]:
                write_tag(f, "KW", kw)

    note = "Imported from IEEE Xplore CSV export"
    ident = clean_val(row.get("Document Identifier", ""))
    if ident:
        note += f"; Document Identifier: {ident}"
    write_tag(f, "N1", note)
    f.write("ER  - \n\n")


def convert_many(input_paths, output_path=None):
    if output_path:
        with open(output_path, "w", encoding="utf-8", newline="\n") as f:
            total = 0
            for path in input_paths:
                df = pd.read_csv(path)
                total += len(df)
                for _, row in df.iterrows():
                    row_to_ris(f, row)
        print(f"Wrote {total} records to {output_path}")
    else:
        for path in input_paths:
            df = pd.read_csv(path)
            out = path.with_suffix(".ris")
            with open(out, "w", encoding="utf-8", newline="\n") as f:
                for _, row in df.iterrows():
                    row_to_ris(f, row)
            print(f"Wrote {len(df)} records to {out}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_files", nargs="+", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()
    convert_many(args.csv_files, args.output)


if __name__ == "__main__":
    main()
