# PRS environment: PLINK 1.9 + PRSice-2 on R base
FROM rocker/r-base:4.3.2

# Avoid tzdata prompts, keep image small
ENV DEBIAN_FRONTEND=noninteractive

# Core system deps (add curl for resilient downloads)
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget curl unzip ca-certificates \
    libcurl4-openssl-dev libxml2-dev libssl-dev \
 && rm -rf /var/lib/apt/lists/*

# --- PLINK 1.9 (robust download with HTTPS + fallback) ---
RUN set -eux; \
    url1="https://plink1-assets.s3.amazonaws.com/plink_linux_x86_64.zip"; \
    url2="https://s3.amazonaws.com/plink1-assets/plink_linux_x86_64.zip"; \
    curl -fL "$url1" -o /tmp/plink.zip || curl -fL "$url2" -o /tmp/plink.zip; \
    unzip -q /tmp/plink.zip -d /usr/local/bin/; \
    rm -f /tmp/plink.zip; \
    chmod +x /usr/local/bin/plink

# --- PRSice-2 (Linux build + R script) ---
RUN set -eux; \
    curl -fL "https://github.com/choishingwan/PRSice/releases/latest/download/PRSice_linux.zip" \
      -o /tmp/PRSice_linux.zip; \
    unzip -q /tmp/PRSice_linux.zip -d /opt/PRSice; \
    ln -sf /opt/PRSice/PRSice.R /usr/local/bin/PRSice.R; \
    ln -sf /opt/PRSice/PRSice_linux /usr/local/bin/PRSice_linux; \
    rm -f /tmp/PRSice_linux.zip

# R packages commonly used by PRSice examples
RUN R -q -e "install.packages(c('data.table','magrittr','stringr'), repos='https://cloud.r-project.org')"

# Working directory
WORKDIR /work

# Default: show versions (you can override CMD at runtime)
CMD ["bash","-lc","echo 'PLINK:' && plink --version && echo && echo 'PRSice:' && /usr/local/bin/PRSice_linux --help | head -n 10 && echo && Rscript -e 'sessionInfo()'"]
