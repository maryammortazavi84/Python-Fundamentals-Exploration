from __future__ import annotations
from account_m import Account
# from bank import BankService
from pathlib import Path
all_customers = []

def save_all_customers(file_name="customer.txt"):
    lines = []
    for person in all_customers:
        parts = []
        parts.append(person.name)
        parts.append(str(person.customer_id))

        account_str = []

        for bank_name,acc in person.accounts.items():
            account_line = f"{acc._psw}:{bank_name}:{acc.balance}:{acc._block_balance}" 
            account_str.append(account_line)
            
        if account_str:
            parts.append("|".join(account_str))
        else:
            parts.append("")

        line = "|".join(parts)
        lines.append(line)

            
    path = Path(file_name)
    path.write_text("\n".join(lines), encoding="utf-8")

def load_all_customers(file_name="customer.txt"):
    all_customers.clear()
    try:
        with open(file_name, "r",encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                name = parts[0]
                cust_id = int(parts[1])
                account_parts = parts[2:]
                person = Person(name)
                person._customer_id = cust_id

                for acc_str in account_parts:
                    if not acc_str:
                        continue
                    psw, bank, bal, blockd = acc_str.split(":")

                    acc = Account(cust_id, name, bank, psw, int(bal))
                    person.accounts[bank] = acc
                    acc._block_balance = int(blockd)


    except FileNotFoundError:
        pass


                    



class Person:
    _next_customer_id = 1000

    def __init__(self, name:str, master_password: str = None):
        cleaned_name = name.strip()
        if not cleaned_name:
            raise ValueError("[Security] Person name cannot be empty or just spaces!")
        if cleaned_name.isdigit() or len(cleaned_name) < 3:
            raise ValueError("[Security] Person name must contain letters and be at least 3 characters long!")
        if not any(c.isalpha() for c in cleaned_name):
            raise ValueError("[Security] Person name must contain at least one letter!")
        
        self._name = cleaned_name.title()
        self._customer_id = Person._generate_id()
        self.accounts: dict[str, Account] = {}
        self._master_password = master_password

        if master_password is None:
            self._master_password = "1234"

        all_customers.append(self)

    def __str__(self):
        result = []
        result.append("=" * 75)
        result.append(f"Person: {self.name}")
        result.append(f"Customer ID: {self.customer_id}")
        result.append(f"Total accounts: {len(self.accounts)}")
        result.append("=" * 75)
    
    # سرستون‌ها
        result.append(f"{'Bank':<12} {'Acc No':<12} {'Balance':>15} {'Available':>15} {'Blocked':>12}")
        result.append("-" * 75)
    
    # هر حساب — فقط یک f-string بزرگ!
        for bank_name, account in self.accounts.items():
            result.append(
                f"{bank_name:<12} "                  # بانک چپ‌چین
                f"{self.customer_id:<12} "
                f"{account.balance:>15}"      # شماره حساب (نه customer_id!)
                f"{account.available_balance:>15,} "  # اعداد راست‌چین + کاما
                f"{account.block_balance:>12,} "    # درستش اینه: blocked_balance
            )

        result.append("=" * 75)
        result.append(f"{'Total Balance:':<20} {self.total_balance:>20,}")
        result.append(f"{'Total Available:':<20} {self.total_available_balance:>20,}")
    
        result.append("=" * 75)
    
        return "\n".join(result)
    
    def open_account(self, bank:"BankService", psw:str, initial_balance:int=0) -> None:
        if bank.bank_name in self.accounts:
            raise ValueError(f"[{self.customer_id}] :You already have an account in {bank.bank_name}!")

        account = bank.create_account(self, psw, initial_balance)
        self.accounts[bank.bank_name] = account
        print(f"Account successfully opened in {bank.bank_name} | Acc No: {self.customer_id}")

    def get_account(self, bank_name:str) -> Account:
       bank_name = bank_name.strip().title()
       if bank_name not in self.accounts:
           raise ValueError(f"[{self.customer_id}] :No account found in {bank_name}")
       return self.accounts[bank_name] 
    
    def deposit_to(self, amount:int, psw:str, bank:"BankService") -> None:
        """Deposit money into one of the person's bank accounts."""
        success = bank.deposit(self.customer_id, amount, psw)
        if not success:
            raise ValueError("Deposit failed")

    def withdraw_from(self, amount:int, psw:str, bank:"BankService") -> None:
        """Withdraw money from one of the person's bank accounts."""
        success = bank.withdraw(self.customer_id, amount, psw)
        if not success:
            raise ValueError("withdraw failed")

    @classmethod
    def _generate_id(cls):
        cls._next_customer_id += 1 
        return cls._next_customer_id 
     
    @classmethod
    def find_by_id(cls, customer_id:int) -> Person | None:
        for customer in all_customers:
            if customer.customer_id == customer_id:
                return customer
        return None
        
    @classmethod
    def find_by_name(cls, name:str) -> list:
        name = name.title()
        all_found =[]
        for customer in all_customers:
            if customer.name == name:
               all_found.append(customer)

        return all_found 
    
    @staticmethod
    def login() -> Person:
        while True:
            user_input = input("Please enter your id or your name: ").strip()

            selected_person = None 

            try:
             
                cust_id = int(user_input)
                selected_person = Person.find_by_id(cust_id)
                if not selected_person:
                    print("ID not found. Try again.")
                    continue

            except ValueError:
           
                found_persons = Person.find_by_name(user_input)

                if not found_persons:
                    print("Name not found. Try again.")
                    continue

                if len(found_persons) == 1:
                    selected_person = found_persons[0]
                else:
                    print("Multiple users found:")
                    for i, u in enumerate(found_persons, 1):
                        print(f"{i}. {u.display_name}")

                    try:
                        choice = int(input("Please select by number: ")) - 1
                        selected_person = found_persons[choice]
                    except (ValueError, IndexError):
                        print("Invalid selection. Try again.")
                        continue

           
            while True:
                master_psw = input("Enter your master password: ")
                if master_psw == selected_person._master_password:
                    print(f"Welcome {selected_person.display_name}!")
                    return selected_person
                else:
                    print("Wrong master password. Try again.")

    @property
    def total_balance(self) -> int:
       """Total money across all accounts (including blocked amounts)"""
       return sum(account.balance for account in self.accounts.values())

    @property
    def total_available_balance(self) ->int:
        """Total money that can actually be withdrawn right now"""
        return sum(account.available_balance for account in self.accounts.values())         

    @property
    def name(self):
        """Person's full name - immutable after creation"""
        return self._name

    @property
    def display_name(self):
        return f"{self._name} (ID: {self.customer_id})"

    @property
    def customer_id(self):
        """Unique and immutable customer identifier - starts from 1001"""
        return self._customer_id


       







    





 