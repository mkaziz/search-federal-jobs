from django.conf.urls import patterns, url
from jobsapp.views import *

from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', index),
)

