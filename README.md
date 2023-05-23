# Poll-App
A Simple Poll app that lists available polls, take votes, show results.

# SETUP
### Initial
- create project
```
django-admin startproject my_poll_site
```
- create polls app
```
python manage.py startapp polls
```
### DB
- install Postgre sql adapter
```
pip install psycopg2
```
- Login to postgresql as super user, create user and grant permissions
```
sudo -i -u postgres
psql
Create user hsmgowtham with SUPERUSER;
ALTER USER hsmgowtham WITH PASSWORD 'hsmgowtham';
```
- create table for the polls app and grant permissions
```
CREATE DATABASE poll_app
    WITH
    OWNER = hsmgowtham;
GRANT ALL ON DATABASE otoo_db TO hsmgowtham;
```
### Installed Apps to DB
- To create db tables for the installed apps
```
python manage.py migrate
```
- create migration files for the polls app model changes
```
python manage.py makemigrations polls
```
# Extra Command line utilities
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