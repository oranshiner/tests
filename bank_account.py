import os
from bank_account_commission import calculate_commission
import sqlite3
from config import KEY


class BankAccount:
    def __init__(self, account_id):
        self.account_id = account_id
        self.balance = 0
        self.conn = sqlite3.connect('test_db.db')
        self.cursor = self.conn.cursor()
        env = os.getenv('ENV')
        if env == 'production':
            self.key = 'production_key'
        elif env == 'staging':
            self.key = 'staging_key'
        else:
            self.key = 'test_key'

    def validate_amount(self, amount: float) -> None:
        """ Validates the amount and raises a ValueError if it is invalid. """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Invalid amount")

    def deposit(self, amount: float) -> float:
        """ Deposits money into the account and deducts commission. Returns the updated balance. """
        self.validate_amount(amount)
        commission = self.calculate_commission()
        self.balance += (amount - commission)
        # Save the updated balance to the SQL database
        self.cursor.execute("UPDATE your_table SET balance = ? WHERE account_id = ?", (self.balance, self.account_id))
        self.conn.commit()
        return self.balance

    def withdraw(self, amount: float) -> float:
        """ Withdraws money from the account and deducts commission. Returns the updated balance. """
        self.validate_amount(amount)
        commission = self.calculate_commission()
        if self.balance >= amount + commission:
            self.balance -= (amount + commission)
            # Save the updated balance to the SQL database
            self.cursor.execute("UPDATE your_table SET balance = ? WHERE account_id = ?", (self.balance, self.account_id))
            self.conn.commit()
            return self.balance

    def transfer(self, amount: float, recipient: 'BankAccount') -> str:
        """ Transfers money from the account to another account. Returns a string indicating the transfer details. Raises a ValueError if there are insufficient funds. """
        self.validate_amount(amount)
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            # Save the updated balance to the SQL database
            self.cursor.execute("UPDATE your_table SET balance = ? WHERE account_id = ?", (self.balance, self.account_id))
            self.conn.commit()
            return f"Transferred {amount} from {self.first_name} {self.last_name} to {recipient.first_name} {recipient.last_name}"
        else:
            raise ValueError("Insufficient balance")