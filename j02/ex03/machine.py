from beverages import *
import random

class CoffeeMachine():
	broken = 0

	class EmptyCup(HotBeverage):
		def __init__(self):
			self.name = "empty cup"
			self.price = 0.90
		def description(self):
			return ("An empty cup?! Gimme my money back!")
	
	def BrokenMachineException(Exception):
		def __init__(self, error = "This coffee machine has to be repaired."):

	def serve(self, beverage):
		if self.broken > 10:
			self.BrokenMachineException()
		self.broken += 1
		i = random.randint(1, 2)
		if i == 1:
			return (beverage)
		if i == 2:
			return (self.EmptyCup())

	def repair():
		broken = 0

if __name__ == '__main__':
	machine = CoffeeMachine()
	cof = Coffee()
	t = Tea()
	cho = Chocolate()
	cap = Cappuccino()
	# print(machine.EmptyCup())
	for i in range(15):
		print(machine.serve(t))
