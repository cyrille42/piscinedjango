from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from .obj.player import *
from option.views import mem

#remplacer les pos joueurs par des getteur du gestionaire de fichier lors du load de map
player = Player(map=settings.LEN_MAP)
# load tmp a chaque action
def worldmap(request):
	return render(request, 'worldmap/worldmap.html',{'x' : range(settings.LEN_MAP[0]), 'y' : range(settings.LEN_MAP[1]), 'posx' : mem.get_posx(), 'posy' : mem.get_posy(), 'ball' : player.getball()})

def up(request):
	global player
	player.up()
	global mem
	mem.set_pos([player.getx(),player.gety()])
	mem.save()
	return redirect('http://127.0.0.1:8000/worldmap/')

def down(request):
	global player
	player.down()
	global mem
	mem.set_pos([player.getx(),player.gety()])
	mem.save()
	return redirect('http://127.0.0.1:8000/worldmap/')

def right(request):
	global player
	player.right()
	global mem
	mem.set_pos([player.getx(),player.gety()])
	mem.save()
	return redirect('http://127.0.0.1:8000/worldmap/')

def left(request):
	global player
	player.left()
	global mem
	mem.set_pos([player.getx(),player.gety()])
	mem.save()
	return redirect('http://127.0.0.1:8000/worldmap/')