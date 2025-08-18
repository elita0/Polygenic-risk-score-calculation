# Polygenic risk score calculation

This pipeline calculates polygeic risk score(PRS) using two tools PLINK-2 and PRSice1.9.

It requires folowing inputs:
1.	A target cohort: genotype data of the individuals for which you wish to obtain PRS scores
2.	A base cohort: GWAS summary statistics which will be used to calculate the PRS. 
3.	A target phenotype: a file specifying sample IDs, phenotypes and covariates (optional)


## Data

In this example, the sample data comes from the CARDIoGRAMplusC4D database. Phenotype data is defined as case–control status, where individuals are assigned to either the case group or the control group. The raw data is provided in Excel format and is converted to PLINK-compatible files (.ped/.map) using map_ped.py.

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

## PRS calcuation with
PRS calcualtio using plink
##Softvere
-All files in the same directiroy including PLINK and PRSice
## PLINK
As a minor allele is used GWAS data


```
Rscript PRSice.R --prsice PRSice_win64.exe --base gwas_summary_stats.txt --target genotype_binary --binary-target T --pheno phenotype.txt --covariate covariates.txt --snp SNP --chr CHR --bp BP --a1 A1 --a2 A2 --stat BETA --pvalue P --out PRS_output
```
 GWAS data

|SNP | CHR |BPT|A1|A2|BETA|P-value|
|-----:|---------------|-|-|----|-|-|
|     1|               ||||||
|     3|               ||||||

## output file format

|FID | IID |ALLELE_CT|NAMED_ALLELE_DOSAGE_SUM|SCORE1_AVG|
|-----:|---------------|-|-|----|
|     1|               ||||
|     2|               ||||
|     3|               ||||

