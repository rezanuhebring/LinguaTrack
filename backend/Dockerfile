# Set the base image to Python
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y netcat-traditional postgresql-client
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Copy the project code
COPY . .

# Expose the port
EXPOSE 8000

# Set the entrypoint
ENTRYPOINT ["/entrypoint.sh"]