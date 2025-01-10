from Tasks import create_task
import sqlite3
from Database import initialize_database
from Users import delete_user, login_user, register_user, show_all_users

def main_menu():
    print("Willkommen im Spiel!")
    print("1. Benutzer registrieren")
    print("2. Benutzer einloggen")
    print("3. Task erstellen")
    print("4. User löschen")
    
    choice = input("Wähle eine Option: ")
    
    if choice == "1":
        username = input("Benutzername: ")
        user_class = input("Klasse des Benutzers (Ritter, Bogenschütze, Magier): ")
        if user_class not in ["Ritter", "Bogenschütze", "Magier"]:
            print("Ungültige Klasse.")
            return
                
        password = input("Passwort: ")
        register_user(username, password, user_class)
    elif choice == "2":
        username = input("Benutzername: ")
        password = input("Passwort: ")
        user = login_user(username, password)
        if user:
            print(f"Willkommen zurück, {user[1]}!")
        else:
            print("Falscher Benutzername oder Passwort.")
    elif choice == "3":
        name = input("Name der Aufgabe: ")
        difficulty = input("Schwierigkeit der Aufgabe (leicht, mittel, schwer): ")
        if difficulty not in ["leicht", "mittel", "schwer"]:
            print("Ungültige Schwierigkeit.")
            return
        create_task(name, difficulty)
    elif choice == "4":
        show_all_users(username, password, user_class)
        username = input("Benutzername: ")
        password = input("Passwort: ")
        user_class =input("Userclass:")
        delete_user(username, password, user_class)
        print("Benutzer gelöscht.")
    else:
        print("Ungültige Auswahl.")
        main_menu()

main_menu()