import unittest
from bank_account import BankAccount, commission
class TestBankAccount(unittest.TestCase):

    # Deposit positive amount increases balance
    def test_deposit_positive_amount_increases_balance(self):
        account = BankAccount("John", 100, True)
        initial_balance = account.balance
        amount = 50
        account.deposit(amount)
        self.assertEqual(account.balance, initial_balance + amount - commission(account.isClient))

    # Withdraw positive amount decreases balance
    def test_withdraw_positive_amount_decreases_balance(self):
        account = BankAccount("John", 100, True)
        initial_balance = account.balance
        amount = 50
        account.withdraw(amount)
        self.assertEqual(account.balance, initial_balance - amount - commission(account.isClient))

    # Transfer positive amount to another account decreases balance and increases the other account's balance
    def test_transfer_positive_amount_decreases_balance_and_increases_other_account_balance(self):
        account1 = BankAccount("John", 100, True)
        account2 = BankAccount("Jane", 50, False)
        initial_balance1 = account1.balance
        initial_balance2 = account2.balance
        amount = 50
        account1.transfer(amount, account2)
        self.assertEqual(account1.balance, initial_balance1 - amount - commission(account1.isClient))
        self.assertEqual(account2.balance, initial_balance2 + amount)

    # Deposit zero amount does not change balance
    def test_deposit_zero_amount_does_not_change_balance(self):
        account = BankAccount("John", 100, True)
        initial_balance = account.balance
        amount = 0
        account.deposit(amount)
        self.assertEqual(account.balance, initial_balance)

    # Deposit negative amount does not change balance and prints error message
    def test_deposit_negative_amount_does_not_change_balance_and_prints_error_message(self):
        account = BankAccount("John", 100, True)
        initial_balance = account.balance
        amount = -50
        account.deposit(amount)
        self.assertEqual(account.balance, initial_balance)

    # Withdraw more than balance prints error message and does not change balance
    def test_withdraw_more_than_balance_prints_error_message_and_does_not_change_balance(self):
        account = BankAccount("John", 100, True)
        initial_balance = account.balance
        amount = 150
        account.withdraw(amount)
        self.assertEqual(account.balance, initial_balance)