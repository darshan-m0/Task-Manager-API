# Task-Manager-API

A Django REST Framework based Task Manager with JWT authentication and Role-Based Access Control (RBAC).

## Features

- ✅ User Registration & Login with JWT
- ✅ Task CRUD Operations (Create, Read, Update, Delete)
- ✅ Role-Based Access Control (Admin/User)
- ✅ Admin can view/manage all tasks
- ✅ Users can only view/manage their own tasks
- ✅ Mark tasks as complete/incomplete
- ✅ SQLite Database
- ✅ API Documentation via Django REST Framework

## Tech Stack

- Python 3.9+
- Django 4.x
- Django REST Framework
- Simple JWT for authentication
- SQLite (default Django database)

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/darshan-m0/Task-Manager-API
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create Superusers
```bash
cd config++
python manage.py createsuperuser
```

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Admin Groups & Test Users using Script
```bash
python manage.py setup_roles
```

### 7. Run The Server
```bash
python manage.py runserver
```

Server runs at: http://localhost:8000/

## 🔗 API Endpoints

### 🔐 **Authentication**

| Method | Endpoint | Description | Status |
|--------|----------|-------------|--------|
| `POST` | `/api/auth/register/` | Register new user | ![Public](https://img.shields.io/badge/access-public-green) |
| `POST` | `/api/auth/login/` | Login & get JWT tokens | ![Public](https://img.shields.io/badge/access-public-green) |
| `POST` | `/api/auth/refresh/` | Refresh access token | ![Public](https://img.shields.io/badge/access-public-green) |

### 📋 **Tasks**

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/tasks/` | List tasks (role-aware) | 🔒 |
| `POST` | `/api/tasks/` | Create new task | 🔒 |
| `GET` | `/api/tasks/{id}/` | Get task details | 🔒 |
| `PUT` | `/api/tasks/{id}/` | Update task | 🔒 |
| `PATCH` | `/api/tasks/{id}/` | Partial update | 🔒 |
| `DELETE` | `/api/tasks/{id}/` | Delete task | 🔒 |
| `POST` | `/api/tasks/{id}/toggle_status/` | Toggle complete/incomplete | 🔒 |

**Legend:** 
- 🔒 = Requires JWT Token
- Admin: Can access all tasks
- User: Can only access own tasks

## 🔐 Authentication Endpoints

### 1. Register User
```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "john", "password": "john123", "password2": "john123", "email": "john@example.com"}'
```

### 2. Login (Get Tokens)
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "john", "password": "john123"}'
```

##### Response:
```bash
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
}
```

### 3. Refresh Token
```bash
curl -X POST http://localhost:8000/api/auth/refresh/ \
  -H "Content-Type: application/json" \
  -d '{"refresh": "your_refresh_token"}'
```

## 📝 Task Management (All Need Token)

### Header for all task requests:
```text
Authorization: Bearer <your_access_token>
Content-Type: application/json
```

### 1. Create Task
```bash
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"title": "My Task", "description": "Task details", "status": false}'
```

### 2. Get All Tasks
```bash
curl -X GET http://localhost:8000/api/tasks/ \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### 3. Get Specific Task
```bash
curl -X GET http://localhost:8000/api/tasks/1/ \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### 4. Update Task
```bash
curl -X PUT http://localhost:8000/api/tasks/1/ \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{"title": "Updated", "description": "New details", "status": true}'
```

### 6. Delete Task
```bash
curl -X DELETE http://localhost:8000/api/tasks/1/ \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### 7. Toggle Complete/Incomplete
```bash
curl -X POST http://localhost:8000/api/tasks/1/toggle_status/ \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{}'
```

## 👑 RBAC - Admin vs User

### Admin User:
```bash
# Login as admin (created by setup_roles)
curl -X POST http://localhost:8000/api/auth/login/ \
  -d '{"username": "admin", "password": "admin123"}'

# Admin sees ALL tasks from ALL users
curl -X GET http://localhost:8000/api/tasks/ \
  -H "Authorization: Bearer ADMIN_TOKEN"
```

### Regular User:
```bash
# Login as user
curl -X POST http://localhost:8000/api/auth/login/ \
  -d '{"username": "user", "password": "user123"}'

# User sees ONLY own tasks
curl -X GET http://localhost:8000/api/tasks/ \
  -H "Authorization: Bearer USER_TOKEN"
```

## ⚠️ Common Errors

### Error	Solution

401: Authentication credentials were not provided	------------> Add Authorization: Bearer <token> header

401: Given token not valid ------------>	Token expired. Login again

404: Not found ------------>	Task doesn't exist OR no permission

400: Bad Request ------------>	Check JSON format in request body

### 🐳 Docker

### dockerfile
```bash
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### For Testing Purpose, use predefined admin and users:
username:admin
password:111

username:test 
password:test123
```bash
# Run all tests
python manage.py test

# Run specific test file
python manage.py test tasks.tests

# Run with verbose output
python manage.py test --verbosity=2
```

