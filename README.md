# LinguaTrack - Translation and Editing Management App

This application is designed to manage translation and editing projects, from order placement to final delivery and invoicing.

## Project Structure

- `backend/`: Django REST Framework application handling the API and business logic.
- `frontend/`: React.js application for the user interface.
- `proxy/`: Nginx reverse proxy to route traffic to the backend and frontend.
- `docker-compose.yml`: Orchestrates all the services.

## Getting Started

1.  **Build the images:**
    ```bash
    docker-compose build
    ```
2.  **Run the services:**
    ```bash
    docker-compose up -d
    ```
3.  **Apply database migrations (first time only):**
    ```bash
    docker-compose exec backend python manage.py migrate
    ```

The application should then be available at `http://localhost`.
