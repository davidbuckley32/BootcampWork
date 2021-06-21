class BankAccount:
	def __init__(self, int_rate = 0, balance = 0):
		self.int = int_rate
        self.balance = balance

	def deposit(self, amount = 0):
		self.balance = balance + amount
	def withdraw(self, amount):
		self.balance = balance - amount
	def display_account_info(self):
		print("Balance " + self.balance)
	def yield_interest(self):
		self.balance = self.balance + (self.balance * self.int)
