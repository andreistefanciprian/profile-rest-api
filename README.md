# How to deploy this project in GCP
```bash
# deploy this project in GCP (make sure ssh pub key present on GCP machine root user is also added to github)
curl -sL https://raw.githubusercontent.com/andreistefanciprian/profile-rest-api/master/cloud_aws/setup.sh?token=AGXEMXUHZ565DK4LT3YDYSS5GGPXK | sudo bash -

# Later updates if code changed after app install
sudo sh ./deploy/update.sh

# create superuser
sudo env/bin/python manage.py createsuperuser
```

# Ignore steps below as they are covered by deploy scripts
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

# After adding new model to profiles_api app
python manage.py makemigrations
python manage.py migrate
```

## Create usperuser
```bash
python manage.py createsuperuser
```

