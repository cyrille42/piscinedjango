from django.shortcuts import render
import psycopg2
# Create your views here.

def index(request):
	try:
		conn = psycopg2.connect(database='formationdjango', host='localhost', user='djangouser',password='secret')
		curr = conn.cursor()	
		curr.execute(""" CREATE TABLE IF NOT EXISTS ex00_movies (
			title 			varchar(64)		NOT NULL,
			episode_nb 		int				PRIMARY KEY,
			opening_crawl 	text,
			director 		varchar(32)		NOT NULL,
			producer 		varchar(128)	NOT NULL,
			release_date	 date 			NOT NULL)
			""")
		conn.commit()
		conn.close()
	except Exception as e:
		return render(request, 'ex00/ex00.html', {'error': e})	
	return render(request, 'ex00/ex00.html', {'error': "OK"})