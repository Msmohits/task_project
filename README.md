# Task Project

## Overview
Task Project is a small-scale RESTful API application built using **Django** and **Django REST Framework (DRF)**. It provides a simple task management system with CRUD operations, task assignment, authentication, and filtering by status.

## Features
- **CRUD Operations:** Create, Read, Update, and Delete tasks.
- **User Authentication:** Token-based authentication.
- **Task Assignment:** Assign tasks to users.
- **Filtering:** Filter tasks by status ("pending", "completed").
- **Rate Limiting:** Implemented using Django’s built-in mechanisms or Redis.
- **AWS Simulation:** Simulated AWS Lambda function that logs notifications when a task is marked as completed.
- **Database:** PostgreSQL (compatible with AWS Aurora DB).

---

## Setup Instructions

### Prerequisites
1. Install Python 3.12
2. Install `pip` and `virtualenv`

### Installation
#### 1. Clone the Repository
```bash
git clone https://github.com/Msmohits/task_project.git
cd task_project
```

#### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Configure Environment Variables
Create a `.env` file in the project root and add:
```env
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://username:password@localhost:5432/task_db
```

#### 5. Apply Migrations
```bash
python manage.py migrate
```

#### 6. Create a Superuser (Admin)
```bash
python manage.py createsuperuser
```
Follow the prompts to set up the admin account.

#### 7. Start the Development Server
```bash
python manage.py runserver
```
Access the API at: `http://127.0.0.1:8000/`

---

## API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/token/` | Obtain a new access token |
| POST | `/api/token/refresh/` | Refresh the access token |

### Tasks
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tasks/` | List all tasks (filterable by status) |
| POST | `/api/tasks/` | Create a new task |
| GET | `/api/tasks/{id}/` | Retrieve task details |
| PUT | `/api/tasks/{id}/` | Update task details |
| DELETE | `/api/tasks/{id}/` | Delete a task |

### Rate-Limited API
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/limited/` | Example rate-limited API endpoint |

---

## AWS Lambda Simulation
A simple script simulates an AWS Lambda function to log a notification when a task is marked as completed.
```python
import logging

def simulate_lambda_notification(task_id):
    logging.info(f"Task {task_id} marked as completed. Simulating AWS Lambda notification.")
```

---

## Running Tests
Run the test suite using:
```bash
python manage.py test
```

---

## Documentation
Swagger and ReDoc are integrated for API documentation:
- Swagger UI: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- ReDoc: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

---

## Design Choices
- **Django REST Framework (DRF):** Used for building a scalable and modular REST API.
- **Token-Based Authentication:** Ensures secure access to protected endpoints.
- **Rate Limiting:** Protects API from excessive usage.
- **AWS Lambda Simulation:** Mimics real-world cloud integrations.

---

## Contributors
- **Mohit Sharma** (Backend Developer)

---

## License
This project is licensed under the MIT License.

