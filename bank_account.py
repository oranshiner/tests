from bank_account_commission import commission


class BankAccount:
    """ create a bank account """
    def __init__(self, name, balance, isClient):
        self.name = name
        self.balance = balance
        self.isClient = isClient

    def client(self):
        """ client information """
        return f'Account name: {self.name}, balance: {self.balance}'

    def deposit(self, amount):
        """ deposit money """
        if amount > 0:
            self.balance += (amount - commission(self.isClient))
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        """ withdraw money """
        if self.balance >= amount > 0:
            self.balance -= (amount + commission(self.isClient))
        else:
            print("Insufficient funds")
        
