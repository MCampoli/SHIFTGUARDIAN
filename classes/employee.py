# === PLIK: classes/employee.py ===
class Employee:
    def __init__(self, emp_id, first_name, last_name, position, email):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.email = email

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.position}, ID: {self.emp_id}, Email: {self.email})"