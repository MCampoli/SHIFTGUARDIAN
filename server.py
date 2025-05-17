import socket
import threading
import json
import time

HOST = '127.0.0.1'
PORT = 65432
MAX_CLIENTS = 3
connected_clients = 0
lock = threading.Lock()

def load_data():
    """Ładuje dane z pliku JSON"""
    with open("data/users.json", "r", encoding="utf-8") as file:
        return json.load(file)

def handle_client(conn, addr, data):
    """Obsługuje połączenie z klientem"""
    global connected_clients
    print(f"[Server] Połączono z {addr}")

    try:
        username = conn.recv(1024).decode()
        if not username:
            print(f"[Server] {addr} - brak loginu, zamykam połączenie")
            return

        conn.send(b"PASSWORD")

        password = conn.recv(1024).decode()
        if not password:
            print(f"[Server] {addr} - brak hasła, zamykam połączenie")
            return

        if username not in data["users"] or data["users"][username]["password"] != password:
            conn.send(b"REFUSED: Niepoprawne dane logowania.")
            print(f"[Server] {addr} - nieudane logowanie: {username}")
            return

        conn.send(f"OK: Zalogowano jako {username}".encode())
        print(f"[Server] {addr} - zalogowany użytkownik: {username}")

        while True:
            request = conn.recv(1024).decode()
            if not request:
                print(f"[Server] {addr} - połączenie zamknięte przez klienta")
                break

            print(f"[Server] Otrzymano zapytanie od {username}: {request}")

            # Obsługuje zapytania
            if request == "Employee":
                response = data.get("employees", [])
            elif request == "Department":
                response = data.get("departments", [])
            elif request == "Shift":
                response = data.get("shifts", [])
            else:
                response = []

            time.sleep(1)  # Symulacja opóźnienia

            # Serializacja danych do JSON
            serialized = json.dumps(response, ensure_ascii=False).encode('utf-8')
            conn.sendall(serialized)

    except Exception as e:
        print(f"[Server] Exception podczas obsługi klienta {addr}: {e}")

    finally:
        with lock:
            connected_clients = max(connected_clients - 1, 0)
        conn.close()
        print(f"[Server] Rozłączono klienta {addr}, aktywni klienci: {connected_clients}")

def main():
    global connected_clients
    data = load_data()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"[Server] Nasłuchuję na {HOST}:{PORT}")

        while True:
            conn, addr = server_socket.accept()

            with lock:
                if connected_clients >= MAX_CLIENTS:
                    print(f"[Server] Odrzucono połączenie {addr} - limit klientów osiągnięty")
                    conn.send(b"REFUSED: Serwer zajety.")
                    conn.close()
                    continue
                connected_clients += 1

            threading.Thread(target=handle_client, args=(conn, addr, data), daemon=True).start()

if __name__ == "__main__":
    main()
