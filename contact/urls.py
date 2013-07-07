from django.conf.urls import patterns, url
from contact import views
urlpatterns = patterns('',
        url(r'^alldepart/$', views.allDepart),
        url(r'^person/(?P<keywords>.+)/$', views.person),
        url(r'^depart/(?P<departID>\d+)$', views.depart),
        )
