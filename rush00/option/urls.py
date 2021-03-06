from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.option, name='option'),
    url(r'^newgame$', views.newgame, name='newgame'),
    url(r'^save_menu$', views.save_menu, name='save_menu'),
    url(r'^load_menu$', views.load_menu, name='load_menu'),
    url(r'^save$', views.save, name='save'),
    url(r'^up$', views.up, name='up'),
    url(r'^down$', views.down, name='down'),
    url(r'^load$', views.load, name='load'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^download$', views.download, name='download'),
    # url(r'^load$', views.load, name='load'),
]
