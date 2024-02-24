# MyCampus-backend

## Description

This is the backend for the MyCampus project. It is a RESTful API that provides endpoints for the frontend to interact with the database. The Backend is built using Django and Django Rest Framework.

## Installation

1. Clone the repository
2. Install the required packages using the following command:

```bash
pip install -r requirements.txt
```

3. Set up an environment variable for the secret key and the database credentials. The environment variables are as follows

```bash
    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=your_db_host
    DB_PORT=your_db_port
```

4. Run The following command to start the server

```bash
python manage.py runserver
```

5. The server will start at <http://127.00.1:8000>
6. To migrate the database run the following command

```bash
python manage.py makemigrations
python manage.py migrate
```

## Usage

The API provides the following endpoints:

### User Endpoints

1. **POST /api/v2/users/** - This endpoint is used to create a new user and to get the details of the user.
2. **POST /api/v1/auth/jwt/create** - This endpoint is used to login a user.
3. **POST /api/v1/auth/jwt/refresh** - This endpoint is used to refresh the JWT token.
4. **POST /api/v1/auth/jwt/verify** - This endpoint is used to verify the JWT token.
5. **PUT /api/v2/users/me** - This endpoint is used to update the details of the user.
6. **GET /api/v2/users/me** - This endpoint is used to get the details of the user.
7. **GET /api/v2/users/** - This endpoint is used to get the details of all the users.
8. **GET /api/v2/users/{id}** - This endpoint is used to get the details of a specific user.
9. **PATCH /api/v2/users/me** - This endpoint is used to update the details of the user.
