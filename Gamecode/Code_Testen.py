# Login von Leon
def login(username, password):
    correct_username = "Leon" 
    correct_password = "Hein"
    
    if username == correct_username and password == correct_password:
        return "Die Anmeldung war erfolgreich!"
    else:
        return "Das Benutzername oder Passwort war falsch :-(."

benutzername = input("Benutzername: ")
passwort = input("Passwort: ")

if login(benutzername, passwort) == "Die Anmeldung war erfolgreich!":
    current_user = benutzername
else:
    current_user = None

print(login(benutzername, passwort))

class Character:
    def __init__(self, name, character_class, max_health):
        self.name = name
        self.character_class = character_class
        self.max_health = max_health
        self.current_health = max_health

    def take_damage(self, amount):
        self.current_health -= amount
        if self.current_health < 0:
            self.current_health = 0

    def heal(self, amount):
        self.current_health += amount
        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def display_health(self):
        health_bar = "[" + "#" * self.current_health + " " * (self.max_health - self.current_health) + "]"
        return f"{self.name} ({self.character_class}) Health: {health_bar} {self.current_health}/{self.max_health}"

def choose_class():
    print("Wähle eine Klasse:")
    print("1. Krieger")
    print("2. Magier")
    print("3. Bogenschütze")
    
    choice = input("Gib die Nummer der gewünschten Klasse ein: ")
    
    if choice == '1':
        return "Krieger"
    elif choice == '2':
        return "Magier"
    elif choice == '3':
        return "Bogenschütze"
    else:
        print("Ungültige Auswahl. Standardmäßig wird 'Krieger' gewählt.")
        return "Krieger"

if current_user:
    character_name = input("Gib den Namen deines Charakters ein: ")
    character_class = choose_class()
    character = Character(character_name, character_class, 100)
    print(character.display_health())

    # Schaden zufügen über Eingabe
    damage = int(input("Wie viel Schaden soll zugefügt werden? "))
    character.take_damage(damage)
    print(character.display_health())
