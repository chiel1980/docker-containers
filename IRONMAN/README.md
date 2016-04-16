# IRONMAN
Ironman is a simple, pragmatic and secure Django tool that allows risk/compliance/security/audit professionals to easily create and administrate controls and risk assessments and automate as much as possible

# What does it deliver

* easy tool for administering controls, risk assessments 
* a report tool (django-report-builder)
* a dashboard (wip) using AdminLTE for quick and clear overview of controls that have failed

# Docker containers for Ironman
Ironman is set up to use docker containers for security and easy deployment.
You can also just grab the config and use the config in a VM if you want.

# Dependencies
please be aware that you need:

* kernel 3.10 for docker
* docker 1.x preferably 1.10 or up for security reasons
* docker-compose for easy build and starting the containers
* a docker volume mounted /webapp:/webapp for storage of the db.sqlite3 DB (for persistency of your data)
* Atlassian JIRA for creation of tickets and evidence
* jirash or something similar for talking to the JIRA API

# Sources of information
* Docker: https://www.django.com
* Django: https://www.djangoproject.com
* AdminLTE: https://almsaeedstudio.com/preview
* Atlassian JIRA: https://www.atlassian.com/software/jira
* jirash: https://github.com/trentm/jirash

# Todo
* add dashboard to repo
* make it an app only setup instead of also including rainloop webmail for personal use ;)
