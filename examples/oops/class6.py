#Bank System (with Account Types and Transactions)
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(Account):
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited to {self.owner}'s savings account")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} withdrawn from savings")
        else:
            print("Insufficient balance")

class CurrentAccount(Account):
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited to {self.owner}'s current account")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"{amount} withdrawn from current")

# Example
acc1 = SavingsAccount("Alice", 1000)
acc1.deposit(500)
acc1.withdraw(200)
print("Balance:", acc1.balance)

acc2=CurrentAccount("Joy", 3000)
acc2.withdraw(2900)
acc2.deposit(100)
print("Balance:", acc2.balance)

# Employee Management System (Inheritance + Composition)
class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state

class Employee:
    def __init__(self, name, emp_id, address):
        self.name = name
        self.emp_id = emp_id
        self.address = address

    def display(self):
        print(f"{self.name} ({self.emp_id}) - {self.address.city}, {self.address.state}")

# Example
addr = Address("Bangalore", "Karnataka")
emp = Employee("John", "E123", addr)
emp.display()

#Inventory System (Class with Class Method, Static Method)
class Product:
    inventory = []

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.inventory.append(self)

    @classmethod
    def show_inventory(cls):
        for item in cls.inventory:
            print(f"{item.name}: Rs.{item.price}")

    @staticmethod
    def discount_price(price, discount):
        return price - (price * discount / 100)

Product("Mouse", 500)
Product("Keyboard", 1000)
Product.show_inventory()

print("Discounted Price:", Product.discount_price(1000, 10))
