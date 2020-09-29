class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        self.account2 = BankAccount(int_rate=0.02, balance=1)
    def make_deposit(self,accountNum, amount):
        if accountNum != 2:
            print(f"Balance was: ${self.account.balance}")
            self.account.balance += amount
            print(f"Deposited ${amount} into {self.name}'s BankAccount{accountNum} \nBalance is now: ${self.account.balance}")
        elif accountNum == 2:
            print(f"Balance was: ${self.account2.balance}")
            self.account2.balance += amount
            print(f"Deposited ${amount} into {self.name}'s BankAccount{accountNum} \nBalance is now: ${self.account2.balance}")
        return self
    def make_withdrawl(self,accountNum, amount):
        if accountNum != 2:
            print(f"Balance was: ${self.account.balance}")
            self.account.balance -= amount
            print(f"Withdrew ${amount} from {self.name}'s BankAccount{accountNum} \nBalance is now: ${self.account.balance}")
        elif accountNum == 2:
            print(f"Balance was: ${self.account2.balance}")
            self.account2.balance -= amount
            print(f"Withdrew ${amount} from {self.name}'s BankAccount{accountNum} \nBalance is now: ${self.account2.balance}")
        return self
    def have_display_account_info(self, accountNum):
        if accountNum != 2:
            self.account.display_info = print(f"Balance of {self.name}'s BankAccount{accountNum}: ${self.account.balance}")
        elif accountNum == 2:
            self.account.display_info = print(f"Balance of {self.name}'s BankAccount{accountNum}:${self.account2.balance}")
        return self
class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        elif self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5    
        return self
    def display_account_info(self):
        self.display_info = print(f"Balance: ${self.balance}") 
        return self
    def yield_interest(self):
        if self.balance >= 0:
            self.balance += (self.balance * self.int_rate)
        return self
mitchell = User("Mitchell Golden", "aRealEmail@mail.com")
adrien = User("Adrien Dion", "LiteralRubixGod@mail.com")
mitchell.have_display_account_info(1)
mitchell.have_display_account_info(2)
mitchell.make_deposit(2, 100)
mitchell.make_withdrawl(2, 100)
mitchell.make_deposit(1, 1000)
mitchell.make_withdrawl(1, 500)
adrien.have_display_account_info(1)
adrien.have_display_account_info(2)
adrien.make_deposit(2, 100)
adrien.make_withdrawl(2, 100)
adrien.make_deposit(1, 1000)
adrien.make_withdrawl(1, 500)