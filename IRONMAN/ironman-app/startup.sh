#!/bin/sh
cd /home/django/ironman
sleep 1
su - django -c "cd /home/django/ironman;python manage.py makemigrations controls --noinput"
su - django -c "cd /home/django/ironman;python manage.py makemigrations blog --noinput"
su - django -c "cd /home/django/ironman;python manage.py migrate --noinput"
su - django -c "cd /home/django/ironman;python manage.py collectstatic --noinput"
#
### UWSGI
#
uwsgi --emperor /etc/uwsgi/vassals --uid django --gid django 
