django-random-id-generator
==========================

What is it?
===========

django-simple-blog is a simple Django app to Generate Random and Unique IDs for Django model objects with custom save method


Installation
============

You can get ``django-random-id-generator`` by :


- Download or git clone _`<https://github.com/frankovo/django-random-id-generator.git>`_


Usage
=====

1. Add ``test_app`` to your INSTALLED_APPS setting like this::

       INSTALLED_APPS = [
           ...
           'test_app',
       ]



2. Run ``python manage.py makemigrations test_app``

3. Run ``python manage.py migrate``

4. Run ``python manage.py createsuperuser``

5. Run ``python manage.py runserver``

6. Go to _`<http://127.0.0.1:8000/admin/>`_


Requirements
============

`Django==2.0.3`
