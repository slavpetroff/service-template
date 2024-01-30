# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY pyproject.toml poetry.lock ./

# Install Poetry
RUN pip install poetry

# Disable virtualenv creation to make sure everything is installed in the OS Python
ENV POETRY_VIRTUALENVS_CREATE=false

ENV ENVIRONMENT=production

# Install project dependencies
RUN poetry install --no-root --no-dev

# Copy the rest of the application code to the working directory
COPY . .

# Command to run the application with Uvicorn
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
