# Flask-Blueprints-App

## 📌 Opis projektu

**Flask-Blueprints-App** to aplikacja webowa napisana w języku **Python** z wykorzystaniem frameworka **Flask**. Projekt został zorganizowany w sposób modularny przy użyciu **blueprints**, co ułatwia zarządzanie kodem i skalowalność aplikacji. Do przechowywania danych wykorzystano bazę danych **SQLite**.

## 🛠 Wymagania

Aby uruchomić projekt, potrzebujesz:

- **Python 3.8** lub nowszy
- **pip** – menedżer pakietów dla Pythona
- **virtualenv** (opcjonalnie, ale zalecane) – do stworzenia izolowanego środowiska wirtualnego

## 🚀 Instalacja

### 1️⃣ Klonowanie repozytorium:
```bash
git clone https://github.com/MatiLUzak/FlaskZad3.git
cd FlaskZad3
```

### 2️⃣ Utworzenie i aktywacja środowiska wirtualnego (opcjonalnie, ale zalecane):
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# lub
venv\Scripts\activate  # Windows
```

### 3️⃣ Instalacja zależności:
```bash
pip install -r requirements.txt
```

## ⚙️ Konfiguracja aplikacji

1. **Tworzenie bazy danych SQLite**  
   Jeśli aplikacja wymaga inicjalizacji bazy danych, możesz uruchomić:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```
   *Lub jeśli skrypt do tworzenia bazy jest w pliku `setup.py`:*
   ```bash
   python setup.py
   ```

2. **Ustawienie zmiennych środowiskowych (jeśli wymagane)**  
   Jeśli aplikacja korzysta z pliku `.env`, upewnij się, że zawiera poprawne wartości.

## ▶️ Uruchomienie aplikacji

Aby uruchomić aplikację Flask, użyj:
```bash
flask run
```
Aplikacja domyślnie uruchomi się pod adresem:  
📌 **http://127.0.0.1:5000/**

## 📂 Struktura projektu

```
FlaskZad3/
├── app.py
├── config.py
├── blueprints/
│   ├── auth/
│   │   ├── routes.py
│   │   ├── models.py
│   │   └── __init__.py
│   ├── main/
│   │   ├── routes.py
│   │   ├── models.py
│   │   └── __init__.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── mydatabase.db
├── requirements.txt
├── README.md
└── .gitignore
```

- **app.py** – główny plik aplikacji Flask
- **config.py** – plik konfiguracji aplikacji
- **blueprints/** – modułowy podział aplikacji na blueprints
- **templates/** – szablony HTML
- **static/** – pliki statyczne (CSS, JS, obrazy)
- **mydatabase.db** – baza danych SQLite (jeśli używana)
- **requirements.txt** – lista zależności
- **README.md** – dokumentacja projektu

## ✍️ Autor

- **MatiLUzak** – [GitHub](https://github.com/MatiLUzak)

## 📜 Licencja

Ten projekt jest licencjonowany na podstawie licencji MIT. Szczegóły znajdują się w pliku `LICENSE`.
