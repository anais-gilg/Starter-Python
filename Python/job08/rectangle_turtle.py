# dessiner un rectangle
import turtle

t = turtle.Turtle()

l=int(input("largeur :"))
h=int(input("hauteur :"))

#dessiner le premier coté
t.forward(h)
t.left(90)

#dessiner le deuxième coté
t.forward(l)
t.left(90)

#dessiner le troisième coté
t.forward(h)
t.left(90)

#dessiner le quatrième coté
t.forward(l)
t.left(90)