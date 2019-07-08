## Create and manage project environment

```bash
# Create virtualenv
virtualenv -p /usr/bin/python3 profiles-rest-api

# Activate virtualenv
source profiles-rest-api/bin/activate

# Deactivate environment
deactivate

```

## Install requirements

```bash
pip install -r requirmeents.txt
```


## Start django app

```bash
python manage.py runserver 0.0.0.0:8000
```

## Create django project&app

```bash
# Create django project
django-admin.py startproject profiles_project .
# Create django app
python manage.py startapp profiles_api

```

## Create and run migrations
```bash
python manage.py makemigrations profiles_api
python manage.py migrate
```

## Create usperuser
```bash
python manage.py createsuperuser
```