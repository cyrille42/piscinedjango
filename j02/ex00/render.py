import sys
import re
import os

if __name__ == '__main__':
	if len(sys.argv) == 2:
		name = sys.argv[1].split(".")
		fichier_html = open(name[0]+ ".html",'a')#secure les open sur fichier non exitant et le fichier .template doit exister
		fichier = open(sys.argv[1], "r")
		contenu = fichier.read().split("\n")
		setting = open("settings.py", "r")
		contenu_setting = setting.read().split("\n")
		for arg in contenu:
			if re.match(r".*{*}.*", arg) != None:#si match dans template alors on va chercher le mot exact dans les corchet
				i = 0
				j = 0
				reg = ""
				while i < len(arg):
					if arg[i] == "{":#on va chercher largument dans la ligne du template
						i+=1
						while arg[i] != "}":
							reg += arg[i]
							i += 1
					else:
						i += 1
				for sett in contenu_setting:#on va chercher si sa match dans settings
					pier = sett.split("=")
					if re.match(reg , pier[0]) != None: #si sa match on va chercher le mot de remplacement et on replace
						pier[1] = pier[1].strip()
						pier[1] = pier[1].strip("\"")
						arg = arg.replace("{"+reg+"}",pier[1])
			fichier_html.write(arg+ "\n")
		fichier.close()
		setting.close()
		fichier_html.close()
