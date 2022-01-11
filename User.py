# USER CLASS
class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print("User: ", self.name, "Email: ", self.email)
        self.account.display_account_info()
        return self
    
    def transfer_money(self, person, amount):
        self.account.withdraw(amount)
        person.account.deposit(amount)
        return self

# BANK ACCOUNT CLASS
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


# CALLING USER CLASS FUNCTIONS
# Creating User classes
johnny = User("Johhny", "john@email.com")
brit = User("Britnney", "brit@email.com")
lorax = User("Lorax", "wahoo@email.com")

# Calling functions from User class
johnny.make_deposit(250).make_deposit(500).make_deposit(750).make_withdrawal(250).transfer_money(lorax, 281)
brit.make_deposit(1000).make_deposit(500).make_withdrawal(750).make_withdrawal(250)
lorax.make_deposit(100).make_withdrawal(25).make_withdrawal(12).make_withdrawal(7)
# Displaying User class info
johnny.display_user_balance()
brit.display_user_balance()
lorax.display_user_balance()

# CALLING BANK ACCOUNT FUNCTIONS
# Creating Bank Account info
# Jerry = BankAccount(0.0399, 1000)
# Berry = BankAccount(0.0375, 1500)
# # Displaying Bank Account info
# Jerry.deposit(500).deposit(500).deposit(500).withdraw(500).yield_interest().display_account_info()
# Berry.deposit(250).deposit(250).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()