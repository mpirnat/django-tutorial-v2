from django.conf.urls import patterns, url
from characters import views

urlpatterns = patterns('',
    url(r'^$', views.CharacterIndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.CharacterDetailView.as_view(), name='view'),
    url(r'^create/$', views.create_character, name='create'),
)
