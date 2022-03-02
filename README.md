# django-rest-project

This is an example to show how the Django Rest Framework and asyncrhonous views work.

To run it:

1. Install the requirements.

2. Create one or multiple superusers in the provider app:

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

5. In another terminal setup and run the consumer app:

```
cd consumer
./manage.py migrate
./manage runserver
```

6. Take a look at the output of the consumer app in a browser at http://localhost:7000/users/

=====

**Tasks**

1. Expand the consumer project. Create views for individual users and create links to them from the overview/index page.

2. Expand the provider project. Create your own models and serializers. Then make them available through the consumer project.
