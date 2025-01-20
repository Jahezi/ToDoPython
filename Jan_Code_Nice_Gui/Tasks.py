import sqlite3

def create_task(username):
    task_name = input("Name der Aufgabe: ")
    task_difficulty = input("Schwierigkeit der Aufgabe (Leicht, Mittel, Schwer): ")
    date = input("Datum der Aufgabe: ")

    xp_value = 0 
    if task_difficulty == "Leicht":
        xp_value = 100
    elif task_difficulty== "Mittel":
        xp_value = 25
    elif task_difficulty == "Schwer":
        xp_value = 500
    else:
        print("Ungültige Schwierigkeit")
        return 
    
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO tasks (task_name, task_difficulty,task_xp, task_date, task_user, task_status)
            VALUES (?, ?, ?, ?, ?, "open")
        ''', (task_name, task_difficulty, xp_value, date, username))

        conn.commit()
        print(f"Aufgabe {task_name} erfolgreich erstellt!")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    
    finally:
        conn.close()

def show_tasks(username):
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()

    cursor.execute('''
                    SELECT task_name, task_difficulty, task_xp, task_date, task_status FROM tasks WHERE task_user = ?
                ''', (username,))
    tasks = cursor.fetchall()
    for task in tasks:
        print(f"Taskname: {task[0]}, Schwierigkeit: {task[1]}, XP: {task[2]}, Datum: {task[3]}, Status: {task[4]}")
    conn.close()

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