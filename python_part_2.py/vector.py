import math

class vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    

    def __abs__(self):
        return math.hypot(self.x , self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self,other):
        return vector(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"Vector({self.x!r},{self.y!r})"
    


print(vector("1",3))
v = vector(0, 0)
if v:
    print("non-zero vector")
else:
    print("zero vector")

