class Player():
	def __init__(self, x=0, y=0, ball=0, moviedex=[],map=[0,0]):
		self.posx = x
		self.posy = y
		self.ball = ball
		self.moviedex = moviedex
		self.map = map
		self.error()
	def error(self):
		if self.posx > self.map[0] - 1:
			self.posx = self.map[0] - 1
		if self.posy > self.map[1] - 1:
			self.posy = self.map[1] - 1
		if self.posx < 0:
			self.posx = 0
		if self.posy < 0:
			self.posy = 0
	def up(self):
		self.posy -=1
		self.error()
	def down(self):
		self.posy += 1
		self.error()
	def left(self):
		self.posx -= 1
		self.error()
	def right(self):
		self.posx += 1
		self.error()
	def getx(self):
		return self.posx
	def gety(self):
		return self.posy
	def getball(self):
		return self.ball
	def getmoviedex(self):
		return self.moviedex