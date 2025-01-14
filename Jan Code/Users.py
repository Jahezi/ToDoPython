import sqlite3

def register_user(username, password, user_class, user_race):


    # Verbindung zur Datenbank herstellen
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()
    try:
        # Benutzer in der Datenbank speichern
        cursor.execute('''
            INSERT INTO users (username, user_password, user_class, user_race, user_level, user_xp, user_health, tasks_completed)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (username, password, user_class, user_race, 1, 0, 100, 0))

        # Änderungen speichern
        conn.commit()
        print(f"Benutzer {username} erfolgreich registriert!")

    except sqlite3.IntegrityError:
        print("Fehler: Der Benutzername ist bereits vergeben.")
        return register_user(username, password, user_class, user_race)
    finally:
        conn.close()

def login_user(username, password):
    global user_status
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()

    cursor.execute('''
                    SELECT * FROM users WHERE username = ? AND user_password = ?
                ''', (username, password))
    user = cursor.fetchone()        
    conn.close()
    return user

def show_user_status(username):

    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT username, user_level, user_xp, user_health, user_class, user_race, tasks_completed 
        FROM users 
        WHERE name = ? 
    ''', (username,))
    user = cursor.fetchone()
    if user:
        print(f"\nBenutzername: {user[0]}")
        print(f"Level: {user[1]}")
        print(f"XP: {user[2]}")
        print(f"Gesundheit: {user[3]}")
        print(f"Benutzerklasse: {user[4]}")
        print(f"Benutzerrasse: {user[5]}")
        print(f"Abgeschlossene Aufgaben: {user[6]}")
    else:
        print("Benutzer nicht gefunden.")
    conn.close()


def show_all_users():
    # Verbindung zur SQLite-Datenbank herstellen
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()

    # SQL-Abfrage zur Auswahl aller Benutzernamen
    cursor.execute('''
        SELECT username FROM users
    ''')
    
    # Alle Ergebnisse abrufen
    users = cursor.fetchall()

    # Benutzer anzeigen
    if users:
        print("Alle Benutzer:")
        for user in users:
            print(f"- {user[0]}")
    else:
        print("Keine Benutzer gefunden.")
        

    # Verbindung schließen
    conn.close()
