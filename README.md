##  Task Management System API
    A REST API built with Django, Django REST Framework (DRF), and JWT authentication for managing tasks.
    Supports CRUD operations.

 ## User Authentication (JWT-based)
 ## CRUD Operations (Create, Retrieve, Update, Delete) for tasks


## Create & Activate Virtual Environment.
    python -m venv venv
    source venv/bin/activate  

## Install Dependencies
    pip install -r requirements.txt

## Apply Migrations.
    python manage.py migrate


## Run the Development Server.
    python manage.py runserver

## Authentication.
    1. The API uses JWT (JSON Web Token) authentication.
    2. Before making any task-related requests, obtain an access token via login.

## Register a New User.
    http://127.0.0.1:8000/api/auth/register/

    1. Request Body (JSON):

        {

        "username": "john_doe",
        "password": "securepassword"

        }
    Response:

        {
        "message": "User created successfully"
        }



## Get JWT Token.
    http://127.0.0.1:8000/api/auth/login/

    Request Body (JSON):
        {
        "username": "sushant",
        "password": "securepassword"
        }


    Response:

        {
        "refresh": "our_refresh_token",
        "access": "our_access_token"
        }

## Create a Task.
    POST http://127.0.0.1:8000/api/tasks/

    Request Body:

        {
        "title": "Complete Django Project",
        "description": "Finish the Django API development",
     
        }

    Response:

        {
        "id": 1,
        "title": "Complete Django Project",
        "description": "Finish the Django API development",
        
        }



## Update a Task (PUT).
    PUT http://127.0.0.1:8000/api/auth/tasks/1/


    Request:

        {
            "title": "Updated Django Project",
            "description": "Modify API implementation",
            "status": "completed",
           
        }

    Response:
        {
            "id": 1,
            "title": "Updated Django Project",
            "description": "Modify API implementation",
            "status": "completed",
            "user": 1
        }

## Delete a Task (DELETE).
    DELETE http://127.0.0.1:8000/api/auth/tasks/1/


    Response:

        {
            "message": "Task deleted successfully"
        }






## Tech Stack
1. Backend: Django, Django REST Framework (DRF)
2. Authentication: JWT (SimpleJWT)
3. Database: PostgreSQL 
4. API Testing: Postman




## Sushant jha.







