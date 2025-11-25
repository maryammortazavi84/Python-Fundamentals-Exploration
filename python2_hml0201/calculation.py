"""Safely divides a by b (EAFP style).
    
    Returns math.inf or -math.inf on division by zero.
    Raises clear TypeError if inputs are not numbers.
"""

import math

def safe_divide (a:float,b:float):
    try:
        return a / b
    except ZeroDivisionError:
        return math.inf if a >= 0 else -math.inf
    except TypeError as e:
        print("Error: Both inputs must be numbers!")
        print(f"Detail: {e}")
        return None


print(safe_divide(5,"j"))
        
        
