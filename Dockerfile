# Use an official Python runtime as a base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application source code to the container
COPY . /app

# Install system-level dependencies (e.g., for PostgreSQL)
RUN apt-get update && apt-get install -y gcc libpq-dev

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on (default Django port)
EXPOSE 8000

# Set environment variables to prevent Python from buffering logs
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Run migrations and start the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]