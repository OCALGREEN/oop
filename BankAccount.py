class BankAccount:
    
    def __init__(self, int_rate, balance):
        self.balance = 0
        self.int_rate = 0.025

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < 0:
            print("Insufficient funds: Chargin a $5 fee")
            self.balance -= amount
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print("Balance: ", self.balance)
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self

Jerry = BankAccount(0.0399, 1000)
Berry = BankAccount(0.0375, 1500)

Jerry.deposit(500).deposit(500).deposit(500).withdraw(500).yield_interest().display_account_info()
Berry.deposit(250).deposit(250).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()