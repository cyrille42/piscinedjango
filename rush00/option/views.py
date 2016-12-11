from django.shortcuts import render
from .obj.memory import *
from django.conf import settings
from django.shortcuts import redirect
import os.path

mem = memory()
# Create your views here.

i = 0

def option(request):
	return render(request, 'option/option.html')

#init le jeux et renvoie sur la map
def newgame(request):
	mem.load_default_settings()
	return redirect('http://127.0.0.1:8000/worldmap/')

def save(request):
	return render(request, 'option/option_save.html', {'fleche' : i, 'a' : os.path.isfile("SLOT A")})

def down(request):
	i -= 1
	if i < 0:
		i = 2
	return redirect('http://127.0.0.1:8000/option/save')

def up(request):
	i += 1
	if i > 2:
		i = 0
	return redirect('http://127.0.0.1:8000/option/save')

def load(request):
	mem.load("SLOT A")
	return redirect('http://127.0.0.1:8000/worldmap')