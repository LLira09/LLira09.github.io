from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^writenow', views.writenow),
    url(r'^graphic', views.graphic),
    url(r'^newjersey', views.newjersey),
]
