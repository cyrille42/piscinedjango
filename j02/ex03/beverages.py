class HotBeverage:
	price = 0.30
	name = "hot beverage"
	def __str__(self):
		string = "name : " + self.name + "\nprice : " + str(self.price) + "\ndescription : " + self.description()
		return (string)
	def description(self):
		return ("Just some hot water in a cup.")

class Coffee(HotBeverage):
	def __init__(self):
		self.name = "coffee"
		self.price = 0.40
	def description(self):
		return ("A coffee, to stay awake.")

class Chocolate(HotBeverage):
	def __init__(self):
		self.name = "chocolate"
		self.price = 0.50
	def description(self):
		return ("Chocolate, sweet chocolate...")

class Tea(HotBeverage):
	def __init__(self):
		self.name = "tea"

class Cappuccino(HotBeverage):
	def __init__(self):
		self.name = "cappuccino"
		self.price = 0.45
	def description(self):
		return ("Un po di Italia nella sua tazza!")