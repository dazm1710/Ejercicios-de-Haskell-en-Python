def listaOrdenada(list):
    if(list==[]):
        return True
    if(list[1::]==[]):
        return True
    if((list[:1]<=list[1:2])&listaOrdenada(list[1::])):
            return True
    return False

a=[1,2,3,4,5,6]
b=[5,4,1,2,3]
print listaOrdenada(a)
print listaOrdenada(b)
