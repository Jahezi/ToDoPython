from nicegui import ui

# Funktion zum Öffnen der Login-Maske
def open_login():
    with ui.modal().classes('bg-white p-6 rounded-lg shadow-lg'):
        ui.label("Login").classes("text-xl font-semibold")
        with ui.form():
            ui.input(label="Benutzername", placeholder="Benutzername eingeben")
            ui.input(label="Passwort", placeholder="Passwort eingeben", password=True)
            ui.button("Einloggen").on_click(close_login)
        ui.button("Abbrechen", on_click=close_login).classes("mt-4")
        

# Funktion zum Schließen der Login-Maske
def close_login():
    ui.close_modal()

# Hauptoberfläche
ui.button("Login").on_click(open_login)
ui.run()
