# Spark is the dating app tinder analog

## Description
This project is developed on [Django](https://github.com/django/django) [Django Rest Framework](https://github.com/encode/django-rest-framework) with JWT auth using [simplejwt](https://github.com/jazzband/djangorestframework-simplejwt) 

## RUN
* Create and run containers for django and postgres ```docker-compose up --build```

*From 2nd terminal*

* Apply migrations ```docker-compose run django python manage.py migrate```
* Create superuser (if you want) ```docker-compose run django python manage.py createsuperuser```

## Authentication
You should create a user and then send a POST query to ```api/auth/token```
to get **access token**, and put that token into header **Authorization**, for example via *httpie*: ```http http://127.0.0.1:8000/api/v1/users/create_profile "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2MjA4Mjk1LCJqdGkiOiI4NGNhZmMzMmFiZDA0MDQ2YjZhMzFhZjJjMmRiNjUyYyIsInVzZXJfaWQiOjJ9.NJrs-sXnghAwcMsIWyCvE2RuGcQ3Hiu5p3vBmLkHSvM"``` 

## Structure
|Endpoint|HTTP Method|Result|Is authenticaded|
| ------ | --------- | ---- | --- |
|```api/v1/users/create_user```|POST|New user|:x:|
|```api/v1/users/create_profile```|POST|Create profile for user|:heavy_check_mark:|
|```api/v1/users/user_list```|GET|Get all users|:x:|
|```api/v1/users/profile_list```|GET|Get all profiles|:x:|
|```api/v1/users/interest_list```|GET|Get all interests|:x:|
|```api/v1/chat/swipe```|POST|Swipe person|:x:|
|```api/v1/chat/chat/:id```|POST|Get all messages from user chat|:heavy_check_mark:|



