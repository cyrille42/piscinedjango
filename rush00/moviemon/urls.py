from django.conf.urls import url
from django.contrib import admin
from . import views

app_name='moviemon'
urlpatterns = [
    url(r'^$', views.test, name='test'),
]
