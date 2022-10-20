"""parcourir le contenu du fichier “data.txt” et compter
le nombre de mots (sans caractère spéciaux) qui s’y trouvent."""
#Avec Regex, l'importer avec re

import re

f = open("data.txt", "r")
#ouvrir data.txt pour le lire seulement
text = f.read()
pattern = '[a-zA-Z]+'
matches = re.findall("patern", text)
#patern cest la condtition regex