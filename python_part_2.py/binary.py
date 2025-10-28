#def binary(n, base):
#    if 0<= n <base :
#        return n
#    else:
#        return str(binary(n // base, base)) + str(n % base)

#print(binary(13,4))
from time import time
def decorator(fun):
    def caltime(*args, **kwargs):
        start = time()
        res = fun(*args, **kwargs)
        end = time()
        print(end - start)
        return res
    return caltime

@decorator
def convertor(n,base):
    b ="0123456789abcdefghijk"
    if 0<= n <base :
        return n
    else:
        return str(convertor(n//base ,base)) + b[n%base]
print(convertor(22515484665156484646,16))

    