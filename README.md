# first-django-project

Setup a virtual environment.
```
pip3 install virtualenv
```
Create a virtual environment with name `venv`.
```
virtualenv venv
```
Activate the `venev`
```
source venv/bin/activate
```
Install Django
```
pip install django
```
Create a Django project.
```
django-admin startproject realstate
```
It will create following files;
- wsgi.py - A standard for how Python applications and servers should conform to.
- asgi.py - Just like wsgi but for async applications.
- settings.py - Contains settings for the project.
- urls.py - Here, we define project urls.
- manage.py - File use to run commands in the project.

Apply the migrations;
```
python manage.py migrate
```
Run this command to run django server on localhost:8000;
```
python manage.py runserver
```
Create a superuser and enter the credentials;
```
python manage.py createsuperuser
```
Now, we can access url through the credentials defined in above step.

Create an app `listings`;
```
python manage.py startapp listings
```
Add `listings` to `INSTALLED_APPS` in `settings.py`

### Models
Models are representations for project's database schema. Each model is used to interact with database tables and convert database rows to python objects. (Model is high-level abstraction over database. Django ORM handles low-level database interactions).

Let's create a model for a realstate website in `listings/models.py` and apply migrations;
```
python manage.py makemigrations
python manage.py migrate
```
This will create a  listing table in database with  fields mentioned in models.py.

#### Add models to admin
Import the model class in `admin.py` and register it;
```
admin.site.register(Listing)
``` 

### Views
Views are classes or functions that execute logic when a url is visited. The views follow  CRUD convention.

We will modify `views.py`.
To query the database, Django ORM is used. Our model has property called objects (an entry point to start  querying the database). 

#### Creating a Template
Create a folder templates(to store html files), add it to `TEMPLATES` in `settings.py`.

#### Forms
To create and update, we need forms. Create a forms.py in listings directory. Update and delete are comparitively easier functions.

### Tailwind CSS
A CSS framework to build any design directly in html. Update the  html  files to add design.

#### Images
We need `Pillow` for django to work with images. Install it;
```
pip install pillow
```
To see installed package;
```
pip freeze > requirements.txt
```
## Reference 
-  https://justdjango.com/courses/django-crash-course/listing-app-and-model 