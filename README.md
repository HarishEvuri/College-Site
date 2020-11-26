# College-Site
Django Project for College Management System

## Installation

Python and Django need to be installed

```bash
pip install -r requirements.txt
```

## Usage

Get a local copy of the project directory by cloning "College-site" from github.

Then follow these steps:
1. create the database by typing in mysql command line `create database Collegesite`
2. Provide the required information to the `DATABASES` dictionary by editing `/sample/settings.py`
3. Create the tables with the django command line `python manage.py makemigrations` then `python manage.py migrate`
4. Finally, run the django server `python manage.py runserver` and then go to the browser and enter the url **http://127.0.0.1:8000/**.

## Built With

* [Python 3](https://www.python.org/downloads/) - Programming language
* [Django](https://www.djangoproject.com/) - Web framework 
* [MySQL](https://www.mysql.com/) - Database

## Login

The login page is common for students and teachers.

You can access the django admin page at **http://127.0.0.1:8000/admin** .

A new admin user can be created using

```bash
python manage.py createsuperuser
```

## Users

New students and teachers can be added through the admin page. A new user needs to be created for each. 

The admin page is used to modify all tables such as Students, Teachers, Departments, Courses, Classes etc.

[comment]: <> (**For more details regarding the system and features please refer the reports included.**)
