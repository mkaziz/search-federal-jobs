from django.conf.urls import patterns, url
from jobsapp.views import *

from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^search$', search),
    url(r'^about$', about),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()