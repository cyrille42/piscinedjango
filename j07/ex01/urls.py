from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login$', views.login, name='login'),
    url(r'^article/$', views.article, name='article'),
]
