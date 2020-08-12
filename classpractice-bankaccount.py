class BankAccount:
    def __init__(self):
        self.balance = 0


    def withdraw(self, amount):
        self.balance -= amount
        return self.balance


    def deposit(self, amount):
        self.balance += amount
        return self.balance


a = BankAccount()
b = BankAccount()
c = BankAccount()
a.deposit(450)
b.deposit(945)
b.withdraw(350)
a.withdraw(100)


class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance


    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print("Sorry, minimum balance must be maintained")
        else:
            BankAccount.withdraw(self, amount)
    