import sqlite3
from nicegui import ui

class Database:


    def initialize_database():
       
        conn = sqlite3.connect('Database.db')
        cursor = conn.cursor()

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

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS rewards (
            reward_id INTEGER PRIMARY KEY AUTOINCREMENT,
            reward_name TEXT UNIQUE NOT NULL
        );
        ''')
        cursor.execute('''
                INSERT OR IGNORE INTO rewards (reward_name)
                VALUES
                ('10 Minuten Extra-Pause'),
                ('Eine Tafel Schokolade'),
                ('Ein Tag frei vom Training');
            ''')

    
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

    
        conn.commit()
        conn.close()

class Users:
    
    def is_user_registered():
        
        conn = sqlite3.connect('Database.db')
        cursor = conn.cursor()

       
        cursor.execute('''
            SELECT COUNT(*)
            FROM users
        ''')
        count = cursor.fetchone()[0]


        conn.close()
        return count > 0

    def register_user(username, password, user_class, user_race):
      
        conn = sqlite3.connect('Database.db')
        cursor = conn.cursor()

        try:
          
            cursor.execute('''
                SELECT COUNT(*) FROM users WHERE username = ?
            ''', (username,))
            result = cursor.fetchone()

            if result[0] > 0:
                ui.notify("Fehler: Der Benutzername ist bereits vergeben. Bitte wähle einen anderen.")
                return False 
            cursor.execute('''
                INSERT INTO users (username, user_password, user_class, user_race, user_level, user_xp, user_health, user_pic)
                VALUES (?, ?, ?, ?, ?, ?, ?, '')
            ''', (username, password, user_class, user_race, 1, 0, 100))

           
            conn.commit()
            ui.notify(f"Benutzer {username} erfolgreich registriert!")
            return True  

        except sqlite3.Error as e:
            ui.notify(f"Ein Fehler ist aufgetreten: {e}")
            return False  

        finally:
            
            conn.close()

    def check_user_exists(username):
       
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

  
        cursor.execute("SELECT COUNT(*) FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()

       
        conn.close()

       
        return result[0] > 0

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

    def get_user_data():
        conn = sqlite3.connect('Database.db')
        cursor = conn.cursor()

    
        cursor.execute('''
            SELECT username, user_level, user_xp, user_health, user_class, user_race, user_pic
            FROM users 
        ''', )
        return cursor.fetchone()
        


      
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

    def login_user(username, password):
        conn = sqlite3.connect('Database.db')
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM users WHERE username = ? AND user_password = ?
        ''', (username, password))
        user = cursor.fetchone()
        conn.close()
        return user


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
                       SELECT task_name, task_difficulty, task_xp, task_date, task_status FROM tasks WHERE task_status = 'open'
                   ''', )
       tasks = cursor.fetchall()
       conn.close()    
       return tasks 
    
    def show_all_tasks():
       conn = sqlite3.connect('Database.db')
       cursor = conn.cursor()   
       cursor.execute('''
                       SELECT task_name, task_difficulty, task_xp, task_date, task_status FROM tasks 
                   ''', )
       tasks_all = cursor.fetchall()
       conn.close()    
       return tasks_all

    def close_task(task_name, task_difficulty):
        conn = sqlite3.connect('Database.db')
        cursor = conn.cursor()

 
        if task_difficulty == 'Leicht':
            xp_gain = 10
        elif task_difficulty == 'Mittel':
            xp_gain = 30
        elif task_difficulty == 'Schwer':
            xp_gain = 50
        else:
            xp_gain = 0 

        cursor.execute('''
            UPDATE tasks SET task_status = 'closed' WHERE task_name = ?
        ''', (task_name,))
        ui.notify(f"{task_name} erfolgreich geschlossen!")
        conn.commit()

    
        cursor.execute('''
            UPDATE users
            SET user_xp = user_xp + ?
        ''', (xp_gain,))
        conn.commit()
        ui.notify(f"Task erfolgreich geschlossen! Der User hat jetzt {xp_gain} XP dazugewonnen.")

       
        cursor.execute('''
            UPDATE users
            SET user_level = user_level + 1,
            user_xp = user_xp - 100
            WHERE user_xp >= 100
        ''')
        conn.commit()

        
        ui.notify(f"Task erfolgreich geschlossen! Der User hat jetzt {xp_gain} XP dazugewonnen.")

class functions:
   
    
    def checkpw(self, password, password2, close_dialog):
        if password == password2:
            close_dialog()
            ui.notify('Login successful')
            ui.navigate.to('/Hi')
        else:
            ui.notify('Passwords do not match')


    def on_register_click(register_dialog):
        """ Final step: Notify and close dialog """
        ui.notify("Registrierung abgeschlossen! ✅", type='positive')
        print("Registration complete!")
        register_dialog.close()


              

