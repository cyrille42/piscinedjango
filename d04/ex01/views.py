from django.shortcuts import render

# Create your views here.
# envoyer list et faire for in dans la list pour opti ?
def index(request):
	return render(request, 'ex01/nav.html')

def django(request):
	return render(request, 'ex01/django.html')

def affichage(request):
	return render(request, 'ex01/affichage.html')

def templates(request):
	return render(request, 'ex01/templates.html')