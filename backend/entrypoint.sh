#!/bin/sh

# Wait for the PostgreSQL server to be ready
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "db" -U "$POSTGRES_USER" -d "postgres" -c "\q"; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - continuing"

# Create the database if it doesn't exist
PGPASSWORD=$POSTGRES_PASSWORD psql -h "db" -U "$POSTGRES_USER" -d "postgres" -c "CREATE DATABASE \"$POSTGRES_DB\";" || true

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Create superuser
echo "Creating superuser..."
python create_superuser.py

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start the server
echo "Starting server..."
gunicorn backend.wsgi:application --bind 0.0.0.0:8000
