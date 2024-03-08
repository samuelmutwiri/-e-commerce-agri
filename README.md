# -e-commerce-agri
 An app to manage agricultural logistics

# Creating venv, installing django, and starting the project!!!
1. First things first-Make sure Python 3.8.7 or above is installed
-Windows
> python --version
-linux and Mac/OSX
> python3 --version
if not installed, find it at [Link Python 3.8.7](https://www.python.org/downloads/release/python-387/)

2. Install pipenv
windows
```html
    pip install venv
```
linux and Mac/OSX
```html
    pip3 install pipenv
```
3. Activate pipenv and install django
all platforms
```html
    pipenv install django
    pipenv shell
```
4. create project (agri) (all platforms)
```html
    django-admin startproject agri .
```
Windows
```html
    python manage.py runserver
```
linux and Mac/OSX
```html
    python3 manage.py runserver
```