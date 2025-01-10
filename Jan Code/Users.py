import sqlite3

def register_user(username, password,user_class):


    # Verbindung zur Datenbank herstellen
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()

    try:
        # Benutzer in der Datenbank speichern
        cursor.execute('''
            INSERT INTO users (name, password, class, level, health, tasks_completed)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (username, password, user_class, 1, 100, 0))

        # Änderungen speichern
        conn.commit()
        print(f"Benutzer {username} erfolgreich registriert!")
    except sqlite3.IntegrityError:
        print("Fehler: Der Benutzername ist bereits vergeben.")
    finally:
        conn.close()

def login_user(username, password):
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()

    cursor.execute('''
                    SELECT * FROM users WHERE name = ? AND password = ?
                ''', (username, password))
    user = cursor.fetchone()
    print("Login erfolgreich")

    conn.close()
    return user

def delete_user(username, password, user_class):

    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()

    cursor.execute('''
                    DELETE FROM users WHERE name = ? AND password = ? AND class = ?
                ''', (username, password, user_class))

    conn.commit()

def show_all_users(username, user_class):
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()

    cursor.execute('''
                    SELECT * FROM users WHERE name = ? AND class = ?
                ''', (username, user_class))
    user = cursor.fetchall()
    print(user)
    conn.close()
    return user