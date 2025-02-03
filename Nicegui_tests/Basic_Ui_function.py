from nicegui import ui
from functions import functions

function = functions

# Function to open login dialog
def open_login():
    login_dialog.open()

# Function to open registration dialog
def open_register():
    register_dialog.open()

### LOGIN DIALOG ###
with ui.dialog() as login_dialog:
    with ui.card():
        ui.label('Login').classes('text-xl font-bold')
        username = ui.input('Benutzername').classes('w-full')
        password = ui.input('Passwort', password=True).classes('w-full')
        ui.button('Login', on_click=login_dialog.close).classes('w-3/4')  # Smaller button
        ui.button("Noch kein Konto? Registrieren", on_click=lambda: [login_dialog.close(), open_register()]).props('flat').classes('text-sm')

with ui.dialog() as register_dialog:
    with ui.card():
        ui.label('Registration').classes('text-xl font-bold')
        with ui.stepper().props('vertical').classes('w-full') as stepper:

            # Step 1: Username and Password
            with ui.step('Set Username and Password'):
                reg_username = ui.input(label='Benutzername').props('required').classes('w-full')
                reg_password = ui.input(label='Passwort', password=True, password_toggle_button=True).props('required').classes('w-full')
                with ui.stepper_navigation():
                    ui.button('Next', on_click=function.validate_step_1).classes('w-3/4')

            # Step 2: Choose Class
            with ui.step('Choose Your Class'):
                user_class_input = ui.toggle({1: 'Ritter', 2: 'Bogenschütze', 3: 'Magier'}).props('required').classes('w-full')
                with ui.stepper_navigation():
                    ui.button('Next', on_click=function.validate_step_2).classes('w-3/4')
                    ui.button('Back', on_click=stepper.previous).props('flat').classes('w-1/2')

            # Step 3: Choose Race
            with ui.step('Choose Your Race'):
                user_race_input = ui.toggle({1: 'Mensch', 2: 'Elf', 3: 'Zwerg'}).props('required').classes('w-full')
                with ui.stepper_navigation():
                    ui.button('Next', on_click=function.validate_step_3).classes('w-3/4')
                    ui.button('Back', on_click=stepper.previous).props('flat').classes('w-1/2')

            # Step 4: Complete Registration
            with ui.step('Complete Registration'):
                ui.button('Register', on_click=function.on_register_click).classes('w-3/4')
                with ui.stepper_navigation():
                    ui.button('Back', on_click=stepper.previous).props('flat').classes('w-1/2')

        ui.button("Bereits registriert? Login", on_click=lambda: [register_dialog.close(), open_login()]).props('flat').classes('text-sm')


# Main UI Buttons
with ui.column().classes("items-center w-full"):
    # Hero Quest Title
    ui.label("Hero Quest").classes("text-4xl font-bold text-center my-6")
    ui.button('Login', on_click=open_login).classes('w-1/3')
    ui.button('Register', on_click=open_register).classes('w-1/3')

ui.run()
