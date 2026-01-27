"""
Bank Account class for a person in a specific bank.

Each person can have accounts in multiple banks, but the account number
is the same across all banks (equal to the person's customer_id).

Features:
    - Account number is immutable (read-only)
    - Balance cannot go negative
    - Part of the balance can be blocked (e.g., for checks or loans)
    - Account can be permanently closed
    - All important operations require password verification
"""



from validators import validate_transaction

class Account:

    def __init__(self,account_num:int,name:str, bank_name:str,psw:str,balance:int=0,):
        """
    Initialize a new bank account.

    Args:
        account_num (int): Account number (always equal to person's customer_id)
        name (str): Account holder's name
        bank_name (str): Name of the bank (e.g., "Sepah", "Mellat")
        psw (str): Password for the account
        balance (int, optional): Initial balance. Defaults to 0.
    """
        self._name = name.strip()
        self._psw = psw
        self.balance = balance
        self._is_closed = False
        self._block_balance = 0
        self._account_num = account_num
        self._bank_name = bank_name

    def __str__(self):
        return(f"account[{self.account_num}]: {self._name} \navailable balance: {self.available_balance}")
    
    @validate_transaction
    def block_amount(self,amount:int,psw:str) -> bool:
        if amount > self.available_balance or amount <= 0:
            raise ValueError(f"[{self.account_num}] not enough balance or invalid input.")
        self._block_balance += amount
        return True

    @validate_transaction
    def unblock_amount(self,amount:int,psw:str) -> bool:
        if amount <= 0:
            raise ValueError(f"[{self.account_num}] invalid input")
        self._block_balance = max(0,self._block_balance - amount)
        return True

    @validate_transaction
    def deposit(self, amount:int, psw:str) -> bool:
        self.balance += amount
        return True
    
    @validate_transaction
    def withdraw(self, amount:int, psw:str) -> bool:
        if amount>self.available_balance:
            raise ValueError(f"[{self.account_num}] Insufficient balance!")
        self.balance -= amount
        return True
    
    def close_account(self, psw:str) -> bool:
        if self._is_closed:
            raise ValueError(f"[{self.account_num}] Account already closed!")  
        if psw != self._psw:
            raise ValueError(f"[{self.account_num}] Wrong password!")
        self._is_closed = True
        return True 

    def get_balance(self, psw:str) -> int:
        if psw != self._psw:
            raise ValueError(f"[{self.account_num}] Wrong password!")
        return self.available_balance

    @property
    def is_closed(self):
        return self._is_closed 

    @property
    def block_balance(self):
        return self._block_balance
    
    @property
    def bank_name(self):
        return self._bank_name

    @property
    def account_num(self):
        return self._account_num
    
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,amount:int):
        if amount<0:
            raise ValueError(f"[{self.account_num}] Balance cannot be negative!")
        self._balance = amount

    @property
    def available_balance(self) -> int:
        return self.balance - self._block_balance

    @property
    def name(self):
        return self._name 
    


