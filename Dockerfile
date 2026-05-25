# Base image
# This container already has Python 3.12 installed
FROM python:3.12

# Sets working directory inside container
# All next commands run from /app
WORKDIR /app

# Copy only requirements file first
# Done separately for Docker build optimization/caching
COPY requirements.txt .

# Install Python dependencies inside container
RUN pip install -r requirements.txt

# Copy all project files into container
COPY . .

# Documentation purpose
# Tells container uses port 8000
EXPOSE 8000

# Default command when container starts
# Starts Flask app using Gunicorn
CMD ["gunicorn", "--workers", "2", "--bind", "0.0.0.0:8000", "app:app"]

