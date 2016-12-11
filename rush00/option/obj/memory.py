import os.path
from django.conf import settings
import requests

# content[0] = list pos joueur content[1]  movieball
# content [2] =list des moviemon du moviedex
# content[3] = list des infos des moviemon
class memory():
	content=[[],0,[],[]]

	def load(self,name):
		if os.path.isfile(name):
			file = open(name, "r")
			list_content = file.read().split('\n')
			content[0] = list_content[0].split(":")
			content[1] = list_content[1]
			content[2] = list_content[2].split(":")
			content[3] = list_content[3].split(":\n")
			file.close()
			return(self)
		else:
			return(self)#verifier au retour si on a bien retourne la bonne sauvegarde
	
	def dump(self):
		return (self.content)

	def get_strength(self):
		return (len(content[2]))

	def get_random_movie(self):
		return()

	def get_movie(self,name):
		string = requests.get('http://www.omdbapi.com/?t='+str(name)+'&y=&plot=short&r=json')
		return (string.json())

	def save(self):
		file = open(os.path.join(settings.PROJECT_ROOT, 'tmp'), "w")
		file.write(str(self.content[0][0]) + ":" + str(self.content[0][0]) + "\n")
		file.write(str(self.content[1])+ "\n")
		for i in range(len(self.content[2])):
			file.write(self.content[2] + ":")
		file.write("\n")
		for i in range(len(self.content[3])):
			file.write(str(self.content[3][i]) + ":\n")

	def load_default_settings(self):
		self.content[0] = settings.POS_PLAYER
		self.content[1] = "0"
		self.content[2] = []
		for i in range(len(settings.ID_MMON)):
			self.content[3].append(self.get_movie(settings.ID_MMON[i]))
		self.save()
		return (self)
