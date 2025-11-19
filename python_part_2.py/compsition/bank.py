from account import Account


class Bank:
    def __init__(self,name):
        self._accounts = {}
        self.name = name

    def creat_account(self, name, starting_balance, pasword):
        print("*** attempt to create an account ***")
        account = Account(name, pasword, starting_balance)
        self._accounts[account.account_number] = account
        
        return account

    def open_account(self):
        print("*** open account ***")
        user_name = input("what is the new account name? ")
        user_starting_balance = int(input("what is your starting amount? "))
        user_pass= int(input("what is your new password? "))
        user_account = self.creat_account(user_name, user_starting_balance, user_pass)
        print(f"your new account number is {user_account.account_number}\n")

    def close_account(self):
        print("*** close account ***")
        account_number = int(input("enter account number: "))
        password = int(input("enter password: "))

        account = self._accounts.get(account_number)
        if not (account):
            print("wrong data!")
            return 
        
        if  not account.close_account(password):
            return
        print("✅ Account closed successfully!")


    def diposit(self):
        print("*** deposit ***")
        account_number = int(input("enter account number: "))
        amount = int(input("enter amount: "))
        password = int(input("enter password: "))


        account = self._accounts.get(account_number)
        if not (account):
            print("wrong data!")
            
            return 

        success = account.deposite(amount, password)
        if success:
            print("✅ Deposit successful!")
        else:
            print("❌ Deposit failed.")
        

    def withdraw(self):
        print("*** withdraw ***")

        account_number = int(input("Enter account number: "))
        amount = int(input("Enter amount: "))
        password = int(input("Enter password: "))

        account = self._accounts.get(account_number)
        if not account:
            print("❌ Wrong account number!")
            return
        
        success = account.withdraw(amount, password)
        if success:
            print("✅ Withdrawal successful!")
        else:
            print("❌ Withdrawal failed.")


    def balance(self):
        print("*** balance inquiry ***")
        account_number = int(input("Enter account number: "))
        password = int(input("Enter password: "))

        account = self._accounts.get(account_number)
        if not account:
            print("❌ Wrong account number!")
            return

        if password != account.psw:
            print("❌ Wrong password!")
            return

        print(f"💰 Your available balance: {account.getbalance()}")



        



# -------------------- Test Section --------------------
# Create two sample accounts manually
# bank = Bank()
# for _ in range(3):
#     bank.open_account()   

# bank.close_account()
# bank.diposit()
# bank.withdraw()
# bank.balance()







