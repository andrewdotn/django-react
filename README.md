## Contents

### [`presentation`](presentation)

Slides for
[2016-08-23 PyYYC Presentation](https://pyyyc.org/presentations/2016-08-23).

### [`polls_tutorial`](polls_tutorial)

This is a basic opinion polling webapp, created by following part of the
[Django Tutorial](https://docs.djangoproject.com/en/1.10/intro/).

To get it running on your machine:

 1. Make sure python3 is installed
 2. `pip3 install --user -r requirements.txt`
 3. `./manage.py migrate`
 4. `./manage.py createsuperuser`
 5. `./manage.py runserver`
 6. Visit http://localhost:8000/admin/ to create some questions
 7. Vote on them from http://localhost:8000/polls/

### [`polls_rest`](polls_rest)

`polls_tutorial` augmented with a REST API for getting poll data, and
voting on polls, by following the [Django REST framework quickstart][qs].

[qs]: http://www.django-rest-framework.org/tutorial/quickstart/

### [`polls_react`](polls_react)

`polls_react` with the page-driven frontend replaced with reactive JS.

See the [React tutorial](https://facebook.github.io/react/docs/tutorial.html)
and
[Component Specs and Lifecycle](https://facebook.github.io/react/docs/component-specs.html)
for details.
