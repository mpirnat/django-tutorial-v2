from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from characters import views

urlpatterns = patterns('',
    url(r'^$', views.CharacterIndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.CharacterDetailView.as_view(), name='view'),
    url(r'^create/$', login_required(views.CharacterCreationView.as_view()), name='create'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(views.CharacterUpdateView.as_view()), name='edit'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(views.CharacterDeleteView.as_view()), name='delete'),
)
