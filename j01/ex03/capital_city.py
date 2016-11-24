import sys

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
		for number in states:
			if sys.argv[1] == number:
				for citie in capital_cities:
					if states[number] == citie:
						print(capital_cities[citie])
						i = 1
		if i == 0:
			print("Unknow state")