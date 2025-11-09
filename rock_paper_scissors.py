"""
play rock paper scissors!
"""

import random
print(" lets play rock paper scissors! 1 is rock , 2 is paper , and 3 is scissors")
print()
while True:
    user = int(input("rock paper or scissors? "))
    if 0<user<4:       # Check if input is valid
        computer = random.randint(1,4)
        print(f' your choice was {user} and my choice was {computer}')     # Show both choices as text
        if (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):    # Determine the winner
            print("YOU WON! :)))")
        elif (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user ==3 and computer == 1):    # Determine the loser
            print("you lost! :(((")
        elif user == computer:
            print("teid")
    else:
        print("enter a number from 1 to 3")   # Invalid input
        continue