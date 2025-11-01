class Account:
    def __init__(self, name, psw, balance):
        self.name = name
        self.psw = psw
        self._block_balance = 0
        self._balance = balance

    def _validate_amount_psw(self, amount, psw):
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
        if flag:
            self._block_balance -=amount
            self._balance -= amount
        
        return flag
    
    def block_balance(self, amount, psw):
        flag = self._validate_amount_psw(amount, psw)
        if flag:
            self._block_balance += amount
        
        return flag    

    def getbalance(self):
        return self._balance - self._block_balance
    
    def __str__(self):
        return f"{self.name} {self.getbalance()}"


a1 = Account("mary" , 1234, 1000)
a2 = Account("ali", 7891, 4000)
print(a1)
print(a2)
a1.deposite(100,1234)
print(a1)
a2.withdraw(200,7891)
print(a2)     
a1.withdraw(1123,1234)
print(a1)
