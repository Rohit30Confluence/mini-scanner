# ============================================================================
# mini-scanner Dockerfile
# ============================================================================

FROM python:3.13-slim

LABEL org.opencontainers.image.title="mini-scanner"
LABEL org.opencontainers.image.description="A lightweight Python TCP port scanner"
LABEL org.opencontainers.image.licenses="MIT"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        gcc && \
    rm -rf /var/lib/apt/lists/*

# Copy dependency files
COPY pyproject.toml ./
COPY README.md ./

# Copy source
COPY mini_scanner ./mini_scanner

# Install package
RUN pip install --no-cache-dir --upgrade pip && \
    pip install .

# Default command
ENTRYPOINT ["python", "-m", "mini_scanner"]

CMD ["--help"]