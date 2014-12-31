from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^accounts/', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^characters/', include('characters.urls', namespace='characters')),
    url(r'^admin/', include(admin.site.urls)),
)
