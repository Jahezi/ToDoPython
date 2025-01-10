import sqlite3

def initialize_database():
    # Verbindung zur SQLite-Datenbank
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()
    

    # SQL-Befehl zum Erstellen der Tabellen
    
    # Hier wird die users Tabelle erstellt
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        class TEXT NOT NULL,
        level INTEGER NOT NULL,
        health INTEGER NOT NULL,
        tasks_completed INTEGER NOT NULL
    );
    ''')

    # Hier wird die Monsters tabelle erstellt
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS monsters (
        monster_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        monster_type TEXT NOT NULL,
        level INTEGER NOT NULL,
        health INTEGER NOT NULL
    );
    ''')

    # Hier wird die Tasks Tabelle erstellt
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        difficulty TEXT NOT NULL
    );
    ''')

    print("Datenbank wurde initialisert")

    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()


# Funktion aufrufen, um die Datenbank zu initialisieren
initialize_database()
