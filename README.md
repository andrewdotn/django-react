## Contents

### `polls_tutorial`

This is a basic opinion polling webapp, created by following part of the
[Django Tutorial](https://docs.djangoproject.com/en/1.10/intro/).

To get it running on your machine:

 1. Make sure python3 is installed
 2. `pip3 install -r requirements.txt`
 3. `./manage.py migrate`
 4. `./manage.py createsuperuser`
 5. `./manage.py runserver`
 6. Visit http://localhost:8000/admin/ to create some questions
 7. Vote on them from http://localhost:8000/polls/
