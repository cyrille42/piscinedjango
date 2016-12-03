from django.conf.urls import url
from . import views

app_name='titlescreen'
urlpatterns = [
    url(r'^$', views.titlescreen, name='titlescreen'),
]
