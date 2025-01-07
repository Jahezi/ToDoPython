from nicegui import ui
import sqlite3
from datetime import datetime

# --- Database Setup ---
def setup_database():
    conn = sqlite3.connect('todo_rpg.db')
    cursor = conn.cursor()

    # Create Users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        image TEXT,
        race TEXT,
        class TEXT,
        level INTEGER DEFAULT 1,
        experience INTEGER DEFAULT 0
    )''')

    # Create Tasks table
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        title TEXT NOT NULL,
        description TEXT,
        status TEXT DEFAULT 'open',
        due_date TEXT,
        difficulty INTEGER DEFAULT 1,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )''')

    conn.commit()
    conn.close()

setup_database()

# --- Helper Functions ---
def get_user(user_id):
    conn = sqlite3.connect('todo_rpg.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def add_experience(user_id, xp):
    conn = sqlite3.connect('todo_rpg.db')
    cursor = conn.cursor()
    user = get_user(user_id)

    if user:
        new_xp = user[6] + xp
        new_level = user[5]

        while new_xp >= 100:  # Assume 100 XP per level
            new_xp -= 100
            new_level += 1

        cursor.execute('UPDATE users SET experience = ?, level = ? WHERE id = ?',
                       (new_xp, new_level, user_id))
        conn.commit()
    conn.close()

# --- GUI Components ---
def create_user():
    with ui.dialog() as dialog, ui.card():
        ui.markdown("## Create New User")
        name = ui.input("Name").bind_value()
        image = ui.input("Image URL (optional)").bind_value()
        race = ui.input("Race").bind_value()
        class_ = ui.input("Class").bind_value()

        def save_user():
            if not name.value or not race.value or not class_.value:
                ui.notify("Name, Race, and Class are required fields!", color="red")
                return

            try:
                conn = sqlite3.connect('todo_rpg.db')
                cursor = conn.cursor()
                cursor.execute('''INSERT INTO users (name, image, race, class) VALUES (?, ?, ?, ?)''',
                               (name.value, image.value, race.value, class_.value))
                conn.commit()
                conn.close()
                ui.notify("User created successfully!", color="green")
                dialog.close()
            except Exception as e:
                ui.notify(f"Error creating user: {e}", color="red")

        ui.button("Save", on_click=save_user)
        ui.button("Cancel", on_click=dialog.close)

    dialog.open()

def create_task(user_id):
    with ui.dialog() as dialog, ui.card():
        ui.markdown("## Create New Task")
        title = ui.input("Title").bind_value()
        description = ui.textarea("Description").bind_value()
        due_date = ui.input("Due Date (YYYY-MM-DD)").bind_value()
        difficulty = ui.number("Difficulty (1-5)", value=1, min=1, max=5).bind_value()

        def save_task():
            conn = sqlite3.connect('todo_rpg.db')
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO tasks (user_id, title, description, due_date, difficulty) 
                              VALUES (?, ?, ?, ?, ?)''',
                           (user_id, title.value, description.value, due_date.value, difficulty.value))
            conn.commit()
            conn.close()
            ui.notify("Task created successfully!")
            dialog.close()

        ui.button("Save", on_click=save_task)
        ui.button("Cancel", on_click=dialog.close)

    dialog.open()

def show_tasks(user_id):
    conn = sqlite3.connect('todo_rpg.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE user_id = ?', (user_id,))
    tasks = cursor.fetchall()
    conn.close()

    with ui.card():
        ui.markdown("## Tasks")
        for task in tasks:
            with ui.row():
                ui.label(f"{task[1]}: {task[2]} (Due: {task[4]}) [Difficulty: {task[5]}]")
                if task[3] == 'open':
                    ui.button("Complete", on_click=lambda t=task: complete_task(t[0], user_id))


def complete_task(task_id, user_id):
    conn = sqlite3.connect('todo_rpg.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET status = "completed" WHERE id = ?', (task_id,))
    cursor.execute('SELECT difficulty FROM tasks WHERE id = ?', (task_id,))
    difficulty = cursor.fetchone()[0]
    conn.commit()
    conn.close()

    # Add experience points based on difficulty
    add_experience(user_id, difficulty * 10)
    ui.notify("Task completed and experience added!")

# --- Main App ---
with ui.row():
    ui.button("Create User", on_click=create_user)
    ui.button("Show Tasks", on_click=lambda: show_tasks(1))  # Replace 1 with the actual user ID

ui.run()
