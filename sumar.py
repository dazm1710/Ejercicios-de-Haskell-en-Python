def sumar(list):
    if list==[]:
        return 0
    return list[0]+sumar(list[1:])

a=[1,2,3,4,5]
print sumar(a)
