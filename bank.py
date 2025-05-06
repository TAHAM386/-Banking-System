
import json
import os

from abc import ABC, abstractmethod 

class BankAccount(ABC):
    def __init__ (self,account_number,balance=0): # constructor for bank account

        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):  # deposit method for bank account
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive")
    def withdraw(self, amount):# withdraw method for bank account
        if amount > 0 and amount <= self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
    def get_balance(self):# get balance method for bank account
        return self.balance
# base class for bank account
    @abstractmethod
    def account_type(self):
        pass
   
    # This code implements a simple banking system with two types of accounts: Savings and Current.
class SavingsAccount(BankAccount):
    def __init__ (self,account_number,balance=0,interest_rate=0.01):# constructer for saving acccount
        super().__init__(account_number,balance) # recalling the constructor of the base class
        self.interest_rate = interest_rate
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest 
        print(f"interest added: {interest}. New balance: {self.balance}")
    def account_type(self):
        return "Savings Account"
class CurrentAccount(BankAccount):
    def __init__ (self,account_number,balance=0,overdraft_limit=10000): # constructor for current account we can add here extra atribute here
        super().__init__(account_number,balance) # recalling the constructor of the base class
        self.overdraft_limit = overdraft_limit # overdraft limit for current account
    def withdraw(self, amount): # withdraw method for current account because of overdraft limit
        if amount > 0 and amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds")
    def account_type(self):
        return "Checking Account"
    
account = {} 
if os.path.exists("accounts.json"):
    with open("accounts.json", "r") as f:
        saved_data = json.load(f)
        for acc_id, acc_info in saved_data.items():
            if acc_info["type"] == "savings":
                account[acc_id] = SavingsAccount(acc_id, acc_info["balance"])
            elif acc_info["type"] == "current":
                account[acc_id] = CurrentAccount(acc_id, acc_info["balance"])

while True:   #infinite loop to keep programme running until user exits
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
            account[acc_ID] = SavingsAccount(acc_ID) #  creating a savings account object with the given account ID and add in to dict account
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
        
        if acc_ID not in account:
            print("Account not found")
            continue
        else:
            amount = float(input("Enter amount to withdraw: "))
            account[acc_ID].withdraw(amount)
    elif choice == 4:
        acc_ID = (input("Enter Account ID: "))
        if acc_ID in account:
            print(f"Account Balance: {account[acc_ID].get_balance()}")
        else:
            print("Account not found")
    elif choice == 5:
        print("Exiting...")
        data_to_save = {
        acc_id: acc_obj.to_dict() for acc_id, acc_obj in account.items()
        }
        with open("accounts.json", "w") as f:
            json.dump(data_to_save, f, indent=4)
        print("Data saved to accounts.json")

        break
    else:
        print("Invalid choice")
# This code implements a simple banking system with two types of accounts: Savings and Current.
