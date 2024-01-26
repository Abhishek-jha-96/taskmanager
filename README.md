#DRF Project Task manager

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Run the Project](#run-the-project)
- [API Documentation](#api-documentation)

## Requirements
  Make sure you have the following installed:

- Python (>=3.x)
- venv (optional, but recommended for virtual environment management)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-project.git

Navigate to the project directory:
```
cd task
```
Install django, django restframework, drf-spectacular.

## Database Setup
Apply migrations:
```
python manage.py migrate
```
Create a superuser (optional):
```
python manage.py createsuperuser
```
## Run the Project
Run the development server:
```
python manage.py runserver
```
The project will be accessible at http://127.0.0.1:8000/.

## API Documentation
API documentation is generated using drf-spectacular. Visit the following URL for API documentation:

http://127.0.0.1:8000/swagger/
or

http://127.0.0.1:8000/redoc/
