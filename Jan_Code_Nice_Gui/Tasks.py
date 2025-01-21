import sqlite3

def create_task(username):
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()
    try:
        cursor.execute(
            '''
            INSERT INTO tasks (task_name, task_difficulty, task_xp, task_date, task_user, task_status)
            VALUES (?, ?, ?, ?, ?, "open")
            ''',
            (username, "Leicht", 100, "2025-01-01", username)
        )
        conn.commit()
    finally:
        conn.close()

def show_tasks(username):
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()
    cursor.execute(
        '''
        SELECT task_name, task_difficulty, task_xp, task_date, task_status FROM tasks WHERE task_user = ?
        ''',
        (username,)
    )
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def end_task(username):
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()
    try:
        cursor.execute(
            '''
            UPDATE tasks SET task_status = 'Erfolgreich beendet' WHERE task_user = ? AND task_status = "open"
            ''',
            (username,)
        )
        conn.commit()
    finally:
        conn.close()

def delete_task(username):
    conn = sqlite3.connect('Database.db')
    cursor = conn.cursor()
    try:
        cursor.execute(
            '''
            DELETE FROM tasks WHERE task_user = ?
            ''',
            (username,)
        )
        conn.commit()
    finally:
        conn.close()
