

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


### Docker (optional, recommended for reproducibility)

You can use the provided Docker environment instead of installing tools manually.

Dockerfile: ./Dockerfile

How to run: running_docker.md

(Follow running_docker.md for build/run commands.)


(See running_docker.md
 for full build/run examples.)
