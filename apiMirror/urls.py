from django.conf.urls import patterns, url, include
from apiMirror import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^map/(?P<arg>\w+)/?$', views.API, name='mapAPImirror'),
)