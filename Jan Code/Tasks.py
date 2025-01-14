import sqlite3

def create_task(username):
    task_name = input("Name der Aufgabe: ")
    task_difficulty = input("Schwierigkeit der Aufgabe (Leicht, Mittel, Schwer): ")
    date = input("Datum der Aufgabe: ")

    xp_value = 0 
    if task_difficulty == "Leicht":
        xp_value = 10
    elif task_difficulty== "Mittel":
        xp_value = 25
    elif task_difficulty == "Schwer":
        xp_value = 50
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
                    SELECT task_name, task_difficulty, task_xp, task_date, task_status FROM tasks WHERE task_user = ? AND task_status = "open" 
                ''', (username,))
    tasks = cursor.fetchall()
    for task in tasks:
        print(f"Taskname: {task[0]}, Schwierigkeit: {task[1]}, XP: {task[2]}, Datum: {task[3]}, Status: {task[4]}")
    conn.close()

def end_task(username):
    print("Welche Aufgabe willst du beenden?")
    show_tasks(username)
    taskname = input("Name der Aufgabe: ")
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()
    cursor.execute('''
                    UPDATE status = "Erfolgreich beendet" FROM tasks WHERE task_3name = ?
                ''', (taskname,))
    print("Task erfolgreich gelöscht")
    conn.commit()
    conn.close()

   