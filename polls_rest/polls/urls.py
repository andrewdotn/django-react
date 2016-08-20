from django.conf.urls import include, url

from rest_framework import routers

from . import views

api_router = routers.DefaultRouter()
api_router.register(r'questions', views.QuestionViewSet)

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^api/', include(api_router.urls))
]
