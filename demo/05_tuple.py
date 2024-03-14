# Pour déclarer un tuple, on utilise la syntaxe entre parenthèse
# ou simplement on sépare les éléments avec une virgule
ma_tuple = (1, 2, 3, 4, 5)
ma_tuple = 1, 2, 3, 4, 5


print(ma_tuple)
for element in ma_tuple:
    print(element)


ma_tuple = (1, 2, 3, 4, 5)
var1, var2, var3, var4, var5 = ma_tuple
#var1, var2, var3, var4, var5 = (1, 2, 3, 4, 5)
print(var1)



# la variable underscore "_" dans python
# sert à "se débarasser" de valeurs inutiles 
_ = 2
print(_)

var1, _, _, _, var5 = ma_tuple
print(var1)
print(var5)