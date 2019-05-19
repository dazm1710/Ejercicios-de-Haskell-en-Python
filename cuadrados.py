def cuadrados(list):
    if(list==[]):
        return []
    list[0]=list[0]*list[0]
    return [list[0]]+cuadrados(list[1::])

a=[1,2,3,4,5,6,7,8]
print cuadrados(a)
