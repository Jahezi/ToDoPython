import sqlite3

def register_user(username, user_class):
    # Verbindung zur Datenbank herstellen
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()

    try:
        # Benutzer in der Datenbank speichern
        cursor.execute('''
            INSERT INTO users (name, class, level, health, tasks_completed)
            VALUES (?, ?, ?, ?, ?)
        ''', (username, user_class, 1, 100, 0))

        # Änderungen speichern
        conn.commit()
        print(f"Benutzer {username} erfolgreich registriert!")
    except sqlite3.IntegrityError:
        print("Fehler: Der Benutzername ist bereits vergeben.")
    finally:
        conn.close()



