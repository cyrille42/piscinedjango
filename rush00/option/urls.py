from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.option, name='option'),
    url(r'^newgame$', views.newgame, name='newgame'),
    url(r'^save$', views.save, name='save'),
    url(r'^up$', views.up, name='up'),
    url(r'^down$', views.down, name='down'),
    # url(r'^load$', views.load, name='load'),
]
