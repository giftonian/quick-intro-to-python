# Django Installation using Virtual Environment
## Create project folder
- mkdir my_django_project
- cd my_django_project

## On Mac/Linux
- python3 -m venv venv

## On Mac/Linux
- source venv/bin/activate

## Install latest version
- pip install django

## Verify Installation
- python -m django --version
- Output: 5.0.0 (or your installed version)

## Create Django Project
- django-admin startproject myproject .
- The dot (.) creates project in current directory

## Run Development Server
- python manage.py runserver

## After installing packages
- pip freeze > requirements.txt

## Installing from requirements
- pip install -r requirements.txt

## Check which Python is being used

- Mac/Linux
- which python

## Install additional packages
- pip install djangorestframework
- pip install pillow
- pip install python-decouple

## Update requirements.txt
- pip freeze > requirements.txt

## .gitignore for Django Project

- #Virtual Environment
    - venv/
    - env/
    - ENV/

- #Python
    - *.pyc
    - __pycache__/
    - *.py[cod]

- #Django
    - *.log
    - db.sqlite3
    - media/
    - staticfiles/

- #IDE
    - .vscode/
    - .idea/
    - *.swp

- #Environment variables
    - .env


## Setting up with MySQL DB using .env

- In your project root (same level as manage.py), create a .env file with following contents:

    - #Database Configuration
    - DB_NAME=your_database_name
    - DB_USER=your_mysql_username
    - DB_PASSWORD=your_mysql_password
    - DB_HOST=localhost
    - DB_PORT=3306

    - #Django Secret Key
    - SECRET_KEY=your-secret-key-here

    - #Debug Mode
    - DEBUG=True
    - #Allowed Hosts
    - ALLOWED_HOSTS=localhost,127.0.0.1

- Install MySQL Client
    - #Activate your virtual environment first
    - #Then install MySQL client
    - pip install mysqlclient

    - #If mysqlclient fails (common on Windows), use:
    - pip install pymysql

    - If using **PyMySQL**, add this to myproject/__init__.py:
        - import pymysql
        - pymysql.install_as_MySQLdb()

- Open myproject/settings.py and modify:
    - from decouple import config
    - SECRET_KEY = config('SECRET_KEY')
    - DEBUG = config('DEBUG', default=False, cast=bool)
    - DATABASES = {
        - 'default': {
            - 'ENGINE': 'django.db.backends.mysql',
            - 'NAME': config('DB_NAME'),
            - 'USER': config('DB_USER'),
            - 'PASSWORD': config('DB_PASSWORD'),
            - 'HOST': config('DB_HOST', default='localhost'),
            - 'PORT': config('DB_PORT', default='3306'),
            - 'OPTIONS': {
                - 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                - 'charset': 'utf8mb4',
            - },
        - }
    - }

- Test the DB Connection
    - python manage.py check

- Run the Migration 
    - python manage.py migrate

- Create SuperUser (Recommended)
    - python manage.py createsuperuser


# Resources
1. https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django
