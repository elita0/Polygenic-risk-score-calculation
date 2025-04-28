#script uses excel format input files. Format you can see in .... file. 



import pandas as pd
import os

# Input files
genotypes_path = input("Enter the path to the nucleotide genotypes Excel file: ")
snp_info_path = input("Enter the path to the SNP info Excel file: ")
output_ped_path = input("Enter the path for the output .ped file: ")
output_map_path = input("Enter the path for the output .map file: ")

# Read Excel Files
df = pd.read_excel(genotypes_path, engine='openpyxl')
snp_info = pd.read_excel(snp_info_path, engine='openpyxl')

# --- Create .ped File ---
def create_ped_file(df, output_ped_path):
    with open(output_ped_path, 'w') as ped_file:
        for _, row in df.iterrows():
            participant_id = row.iloc[0]
            family_id = participant_id
            genotype_data = []

            for genotype in row.iloc[1:].values:
                if pd.isna(genotype) or genotype == '':
                    genotype_data.extend(['0', '0'])
                elif ' ' in str(genotype):
                    alleles = genotype.split(' ')
                    genotype_data.extend(alleles if len(alleles) == 2 else ['0', '0'])
                else:
                    genotype_data.extend([genotype, genotype])

            if len(genotype_data) != 2 * len(df.columns[1:]):
                print(f"Warning: Participant {participant_id} has {len(genotype_data)} genotypes instead of {2 * len(df.columns[1:])}")

            ped_line = f"{family_id} {participant_id} 0 0 0 -9 " + " ".join(genotype_data) + "\n"
            ped_file.write(ped_line)

# Create .map File
def create_map_file(snp_info, output_map_path):
    with open(output_map_path, 'w') as map_file:
        for _, row in snp_info.iterrows():
            chromosome = row.get('#CHROM')
            snp_id = str(row.get('ID')).replace('_CAD', '')
            position = row.get('POS')

            if pd.isna(chromosome) or pd.isna(snp_id) or pd.isna(position):
                print(f"Warning: Missing data for SNP {snp_id}")
                continue

            map_file.write(f"{chromosome} {snp_id} 0 {position}\n")

# Verification/debuging
def verify_ped_and_map(ped_path, map_path):
    with open(map_path, 'r') as map_file:
        num_map_snps = sum(1 for _ in map_file)

    with open(ped_path, 'r') as ped_file:
        first_row = ped_file.readline().strip().split()
        total_columns = len(first_row)
        num_ped_snps = (total_columns - 6) / 2

    print(f"\n.map SNPs: {num_map_snps}, .ped SNPs: {num_ped_snps}")
    print("Files are consistent!" if num_map_snps == num_ped_snps else "Mismatch in SNP counts!")

#  Run Everything 
create_ped_file(df, output_ped_path)
create_map_file(snp_info, output_map_path)
verify_ped_and_map(output_ped_path, output_map_path)
