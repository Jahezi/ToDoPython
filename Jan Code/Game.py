from users import register_users

def main_menu():
    print("Willkommen im Spiel!")
    print("1. Benutzer registrieren")
    print("2. Aufgaben anzeigen")
    print("3. Kampf gegen Monster")
    print("4. Beenden")
    
    choice = input("Wähle eine Option: ")
    
    if choice == "1":
        username = input("Benutzername: ")
        user_class = input("Klasse des Benutzers: ")
        register_user(username, user_class)
    
    elif choice == "2":
        user_id = int(input("Benutzer ID: "))
        show_user_tasks(user_id)
    
    elif choice == "3":
        user_id = int(input("Benutzer ID: "))
        monster_id = int(input("Monster ID: "))
        battle_with_monster(user_id, monster_id)
    
    elif choice == "4":
        print("Auf Wiedersehen!")
        exit()
    
    else:
        print("Ungültige Auswahl.")
        main_menu()

main_menu()
