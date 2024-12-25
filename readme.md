# Project Management API

A project management tool API built with Django and Django REST Framework, enabling teams to collaborate on projects, tasks, and comments.

---

## **Features**
- User management (registration, login, CRUD operations)
- Project management (CRUD operations)
- Task management (CRUD with project-specific tasks)
- Comment management (CRUD for task-specific comments)
- JWT-based authentication
- API documentation with Swagger

---

## **Setup Instructions**

### **1. Clone the Repository**
Clone the project from the repository to your local machine:
```bash
git clone https://github.com/mahinhasan/project_management.git
cd project_management


# Create a virtual environment
python -m venv venv

# Activate the virtual environment (Linux/Mac)
source venv/bin/activate

# Activate the virtual environment (Windows)
venv\Scripts\activate
pip install -r requirements.txt
