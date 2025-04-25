# PRS

This pipeline calculates polygeic risk score(PRS) using two tools PLINK-2 and PRSice1.9.
It requires foloqing inputs:
1.	A target cohort: genotype data of the individuals for which you wish to obtain PRS scores
2.	A base cohort: GWAS summary statistics which will be used to calculate the PRS. 
3.	A target phenotype: a file specifying sample IDs, phenotypes and covariates.

## Setting up the environment
Instalation 
PRSice-2 relies on PLINK for genetic data processing. Follow these steps:


https://github.com/choishingwan/PRSice   for PRSice intaltaiton- download

Navigate to the directory where you extracted PRSice (C:\PRSice) using the command:
bash
cd C:\PRSice

##Data

Sample data is from CARDIoGRAMplusC4D database. Sa penotype data was used distibution in cases and controls
.map file
|Chr | SNP |          |Position|
|-----:|---------------|-|----|
|     1|               |-|345666|
|     2|               |-|66345|
|     3|               |-|6452424|

.ped file 
|Family ID |Individual IID|Father's ID (O for unknown)|Mather's ID (O for unknown)|sex|phenotype|First alelle|Second allele|First allele|Second allele|
|-----:|---------------|-|----|---|-|-|-|-|-|
|     1|               |-|||||||
|     2|               |-||||||||
|     3|               |-||||||||



to binary files .bed .bim .fam
.\plink2 --pedmap data.ped data.map --make-bed --out data_binary

## Quality control

## PRS clalcuation with
PRS calcualtio using plink
##Softvere
-All files in the same directiroy including PLINK and PRSice
## PLINK

## PRSice tool
Rscript PRSice.R --prsice PRSice_win64.exe --base gwas_summary_stats.txt --target nucleotides_genotype_binary --binary-target T --pheno phenotype.txt --covariate covariates.txt --snp SNP --chr CHR --bp BP --a1 A1 --a2 A2 --stat BETA --pvalue P --out PRS_output
 GWAS data

|SNP | CHR |BPT|A1M|A2|BETA|P-value|
|-----:|---------------|-|-|----|-|-|
|     1|               ||||||
|     3|               ||||||

## output results

|FID | IID |ALLELE_CT|NAMED_ALLELE_DOSAGE_SUM|SCORE1_AVG|
|-----:|---------------|-|-|----|
|     1|               ||||
|     2|               ||||
|     3|               ||||

