
# download setup.sh script
curl -sL https://raw.githubusercontent.com/andreistefanciprian/profile-rest-api/master/cloud_aws/setup.sh?token=AGXEMXUHZ565DK4LT3YDYSS5GGPXK | sudo bash -

sudo sh ./deploy/update.sh

# create superuser
sudo env/bin/python manage.py createsuperuser