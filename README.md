# Description

This is my personal website

## Installation

first you must install [Django](https://docs.djangoproject.com/en/3.1/topics/install/#how-to-install-django) after that open the folder

note: If you use windows, type `python` instead of `python3`

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



## Libraries
* [tinymce](https://www.tiny.cloud/)
* [Font Awesome 4](#)

## License
[MIT](https://choosealicense.com/licenses/mit/)
