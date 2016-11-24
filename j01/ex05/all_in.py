import sys

def error(lis):
	for arg in lis:
		if (arg == ""):
			return 1
	return 0

if __name__ == '__main__':
	states = {
	"Oregon" : "OR",
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
	}
	capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
	}
	if len(sys.argv) == 2:
		i = 0
		lis = sys.argv[1].split(",")
		if (error(lis) == 0):
			for arg in lis:
				arg = arg.strip()
				for citie in capital_cities:
					if arg.lower() == capital_cities[citie].lower():
						for ground in states:
							if (citie.lower() == states[ground].lower()):
								print(capital_cities[citie] + " is the capital of " + ground)
								i = 1
				for ground in states:
					if arg.lower() == ground.lower():
						for citie in capital_cities:
							if states[ground] == citie:
								print(capital_cities[citie] + " is the capital of " + ground)
								i = 1
				if i == 0 and arg != "":
					print(arg + " is neither a capital city nor a state")
				i = 0
