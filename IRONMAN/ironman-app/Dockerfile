FROM alpine:latest
MAINTAINER Michiel van Es <mve@pragmasec.nl>

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
    openldap-dev \ 
    uwsgi \
    uwsgi-python 

RUN rm -rf /var/cache/apk/*
RUN pip install Django celery whitenoise django-auth-ldap django-report-builder 

# create user and group that matches host UID and GID
RUN addgroup -g 1001 django
RUN adduser -h /home/django -s /bin/sh -u 1001 -G django -D django django
WORKDIR /home/django
RUN chown -R django /home/django
COPY startup.sh /root/startup.sh
ADD ironman /home/django/ironman/
RUN chmod +x /root/startup.sh
RUN chmod -R 775 /home/django
## UWSGI
RUN mkdir -p /etc/uwsgi/vassals/ /var/log/uwsgi/
ADD ironman_uwsgi.ini /etc/uwsgi/vassals/ 
RUN chown -R django.django /etc/uwsgi/vassals/ /var/log/uwsgi/
#
# EXPOSE our PORTS
EXPOSE 3031 

ENTRYPOINT ["/root/startup.sh"]
