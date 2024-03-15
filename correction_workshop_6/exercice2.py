from functools import reduce
def calculer(*args, **kwargs):
    operation = kwargs.get('operation', lambda args:sum(args))
    # if operation == 'somme':
    #     return sum(args)
    # elif operation == 'moyenne':
    #     return sum(args) / len(args) if args else 0
    # elif operation == 'produit':
    #     return reduce(lambda x, y: x * y, args, 1)

    return operation(args)
    

print(calculer(1,4,4,5))
print(calculer(1,4,4,5, operation= lambda args: sum(args) / len(args) if args else 0))
print(calculer(1,4,4,5, operation=lambda args: reduce(lambda x, y: x * y, args, 1)))