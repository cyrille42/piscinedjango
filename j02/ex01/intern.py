class Intern:
	def __init__(self, string="My name? I’m nobody, an intern, I have no name."):
		self.name = string
	def __str__(self):
		return (self.name)
	def work(self):
		raise Exception("I’m just an intern, I can’t do that...")
	def make_coffee(self):
		return (self.coffee())
	class coffee:
		def __str__(self):
			return ("This is the worst coffee you ever tasted.")

if __name__ == '__main__':
	intern1 = Intern()
	interne_mark = Intern("Mark")
	print(intern1)
	print(interne_mark)
	print(intern1.make_coffee())
	print(interne_mark.make_coffee())
	try:
		intern1.work()
	except Exception as e:
		print(e)