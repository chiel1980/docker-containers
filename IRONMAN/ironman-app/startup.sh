#!/bin/sh
cd /home/django/bol
sleep 1
su - django -c "cd /home/django/bol;python manage.py makemigrations controls --noinput"
su - django -c "cd /home/django/bol;python manage.py makemigrations blog --noinput"
su - django -c "cd /home/django/bol;python manage.py migrate --noinput"
su - django -c "cd /home/django/bol;python manage.py collectstatic --noinput"
#
### UWSGI
#
uwsgi --emperor /etc/uwsgi/vassals --uid django --gid django 
