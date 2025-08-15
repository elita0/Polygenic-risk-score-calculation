# Polygenic risk score calculation

This pipeline calculates polygeic risk score(PRS) using two tools PLINK-2 and PRSice1.9.

It requires folowing inputs:
1.	A target cohort: genotype data of the individuals for which you wish to obtain PRS scores
2.	A base cohort: GWAS summary statistics which will be used to calculate the PRS. 
3.	A target phenotype: a file specifying sample IDs, phenotypes and covariates (optional)



## Setting up the environment

### 1. PLINK Installation
1. Download PLINK from [https://www.cog-genomics.org/plink/1.9/](https://www.cog-genomics.org/plink/1.9/), choosing the version for your operating system:
   - Windows (64-bit or 32-bit)
   - macOS
   - Linux
2. This repository is based on using the **Windows** version. PLINK command lines are identical across all operating systems, but minor syntax modifications may be required.
3. Extract the downloaded `.zip` file.
4. *(Optional)* Add PLINK to your system `PATH`:
   - Open **Edit the system environment variables**.
   - Click **Environment Variables**.
   - Under **System variables**, find and edit `Path`.
   - Click **New** and add the folder where you extracted PLINK.

---

### 2. PRSice-2 Installation
PRSice is designed to run from **R** and relies on PLINK for genetic data processing.

1. Download PRSice from [https://github.com/choishingwan/PRSice](https://github.com/choishingwan/PRSice).
2. **Install R** (required):  
   Download and install the latest version of R from [https://cran.r-project.org/](https://cran.r-project.org/).  
   *(Optional but recommended)* Install **RStudio** as an IDE: [https://posit.co/download/rstudio-desktop/](https://posit.co/download/rstudio-desktop/).
3. Install the required R packages:
   ```r
   install.packages(c("data.table", "magrittr", "stringr"))

### PRSice Usage Workflow

Run the Rscript command from your terminal.

Rscript executes the PRSice.R script.

The PRSice.R script calls the PRSice_win64.exe binary to speed up processing.

When genetic data files (.bed, .bim, .fam) need to be loaded, PRSice uses PLINK.

All results are combined to generate the Polygenic Risk Score (PRS) for each individual.

Note: For easier file handling, place all tools and data in the same folder.



## Data

Sample data is from CARDIoGRAMplusC4D database. Sa penotype data was used distibution in cases and controls
Raw data was is excel format and changet to binary files using map_ped.py 
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



to binary files .bed .bim .fam
.\plink2 --pedmap data.ped data.map --make-bed --out data_binary

## Quality control

## PRS clalcuation with
PRS calcualtio using plink
##Softvere
-All files in the same directiroy including PLINK and PRSice
## PLINK
As a minor allele is used GWAS data



Rscript PRSice.R --prsice PRSice_win64.exe --base gwas_summary_stats.txt --target genotype_binary --binary-target T --pheno phenotype.txt --covariate covariates.txt --snp SNP --chr CHR --bp BP --a1 A1 --a2 A2 --stat BETA --pvalue P --out PRS_output
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

