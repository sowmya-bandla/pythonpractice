class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance

# Creating an object
account = BankAccount("Alice", 1000)

# Interacting using public methods
account.deposit(500)         # Deposited 500. New balance is 1500
account.withdraw(300)        # Withdrew 300. New balance is 1200

# Accessing private attribute directly (Not recommended)
#print(account.__balance)   # ❌ This will raise an AttributeError

# Correct way to access private data
print(account.get_balance())  # ✅ Output: 1200
