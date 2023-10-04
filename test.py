import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def test_client(self):
        account = BankAccount("John", 1000, True)
        self.assertEqual(account.client(), "Account name: John, balance: 1000")

    def test_deposit(self):
        account = BankAccount("Mary", 500, True)
        account.deposit(100)
        self.assertEqual(account.balance, 595)

    def test_withdraw(self):
        account = BankAccount("Mike", 200, True)
        account.withdraw(150)
        self.assertEqual(account.balance, 45)

    def test_insufficient_funds(self):
        account = BankAccount("Lisa", 100, False)
        account.withdraw(200)
        self.assertEqual(account.balance, 100)

    def test_transfer(self):
        account1 = BankAccount("John", 500, True)
        account2 = BankAccount("Mary", 300, False)
        account1.transfer(100, account2)
        self.assertEqual(account1.balance, 395)
        self.assertEqual(account2.balance, 400)

