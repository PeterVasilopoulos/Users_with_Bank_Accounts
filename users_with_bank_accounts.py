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
    pass