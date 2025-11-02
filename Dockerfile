FROM python:3.13.5-slim AS compile-image

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

RUN python -m venv /opt/venv

COPY requirements.txt .
RUN /opt/venv/bin/pip install --no-cache-dir --upgrade pip \
    && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

FROM python:3.13.5-slim

RUN apt-get update && apt-get install -y \
    libpq5 \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

COPY --from=compile-image /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app
COPY bot ./bot

CMD ["python", "-m", "bot"]