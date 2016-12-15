from django.shortcuts import render
import psycopg2
# Reste le no data available


def index(request):
	try:
		conn = psycopg2.connect(database='formationdjango', host='localhost', user='djangouser',password='secret')
		curr = conn.cursor()	
		curr.execute(""" CREATE TABLE IF NOT EXISTS ex04_movies (
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

def populate(request):
	tab= []
	try:
		conn = psycopg2.connect(database='formationdjango', host='localhost', user='djangouser',password='secret')
		curr = conn.cursor()
		try:	
			curr.execute(""" INSERT INTO ex04_movies (title,episode_nb,director,producer,release_date) VALUES
				('The Phantome Menace', 1, 'George Lucas', 'Rick McCallum', '1999-05-19')
				""")
		except Exception as e:
			tab.append(e)
		else:
			tab.append("OK")
		try:	
			curr.execute(""" INSERT INTO ex04_movies (title,episode_nb,director,producer,release_date) VALUES
				('Attack of clone', 2, 'George Lucas', 'Rick McCallum', '2002-05-16')
				""")
		except Exception as e:
			tab.append(e)
		else:
			tab.append("OK")
		try:	
			curr.execute(""" INSERT INTO ex04_movies (title,episode_nb,director,producer,release_date) VALUES
				('Revenge of the Sith', 3, 'George Lucas', 'Rick McCallum', '2005-05-19')
				""")
		except Exception as e:
			tab.append(e)
		else:
			tab.append("OK")
		try:	
			curr.execute(""" INSERT INTO ex04_movies (title,episode_nb,director,producer,release_date) VALUES
				('A New Hope', 4, 'George Lucas', 'Gary Kurtz Rick McCallum', '1977-05-25')
				""")
		except Exception as e:
			tab.append(e)
		else:
			tab.append("OK")
		try:	
			curr.execute(""" INSERT INTO ex04_movies (title,episode_nb,director,producer,release_date) VALUES
				('The Empire Strike back', 5, 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17')
				""")
		except Exception as e:
			tab.append(e)
		else:
			tab.append("OK")
		try:	
			curr.execute(""" INSERT INTO ex04_movies (title,episode_nb,director,producer,release_date) VALUES
				('Return of the Jedi', 6, 'Richard Marquand',' Howard Kazanjian ,george lucas ,rick mccallum', '1983-05-25')
				""")
		except Exception as e:
			tab.append(e)
		else:
			tab.append("OK")
		try:	
			curr.execute(""" INSERT INTO ex04_movies (title,episode_nb,director,producer,release_date) VALUES
				('The Force Awakens', 7, 'JJ Abrams', 'Kathleen Kennedy ,JJ abram ,bryan burk', '2015-12-11')
				""")
		except Exception as e:
			tab.append(e)
		else:
			tab.append("OK")
		conn.commit()
		conn.close()
	except Exception as e:
		tab.append(e)
	return render(request, 'ex02/insert.html', {'print': tab})

def display(request):
	tab = []
	conn = psycopg2.connect(database='formationdjango', host='localhost', user='djangouser',password='secret')
	curr = conn.cursor()
	curr.execute(""" SELECT * FROM ex04_movies
				""")
	response = curr.fetchall()
	for row in response:
		tab.append(row)
	conn.commit()
	conn.close()
	return render(request, 'ex02/display.html', {'sql': tab})

def remove(request):
	tab = []
	conn = psycopg2.connect(database='formationdjango', host='localhost', user='djangouser',password='secret')
	curr = conn.cursor()
	if request.method == "POST":
		movie = dict(request.POST)
		curr.execute("DELETE FROM ex04_movies WHERE title = %s", movie['Delete'])
	curr.execute(""" SELECT title FROM ex04_movies
				""")
	response = curr.fetchall()
	for row in response:
		tab.append(str(row).strip('(),\''))
	conn.commit()
	conn.close()
	return render(request, 'ex04/remove.html', {'sql': tab})