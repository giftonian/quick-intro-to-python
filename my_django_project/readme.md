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
    
        ```
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': config('DB_NAME'),
                'USER': config('DB_USER'),
                'PASSWORD': config('DB_PASSWORD'),
                'HOST': config('DB_HOST', default='localhost'),
                'PORT': config('DB_PORT', default='3306'),
                'OPTIONS': {
                    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                    'charset': 'utf8mb4',
                },
            }
        }
        ```

- Test the DB Connection
    - python manage.py check

- Run the Migration 
    - python manage.py migrate

- Create SuperUser (Recommended)
    - python manage.py createsuperuser

# Python/Django Notes
## Django Code Important Files
- **URLs:** While it is possible to process requests from every single URL via a single function, it is much more maintainable to write a separate view function to handle each resource. A URL mapper is used to redirect HTTP requests to the appropriate view based on the request URL. The URL mapper can also match particular patterns of strings or digits that appear in a URL and pass these to a view function as data.
- **View:** A view is (heart of the web application) a request handler function, which receives HTTP requests and returns HTTP responses. Views access the data needed to satisfy requests via models, and delegate the formatting of the response to templates.
- **Models:** Models are Python objects that define the structure of an application's data, and provide mechanisms to manage (add, modify, delete) and query records in the database.
- **Templates:** A template is a text file defining the structure or layout of a file (such as an HTML page), with placeholders used to represent actual content. A view can dynamically create an HTML page using an HTML template, populating it with data from a model. A template can be used to define the structure of any type of file; it doesn't have to be HTML!

## Defining data models (models.py)
- Models define the structure of stored data, including the field types and possibly also their maximum size, default values, selection list options, help text for documentation, label text for forms, etc. 
- The definition of the model is **independent** of the underlying database — you can choose one of several as part of your project settings.
    ```
    # filename: models.py

    from django.db import models

    class Team(models.Model):
        team_name = models.CharField(max_length=40)

        TEAM_LEVELS = (
            ('U09', 'Under 09s'),
            ('U10', 'Under 10s'),
            ('U11', 'Under 11s'),
            # …
            # list other team levels
        )
        team_level = models.CharField(max_length=3, choices=TEAM_LEVELS, default='U11')
    ```

## Querying data (views.py)
- The Django model provides a simple query API for searching the associated database. 
- This can match against a number of fields at a time using different criteria (e.g., exact, case-insensitive, greater than, etc.), and can support complex statements (for example, you can specify a search on U11 teams that have a team name that starts with "Fr" or ends with "al").
- Following code snippet shows a view function (resource handler) for displaying all of our U09 teams. 
- The list_teams = Team.objects.filter(team_level__exact="U09") line shows how we can use the model query API to filter for all records where the team_level field has exactly the text U09 (note how this criteria is passed to the filter() function as an argument, with the field name and match type separated by a double underscore: team_level__exact).
    ```
    ## filename: views.py

    from django.shortcuts import render
    from .models import Team

    def index(request):
        list_teams = Team.objects.filter(team_level__exact="U09")
        context = {'youngest_teams': list_teams}
        return render(request, '/best/index.html', context)
    ```

- This function uses the render() function to create the HttpResponse that is sent back to the browser. This function is a shortcut; it creates an HTML file by combining a specified HTML template and some data to insert in the template (provided in the variable named context).

## Rendering data (HTML templates)
- Template systems allow you to specify the structure of an output document, using placeholders for data that will be filled in when a page is generated.
- Following template has been written under the assumption that it will have access to a list variable called youngest_teams when it is rendered (this is contained in the context variable inside the render() function above). 
    ```
    ## filename: best/templates/best/index.html

    <!doctype html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <title>Home page</title>
    </head>
    <body>
    {% if youngest_teams %}
        <ul>
        {% for team in youngest_teams %}
            <li>{{ team.team_name }}</li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No teams are available.</p>
    {% endif %}
    </body>
    </html>
    ```
## Django Project Files
- **__init__.py** is an empty file that instructs Python to treat this directory as a Python package.
settings.py contains all the website settings, including registering any applications we create, the location of our static files, database configuration details, etc.

- **urls.py** defines the site URL-to-view mappings. While this could contain all the URL mapping code, it is more common to delegate some of the mappings to particular applications, as you'll see later.
- **wsgi.py** is used to help your Django application communicate with the web server. You can treat this as boilerplate.

- **asgi.py** is a standard for Python asynchronous web apps and servers to communicate with each other. 

- **manage.py** script is used to create applications, work with databases, and start the development web server.

# Resources
1. https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django
2. https://github.com/mdn/django-locallibrary-tutorial
