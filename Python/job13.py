"""demander à l’utilisateur de renseigner un nombre entier.
Le programme devra alors parcourir le contenu du fichier “data.txt” compter le
nombre de mots de la taille renseignée qui s’y trouvent."""

nombre = int(input("Entrer un nombre entier : "))

with open("data.txt", "r") as fichier:
    lines = fichier.read().splitlines

nb_words = 0

for line in lines:
    liste = line.split()
    for element in liste:
        if len(element) == nombre:
            nb_words = nb_words + 1

print(nb_words)