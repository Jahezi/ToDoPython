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
        username TEXT UNIQUE NOT NULL,
        user_password TEXT NOT NULL,
        user_class TEXT NOT NULL,
        user_level INTEGER NOT NULL,
        user_xp INTEGER NOT NULL,
        user_health INTEGER NOT NULL,
        user_race  TEXT NOT NULL,
        user_pic TEXT NOT NULL
        
    );
    ''')

    # Hier wird die Monsters tabelle erstellt
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS monsters (
        monster_id INTEGER PRIMARY KEY AUTOINCREMENT,
        monster_name TEXT UNIQUE NOT NULL,
        monster_type TEXT NOT NULL,
        monster_level INTEGER NOT NULL,
        monster_health INTEGER NOT NULL,
        monster_pic TEXT NOT NULL
    );
    ''')

    # Hier wird die Tasks Tabelle erstellt
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_name TEXT UNIQUE NOT NULL,
        task_difficulty TEXT NOT NULL,
        task_XP INTEGER NOT NULL,
        task_date INTEGER NOT NULL,
        task_user TEXT NOT NULL,
        task_status TEXT NOT NULL
    );
    ''')

    print("Datenbank wurde initialisert")

    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()
