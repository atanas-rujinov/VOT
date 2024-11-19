# Dockerfile for the Python app

FROM python:3.10-slim

WORKDIR /app

# Install PostgreSQL client and dependencies
RUN apt-get update && apt-get install -y libpq-dev gcc

# Copy the Python script to the container
COPY app.py /app/

# Install Python dependencies
RUN pip install --no-cache-dir psycopg2

CMD ["python", "app.py"]
