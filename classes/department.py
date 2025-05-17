# === PLIK: classes/department.py ===
class Department:
    def __init__(self, dept_id, name, floor, manager):
        self.dept_id = dept_id
        self.name = name
        self.floor = floor
        self.manager = manager

    def __str__(self):
        return f"Department {self.name} (ID: {self.dept_id}, Floor: {self.floor}, Manager: {self.manager})"