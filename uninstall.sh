#!/bin/bash

set -e

echo "Stopping and removing all Docker containers, networks, and volumes..."
docker-compose down --volumes --remove-orphans

echo "Cleaning up generated files..."
# Remove Certbot configuration and data
rm -rf ./certbot/conf
rm -rf ./certbot/www

# Remove Django static files and media files (if they are outside volumes)
# Note: If media_volume is a named volume, it's removed by docker-compose down --volumes
# If you have local static files that were collected, you might want to remove them here
# rm -rf ./backend/staticfiles

echo "Uninstall script finished."
