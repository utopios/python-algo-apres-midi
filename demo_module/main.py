from math import pi
from functools import reduce
import librairies.fonctions as f1



def main():
    f1.dire_bonjour()
    liste_a = [1,2,3]
    print(reduce(lambda a,b: a+b, liste_a))

if __name__ == "__main__":
    main()