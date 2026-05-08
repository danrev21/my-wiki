#!/usr/bin/env python

# In this example, the __init__ method initializes the account_holder 
# and balance attributes. The __del__ method prints a message when the 
# object is about to be destroyed.

class BankAccount:
    def __init__(self, account_holder, balance=0):             # constructor
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):                                 # class method
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):                                # class method
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def __del__(self):                                         # destructor
        print(f"Account for {self.account_holder} is being closed.")

# Creating an instance of the BankAccount class
account = BankAccount("Alice", 1000)

# Making transactions
account.deposit(500)
account.withdraw(200)

# The destructor will be called when the object is no longer in use