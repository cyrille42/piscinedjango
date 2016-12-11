from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^init$', views.index, name='index'),
]
