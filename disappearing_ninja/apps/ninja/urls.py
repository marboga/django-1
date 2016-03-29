from django.conf.urls import patterns, url
from . import views

urlpatterns = [
    url(r'^$', views.show, name='show'),
    url(r'^(?P<ninja_color>.*)?/$', views.index, name='index'),

]
