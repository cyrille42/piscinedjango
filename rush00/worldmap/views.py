from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from .obj.player import *

#remplacer les pos joueurs par des getteur du gestionaire de fichier lors du load de map
player = Player(settings.POS_PLAYER[0], settings.POS_PLAYER[1],0, map=settings.LEN_MAP)

def worldmap(request):
	return render(request, 'worldmap/worldmap.html',{'x' : range(settings.LEN_MAP[0]), 'y' : range(settings.LEN_MAP[1]), 'posx' : player.getx(), 'posy' : player.gety(), 'ball' : player.getball()})

# si il le faut , sotcker les coor du joueurs a chaque deplacement dans un fichier
def up(request):
	player.up()
	return redirect('http://127.0.0.1:8000/worldmap/')

def down(request):
	player.down()
	return redirect('http://127.0.0.1:8000/worldmap/')

def right(request):
	player.right()
	return redirect('http://127.0.0.1:8000/worldmap/')

def left(request):
	player.left()
	return redirect('http://127.0.0.1:8000/worldmap/')