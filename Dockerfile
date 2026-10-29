
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Keep the existing application startup files.
COPY app/ .

# Include the package structure required by the tests.
COPY app/ ./app/
COPY tests/ ./tests/

EXPOSE 5000

CMD ["python", "docker_server.py"]
