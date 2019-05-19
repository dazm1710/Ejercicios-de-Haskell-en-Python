def invertir(list):
    if list==[]:
        return[]
    return(invertir(list[1::])+list[:1])

a=[1,2,3,4,5]

print invertir(a)
