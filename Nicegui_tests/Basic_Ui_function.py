from nicegui import ui

# Benutzerliste zur Speicherung von Anmeldedaten
users = {}

# Definiere die Hauptseite
@ui.page('/')
def main_page():
    with ui.column():
        ui.label('Dies ist die Hauptseite')
        ui.button('Zur Login-Seite', on_click=lambda: ui.navigate.to('/login'))
        ui.button('Zur Registrierungsseite', on_click=lambda: ui.navigate.to('/register'))

# Definiere die Login-Seite
@ui.page('/login')
def login_page():
    with ui.column():
        ui.label('Dies ist die Login-Seite')
        username = ui.input(label='Benutzername', password=False)
        password = ui.input(label='Passwort', password=True)
        
        def handle_login():
            if username.value in users and users[username.value] == password.value:
                ui.notify(f'Login erfolgreich für Benutzer: {username.value}', duration=3)
            else:
                ui.notify('Ungültiger Benutzername oder Passwort', color='red', duration=3)

        ui.button('Login', on_click=handle_login)
        ui.button('Zurück zur Hauptseite', on_click=lambda: ui.navigate.to('/'))

# Definiere die Registrierungsseite
@ui.page('/register')
def register_page():
    with ui.column():
        ui.label('Dies ist die Registrierungsseite')
        username = ui.input(label='Benutzername', password=False)
        password = ui.input(label='Passwort', password=True)
        email = ui.input(label='E-Mail', password=False)
        
        def handle_register():
            if username.value in users:
                ui.notify('Benutzername existiert bereits', color='red', duration=3)
            else:
                users[username.value] = password.value
                ui.notify(f'Benutzer {username.value} erfolgreich registriert', color='green', duration=3)

        ui.button('Registrieren', on_click=handle_register)
        ui.button('Zurück zur Hauptseite', on_click=lambda: ui.navigate.to('/'))

# Starte die Anwendung
ui.run()
