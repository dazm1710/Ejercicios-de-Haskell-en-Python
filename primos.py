def divisible (a,b):
    if(a%b==0):
        return True
    return False

def divisor(a):
    if(a==1):
        return [1]
    return [a]+divisor(a-1)

def dejarDivisibles(a,list):
    if(list==[]):
        return[]
    if(divisible(a,list[0])):
        return list[:1]+dejarDivisibles(a,list[1::])
    return dejarDivisibles(a,list[1::])

def esPrimo(a):
    if(a==0):
        return 0
    if(a==1):
        return [1]
    lista=divisor(a)
    if len(dejarDivisibles(a,lista))<=2:
        return True
    return False
    
def primos(num):
    if(num==0):
        return [0]
    if (num==1):
        return [1]
    if(esPrimo(num)):
        return (primos(num-1)+[num])
    return primos(num-1)

a=[1,2,3,4,5]
print primos(100)

"""
print divisor(6)
print divisible(6,4)
print divisibles(5)
""" 
