# === PLIK: classes/schedule.py ===
class Schedule:
    def __init__(self, schedule_id, department, date, shifts):
        self.schedule_id = schedule_id
        self.department = department
        self.date = date
        self.shifts = shifts  # List of Shift IDs or Shift objects

    def __str__(self):
        return f"Schedule {self.schedule_id} ({self.department} on {self.date}) with {len(self.shifts)} shifts"