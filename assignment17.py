class BankAccount:
    def __init__(self, int_rate = .025, balance = 0):
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
            print("Balance " + int(self.balance))

    def yield_interest(self):
            self.balance = self.balance + (self.balance * self.int_rate)

BankAccount1 = BankAccount()

BankAccount1.deposit(100)
BankAccount1.deposit(50)
BankAccount1.deposit(3)
BankAccount1.withdraw(25)
BankAccount1.yield_interest()
BankAccount1.display_account_info()

BankAccount2 = BankAccount()

BankAccount2.deposit(100)
BankAccount2.deposit(50)
BankAccount2.withdraw(1)
BankAccount2.withdraw(2)
BankAccount2.withdraw(3)
BankAccount2.withdraw(4)
BankAccount2.yield_interest()
BankAccount2.display_account_info()
