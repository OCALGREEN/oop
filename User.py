class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print("User: ", self.name, "Email: ", self.email, "Balance: ", self.account_balance)
        return self
    
    def transfer_money(self, person, amount):
        self.account_balance -= amount
        person.account_balance += amount
        return self

johnny = User("Johhny", "john@email.com")
brit = User("Britnney", "brit@email.com")
lorax = User("Lorax", "wahoo@email.com")

johnny.make_deposit(250).make_deposit(500).make_deposit(750).make_withdrawal(250).transfer_money(lorax, 250)

brit.make_deposit(1000).make_deposit(500).make_withdrawal(750).make_withdrawal(250)

lorax.make_deposit(100).make_withdrawal(25).make_withdrawal(12).make_withdrawal(7)

johnny.display_user_balance()
brit.display_user_balance()
lorax.display_user_balance()