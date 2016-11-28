from django.shortcuts import render

from .models import Historique
from .forms import HistoriqueForm
from django.utils import timezone
from django.core.files import File
# Create your views here.

def index(request):
	if request.method == "POST":
		form = HistoriqueForm(request.POST)
		# posts = Historique.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
		if form.is_valid():
			post = form.save(commit=False)
			post.created_date = timezone.now()
			# http://stackoverflow.com/questions/13067107/read-a-local-file-in-django si on met le liens dans settings alors on peut le read ?
			with open('logs', 'a') as f:
				myfile = File(f)
				myfile.write(post.content+ " " + str(post.created_date)+ "\n")		
	form = HistoriqueForm()
	return render(request, 'ex02/index.html', {'form': form})