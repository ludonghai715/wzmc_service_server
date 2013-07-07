from django.conf.urls import patterns, url
from address_book import views
urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^alldepart/$', views.allDepart),
        url(r'^departcontact/(?P<departID>\d+)/$', views.departContact),
        url(r'^personcontact/(?P<keywords>.+)$', views.personContact),
        )
