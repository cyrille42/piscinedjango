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
		for citie in capital_cities:
			if sys.argv[1] == capital_cities[citie]:
				for ground in states:
					if (citie == states[ground]):
						print(ground)
						i = 1
		if i == 0:
			print("Unknow capital city")
