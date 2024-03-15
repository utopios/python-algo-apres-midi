
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
# liste_a = []

# def ajouter_dans_la_liste(element:str):
#     #liste_a = []
#     liste_a.append(element)


# ajouter_dans_la_liste("element 1")
# ajouter_dans_la_liste("element 2")

# print(liste_a)

def addition(message, *elements):
    print(message)
    total = 0
    for a in elements:
        total += a
    return total

print(addition(1,2,3,4))
print(addition(1,2,3,4,6,7,8,9,32))
print(addition(1,2,3))

def avec_kwargs(**kwargs): 
    print(kwargs)

avec_kwargs(cle1="val1", cle2="val2")

def avec_args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

avec_args_kwargs(1,3,4,True, "a", cle1="val1", cle2="val2")