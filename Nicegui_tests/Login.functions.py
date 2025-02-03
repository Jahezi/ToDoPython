from nicegui import ui
from functions import functions, Users
import sqlite3

function = functions
User = Users

@ui.page('/')
def Startpage():
    with ui.dialog() as dialog:
        with ui.card():
            ui.label('Login')
            username = ui.input('Benutzername').classes('w-full')
            password = ui.input('Passwort', password=True).classes('w-full')
            def handle_login():
                user = User.login_user(username.value, password.value)
                if user:
                    ui.notify(f"Willkommen {user}")
                    dialog.close()
                    ui.navigate.to('/Hi')

                else:
                    ui.notify("Fehler: Benutzername oder Passwort falsch")

            ui.button('Login', on_click=handle_login).classes('w-full')
    ui.button('Open Login Dialog', on_click=dialog.open)

@ui.page('/Hi')
def hi():
    ui.button('Zurück', on_click=lambda: ui.navigate.to('/'))

ui.run()

