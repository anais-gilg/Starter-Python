a=int(input("Valeur 1 :"))
b=int(input("Valeur 2 :"))
if a < b:
    for i in range(a + 1,b):
        print(i)
elif a > b:
    for i in range(a -1, b, -1):
        print(i)
else:
    print("Valeurs égales")