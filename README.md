# Create and manage project environment

```bash
# Create virtualenv
virtualenv -p /usr/bin/python3 profiles-rest-api

# Activate virtualenv
source profiles-rest-api/bin/activate

# Deactivate environment
deactivate

```

# Install requirements

```bash
pip install -r requirmeents.txt
```

# Create django project&app
```bash
# Create django project
django-admin.py startproject profiles_project .
# Create django app
python manage.py startapp profiles_api

```