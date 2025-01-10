import sqlite3

def create_task(name, difficulty):
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO tasks (name, difficulty)
            VALUES (?, ?)
        ''', (name, difficulty))

        conn.commit()
        print(f"Aufgabe {name} erfolgreich erstellt!")
    except sqlite3.IntegrityError:
        print("Fehler: Die Aufgabe existiert bereits.")
    finally:
        conn.close()