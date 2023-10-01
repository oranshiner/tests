from bank_account import BankAccount


def test_valid_parameters():
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

def setup_method(self, method):
    self.name = "John Doe"
    self.balance = 1000
    self.isClient = True

    def test_initializes_with_name_balance_and_isClient_flag(self):
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