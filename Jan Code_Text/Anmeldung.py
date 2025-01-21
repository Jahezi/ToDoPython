import sqlite3
from Users import register_user, login_user, show_user_status, show_all_users, delete_user
from Tasks import create_task, show_tasks, end_task, delete_task

def not_logged_in_user():
    print("Willkommen im Hero Quest!")
    print("1. Benutzer registrieren")
    print("2. Benutzer einloggen")
    print("3. User anzeigen")
    print("4. Spiel beenden")
    
    choice = input("\nWähle eine Option: ")

    if choice == "1":
        username = input("Benutzername: ")

        while True:
            user_race = input("Rasse des Benutzers (Mensch, Elf, Zwerg): ")
            if user_race in ["Mensch", "Elf", "Zwerg"]:
             break
            else:
             print("Ungültige Rasse.")

        while True:
            user_class = input("Klasse des Benutzers (Ritter, Bogenschütze, Magier): ")
            if user_class in ["Ritter", "Bogenschütze", "Magier"]:
                break
            else:
                print("Ungültige Klasse.")

        while True:
            if user_race == 'Mensch':
                print("Mensch_1")
                print("Mensch_2")
                user_pic = input("Wähle ein Profilbild: ")
                if user_pic in ["Mensch_1", "Mensch_2"]:
                    break
                else:
                    print("Ungültige Eingabe!")

            elif user_race == 'Elf':
                print("Elf_1")
                print("Elf_2")
                user_pic = input("Wähle ein Profilbild: ")
                if user_pic in ["Elf", "Elf"]:
                    break
                else:
                    print("Ungültige Eingabe!")
            elif user_race == 'Zwerg':
                print("Zwerg_1")
                print("Zwerg_2")
                user_pic = input("Wähle ein Profilbild: ")
                if user_pic in ["Zwerg_1", "Zwerg_2"]:
                    break
                else:
                    print("Ungültige Eingabe!")
            
        password = input("Passwort: ")
        register_user(username, password, user_class, user_race,user_pic)
        return not_logged_in_user()
    
    elif choice == "2":
        username = input("Benutzername: ")
        password = input("Passwort: ")
        user = login_user(username, password)
        if user:
            print(f"Willkommen! {username} erfolgreich eingeloggt!")
            return logged_in_user(username)
        
        else:
            print("Fehler: Benutzername oder Passwort falsch")
            return not_logged_in_user()
        
    elif choice == "3":
        show_all_users()
        return not_logged_in_user()
    
    elif choice == "4":
        print("Spiel wurde beendet")
        return
    else:
        print("Ungültige Eingabe.")
        return not_logged_in_user()

def logged_in_user(username):
    print("\n1. Task erstellen")
    print("2. Task anzeigen")
    print("3. Task beenden")
    print("4. Status anzeigen")
    print("5. Optionen")
    print("6. Log off")
    print("7. Spiel beenden")

    choice = input("Wähle eine Option: ")

    if choice == "1":
        create_task(username)
        return logged_in_user(username)
    
    elif choice == "2":
        show_tasks(username)
        input("\nDrücke Enter um ins Menü zurückzukehren.")
        return logged_in_user(username)
        
    elif choice == "3":
        print("Hier siehst du alle Tasks:\n")
        show_tasks(username)
        print("1. Einen Task beenden.")
        print("2. Zurück ins Menü.")
        choice = input("Wähle eine Option: ")
        
        if choice == "1":
            end_task(username)
            return logged_in_user(username)
        
        elif choice == "2":
            return logged_in_user(username)
        
        else:
            print("Ungültige Eingabe.")
            return logged_in_user(username)
    
    elif choice == "4":
        show_user_status(username)
        return logged_in_user(username)
    
    elif choice == "5":
        print("1. User löschen")
        print("2. Task löschen")
        print("3. Zurück ins Menü")

        choice = input("Wähle eine Option: ")

        if choice == "1":
            choice =  input("Möchtest du deinen Benutzer löschen? (Ja/Nein)")
            if choice == "Ja":
                delete_user(username)
                return not_logged_in_user()
            else:
                print("Löschvorgang abgebrochen.")
                return 

        elif choice == "2":
            delete_task(username)
            return logged_in_user(username)
        else:
            return logged_in_user(username)

    elif choice == "6":
        print("Du wurdest ausgeloggt.")
        return not_logged_in_user()
    
    elif choice == "7":
        print("Spiel wurde beendet")
        return
    else:
        print("Ungültige Eingabe.")
        return logged_in_user(username)




            
        
        
