# dessiner un triangle
import turtle # j'invoque la tortue mdr

t = turtle.Turtle()

l=int(input("largeur :"))
h=int(input("hauteur :"))

#dessiner le premier coté
t.forward(l) # je commence par la largeur pour faire le socle
t.left(120) # 120 représente le degré d'inclinaison de mon angle

#dessiner le deuxième coté
t.forward(h)
t.left(120) 

#dessiner le troisième coté
t.forward(h)
t.left(120)