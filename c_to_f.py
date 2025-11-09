"""
convert c to f
"""


#functions
def c_to_f(c:int)-> int:
    return 32 + (1.8 * c)
c =input("enter c: ")
c = c.split(",")
#main code
numbers = map(float, c)
f = map(c_to_f , numbers)
print(list(f))

