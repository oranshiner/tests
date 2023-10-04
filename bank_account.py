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

    def transfer(self, amount, account):
        """ transfer money """
        if self.balance >= amount > 0:
            self.balance -= (amount + commission(self.isClient))
            account.deposit(amount)
            print(f"Transferred {amount} to {account.name}")
        else:
            print("Insufficient funds")

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

def test_initializes_with_name_balance_and_is_client_flag(self):
    """
    Test that the BankAccount class correctly initializes with a name, balance, and isClient flag.
    """
    # Given
    name = "John Doe"
    balance = 1000
    isClient = True

    # When
    account = BankAccount(name, balance, isClient)

    # Then
    assert account.name == name
    assert account.balance == balance
    assert account.isClient == isClient
