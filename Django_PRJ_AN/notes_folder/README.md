 
.venv activate:

 * python -m venv .venv
 * source .venv/Scripts/activate
 * cd project_root
 * pip install -r requirements.txt
 
migration:

* python manage.py migrate
* python manage.py createsuperuser

 _ _ _
 _ _ _

* python manage.py runserver
* python .\project_root\manage.py runserver

Tests: 
* python .\project_root\manage.py test

To test a specific Django app:
* python .\project_root\manage.py test myapp

Or a particular test:
* python .\project_root\manage.py test myapp.tests.TestSomething.test_something

-:- \
-:- \
-:-

example:

python manage.py runserver \
python manage.py test \
python manage.py makemigrations \
python manage.py migrate \
python manage.py createsuperuser \
python manage.py shell 