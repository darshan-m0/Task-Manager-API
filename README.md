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

## Project Structure
task_manager/
├── task_manager/ # Main project settings
│ ├── settings.py # Project configuration
│ ├── urls.py # URL routing
│ └── wsgi.py # WSGI config
├── tasks/ # Main application
│ ├── models.py # Database models
│ ├── views.py # API views
│ ├── serializers.py # Data serializers
│ ├── permissions.py # Custom permissions
│ ├── urls.py # App URLs
│ ├── admin.py # Django admin
│ └── tests.py # Unit tests
├── manage.py # Django management script
├── requirements.txt # Python dependencies
└── README.md # This file

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

