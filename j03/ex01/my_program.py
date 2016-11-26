from path import path
import os

if __name__ == '__main__':
	path.mkdir('./test')#error si dossier existe deja
	fichier = open("test/fichier.txt", "a")
	fichier.write("pierrus le pgm")
	fichier = open("test/fichier.txt", "r")
	contenu = fichier.read()
	print(contenu)