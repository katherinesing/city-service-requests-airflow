# Dockerfile
# Use the same version as in your original docker-compose.yaml file
FROM apache/airflow:3.1.5

# Switch to root user temporarily to perform system-level installs if needed (e.g., apt packages)
# USER root
# RUN apt-get update && apt-get install -y --no-install-recommends ...

# Switch back to the 'airflow' user to install Python packages
USER airflow

# Copy your requirements file into the container
COPY requirements.txt /requirements.txt

# Install the dependencies from the copied file
RUN pip install --no-cache-dir -r /requirements.txt