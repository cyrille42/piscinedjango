class Elem():
	def __init__(self,tag="body",attr={},content=[''],tag_type='double'):
		self.tag = tag
		self.attr = attr
		self.text = ""
		# split content pour trouver le nombre de tab a appliquer devamt les self.tag OU just tab devant les balise une fois et quand elle servirons de content , elle serons automatiquement indenter
		if content[0] != '':
			for i in range(len(content)):
					self.text += "\t"+str(content[i])+"\n"
		if self.text == "":
			self.html = ["<"+self.tag+"></"+self.tag+">"]
		else:
			self.html = ["<"+self.tag+">\n"+self.text+"</"+self.tag+">"]
	def add_content(self,add):
		self.content += add
		self.html = ["<"+self.tag+">\n"+self.text+"\n</"+self.tag+">"]

	def __str__(self):
		result = ""
		for i in range(len(self.html)):
			result += self.html[i]
		return (result)

class Text():
	def __init__(self,string=""):
		self.string = str(string)
		self.string = self.string.replace("\n", "\n<br />\n")
	def __str__(self):
		return (self.string)	


if __name__ == '__main__':
	print(Elem(tag='body', attr={}, content=['foo', Elem()], tag_type='double'))