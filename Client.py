class Client:
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
            
            return Client(first_name, last_name, id_number, address, gender, date_of_birth)
