# Poll-App
A Simple Poll app that lists available polls, take votes, show results.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Polls app is personal project developed in python that create polls, takes votes, show results. This project is a rest framework extension of existing Django Project Tutorial - the Polls App.

## Prerequisites

Before using the Polls App, ensure you have the following prerequisites:

- Python 3.7 or above

## SETUP
**Initial Setup**

1. Install the required dependencies:

```
pip install -r requirements.txt
```
2. create project
```
django-admin startproject my_poll_site
```
3. create polls app
```
python manage.py startapp polls
``` 
4. Login to postgresql as super user
```
sudo -i -u postgres
```
5. create user and grant permissions
```
psql
Create user hsmgowtham with SUPERUSER;
ALTER USER hsmgowtham WITH PASSWORD 'hsmgowtham';
```
6. create table for the polls app and grant permissions
```
CREATE DATABASE poll_app
    WITH
    OWNER = hsmgowtham;
GRANT ALL ON DATABASE otoo_db TO hsmgowtham;
```
**Installed Apps to DB**

4. To create db tables for the installed apps
```
python manage.py migrate
```
5. create migration files for the polls app model changes
```
python manage.py makemigrations polls
```
## Extra Command line utilities
- to check what sql will get executed for models code
```
python manage.py sqlmigrate polls 0001
```
- to check for any problesm without making any migrations or touching the database
```
python manage.py check
```
- run migrate to create models in DB
```
python manage.py migrate
```
- to create python shell
```
python manage.py shell
```
## Create Django Admin User
```
python manage.py createsuperuser
```
## Django Rest Framework - Key Terms
### Serializers
Serializers help convert complex objects, such as Django models, into a representation that can be easily rendered into different formats like JSON, XML, or other content types. Serializers define how the data should be serialized, which fields to include or exclude, and how relationships between objects should be represented.

The same JSON converted data is usually passed to frontend as an API response

## References
- https://docs.djangoproject.com/en/4.2/intro/tutorial01/
- https://www.django-rest-framework.org/tutorial