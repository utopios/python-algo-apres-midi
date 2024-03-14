
# def dire_bonjour(firstname:str, lastname:str="TATA", age:int=0):
#     print(f"Bonjour {firstname} {lastname} {age*2}")

# def dire_bonjour(name):
#     print(name)

# dire_bonjour("ihab", "Abadi","36")
# dire_bonjour("Jean", "Dupond",100)
# dire_bonjour("Toto")

# def carre(nombre:int) -> int:
#     return nombre**2

# resultat_carre_134 = carre(134)
# print(resultat_carre_134)

## Variable non muable
# a = 10

# def multiple_2():
#     global a
#     a *= 2
#     print(a)



# print(f"Avant ==> {a}")

# multiple_2()

# print(f"Après ==> {a}")

## Pour les mutables
liste_a = []

def ajouter_dans_la_liste(element:str):
    #liste_a = []
    liste_a.append(element)


ajouter_dans_la_liste("element 1")
ajouter_dans_la_liste("element 2")

print(liste_a)


