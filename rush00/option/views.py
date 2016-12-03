from django.shortcuts import render
from .obj.memory import *
from django.conf import settings
from django.shortcuts import redirect

mem = memory()
# Create your views here.

def option(request):
	return render(request, 'option/option.html')

#init le jeux et renvoie sur la map
def newgame(request):
	mem.load_default_settings()
	return redirect('http://127.0.0.1:8000/worldmap/')

def save(request):
	return redirect('http://127.0.0.1:8000/option/')