"""Le programme devra contenir une fonction qui prend en
paramètres un nombre de paramètres indéfini."""

def myFonction( *params ):
    print(params)

myFonction("toto", "tata")