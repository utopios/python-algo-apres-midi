operation_addition = lambda a,b: a+b

def calculatrice(a,b, operation):
    # match operation:
    #     case "addition":
    #         return a + b
    #     case "soustraction":
    #         return a - b 
    return operation(a, b)

# print(calculatrice(10,30, "addition"))
print(calculatrice(10,30, operation_addition))
print(calculatrice(10,30, lambda a,b: a - b))
print(calculatrice(10,30, lambda a,b: a * b))

liste_a = [10,30,5,60]

# def filtrer_list(liste_elements, fonction_condition):
#     ## 
#     resultat = []
#     for element in liste_elements:
#         if fonction_condition(element):
#             resultat.append(element)
#     return resultat

# print(filtrer_list(liste_a, lambda a: a > 0))
# print(filtrer_list(liste_a, lambda a: a < 30))

print(list(filter(lambda element: element > 10, liste_a)))


print(list(map(lambda e: e**2, liste_a)))