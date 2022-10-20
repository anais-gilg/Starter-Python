"""Écrire un programme triangle.py qui affiche dans le terminal un triangle avec des ‘_’, des
\ et des /
en fonction de l’input entré, qui représentera la hauteur."""

left = "/"
right = "\\" #mettre deux antislash si on veut en afficher un
base = "__"

userinput = int(input("Hauteur :"))

for i in range(userinput):
    print((userinput - i) * " " + left + ((i * 2) * " ")+ right)
    # * " " veut dire je met autant d'espace que multiplié
    if i == userinput - 1:
        print(left + base * userinput + right)