# PRS environment: PLINK 1.9 + PRSice-2 (R base)
# Suitable for PRS pipelines (QC + PRS calculation)

FROM rocker/r-base:4.3.2

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget unzip ca-certificates libcurl4-openssl-dev libxml2-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# --- PLINK 1.9 (Linux x86_64) ---
RUN wget -qO /tmp/plink.zip http://s3.amazonaws.com/plink1-assets/plink_linux_x86_64.zip \
 && unzip /tmp/plink.zip -d /usr/local/bin/ \
 && rm -f /tmp/plink.zip

# --- PRSice-2 (Linux build + R script) ---
RUN wget -qO /tmp/PRSice_linux.zip https://github.com/choishingwan/PRSice/releases/latest/download/PRSice_linux.zip \
 && unzip /tmp/PRSice_linux.zip -d /opt/PRSice \
 && ln -s /opt/PRSice/PRSice.R /usr/local/bin/PRSice.R \
 && ln -s /opt/PRSice/PRSice_linux /usr/local/bin/PRSice_linux \
 && rm -f /tmp/PRSice_linux.zip

# --- R packages commonly used with PRSice examples ---
RUN R -q -e "install.packages(c('data.table','magrittr','stringr'), repos='https://cloud.r-project.org')"

# Working directory inside the container
WORKDIR /work

# Print tool versions by default (override with your own command)
CMD ["bash","-lc","echo 'PLINK:' && plink --version && echo && echo 'PRSice:' && /usr/local/bin/PRSice_linux --help | head -n 10 && echo && Rscript -e 'sessionInfo()'"]
