# Week 5 - Task 5: Encapsulation and Abstraction
# Project: Bank Account Management System

from abc import ABC, abstractmethod


# Abstraction: Abstract parent class
class BankAccount(ABC):

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute

    # Getter method
    def get_balance(self):
        return self.__balance

    # Setter method
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
            print("Balance updated successfully.")
        else:
            print("Invalid amount! Balance cannot be negative.")

    # Abstract method
    @abstractmethod
    def account_type(self):
        pass

    # Display account information
    def display_details(self):
        print("Account Holder:", self.account_holder)
        print("Account Type:", self.account_type())
        print("Account Balance:", self.get_balance())


# Child class
class SavingsAccount(BankAccount):

    def account_type(self):
        return "Savings Account"


# Creating an object
account = SavingsAccount("Kalyan", 5000)

print("BANK ACCOUNT MANAGEMENT SYSTEM")
print("--------------------------------")

# Display initial account details
print("\nInitial Account Details:")
account.display_details()

# Updating balance using setter method
print("\nUpdating Account Balance:")
account.set_balance(8000)

# Display updated balance
print("\nUpdated Account Details:")
account.display_details()

# Demonstrating validation
print("\nTesting Invalid Balance:")
account.set_balance(-1000)

print("\nFinal Account Balance:", account.get_balance())

print("--------------------------------")
print("Program completed successfully.")