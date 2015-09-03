from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'powerpleaser.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/', include('api.urls')),
    url(r'^$', 'powerpleaser.views.home', name='home'),
)
