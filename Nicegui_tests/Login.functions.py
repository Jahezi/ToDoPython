from nicegui import ui
from functions import Users, Database, functions, Tasks
import sqlite3

function = functions
User = Users
Databass = Database
Task = Tasks

Databass.initialize_database()

def check_user_exists():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0

@ui.page('/registration')
def Startpage():
    # login
    with ui.dialog() as logindialog:
        with ui.card():
            ui.label('Login')
            username = ui.input('Benutzername').classes('w-full')
            password = ui.input('Passwort', password=True).classes('w-full')

            def handle_login():
                user = User.login_user(username.value, password.value)
                if user:
                    ui.notify(f"Willkommen {user}")
                    logindialog.close()
                    ui.navigate.to('/user')
                else:
                    ui.notify("Fehler: Benutzername oder Passwort falsch")

            ui.button('Login', on_click=handle_login).classes('w-full')

    def validate_step_1():
        username_valid = username_input.value is not None and username_input.value != ""
        password_valid = password_input.value is not None and password_input.value != ""
        passwords_match = password_input.value == confirm_password_input.value

        if User.check_user_exists(username_input.value):
            ui.notify("Benutzer existiert bereits. Weiterleitung zur User-Page...", type='info')
            ui.open_page('/user_page')  # Zur User-Page weiterleiten
            return

        if not passwords_match:
            confirm_password_input.props('error').update()
            ui.notify("Passwörter stimmen nicht überein!", type='warning')
        else:
            confirm_password_input.props(remove='error').update()

        if username_valid and password_valid and passwords_match:
            stepper.next()

    def validate_step_2():
        if user_class_input.value is None:
            user_class_input.props('error').update()
            ui.notify("Bitte wählen Sie eine Klasse aus!", type='warning')
        else:
            user_class_input.props(remove='error').update()
            stepper.next()

    def validate_step_3():
        if user_race_input.value is None:
            user_race_input.props('error').update()
            ui.notify("Bitte wählen Sie eine Rasse aus!", type='warning')
        else:
            user_race_input.props(remove='error').update()
            stepper.next()

    def on_register_click():
        user = User.register_user(username_input.value, password_input.value, user_class_input.value, user_race_input.value)
        if user:
            ui.notify(f"Registrierung abgeschlossen! Willkommen {user} ✅", type='positive')
            register_dialog.close()
        else:
            ui.notify("Fehler: Registrierung fehlgeschlagen")

    with ui.dialog() as register_dialog:
        with ui.card():
            ui.label('Registration')
            with ui.stepper().props('vertical').classes('w-full') as stepper:

                # Step 1: Username and Password
                with ui.step('Set Username and Password'):
                    username_input = ui.input(label='Benutzername').props('required').classes('w-full')
                    password_input = ui.input(label='Passwort', password=True, password_toggle_button=True).props('required').classes('w-full')
                    confirm_password_input = ui.input(label='Passwort bestätigen', password=True, password_toggle_button=True).props('required').classes('w-full')
                    with ui.stepper_navigation():
                        ui.button('Next', on_click=validate_step_1).classes('w-full')

                # Step 2: Choose Class
                with ui.step('Choose Your Class'):
                    user_class_input = ui.toggle({'Ritter': 'Ritter', 'Bogenschütze': 'Bogenschütze', 'Magier': 'Magier'}).props('required').classes('w-full')
                    with ui.stepper_navigation():
                        ui.button('Next', on_click=validate_step_2).classes('w-full')
                        ui.button('Back', on_click=stepper.previous).props('flat').classes('w-full')

                # Step 3: Choose Race
                with ui.step('Choose Your Race'):
                    user_race_input = ui.toggle({'Mensch': 'Mensch', 'Elf': 'Elf', 'Zwerg': 'Zwerg'}).props('required').classes('w-full')
                    with ui.stepper_navigation():
                        ui.button('Next', on_click=validate_step_3).classes('w-full')
                        ui.button('Back', on_click=stepper.previous).props('flat').classes('w-full')

                # Step 4: Complete Registration
                with ui.step('Complete Registration'):
                    ui.button('Register', on_click=on_register_click).classes('w-full')
                    with ui.stepper_navigation():
                        ui.button('Back', on_click=stepper.previous).props('flat').classes('w-full')

    ui.button('Open Login Dialog', on_click=logindialog.open)
    ui.button('Open Register Dialog', on_click=register_dialog.open)

@ui.page('/')
def index():
    if not check_user_exists():
        return ui.open_page('/registration')
    return "Willkommen auf der Hauptseite"

if __name__ == '__main__':
    ui.run()
