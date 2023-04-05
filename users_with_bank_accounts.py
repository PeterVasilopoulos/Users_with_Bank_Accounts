# User Class
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email 
        self.account = BankAccount(int_rate = 0.02, balance = 0)

    def make_deposit(self, amount):
        pass 


# Bank Account Class
class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0):
        # Assign attribute values
        self.int_rate = int_rate
        self.balance = balance
    
    # Deposit 
    def deposit(self, amount):
        self.balance += amount
        return self

    # Withdraw
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insuffiencet funds: Charging a $5 fee")
            self.balance -= amount
        return self

    # Display account info
    def display_account_info(self):
        print(f"Interest Rate: {self.int_rate}, Balance: {self.balance}")
        return self

    # Yield interest
    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self
