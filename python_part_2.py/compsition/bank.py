from __future__ import annotations
from account_m import Account
# from person import Person


class BankService:
    def __init__(self, bank_name:str):
        bank_name = bank_name.strip()
        if not bank_name:
            raise ValueError("Bank name cannot be empty!")
        self._accounts = {}
        self._bank_name = bank_name.title()

    def __str__(self):
        lines = []
        lines.append(f"Bank: {self.bank_name}")
        lines.append("=" * 50)
        lines.append(f"{'Customer ID':<12} {'Name':<20} {'Balance':>10}")
        lines.append("-" * 50)

        for account in self._accounts.values():
            lines.append(
            f"{account.account_num:<12} "
            f"{account.name:<20} "
            f"{account.balance:>10,}"
        )

        lines.append("=" * 50)
        lines.append(f"Total customers: {len(self._accounts)}")
        return "\n".join(lines)

    def create_account(self, person:"Person", psw:str, initial_balance:int=0) -> Account:
        if not psw or len(psw.strip()) < 4:
            raise ValueError(f"[{person.customer_id}] Password too weak! Minimum 4 characters.")
        if initial_balance < 0:
            raise ValueError(f"[{person.customer_id}] Initial balance cannot be negative!")
        
        if person.customer_id in self._accounts:
            raise ValueError("you already have an account in this bank!")
        account = Account(person.customer_id, person.name, self.bank_name, psw, initial_balance)
        self._accounts[person.customer_id] = account
        return account

    def deposit(self, customer_id:int, amount:int, psw:str) -> bool:
        if customer_id not in self._accounts:
            raise ValueError(f"[{customer_id}] No account found in {self.bank_name}")

        account = self._accounts[customer_id]
        result = account.deposit(amount,psw)
        return result                

    def withdraw(self, customer_id:int, amount:int, psw:str) -> bool:
        if customer_id not in self._accounts:
            raise ValueError(f"[{customer_id}] No account found in {self.bank_name}")

        account = self._accounts[customer_id]
        result = account.withdraw(amount,psw)
        return result

    def close_account(self, customer_id:int, psw:str) -> bool:
        if customer_id not in self._accounts:
            raise ValueError(f"[{customer_id}] No account found in {self.bank_name}")

        account = self._accounts[customer_id]
        result = account.close_account(psw)
        if result:  # یعنی حساب با موفقیت بسته شد
            del self._accounts[customer_id]
        return result

    def get_balance(self, customer_id:int, psw:str) ->int:
        if customer_id not in self._accounts:
            raise ValueError(f"[{customer_id}] No account found in {self.bank_name}")

        account = self._accounts[customer_id]
        return account.get_balance(psw)


    @property
    def bank_name(self):
        return self._bank_name
    

