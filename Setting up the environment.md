

## Setting up the environment

### 1. Download PLINK


PLINK 2.0 (recommended):
🔗 https://www.cog-genomics.org/plink/2.0/

Steps:

Download the .zip file for Windows.

Extract it to a local folder, e.g. C:\Users\<username>\plink\.

(Optional) Add that folder to your system PATH environment variable,
or run PLINK directly from the folder (e.g. .\plink2.exe in PowerShell).

Example test:

```
.\plink2.exe --version
```

### 2. Download PRSice-2

Download the PRSice-2 Windows package (PRSice_win64.zip).
🔗[ https://www.prsice.info/
](https://github.com/choishingwan/PRSice?tab=readme-ov-file)


Extract all files to a working directory (e.g. C:\Users\<username>\PRSice\).

Make sure you have R installed and added to PATH:
🔗 https://cran.r-project.org/

Test that PRSice runs:

```
Rscript PRSice.R --help
```

### PRSice Usage Workflow

Run the Rscript command from your terminal.

Rscript executes the PRSice.R script.

The PRSice.R script calls the PRSice_win64.exe binary to speed up processing.

When genetic data files (.bed, .bim, .fam) need to be loaded, PRSice uses PLINK.

All results are combined to generate the Polygenic Risk Score (PRS) for each individual.

Note: For easier file handling, place all tools and data in the same folder.


### Docker (optional, recommended for reproducibility)

You can use the provided Docker environment instead of installing tools manually.

Dockerfile: [./Dockerfile](./Dockerfile)  
How to run: [./running_docker.md](./running_docker.md)

