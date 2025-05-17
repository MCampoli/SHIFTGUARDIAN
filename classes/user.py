# === PLIK: classes/user.py ===
class User:
    def __init__(self, user_id, username, full_name, role, email):
        self.user_id = user_id
        self.username = username
        self.full_name = full_name
        self.role = role
        self.email = email

    def __str__(self):
        return f"User {self.username} ({self.role}) - {self.full_name}, Email: {self.email}"