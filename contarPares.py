def dejarPares(list):
    if(list==[]):
        return[]
    if(list[0]%2==0):
        return list[:1] + dejarPares(list[1::])
    return dejarPares(list[1::])

def contarPares(list):
    list=dejarPares(list)
    return len(list)

a=[1,2,3,4,5,6,7,8,8,10,9]

print contarPares(a)
