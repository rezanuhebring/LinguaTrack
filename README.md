# LinguaTrack - Translation and Editing Management App

This application is designed to manage translation and editing projects, from order placement to final delivery and invoicing.

## Project Structure

- `backend/`: Django REST Framework application handling the API and business logic.
- `frontend/`: React.js application for the user interface.
- `proxy/`: Nginx reverse proxy to route traffic to the backend and frontend.
- `docker-compose.yml`: Orchestrates all the services.

## Getting Started

1.  **Build and Run the services:**
    To build the images and start all services in detached mode, run:
    ```bash
    docker-compose up -d --build
    ```
    This command will also apply database migrations automatically on the backend service startup.

2.  **Creating an Admin User:**
    To create a superuser (admin user) for the Django backend, use the provided script. You can set custom credentials using environment variables, or use the defaults (`admin`/`adminpassword`).

    **Using default credentials:**
    ```bash
    docker-compose exec backend python create_superuser.py
    ```

    **Using custom credentials:**
    ```bash
    docker-compose exec -e DJANGO_SUPERUSER_USERNAME=myadmin -e DJANGO_SUPERUSER_EMAIL=admin@example.com -e DJANGO_SUPERUSER_PASSWORD=mypassword backend python create_superuser.py
    ```

## Accessing the Application

-   **Frontend:** The application should be available at `http://localhost`.
-   **Django Admin Panel:** Access the admin panel at `http://localhost:8000/admin/` using the superuser credentials you created.

## Authentication Endpoints

The backend now includes JWT authentication endpoints:
-   `http://localhost:8000/api/token/`: Obtain JWT tokens (access and refresh) by sending `username` and `password`.
-   `http://localhost:8000/api/token/refresh/`: Refresh an expired access token using a refresh token.
-   `http://localhost:8000/api/register/`: Register a new user (requires `username`, `email`, `password`, and `role`).