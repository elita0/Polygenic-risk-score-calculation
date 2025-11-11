# Polygenic risk score calculation

This repository provides a complete workflow for calculating Polygenic Risk Scores (PRS) using PLINK 1.9/2.0 and PRSice-2.

It includes:

Environment setup instructions (PLINK, R, PRSice)
Data conversion script (map_ped.py)
QC and PRS computation pipeline
Example input/output file structures

Required input files:
1.	A target cohort: genotype data of the individuals for which you wish to obtain PRS scores
2.	A base cohort: GWAS summary statistics which will be used to calculate the PRS. 
3.	A target phenotype: a file specifying sample IDs, phenotypes and covariates (optional)


## Data
Raw genotype tables should be converted to **PLINK binary files** for downstream analyses.  
See [ped_map_file_structure.md](./ped_map_file_structure.md#example-input-and-output-file-structure) and [map_ped.py](./map_ped.py) for detailed instructions on converting raw tables to `.ped` and `.map` formats.  

Both PRSice and PLINK allow adding phenotype and covariate data (e.g., age, sex, disease status) at run time — e.g., PRSice (--pheno / --cov) or PLINK (--pheno / --covar) — to link outcomes and covariates with genotype IDs (FID / IID).


.map file
|Chr | SNP |          |Position|
|-----:|---------------|-|----|
|     1|               |-|345666|
|     2|               |-|66345|
|     3|               |-|6452424|

.ped file 
|Family ID |Individual IID|Father's ID (0 for unknown)|Mather's ID (0 for unknown)|sex|phenotype|SNP1 First alelle|SNP1 Second allele|SNP2 First allele|SNP2 Second allele|..|
|-----:|---------------|-|----|---|-|-|-|-|-|-|
|     1|               ||||||||||
|     2|               ||||||||||
|     3|               ||||||||||



To convert the `.ped` and `.map` files into binary PLINK files (`.bed`, `.bim`, `.fam`), run the following command in the command line:

```bash
./plink2 --pedmap data.ped data.map --make-bed --out data_binary
```

## Quality control

Quality control ensures that genotype data are reliable before calculating PRS.
Typical QC steps include:

- Minor Allele Frequency (MAF) filter
Removes rare variants with very low allele frequencies (e.g., --maf 0.01 keeps SNPs with MAF ≥ 1%).

- Hardy–Weinberg Equilibrium (HWE) test
Excludes SNPs deviating from expected genotype proportions in controls (e.g., --hwe 1e-6).

- Genotyping missingness per SNP (--geno)
Removes SNPs with high missing call rates (e.g., --geno 0.05 excludes SNPs missing in > 5% of samples).

- Individual missingness (--mind)
Removes individuals with excessive missing genotypes (e.g., --mind 0.1 excludes samples with > 10% missing data).




For other QC checks, see the [PRS Tutorial on Target Data](https://choishingwan.github.io/PRS-Tutorial/target/).

### Ambiguous SNPs in PRSice

When calculating PRS with PRSice, you may get errors about ambiguous SNPs (A/T or C/G).  
Include ambiguous SNPs only if the GWAS summary statistics and the target genotype data are aligned on the same strand.
Otherwise, ambiguous SNPs should be removed to prevent strand mismatches.

- `--keep-ambig` → keep ambiguous SNPs in the analysis  
- `--remove-ambig` (older versions) → explicitly drop ambiguous SNPs  



## PRS calculation

-All files should be in the same directiroy including PLINK and PRSice tools
### PLINK
As a minor allele is used GWAS data


```
Rscript PRSice.R \
  --prsice PRSice_win64.exe \
  --base gwas_summary_stats.txt \
  --target genotype_binary \
  --pheno phenotype.txt \
  --cov covariates.txt \
  --snp SNP --chr CHR --bp BP --A1 A1 --A2 A2 \
  --stat BETA --pvalue P \
  --binary-target T \
  --out PRS_output

```
 GWAS data

|SNP | CHR |BPT|A1|A2|BETA|P-value|
|-----:|---------------|-|-|----|-|-|
|     1|               ||||||
|     3|               ||||||

### output file format

|FID | IID |ALLELE_CT|NAMED_ALLELE_DOSAGE_SUM|SCORE1_AVG|
|-----:|---------------|-|-|----|
|     1|               ||||
|     2|               ||||
|     3|               ||||

