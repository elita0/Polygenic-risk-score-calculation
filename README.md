# PRS

This pipeline calculates polygeic risk score(PRS) using two tools PLINK-2 and PRSice1.9.

It requires folowing inputs:
1.	A target cohort: genotype data of the individuals for which you wish to obtain PRS scores
2.	A base cohort: GWAS summary statistics which will be used to calculate the PRS. 
3.	A target phenotype: a file specifying sample IDs, phenotypes and covariates (optional)



## Setting up the environment (All tools and data shoulde be located in one file)
PLINK instalation 
https://www.cog-genomics.org/plink/1.9/


Instalation 
PRSice-2 relies on PLINK for genetic data processing. 

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

PRSice usage explanation shame
R- paltform where PRSice works
Rscript comand that R scirpts form comandline
PRSice.R sciript that reads GWAS data
PRSice_win64.exe palīgprogrammas file, wich helps faster run 
![image](https://github.com/user-attachments/assets/b387154b-607e-42d3-ada2-0a39a1b82049)


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

