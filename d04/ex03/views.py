from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'ex03/ex03.html', {'col' : range(4), 'lig' : range(51)})