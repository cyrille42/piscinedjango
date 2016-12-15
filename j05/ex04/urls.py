from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^init$', views.index, name='index'),
    url(r'^populate$', views.populate, name='populate'),
	url(r'^display$', views.display, name='display'),
	url(r'^remove$', views.remove, name='remove'),
]