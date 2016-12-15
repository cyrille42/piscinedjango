from django.shortcuts import render
from .obj.memory import *
from .obj.arrow import *
from django.conf import settings
from django.shortcuts import redirect
import os.path
from worldmap.views import player

mem = memory()
# Create your views here.

arrow = arrow()

def option(request):
	return render(request, 'option/option.html')

#init le jeux et renvoie sur la map
def newgame(request):
	global mem
	mem.load_default_settings()
	global player
	# rjouter une reinitialisation des coorodnner du joueurs
	return redirect('http://127.0.0.1:8000/worldmap/')

def save_menu(request):
	return render(request, 'option/option_save.html', {'i' : arrow.geti() ,'a' : os.path.isfile(settings.PROJECT_ROOT+"/SLOT A"), 'b' : os.path.isfile(settings.PROJECT_ROOT+"/SLOT B"), 'c' : os.path.isfile(settings.PROJECT_ROOT+"/SLOT C")})

def load_menu(request):
	return render(request, 'option/option_load.html', {'i' : arrow.getj() ,'a' : os.path.isfile(settings.PROJECT_ROOT+"/SLOT A"), 'b' : os.path.isfile(settings.PROJECT_ROOT+"/SLOT B"), 'c' : os.path.isfile(settings.PROJECT_ROOT+"/SLOT C")})

def save(request):
	if arrow.geti() == 0:
		global mem
		mem.save_slot("SLOT A")
	if arrow.geti() == 1:
		global mem
		mem.save_slot("SLOT B")
	if arrow.geti() == 2:
		global mem
		mem.save_slot("SLOT C")
	return redirect('http://127.0.0.1:8000/option/save_menu')

def down(request):
	arrow.seti(1)
	return redirect('http://127.0.0.1:8000/option/save_menu')

def up(request):
	arrow.seti(-1)
	return redirect('http://127.0.0.1:8000/option/save_menu')

def download(request):
	arrow.setj(1)
	return redirect('http://127.0.0.1:8000/option/load_menu')

def upload(request):
	arrow.setj(-1)
	return redirect('http://127.0.0.1:8000/option/load_menu')

def load(request):
	if arrow.getj() == 0:
		if os.path.isfile(settings.PROJECT_ROOT+"/SLOT A"):
			global mem
			mem.load("SLOT A")
		else:
			return redirect('http://127.0.0.1:8000/option/load_menu')
	if arrow.getj() == 1:
		if os.path.isfile(settings.PROJECT_ROOT+"/SLOT B"):
			global mem
			mem.load("SLOT B")
		else:
			return redirect('http://127.0.0.1:8000/option/load_menu')
	if arrow.getj() == 2:
		if os.path.isfile(settings.PROJECT_ROOT+"/SLOT C"):
			global mem
			mem.load("SLOT C")
		else:
			return redirect('http://127.0.0.1:8000/option/load_menu')
	return redirect('http://127.0.0.1:8000/worldmap')