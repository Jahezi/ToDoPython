import sqlite3
from nicegui import ui

class Database:


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
            user_race TEXT NOT NULL,
            user_pic TEXT NOT NULL
        );
        ''')

        # Hier wird die Monsters Tabelle erstellt
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
            task_xp INTEGER NOT NULL,
            task_date INTEGER NOT NULL,
            task_user TEXT NOT NULL,
            task_status TEXT NOT NULL
        );
        ''')

        ui.notify("Datenbank wurde initialisiert")
        print("Datenbank wurde initialisiert")

        # Änderungen speichern und Verbindung schließen
        conn.commit()
        conn.close()

class Users:
    

    def register_user(username, password, user_class, user_race):
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
                ui.notify("Fehler: Der Benutzername ist bereits vergeben. Bitte wähle einen anderen.")
                return False  # Benutzername existiert bereits

            # Benutzer in der Datenbank speichern
            cursor.execute('''
                INSERT INTO users (username, user_password, user_class, user_race, user_level, user_xp, user_health, user_pic)
                VALUES (?, ?, ?, ?, ?, ?, ?, '')
            ''', (username, password, user_class, user_race, 1, 0, 100))

            # Änderungen speichern
            conn.commit()
            ui.notify(f"Benutzer {username} erfolgreich registriert!")
            return True  # Benutzer erfolgreich registriert

        except sqlite3.Error as e:
            ui.notify(f"Ein Fehler ist aufgetreten: {e}")
            return False  # Ein anderer Fehler ist aufgetreten

        finally:
            # Verbindung zur Datenbank schließen
            conn.close()

    def login_user(username, password):
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



class Tasks:
    
    def create_task(task_name, task_difficulty, date):

        if task_difficulty == "Leicht":
            xp_value = 25
        elif task_difficulty== "Mittel":
            xp_value = 50
        elif task_difficulty == "Schwer":
            xp_value = 100
        else:
            ui.notify("Ungültige Schwierigkeit")
            return 

        conn = sqlite3.connect('Database.db')
        cursor = conn.cursor()

        try:
            cursor.execute('''
                INSERT INTO tasks (task_name, task_difficulty,task_xp, task_date, task_user, task_status)
                VALUES (?, ?, ?, ?, "Hello", "open")
            ''', (task_name, task_difficulty, xp_value, date))

            conn.commit()
            ui.notify(f"Aufgabe {task_name} erfolgreich erstellt!", type='positive')
            return True
        
        except sqlite3.Error as e:
            ui.notify("Fehler, Task nicht erstellt")
            return False

        finally:
            conn.close()

    def show_tasks():
       conn = sqlite3.connect('Database.db')
       cursor = conn.cursor()   
       cursor.execute('''
                       SELECT task_name, task_difficulty, task_xp, task_date, task_status FROM tasks
                   ''', )
       tasks = cursor.fetchall()
       conn.close()    
       return tasks 

    def end_task(username):
        print("Welche Aufgabe willst du beenden?")
        taskname = input("Name der Aufgabe: ")
        conn = sqlite3.connect('Database.db')
        cursor = conn.cursor()
        # Überprüfen, ob der Task bereits beendet ist
        cursor.execute('''
            SELECT task_status FROM tasks WHERE task_name = ?
        ''', (taskname,))
        result = cursor.fetchone()

        if result is None:
            print("Dieser Task existiert nicht.")
        elif result[0] == 'Erfolgreich beendet':
            print("Dieser Task wurde bereits erfolgreich beendet.")
        else:
            # Task als erfolgreich beendet markieren
            cursor.execute('''
                UPDATE tasks SET task_status = 'Erfolgreich beendet' WHERE task_name = ? AND task_status = 'open'
            ''', (taskname,))
            print("Task erfolgreich beendet!")
            conn.commit()
            conn.close()
            level_up(username, taskname)

    def level_up(username, taskname):
        # Verbindung zur Datenbank herstellen
        conn = sqlite3.connect('Database.db')
        cursor = conn.cursor()

        # Daten aus der Datenbank abrufen
        cursor.execute('''
                       SELECT task_XP, user_xp, user_level
                       FROM users
                       INNER JOIN tasks ON users.username = tasks.task_user
                       WHERE task_name = ? AND username = ?
                    ''', (taskname, username))
        XP = cursor.fetchone()

        if XP is None:
            print("Benutzer oder Aufgabe nicht gefunden.")
            return

        task_xp = XP[0]
        user_xp = XP[1]
        user_level = XP[2]

        # Überprüfen, ob der Benutzer bereits das maximale Level (Level 5) erreicht hat
        if user_level == 5:
            print("Glückwunsch! Du hast bereits das maximale Level erreicht!")
            conn.close()
            return

        # Neue Gesamt-XP berechnen
        new_total_xp = min(task_xp + user_xp, 400)

        # Berechnung des neuen Levels basierend auf den Gesamt-XP
        if new_total_xp >= 400:
            new_level = 5
        elif new_total_xp >= 300:
            new_level = 4
        elif new_total_xp >= 200:
            new_level = 3
        elif new_total_xp >= 100:
            new_level = 2
        else:
            new_level = 1  # Wenn der Wert unter 100 bleibt, bleibt das Level 1

        # Wenn das Level sich geändert hat, aktualisieren und ausgeben
        if new_level > user_level:
            cursor.execute('''
                           UPDATE users SET user_level = ?, user_xp = ? 
                           WHERE username = ?
                        ''', (new_level, new_total_xp, username))
            conn.commit()  # Änderungen speichern
            print(f"Glückwunsch! Du hast Level {new_level} erreicht!")
        else:
            # Gesamt-XP trotzdem aktualisieren, falls kein Level-Up
            cursor.execute('''
                           UPDATE users SET user_xp = ? 
                           WHERE username = ?
                        ''', (new_total_xp, username))
            conn.commit()

        conn.close()   
    
    def delete_task(username):
        print("Hier siehst du alle Tasks:")
        show_tasks(username)
        print("Welche Aufgabe willst du löschen?")
        taskname = input("Name der Aufgabe: ")
        choice = input("Bist du sicher? Drücke 1 zum bestätigen oder 2 zum abbrechen.")
        if choice == "1":
            conn = sqlite3.connect('Database.db')
            cursor = conn.cursor()
            cursor.execute('''
                            DELETE FROM tasks WHERE task_name = ?
                        ''', (taskname,))
            print("Task erfolgreich gelöscht!")
            conn.commit()
            conn.close()
            return
        else:
            print("Task nicht gelöscht.")
            return
    
    def close_task(taskname):
            conn = sqlite3.connect('Database.db')
            cursor = conn.cursor()
            cursor.execute('''
                            UPDATE tasks SET STATUS = closed WHERE task_name = ?
                        ''', (taskname,))
            ui.notify("Task erfolgreich geschlossen!")
            conn.commit()
            conn.close()



