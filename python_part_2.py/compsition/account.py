class Account:
    number_of_created_account = 0
    def __init__(self, name, psw, balance):
        self.name = name
        self.psw = psw
        self._block_balance = 0
        self._balance = balance
        Account.number_of_created_account +=1
        self.account_number = Account.number_of_created_account
        self.is_closed = False

    def _validate_amount_psw(self, amount, psw):
        if self.is_closed:
            print("sorry your account is blocked")
            return False
        
        if psw != self.psw:
            print("wrong password!")
            return False

        if amount<0:
            print("invalid data!")
            return False
        
        return True

    def deposite(self, amount, psw) -> bool:
        flag = self._validate_amount_psw(amount, psw)
        if flag:
            self._balance += amount
        
        return flag

    def withdraw(self, amount, psw):
        flag = self._validate_amount_psw(amount, psw)
        if not flag:
            return False

        if self.getbalance() < amount:
            print("not enough balance!")
            return False

        self._block_balance -= amount
        self._balance -= amount
        return True
    
    def block_balance(self, amount, psw):
        flag = self._validate_amount_psw(amount, psw)
        if flag:
            self._block_balance += amount
        
        return flag    

    def getbalance(self):
        return self._balance - self._block_balance
    
    def close_account(self, pwd):
        if not self._validate_amount_psw(0,pwd):
            return False
        self.is_closed = True

    def reopened(self, pwd):
        if not self._validate_amount_psw(0,pwd):
            return False
        self.is_closed = False


    def __str__(self):
        return f"{self.name} {self.getbalance()}"



#check the code.....
#a1 = Account("mary",1234,5000)
#a2 = Account("ali",4567,8000)
#print(f'we have {Account.number_of_created_account} accounts ---> {a1},{a2}')

#print("\n--- Mary deposits 1000 ---")
#a1.deposite(1000,1234)
#print(a1)

#print("\n--- Ali blocks 2000 ---")
#a2.block_balance(2000, 4567)
#print(a2)

#print("\n--- Ali tries to withdraw 4000 (should fail, because 2000 blocked) ---")
#a2.withdraw(9000, 4567)
#print(a2)

#print("\n--- Ali withdraws 2000 (ok) ---")
#a2.withdraw(2500, 4567)
#print(a2)

#print("\n--- Ali releases the 2000 blocked ---")
#a2.block_balance(0, 4567)
#print(a2)
#a1 = Account("mary", 1234, 1000)

#print("\n--- Try withdrawing more than balance ---")
#a1.withdraw(5000, 1234)

#print(a1)
