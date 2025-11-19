"""
main program. shows the menu to the user
"""
from bank import Bank 


# banks = {
#     'melli' : Bank("melli"),
#     'saman' : Bank("saman"),
# }

def validation(choice:str)->int:
    while True:
        if not choice.isdigit():
            choice = input("""
please enter a valid number!!!
1.open a new account
2.close your account
3.deposite
4.withdraw
5.balance inquary
6.exit
please enter your choice:  
""")
            continue
        if not 0< int(choice) <7:
            choice = input("enter a number between 1 to 6!!!")
            continue

        valid_choice = int(choice)    
        return(valid_choice)






def main():
    my_bank = Bank()
    while True:
        choice = (input("""
***welcome to your pannel***
1.open a new account
2.close your account
3.deposite
4.withdraw
5.balance inquary
6.exit
please enter your choice:  """))
        valid_choice = validation(choice)    
        if valid_choice == 1:
            my_bank.open_account()

        if valid_choice == 2:
            my_bank.close_account()

        if valid_choice == 3:
            my_bank.diposit()

        if valid_choice == 4:
            my_bank.withdraw()

        if valid_choice == 5:
            my_bank.balance()

        if valid_choice == 6:
            print("***THANK YOU FOR USING OUR PROGRAM:)))***")
            break
        

        
main()









