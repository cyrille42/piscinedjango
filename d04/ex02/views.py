from django.shortcuts import render

from .models import Historique
from .forms import HistoriqueForm
from django.utils import timezone
from django.core.files import File
import os
from django.conf import settings
# Create your views here.

def index(request):
	if request.method == "POST":
		form = HistoriqueForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.created_date = timezone.now()
			myfile = open(os.path.join(settings.PROJECT_ROOT, 'logs'), 'a')
			myfile.write(str(post.created_date)+ " " + post.content+ "\n")
	myfile = open(os.path.join(settings.PROJECT_ROOT, 'logs'), 'r')
	content = myfile.read().split("\n")
	form = HistoriqueForm()
	return render(request, 'ex02/index.html', {'form': form, 'content': content})