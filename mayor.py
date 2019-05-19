def mayor(list):
    if (list==[]):
        return False
    if(list[:1]>mayor(list[1::])):
       return list[:1]
    return mayor(list[1::])

a=[1,2,3,8,5,6]

print mayor(a)
