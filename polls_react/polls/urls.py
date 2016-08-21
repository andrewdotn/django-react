from django.conf.urls import include, url
from django.urls.exceptions import NoReverseMatch

from . import views

from rest_framework import reverse, routers

# Monkey patch namespace support into Django REST framework
ORIG_REVERSE = reverse._reverse
def namespace_aware_reverse(viewname, args=None, kwargs=None, request=None,
                            format=None, **extra):
    """If reverse fails, try again using the namespace under which the current
    request was found.

    To be monkey-patched into rest_framework.reverse._reverse"""
    try:
        return ORIG_REVERSE(viewname, args=args, kwargs=kwargs, request=request,
                 format=format, **extra)
    except NoReverseMatch:
        viewname = request.resolver_match.namespace + ':' + viewname
        return ORIG_REVERSE(viewname, args=args, kwargs=kwargs, request=request,
                     format=format, **extra)
reverse._reverse = namespace_aware_reverse

##

api_router = routers.DefaultRouter()
api_router.register(r'questions', views.QuestionViewSet)
api_router.register(r'choices', views.ChoiceViewSet)

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^api/', include(api_router.urls))
]
