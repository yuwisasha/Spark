# Spark is the dating app tinder analog

## Description
This project is developed on [Django Rest Framework](https://github.com/encode/django-rest-framework) with JWT auth using [simplejwt](https://github.com/jazzband/djangorestframework-simplejwt) 

## RUN
* Create containers for django and postgres ```docker-compose up --build```
* Apply migrations ```docker-compose run django python manage.py migrate```
* Create superuser (if you want) ```docker-compose run django python manage.py createsuperuser```
