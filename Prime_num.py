"""
This program checks whether a given number is a prime number or not.
It asks the user to input a number greater than 1 and validates the input.
The user can run the program multiple times as specified.
"""

def prime_num():
    number = int(input("enter the number: "))
    is_prime = True
    while number<=1:
        # validate input (number must be greater than 1)
        print(" enter a number greater than 1. 0 and 1 are not prime numbers!")
        number = int(input("enter the number: "))
    for num in range(2 , number-1):# check divisibility from 2 to number-1 ps. I know there is a better way to check it but it was hard math so i did it this way:)))
        if number % num == 0:
            is_prime = False
            break
    if is_prime:
        print("its a prime number.")
    else:
        print("its not a prime number.")        

    


# allow user to repeat the program multiple times
repeat = int (input('how many times do you want to use this program? '))
for _ in range(repeat):
    prime_num()