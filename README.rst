django-random-id-generator
==========================

What is it?
===========

django-random-id-generator is a simple Django app to Generate Random and Unique IDs for Django model objects with custom save method


Installation
============

You can get ``django-random-id-generator`` by :


- Download or git clone `<https://github.com/frankovo/django-random-id-generator.git>`_


Usage
=====

1. Add ``random_id`` to your INSTALLED_APPS setting like this::

       INSTALLED_APPS = [
           # Django default apps 
           ...
           'random_id',
       ]



2. Run ``python manage.py makemigrations random_id``

3. Run ``python manage.py migrate``

4. Run ``python manage.py createsuperuser``

5. Run ``python manage.py runserver``

6. Go to `<http://127.0.0.1:8000/admin/>`_


Requirements
============

`Django==2.0.3`


Note
===========

Django==2.0.3 requires Python 3.4, 3.5, 3.6
