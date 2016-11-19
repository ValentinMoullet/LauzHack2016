from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^pickVideo/$', views.pickVideo, name="pickVideo"),
    url(r'^pickChannel/$', views.pickChannel, name="pickChannel"),
    url(r'^youWatch/$', views.youWatch, name="youWatch"),
    url(r'^youAre/$', views.youAre, name="youAre"),
]
