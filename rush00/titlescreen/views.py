from django.shortcuts import render
from django.conf import settings

# Gere les battles et le moviedex
def titlescreen(request):
	return render(request, 'titlescreen/title.html')
