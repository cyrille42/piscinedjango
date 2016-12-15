import os.path
from django.conf import settings

class arrow():
	i = 0
	j = 0
	def geti(self):
		return(self.i)
	def seti(self, number):
		self.i += number
		if (self.i > 2):
			self.i = 0
		if (self.i < 0):
			self.i = 2
	def getj(self):
		return(self.i)
	def setj(self, number):
		self.i += number
		if (self.i > 2):
			self.i = 0
		if (self.i < 0):
			self.i = 2