# PRS environment: R + PLINK 1.9/2.0 + PRSice-2
FROM rocker/r-base:4.3.2

ENV DEBIAN_FRONTEND=noninteractive

# Core tools/libs
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget curl unzip ca-certificates \
    libcurl4-openssl-dev libxml2-dev libssl-dev \
 && rm -rf /var/lib/apt/lists/*

# ---------- PLINK 2 (recommended) ----------
RUN set -eux; \
    curl -fL "https://s3.amazonaws.com/plink2-assets/plink2_linux_x86_64_latest.zip" \
      -o /tmp/plink2.zip; \
    unzip -q /tmp/plink2.zip -d /usr/local/bin/; \
    rm -f /tmp/plink2.zip; \
    chmod +x /usr/local/bin/plink2

# ---------- PLINK 1.9 (fallback; use dated asset) ----------
RUN set -eux; \
    ( \
      curl -fL "https://s3.amazonaws.com/plink1-assets/plink_linux_x86_64_20230116.zip" -o /tmp/plink1.zip \
      || curl -fL "https://s3.amazonaws.com/plink1-assets/plink_linux_x86_64_20221024.zip" -o /tmp/plink1.zip \
    ); \
    unzip -q /tmp/plink1.zip -d /usr/local/bin/; \
    rm -f /tmp/plink1.zip; \
    chmod +x /usr/local/bin/plink

# ---------- PRSice-2 (Linux) ----------
RUN set -eux; \
    curl -fL "https://github.com/choishingwan/PRSice/releases/latest/download/PRSice_linux.zip" \
      -o /tmp/PRSice_linux.zip; \
    unzip -q /tmp/PRSice_linux.zip -d /opt/PRSice; \
    ln -sf /opt/PRSice/PRSice.R     /usr/local/bin/PRSice.R; \
    ln -sf /opt/PRSice/PRSice_linux /usr/local/bin/PRSice_linux; \
    rm -f /tmp/PRSice_linux.zip; \
    chmod +x /usr/local/bin/PRSice_linux

# R packages commonly used by PRSice examples
RUN R -q -e "install.packages(c('data.table','magrittr','stringr'), repos='https://cloud.r-project.org')"

WORKDIR /work

# Show versions on container start (safe even if help returns nonzero)
CMD ["bash","-lc", "\
  echo 'PLINK 2:' && plink2 --version && echo && \
  echo 'PLINK 1.9:' && plink --version  || true && echo && \
  echo 'PRSice-2:' && /usr/local/bin/PRSice_linux --help | head -n 15 || true && echo && \
  echo 'R:' && Rscript --version && echo && Rscript -e 'sessionInfo()' \
"]
