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
			self.content = file.read().split('\n')
			return(self)
		else:
			return(self)#verifier au retour si on a bien retourne la bonne sauvegarde
	
	def dump(self):
		return (self.content)

	def get_strength(self):
		return (len(content[2]))

	def get_movie(self,name):
		string = requests.get('http://www.omdbapi.com/?t='+str(name)+'&y=&plot=short&r=json')
		return (string.json())

	def load_default_settings(self):
		self.content[0] = settings.POS_PLAYER
		self.content[1] = 0
		self.content[2] = []
		for i in range(len(settings.ID_MMON)):
			self.content[3].append(self.get_movie(settings.ID_MMON[i]))
		return (self)
