from django.conf.urls import patterns, url
from characters import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<character_id>\d+)/$', views.view_character, name='view'),
)
