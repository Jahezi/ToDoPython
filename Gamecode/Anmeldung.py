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
    def __init__(self, name, max_health):
        self.name = name
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
        return f"{self.name} Health: {health_bar} {self.current_health}/{self.max_health}"

# Beispielaufruf
char = Character("Leon", 100)
print(char.display_health())

# Schaden zufügen über Eingabe
damage = int(input("Wie viel Schaden soll zugefügt werden? "))
char.take_damage(damage)
print(char.display_health())
