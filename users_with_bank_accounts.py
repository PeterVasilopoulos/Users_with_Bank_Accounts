# User Class
class User:
    def __init__(self, name, email):
        # Assign attribute values
        self.name = name
        self.email = email 
        # Create instance of bank account
        self.account = BankAccount(int_rate = 0.02, balance = 0)

    # Make Deposit
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    # Make Withdrawal
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    # Display user balance
    def display_user_balance(self):
        self.account.display_account_info()
        return self


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


pog = User("K", "k@mail.com")
pog.make_deposit(50)
pog.make_withdrawal(20)
pog.display_user_balance()