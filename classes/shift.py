# === PLIK: classes/shift.py ===
class Shift:
    def __init__(self, shift_id, employee_name, start_time, end_time):
        self.shift_id = shift_id
        self.employee_name = employee_name
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"Shift ID: {self.shift_id} | {self.employee_name} | {self.start_time} - {self.end_time}"
