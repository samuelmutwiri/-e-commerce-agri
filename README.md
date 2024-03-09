# -e-commerce-agri
 An app to manage agricultural logistics

# Creating venv, installing django, and starting the project...  
1. First things first-Make sure Python 3.8.7 or above is installed.  
Windows
```html
    python --version
```
Linux and Mac/OSX
```html
    python3 --version
```
If not installed, find it at [Python 3.8.7](https://www.python.org/downloads/release/python-387/)

2. Install pipenv  
Windows
```html
    pip install venv
```
Linux and Mac/OSX
```html
    pip3 install pipenv
```
3. Activate pipenv and install django  
All platforms
```html
    pipenv install django
    pipenv shell
```
4. create project (agri)  
All platforms
```html
    django-admin startproject agri .
```
Windows
```html
    python manage.py runserver
```
Linux and Mac/OSX
```html
    python3 manage.py runserver
```