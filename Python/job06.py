"""un prompteur doit s’afficher “>”, et le programme devra attendre un input.
Si l’input entré est “Bonjour”, le programme devra répondre “Bonjour à toi”
Si l’input entré est “Au revoir”, le programme devra quitter"""

a=str(input(">"))

while True:
  if a == "Bonjour": 
    print("Bonjour à toi")
    a=str(input(">"))
    
  elif a == "Au revoir":
    break
  
  else :
    print(a)
    a=str(input(">"))