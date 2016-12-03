from django.conf.urls import url
from . import views

app_name='worldmap'
urlpatterns = [
    url(r'^$', views.worldmap, name='worldmap'),
    url(r'^up$', views.up, name='up'),
    url(r'^down$', views.down, name='down'),
    url(r'^left$', views.left, name='left'),
    url(r'^right$', views.right, name='right'),
]
