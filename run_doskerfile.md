1. Build the Docker image

Make sure you are in the same directory as the `Dockerfile`, then run:

```bash
docker build -t prs-env .

2. Run an interactive session
docker run --rm -it -v "$PWD":/work prs-env bash

3. Example workflow

Example: Quality control + PRS calculation.

# Quality control
plink --bfile data_binary --maf 0.01 --hwe 1e-6 --geno 0.05 --mind 0.1 --make-bed --out data_qc

# PRS calculation
Rscript PRSice.R \
  --prsice /usr/local/bin/PRSice_linux \
  --base gwas_summary_stats.txt \
  --target data_qc \
  --pheno phenotype.txt \
  --cov covariates.txt \
  --snp SNP --chr CHR --bp BP --A1 A1 --A2 A2 \
  --stat BETA --pvalue P \
  --binary-target T \
  --out PRS_output
