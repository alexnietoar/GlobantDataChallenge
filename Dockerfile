# Base image
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code to the container
COPY . .

# Expose the necessary port
EXPOSE 5000

# Start the API server
CMD ["python", "src/api/api.py"]