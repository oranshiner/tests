from bank_account_commission import commission

class BankAccount:
    """ create a bank account """
    def __init__(self, name, balance, is_client):
        self.name = name
        self.balance = balance
        self.is_client = is_client

    def get_client_info(self):
        """ retrieve client information """
        return f'Account name: {self.name}, balance: {self.balance}'

    def validate_amount(self, amount):
        """ validate the amount """
        if amount <= 0:
            raise ValueError("Invalid amount")

    def deposit(self, amount):
        """ deposit money """
        self.validate_amount(amount)
        self.balance += (amount - commission(self.is_client))
        return self.balance

    def withdraw(self, amount):
        """ withdraw money """
        self.validate_amount(amount)
        if self.balance >= amount + commission(self.is_client):
            self.balance -= (amount + commission(self.is_client))
            return self.balance
        
    def transfer(self, amount, recipient):
        """
        Transfer money to another bank account+
        """
        if self.balance >= amount:
          self.balance -= amount
          recipient.balance += amount
          print(f"Transferred {amount} to {recipient.name}")
        else:
          print("Insufficient balance")

    def validate_amount(self, amount):
        """ validate the amount """
        if not isinstance(amount, (int, float)):
            raise ValueError("Invalid amount")
        else:
            raise InsufficientFundsError("Insufficient funds")

    def client(self):
        """ client information """
        return {'Account name': self.name, 'balance': self.balance}