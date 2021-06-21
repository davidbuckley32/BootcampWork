class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance = 0)
        self.account.deposit(100)
        self.account.withdraw(50)
        self.account.display_account_info()

class BankAccount:
    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount

    def withdraw(self, amount):
            self.withdraw = amount
            if self.withdraw > self.balance:
                print("Insufficient funds: Charging a 5$ fee")
                self.balance = self.balance - 5
            else:
                self.balance = self.balance - self.withdraw

    def display_account_info(self):
            print("Balance " + str(self.balance))

    def yield_interest(self):
            self.balance = self.balance + (self.balance * self.int_rate)
User("David", "notmyreal@email.com")