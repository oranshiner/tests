from bank_account import BankAccount


def test_valid_parameters(self):
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