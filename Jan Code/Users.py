import sqlite3

import sqlite3

def register_user(username, password, user_class, user_race, user_pic):
    # Verbindung zur Datenbank herstellen
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()

    try:
        # Prüfen, ob der Benutzername bereits existiert
        cursor.execute('''
            SELECT COUNT(*) FROM users WHERE username = ?
        ''', (username,))
        result = cursor.fetchone()

        if result[0] > 0:
            print("Fehler: Der Benutzername ist bereits vergeben. Bitte wähle einen anderen.")
            return False  # Benutzername existiert bereits

        # Benutzer in der Datenbank speichern
        cursor.execute('''
            INSERT INTO users (username, user_password, user_class, user_race, user_level, user_xp, user_health, user_pic )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (username, password, user_class, user_race, 1, 0, 100, user_pic))

        

        # Änderungen speichern
        conn.commit()
        print(f"Benutzer {username} erfolgreich registriert!")
        return True  # Benutzer erfolgreich registriert

    except sqlite3.Error as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        return False  # Ein anderer Fehler ist aufgetreten

    finally:
        # Verbindung zur Datenbank schließen
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
        SELECT username, user_level, user_xp, user_health, user_class, user_race, user_pic
        FROM users 
        WHERE username = ? 
    ''', (username,))
    user = cursor.fetchone()
    if user:
        print(f"\nBenutzername: {user[0]}")
        print(f"Level: {user[1]}")
        print(f"XP: {user[2]}")
        print(f"Gesundheit: {user[3]}")
        print(f"Benutzerklasse: {user[4]}")
        print(f"Rasse: {user[5]}")
        print(f"Bild {user[6]}")
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

def delete_user(username):
        conn = sqlite3.connect('Database.db')
        cursor = conn.cursor()

        cursor.execute('''
            DELETE FROM users WHERE username = ?
        ''', (username,))
        print(f"Benutzer {username} wurde gelöscht.")

        cursor.execute('''
            DELETE FROM tasks WHERE task_user = ?
        ''', (username,))
        print(f"Alle Aufgaben von {username} wurden gelöscht.")

        conn.commit()
        conn.close()
   