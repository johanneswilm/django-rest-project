# django-rest-project

This is an example to show how the Django Rest Framework and asyncrhonous views work.

** Setup redis **
Install the redis server:
    MAC: brew install redis
    Ubuntu: apt install redis-server
```
pip install redis
```

** Install app

To run it:


1. Install the requirements.

2. Create one or multiple superusers in the provider project:

```
cd provider
./manage.py migrate
./manage.py createsuperuser
```

3. Run the provider server:

```
./manage.py runserver
```

This will run the django provider project on port 8000. It includes the Django Rest Framework and is a slightly modified version of https://www.django-rest-framework.org/tutorial/quickstart/ .

4. Try to connect with the provider looking at http://localhost:8000/users/ in a browser.You can log in and browse around. You can add more users via the command line or http://localhost:8000/admin/

5. Log into the admin screen at http://localhost:8000/admin/ and create a token for one of your users. Copy the token key.

6. In another terminal enter the consumer project and copy local_settings.py.default to local_settings.py:

```
cd consumer
cp local_settings.py.default local_settings.py
```

7. Edit the local_settings.py file and make the AUTH_TOKEN equal to the key you copied in step 5.

8. Setup and run the consumer project:

```
./manage.py migrate
./manage.py createsuperuser # Create at least one user
./manage.py runserver
```

7. Take a look at the output of the consumer project in a browser at http://localhost:7000/users/


=====

**Tasks**

1. Expand the consumer project. Create views for individual users and create links to them from the overview/index page.

2. Expand the provider project. Create your own models and serializers. Then make them available through the consumer project.

3. Add an interface and methods to modify fields on an existing model instance, create new model instances or delete existing ones.
