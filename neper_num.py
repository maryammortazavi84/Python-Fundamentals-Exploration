"""
This program calculates the exponential value e^x using
the Taylor series expansion up to n terms.
It takes x and n as user inputs.
"""
#Returns a list of powers of x from x¹ to xⁿ
def cal_x(x:float, n:int) -> list:
    x_list =[]
    for num in range(1, n+1):
        x_list.append(x**num)
    return x_list

#Returns a list of factorials from 1! to n!.
def factorial(n:int) -> list:
    factorial_list = []
    for f in range(1,n+1):
        result = 1
        for i in range(1,f+1):
            result *= i
        factorial_list.append(result)
    return factorial_list

#main code
x = float(input("enter x: "))
n = int(input("enter n: "))
x_list = cal_x(x, n)
factorial_list = factorial(n)
neper = 1

for i in range(1,n+1):
    neper += (x_list[i-1]/factorial_list[i-1])

print(f'the result is: {neper:.3f}')