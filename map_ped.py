#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
map_ped_basic.py
----------------
Convert genotype and SNP information tables (Excel/CSV/TSV) into
PLINK-compatible .ped and .map files.

Usage:
    python map_ped_basic.py
    (then follow interactive prompts)

Author: Open, reusable script for PRS / GWAS workflows.
"""

import pandas as pd
from pathlib import Path
import re

# =========================
# Input paths (interactive)
# =========================
genotypes_path = input("Enter the path to the genotype table (Excel/CSV/TSV): ").strip()
snp_info_path  = input("Enter the path to the SNP info table (Excel/CSV/TSV): ").strip()
output_ped_path = input("Enter the path for the output .ped file: ").strip()
output_map_path = input("Enter the path for the output .map file: ").strip()

# =========================
# Helper: read any supported table type
# =========================
def read_table(path: str) -> pd.DataFrame:
    """Reads Excel (.xlsx/.xls) or CSV/TSV (.csv/.tsv/.txt) automatically."""
    p = Path(path)
    suf = p.suffix.lower()
    if suf in [".xlsx", ".xls"]:
        return pd.read_excel(p, engine="openpyxl")
    elif suf in [".csv"]:
        return pd.read_csv(p)
    elif suf in [".tsv", ".txt"]:
        return pd.read_csv(p, sep="\t")
    else:
        # Try Excel first, then CSV as fallback
        try:
            return pd.read_excel(p, engine="openpyxl")
        except Exception:
            return pd.read_csv(p)

# =========================
# Read the input files
# =========================
df = read_table(genotypes_path)
snp_info = read_table(snp_info_path)

# =========================
# Genotype normalization
# Accepts values such as "A G", "AG", "A/G", "A|G", or a single allele.
# =========================
VALID = {"A", "C", "G", "T"}

def normalize_genotype(val):
    """Convert genotype string into two alleles (A1, A2)."""
    if pd.isna(val) or str(val).strip() == "":
        return ["0", "0"]
    s = str(val).strip().upper()
    s = re.sub(r"[/|;,]", " ", s)
    parts = s.split()
    if len(parts) == 2:
        a1, a2 = parts[0], parts[1]
    elif len(parts) == 1 and len(parts[0]) == 2 and all(ch in VALID for ch in parts[0]):
        a1, a2 = parts[0][0], parts[0][1]
    elif len(parts) == 1 and len(parts[0]) == 1 and parts[0] in VALID:
        a1, a2 = parts[0], parts[0]
    else:
        return ["0", "0"]
    if a1 not in VALID or a2 not in VALID:
        return ["0", "0"]
    return [a1, a2]

# =========================
# Create .ped file
# =========================
def create_ped_file(df, output_ped_path):
    """Generate a PLINK .ped file from genotype table."""
    with open(output_ped_path, 'w') as ped_file:
        for _, row in df.iterrows():
            participant_id = row.iloc[0]      # assume first column = Sample ID
            family_id = participant_id        # use same ID as family ID
            genotype_data = []

            # Remaining columns are genotypes
            for genotype in row.iloc[1:].values:
                a1, a2 = normalize_genotype(genotype)
                genotype_data.extend([a1, a2])

            expected = 2 * len(df.columns[1:])
            if len(genotype_data) != expected:
                print(f"Warning: Participant {participant_id} has {len(genotype_data)} genotype tokens instead of {expected}")

            # Sex=0, Phenotype=-9 (placeholders; can be updated later)
            ped_line = f"{family_id} {participant_id} 0 0 0 -9 " + " ".join(genotype_data) + "\n"
            ped_file.write(ped_line)

# =========================
# Create .map file
# Required columns: #CHROM, ID, POS
# =========================
def create_map_file(snp_info, output_map_path):
    """Generate a PLINK .map file from SNP info table."""
    missing = 0
    with open(output_map_path, 'w') as map_file:
        for _, row in snp_info.iterrows():
            chrom = row.get('#CHROM')
            snp_id = row.get('ID')
            pos = row.get('POS')

            if pd.isna(chrom) or pd.isna(snp_id) or pd.isna(pos):
                missing += 1
                continue

            map_file.write(f"{int(chrom)} {str(snp_id)} 0 {int(pos)}\n")
    if missing > 0:
        print(f"Note: skipped {missing} SNP rows due to missing #CHROM/ID/POS")

# =========================
# Simple consistency check
# =========================
def verify_ped_and_map(ped_path, map_path):
    """Compare number of SNPs between .ped and .map files."""
    with open(map_path, 'r') as map_file:
        num_map_snps = sum(1 for _ in map_file)

    with open(ped_path, 'r') as ped_file:
        first_row = ped_file.readline().strip().split()
        total_columns = len(first_row)
        num_ped_snps = (total_columns - 6) / 2

    print(f"\n.map SNPs: {num_map_snps}, .ped SNPs: {num_ped_snps}")
    print("Files are consistent!" if num_map_snps == num_ped_snps else "Mismatch in SNP counts!")

# =========================
# Run all steps
# =========================
create_ped_file(df, output_ped_path)
create_map_file(snp_info, output_map_path)
verify_ped_and_map(output_ped_path, output_map_path)

print("\nNext step (convert to binary PLINK format):")
print(f"  plink --ped {output_ped_path} --map {output_map_path} --make-bed --out data_binary")

