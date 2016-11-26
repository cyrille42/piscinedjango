import sys
import requests
import dewiki

if __name__ == '__main__':
	if len(sys.argv) ==	2:
		r = requests.get('https://fr.wikipedia.org/wiki/'+ sys.argv[1])
		# print (r.text)
		zgeg = dewiki.Parser()
		# name = sys.argv[1].replace(" ", "")
		# fichier = open(name+".wiki", "a")
	else:
		print("only one arg needed")