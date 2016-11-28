from django.conf.urls import url
from django.contrib import admin
from . import views

app_name='ex01'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^django/$', views.django, name='django'),
    url(r'^affichage/$', views.affichage, name='affichage'),
    url(r'^templates/$', views.templates, name='templates'),
]
