# SHIFTGUARDIAN

👩‍💻 Autor
Monika Campoli
📧 wwx21082@student.warszawa.merito.pl

SHIFTGUARDIAN to aplikacja klient-serwer napisana w Pythonie, służąca do zarządzania zmianami pracowniczymi. 
Projekt realizowany jest jako zaliczenie przedmiotu **Programowanie zaawansowane** na studiach informatycznych.

## 📌 Funkcje

- ✅ Logowanie użytkowników na podstawie pliku `users.json`
- 👥 Obsługa podstawowych danych o użytkownikach, pracownikach, działach, zmianach i harmonogramach
- 🧱 Architektura obiektowa z klasami: `Employee`, `Department`, `Shift`, `Schedule`, `User`
- 🔄 Obsługa wielu klientów (multi-threading w serwerze)
- 💾 Odczyt danych z plików JSON
- 🔌 Prosta komunikacja sieciowa (socket)
- 📦 Możliwość dalszej rozbudowy (CRUD, role, logi, GUI, itp.)

## 🛠️ Technologie

- Python 3.13.2
- Socket (komunikacja klient-serwer)
- JSON (do przechowywania danych)
- Wątki (`threading`)
- Visual Studio Code

## 📁 Struktura katalogów
SHIFTGUARDIAN/
├── classes/ # Klasy: Employee, Department, Shift, Schedule, User
├── data/ # Pliki JSON z danymi (np. users.json)
├── utils/ # Pliki pomocnicze
├── client.py # Kod klienta
├── server.py # Kod serwera
├── readme.md # Ten plik
└── .gitignore # Ignorowane pliki (np. *.pyc)


## 🧪 Jak uruchomić

1. **Uruchom serwer**:
   ```bash
   python server.py
   
2. **Uruchom client**:
   ```bash
   python client.py

## Wymagania: 
Wymagany Python 3.13.2 (lub kompatybilna wersja 3.11+).
