from django.conf.urls import patterns, url
from accounts import views

urlpatterns = patterns('',
    url(r'^register/$', views.RegistrationView.as_view(), name='register'),
)
