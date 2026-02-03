FROM python:3.12-slim

# Prevent python from writing pyc files & enable logs instantly
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies only if needed (remove if not required)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip first for faster installs
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy project
COPY bot/ bot/

# Run as non-root (better security)
RUN useradd -m botuser
USER botuser

CMD ["python", "-m", "bot.main"]
