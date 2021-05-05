# Description

This is my personal website

# Features

## Portfolio page
- [x] Name
- [X] Social Media
- [x] Skills
- [x] Projects

## Blog
- [x] Articles
- [x] Tags
- [x] Categories
- [x] Article created and updated date

## Technical
- [X] Postgres

# Installation

## Django

note: If you use windows, type `python` instead of `python3`

first check your python version is  3.x 

check if `pip` is already installed on your pc 

```bash 
python3 -m pip --version
```
if you haven't [check this](https://pip.pypa.io/en/stable/installing/)

then install Django

```bash
python -m pip install Django
```

## Postgres

Check [this](https://djangocentral.com/using-postgresql-with-django/)
## Project

After all that let's set up the project! Open the terminal with the path of the folder where you have the project.

```bash
python3 manage.py migrate
```

```bash
python3 manage.py makemigrations
```

```bash
python manage.py migrate --run-syncdb
```

```bash
python3 manage.py runserver
```

if you want to create a super user:

```bash
python3 manage.py createsuperuser
```

add `username`, `email` and `passwrod`.

after run

```bash
python3 manage.py runserver
```

Open your browser at this link `localhost:8000/admin` and add `informations`,`tags`, `categories`, `articles`, `projects` and `skills`.

Finally, go to the home page `localhost:8000` and done!



# Libraries
* [tinymce](https://www.tiny.cloud/)
* [Font Awesome 4](#)

# License
[MIT](https://choosealicense.com/licenses/mit/)
