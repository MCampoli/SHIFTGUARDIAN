import socket
import json
import threading
import time

HOST = '127.0.0.1'
PORT = 65432

def receive_data(sock, label):
    try:
        data = sock.recv(4096)
        if data:
            decoded = json.loads(data.decode('utf-8'))
            output = [f"\n=== {label.upper()} ==="]
            for item in decoded:
                if isinstance(item, dict):
                    for key, value in item.items():
                        output.append(f"{key}: {value}")
                    output.append("-------------------")
                else:
                    output.append(str(item))
            output.append(f"=== KONIEC {label.upper()} ===\n")
            print("\n".join(output))
    except Exception as e:
        print(f"Błąd podczas odczytu danych {label}: {e}")
        
def client_session(client_id, login, password):
    """Obsługuje sesję klienta, logowanie oraz pobieranie danych z serwera"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))

            print(f"[Client {client_id}] Próba logowania jako {login}...")
            s.sendall(login.encode())  # Wysyłanie loginu
            response = s.recv(1024).decode()

            if response == "PASSWORD":
                s.sendall(password.encode())  # Wysyłanie hasła
                response = s.recv(1024).decode()

                if not response.startswith("OK"):
                    print(f"[Client {client_id}] Nieudane logowanie: {response}")
                    return

                print(f"[Client {client_id}] Zalogowano jako {login}.")

                for class_name in ["Employee", "Department", "Shift"]:
                    print(f"[Client {client_id}] Żądanie danych: {class_name}")
                    s.sendall(class_name.encode())
                    receive_data(s, class_name)
                    time.sleep(1)
            else:
                print(f"[Client {client_id}] Nieudane logowanie: {response}")

    except Exception as e:
        print(f"[Client {client_id}] Błąd: {e}")

if __name__ == "__main__":
    users = [
        ("user1", "password1"),
        ("user2", "password2"),
        ("user3", "password3"),
        ("user4", "wrongpassword")  # Niepoprawne hasło
    ]

    threads = []
    for i, (login, password) in enumerate(users):
        t = threading.Thread(target=client_session, args=(i+1, login, password), daemon=True)
        t.start()
        threads.append(t)

    for t in threads:
        t.join(timeout=15)  # Czekaj na zakończenie wątków (max 15 sekund)
