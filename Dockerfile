FROM python:3.9.0-slim

# Creates application directory
WORKDIR /app

# Installs poetry and pip
RUN pip install --upgrade pip && \
    pip install poetry

# Copy dependency definition to cache
COPY poetry.lock pyproject.toml README.md /app/

# Installs projects dependencies as a separate layer
RUN poetry export -f requirements.txt -o requirements.txt --dev && \
    pip uninstall --yes poetry && \
    pip install --require-hashes -r requirements.txt

# Copies and chowns for the userapp on a single layer
COPY . /app
