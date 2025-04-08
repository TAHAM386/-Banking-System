from abc import ABC, abstractmethod 

class BankAccount(ABC):
    def __init__ (self,account_number,balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
    def get_balance(self):
        return self.balance

    @abstractmethod
    def account_type(self):
        pass
    # base class for bank account
    # This code implements a simple banking system with two types of accounts: Savings and Current.
class SavingsAccount(BankAccount):
    def __init__ (self,account_number,balance=0,interest_rate=0.01):
        super().__init__(account_number,balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest 
        print(f"interest added: {interest}. New balance: {self.balance}")
    def account_type(self):
        return "Savings Account"
class CurrentAccount(BankAccount):
    def __init__ (self,account_number,balance=0,overdraft_limit=10000):
        super().__init__(account_number,balance)
        self.overdraft_limit = overdraft_limit
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds")
    def account_type(self):
        return "Checking Account"
    
account = {}

while True:
    print("==========================")
    print("1. Create Bank Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. exit")
    print("==========================")
    choice=int(input("Enter your choice: "))
    if choice == 1:
        acc_ID =(input("Enter Account ID: "))
       
        
        acc_type = input("Enter account type (savings/current): ").lower()
        if acc_type == "savings":
            account[acc_ID] = SavingsAccount(acc_ID)
            print("Account created successfully")
        elif acc_type == "current":
            account[acc_ID] = CurrentAccount(acc_ID)
            print("Account created successfully")
        else:
            print("Invalid account type")
            continue
    elif choice == 2:
        acc_ID = (input("Enter Account Number: "))
        amount = float(input("Enter amount to deposit: "))   
        if acc_ID in account:
            account[acc_ID].deposit(amount)
        else:
                print("Account not found")  
    elif choice == 3:
        acc_ID = (input("Enter Account ID: "))
        amount = float(input("Enter amount to withdraw: "))
        if acc_ID in account:
            account[acc_ID].withdraw(amount)
        else:
            print("Account not found")
    elif choice == 4:
        acc_ID = (input("Enter Account ID: "))
        if acc_ID in account:
            print(f"Account Balance: {account[acc_ID].get_balance()}")
        else:
            print("Account not found")
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
# This code implements a simple banking system with two types of accounts: Savings and Current.