class functions:
    # auth.py
    
    def checkpw(self, password, password2, close_dialog):
        if password == password2:
            close_dialog()
            ui.notify('Login successful')
            ui.navigate.to('/Hi')
        else:
            ui.notify('Passwords do not match')


    def validate_step_1(reg_username, reg_password, stepper):
        """ Validate username and password before proceeding. """
        username_valid = bool(reg_username.value.strip())
        password_valid = bool(reg_password.value.strip())

        if not username_valid:
            reg_username.props('error').update()
            ui.notify("Bitte geben Sie einen Benutzernamen ein!", type='warning')
        else:
            reg_username.props(remove='error').update()

        if not password_valid:
            reg_password.props('error').update()
            ui.notify("Bitte geben Sie ein Passwort ein!", type='warning')
        else:
            reg_password.props(remove='error').update()

        if username_valid and password_valid:
            stepper.next()

    def validate_step_2(user_class_input, stepper):
        """ Validate class selection before proceeding. """
        if user_class_input.value is None:
            user_class_input.props('error').update()
            ui.notify("Bitte wählen Sie eine Klasse aus!", type='warning')
        else:
            user_class_input.props(remove='error').update()
            stepper.next()

    def validate_step_3(user_race_input, stepper):
        """ Validate race selection before proceeding. """
        if user_race_input.value is None:
            user_race_input.props('error').update()
            ui.notify("Bitte wählen Sie eine Rasse aus!", type='warning')
        else:
            user_race_input.props(remove='error').update()
            stepper.next()

    def on_register_click(register_dialog):
        """ Final step: Notify and close dialog """
        ui.notify("Registrierung abgeschlossen! ✅", type='positive')
        print("Registration complete!")
        register_dialog.close()

