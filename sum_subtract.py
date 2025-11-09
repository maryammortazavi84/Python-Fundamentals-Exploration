"""
This program calculates the value of the equation:
1 - 2 + 3 - 4 + 5 ... ± n
and prints the expression with the result.
"""
#getting the input and check if its valid
n = int (input("please enter a number: "))
total = 0
expre = ""
if n < 1 :
    print("enter a number greater than 0")
else:
    for i in range (1 , n+1):  #loop through numbers from 1 to n 
        if i == 1 :            #first number (always positive)
            expre += "1"       
            total += 1
        elif i % 2 == 0:       #subtract even numbers
            total -= i
            expre+= f'-{i}'
        else:
            total += i         #add odd numbers
            expre += f'+{i}'
    print (f'{expre} = {total}')




