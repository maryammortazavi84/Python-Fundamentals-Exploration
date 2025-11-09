"""
Simple program to calculate the minimum and maximum 
from a list of numbers provided by the user. 
Demonstrates the use of functions and basic input handling.
"""

def menu():
    print("""
welcome
1.calculate min
2.calculate max
3.exit
          

 """)
def valid_input(user_input):
    # Check if the user input is valid
    if user_input == 1 or user_input == 2 or user_input == 3:
        return user_input
    else:
        print("your choice is not valid. enter 1, 2 or 3") 
        return None
def find_min():
    numbers = (input(" enter your number list with one space in between: "))
    numbers = numbers.split()
     # Get numbers from user and convert to integers
    numbers = [int(number) for number in numbers]
    min = numbers[0]
    for number in numbers:
        if number<min:
            min = number
    return min
def find_max():
    numbers = input(" enter your number list with one space in between: ")
    numbers = numbers.split()
    numbers = [int(number) for number in numbers]
    max = numbers[0]
    for number in numbers:
        if number>max:
            max = number
    return max



# Main program loop
while True:
    menu()
    user_input = int(input("enter your choice: "))
    choice = valid_input(user_input)
    if choice == 1:
         minimum = find_min()
         print(f'  min = {minimum}')
    elif choice == 2:
        maximum = find_max()
        print(f'  max = {maximum}')
    elif choice == 3:
        print("""thank you for using our program.
              BYE!
              """)
        break









