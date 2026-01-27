"""
creating a decorator for validation
"""

def validate_transaction(func):
    def wrapper(self, amount, psw:str):
        if self._is_closed:
            raise ValueError(f'[{self.account_num}] is closed!')
        if psw != self._psw:
            raise ValueError(f'[{self.account_num}] - invalid password!')
        if amount is not None and amount<0:
            raise ValueError(f"Account [{self.account_num}] - Amount must be positive!")
        
        return func(self,amount,psw)
    return wrapper
