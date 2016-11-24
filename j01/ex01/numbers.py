if __name__ == '__main__':
	fichier = open("numbers.txt", "r")
	contenu = fichier.read().split(",")
	for i in range(len(contenu)):
		print (int(contenu[i]))
	fichier.close()