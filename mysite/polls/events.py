from django.conf.urls.defaults import *
from events import views

urlpatterns = patterns('',
    url(r'^tonight/$', views.tonight, name='ev_tonight'),
)
