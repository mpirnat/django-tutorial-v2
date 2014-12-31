from django.conf.urls import patterns, url

from characters import views

urlpatterns = patterns('',
    url(r'^$', views.CharacterIndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.CharacterDetailView.as_view(), name='view'),
    url(r'^create/$', views.CharacterCreationView.as_view(), name='create'),
    url(r'^edit/(?P<pk>\d+)/$', views.CharacterUpdateView.as_view(), name='edit'),
    url(r'^delete/(?P<pk>\d+)/$', views.CharacterDeleteView.as_view(), name='delete'),
)
