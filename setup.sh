#!/bin/bash

set -e

# Function to display usage
usage() {
  echo "Usage: $0 [development|production]"
  echo "  development: Sets up the application for local development."
  echo "  production: Sets up the application for production deployment (requires domain and open ports 80/443)."
  exit 1
}

# Check for docker-compose dependency
if ! command -v docker-compose &> /dev/null
then
    echo "Error: docker-compose is not installed or not in your PATH."
    echo "Please install Docker Compose to run this script."
    echo "Refer to https://docs.docker.com/compose/install/ for installation instructions."
    exit 1
fi

# Check if an argument is provided
if [ -z "$1" ]; then
  usage
fi

ENV_TYPE=$1

echo "Setting up LinguaTrack for $ENV_TYPE environment..."

# Build and start services
echo "Building and starting Docker services..."
docker-compose up -d --build

# Wait for services to be healthy (optional, but good practice)
echo "Waiting for services to become healthy..."
sleep 10 # Give services some time to start



if [ "$ENV_TYPE" == "development" ]; then
  echo "
--- Development Setup Complete ---
"
  

  echo "
Application is running:
  Frontend: http://localhost
  Django Admin: http://localhost:8000/admin/
"
  echo "You can log in to the Django Admin with the superuser credentials you just created."
  echo "For frontend login, use the login form at http://localhost with any registered user."

elif [ "$ENV_TYPE" == "production" ]; then
  echo "
--- Production Setup Steps ---
"
  echo "Ensure your domain is pointing to this server and ports 80/443 are open."

  read -p "Enter your domain name (e.g., example.com): " DOMAIN
  read -p "Enter your email address for Certbot (e.g., your_email@example.com): " EMAIL

  echo "Acquiring Let's Encrypt SSL certificates..."
  docker-compose run --rm certbot certonly --webroot --webroot-path=/var/www/certbot --email "$EMAIL" --agree-tos --no-eff-email -d "$DOMAIN" -d "www.$DOMAIN"

  echo "Restarting Nginx proxy to use the new certificates..."
  docker-compose restart proxy

  echo "Collecting static files for Django..."
  docker-compose exec backend python manage.py collectstatic --noinput

  echo "
Production setup is largely complete. Please ensure all sensitive environment variables (e.g., SECRET_KEY, Twilio, OpenAI API keys) are set in your .env file or directly in your production environment.
"
else
  usage
fi

echo "Setup script finished."
