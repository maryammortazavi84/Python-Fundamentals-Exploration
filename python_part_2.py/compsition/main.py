"""
main program. shows the menu to the user
"""
from pathlib import Path
from bank import BankService 
from person import Person, load_all_customers, save_all_customers
from account_m import Account
from person import all_customers

banks = {
    "Melli": BankService("Melli"),
    "Saderat": BankService("Saderat"),
    "Sepah": BankService("Sepah"),
}

def get_bank_from_user() -> BankService | None:
    bankname = input("Enter bank name: ").strip().title()
    
    if bankname not in banks:
        print(f"Bank '{bankname}' not found!")
        print(f"Available banks: {', '.join(banks.keys())}")
        return None
    
    return banks[bankname]

load_all_customers()
for person in all_customers:
    for bank_name, account in person.accounts.items():
        bank = banks.get(bank_name)  
        if bank and person.customer_id not in bank._accounts:
            bank._accounts[person.customer_id] = account

print("Welcome to the Banking System")
print("Previous customer data loaded successfully\n")

def show_main_menu():
    print("**********MAIN MENU**********")
    print("""1. Register new customer
2. Login
3. Exit""")
    
def register_new_person() -> Person:
    name = input("Please enter your name: ")
    master_psw = input("Create a master password (for login security, min 4 chars): ")
    if len(master_psw) < 4:
        print("Master password too short!")
        return register_new_person()
    customer = Person(name, master_psw)
    return customer
    
def show_customer_menu() -> None:
    print("**********CUSTOMER MENU**********")
    print("""1. Open new account in a bank
2. Deposit to an account
3. Withdraw from an account
4. View full customer information(all accounts + totals)
5. close an account
6. Log out""")
    
def customer_menu(person: Person) ->None:
    while True:
        show_customer_menu()
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
        except ValueError as e:
            print(f'Enter a valid number!\nDetails: {e}')
            continue

        if not 0 < choice < 7:
            print("Enter a number between 1 to 6!")
            continue
        
        if choice == 1:
            bank = get_bank_from_user()
            if bank is None:
                continue
            psw = input("Enter your password: ")
            initial_balance = input("Enter your initial balance: ")
            try:
                initial_balance = int(initial_balance)
            except ValueError as e:
                print("Invalid input!.\nDetails:",e)
                continue
            
            try:
                person.open_account(bank, psw, initial_balance)  
                save_all_customers()  
                print("Account opened successfully!")  
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 2:
            bank = get_bank_from_user()
            if bank is None:
                continue
            psw = input("Enter your password: ")
            amount = input("Enter the amount: ")
            try:
                amount = int(amount)
            except ValueError as e:
                print("Invalid input!\nDetails: ",e)
                continue

            try:
                person.deposit_to(amount, psw, bank)  
                save_all_customers() 
                print("Deposit successful!") 
            except ValueError as e:
                print(f"Error: {e}")


        elif choice == 3:
            bank = get_bank_from_user()
            if bank is None:
                continue
            psw = input("Enter your password: ")
            amount = input("Enter the amount: ")
            try:
                amount = int(amount)
            except ValueError as e:
                print("Invalid input!\nDetails: ",e)
                continue

            try:
                person.withdraw_from(amount, psw, bank) 
                save_all_customers() 
                print("Withdraw successful!") 
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == 4:
            print(person)

        elif choice == 5:
            bank = get_bank_from_user()
            if bank is None:
                continue

            psw = input("Enter your password: ")

            success = bank.close_account(person.customer_id, psw)
            if success:
                del person.accounts[bank.bank_name]
                print(f"Account in {bank.bank_name} successfully closed.")
            else:
                print("Failed to close the account.")

        else:
            print("Thanks for using our program.")
            break





while True:
    show_main_menu()
    choice = input("Enter your choice: ")
    try:
        choice = int(choice)
    except ValueError as e:
        print("Invalid input!\nDetails: ",e)
        continue
    if not 0 < choice < 4 :
        print("Enter a number between 1 to 3!")
        continue
    
    if choice == 1:
        try:
            new_person = register_new_person()
            save_all_customers()
            print(f"Registration successful! Welcome {new_person.display_name}")
            print("You can now login.")
        except ValueError as e:
            print(f"Registration failed: {e}")
            print("Please try again with a valid name.\n")

    elif choice == 2:
        person = Person.login()
        if person:
            try:
                customer_menu(person)
                save_all_customers()
            except ValueError as e:
                print(f"An error occurred: {e}")
                print("Returning to main menu...\n")

    else:
        save_all_customers()
        print("Thanks for using our program.")
        break

     

        










