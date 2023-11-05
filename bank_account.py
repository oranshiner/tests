from bank_account_commission import commission

class BankAccount:
    """
    The BankAccount class represents a bank account and provides methods for depositing, withdrawing, and transferring money.
    It also includes a method for validating the amount and raises appropriate exceptions for invalid amounts or insufficient funds.
    """

    def __init__(self):
        self.balance = 0

    def validate_amount(self, amount: float) -> None:
        """
        Validates the amount and raises a ValueError if it is invalid.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Invalid amount")

    def deposit(self, amount: float) -> float:
        """
        Deposits money into the account and deducts commission.
        Returns the updated balance.
        """
        self.validate_amount(amount)
        commission = self.calculate_commission()
        self.balance += (amount - commission)
        return self.balance

    def withdraw(self, amount: float) -> float:
        """
        Withdraws money from the account and deducts commission.
        Returns the updated balance.
        """
        self.validate_amount(amount)
        commission = self.calculate_commission()
        if self.balance >= amount + commission:
            self.balance -= (amount + commission)
            return self.balance

    def transfer(self, amount: float, recipient: 'BankAccount') -> str:
        """
        Transfers money from the account to another account.
        Returns a string indicating the transfer details.
        Raises a ValueError if there are insufficient funds.
        """
        self.validate_amount(amount)
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            return f"Transferred {amount} from {self.first_name} {self.last_name} to {recipient.first_name} {recipient.last_name}"
        else:
            raise ValueError("Insufficient balance")

    def calculate_commission(self) -> float:
        """
        Calculates the commission based on the account type.
        Returns the commission amount.
        """
        if self.is_client:
            return 0.01 * self.balance
        else:
            return 0

    @property
    def is_client(self) -> bool:
        """
        Checks if the account is a client account.
        Returns True if it is a client account, False otherwise.
        """
        # Assume there is a field named 'account_type' that represents the type of the account
        return self.account_type == 'client'


class Client:
    
    client_list = ["John", "Doe", "123456789", "123 Main St", "Male", "1990-01-01", "Jane", "Smith", "987654321", "456 Elm St", "Female", "1995-05-05"]

    def __init__(self, first_name, last_name, id_number, address, sex, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.address = address
        self.gender = gender
        self.date_of_birth = date_of_birth

    def new_client(self):
        while True:
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            id_number = input("Enter ID number (9 digits): ")
            address = input("Enter address: ")
            gender = input("Enter gender: ")
            date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
            
            # Verify age is above 16
            from datetime import datetime
            dob = datetime.strptime(date_of_birth, '%Y-%m-%d')
            age = (datetime.now() - dob).days // 365
            if age < 16:
                print("Client must be at least 16 years old.")
                continue
            
            # Verify ID contains 9 digits
            if len(id_number) != 9:
                print("ID number must contain 9 digits.")
                continue
            
            # Verify all fields are not empty
            if not all([first_name, last_name, id_number, address, gender, date_of_birth]):
                print("All fields are required.")
                continue

            '''add client to client_list'''
            self.client_list.append(first_name)
            
                    
    def get_client(self):
        return self.client_list
    