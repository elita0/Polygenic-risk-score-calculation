# PRS

This pipeline calculates polygeic risk score(PRS) using two tools PLINK-2 and PRSice1.9.
It requires foloqing inputs:
1.	A target cohort: genotype data of the individuals for which you wish to obtain PRS scores
2.	A base cohort: GWAS summary statistics which will be used to calculate the PRS. 
3.	A target phenotype: a file specifying sample IDs, phenotypes and covariates.

## Setting up the environment
Instalation 


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

## Quality control

## PRS clalcuation with
PRS calcualtio using plink
##Softvere

## output results

|FID | IID |ALLELE_CT|NAMED_ALLELE_DOSAGE_SUM|SCORE1_AVG|
|-----:|---------------|-|-|----|
|     1|               ||||
|     2|               ||||
|     3|               ||||

