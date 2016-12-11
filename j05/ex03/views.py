from django.shortcuts import render
from .models import Movies
# Create your views here.

def populate(request):
	tab = []
	try:	
		Movies(title='The Phantome Menace', episode_nb=1, director='George Lucas', producer='Rick McCallum', release_date='1999-05-19').save()
	except Exception as e:
		tab.append(e)
	else:
		tab.append("OK")
	try:	
		Movies(title='Attack of clone', episode_nb=2, director='George Lucas', producer='Rick McCallum', release_date='2002-05-16').save()
	except Exception as e:
		tab.append(e)
	else:
		tab.append("OK")
	try:	
		Movies(title='Revenge of the Sith', episode_nb=3, director='George Lucas', producer='Rick McCallum', release_date='2005-05-19').save()
	except Exception as e:
		tab.append(e)
	else:
		tab.append("OK")
	try:	
		Movies(title='A New Hope', episode_nb=4, director='George Lucas', producer='Gary Kurtz Rick McCallum', release_date='1977-05-25').save()
	except Exception as e:
		tab.append(e)
	else:
		tab.append("OK")
	try:	
		Movies(title='The Empire Strike back', episode_nb=5, director='Irvin Kershner', producer='Gary Kurtz, Rick McCallum', release_date='1980-05-17').save()
	except Exception as e:
		tab.append(e)
	else:
		tab.append("OK")
	try:	
		Movies(title='Return of the Jedi', episode_nb=6, director='Richard Marquand',producer=' Howard Kazanjian ,george lucas ,rick mccallum', release_date='1983-05-25').save()
	except Exception as e:
		tab.append(e)
	else:
		tab.append("OK")
	try:	
		Movies(title='The Force Awakens', episode_nb=7, director='JJ Abrams', producer='Kathleen Kennedy ,JJ abram ,bryan burk', release_date='2015-12-11').save()
	except Exception as e:
		tab.append(e)
	else:
		tab.append("OK")
	return render(request, 'ex02/insert.html', {'print': tab})

def display(request):
	tab = Movies.objects.all()
	return render(request, 'ex02/display.html', {'sql': tab})