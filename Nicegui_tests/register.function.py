from nicegui import ui
from functions import Users, Database

user = Users
Databass = Database

Databass.initialize_database()

def validate_step_1():
    """ Validate username and passwords before proceeding. """
    username_valid = bool(username_input.value.strip())
    password_valid = bool(password_input.value.strip())
    passwords_match = password_input.value == confirm_password_input.value

    if not username_valid:
        username_input.props('error').update()
        ui.notify("Bitte geben Sie einen Benutzernamen ein!", type='warning')
    else:
        username_input.props(remove='error').update()

    if not password_valid:
        password_input.props('error').update()
        ui.notify("Bitte geben Sie ein Passwort ein!", type='warning')
    else:
        password_input.props(remove='error').update()

    if not passwords_match:
        confirm_password_input.props('error').update()
        ui.notify("Passwörter stimmen nicht überein!", type='warning')
    else:
        confirm_password_input.props(remove='error').update()

    if username_valid and password_valid and passwords_match:
        stepper.next()

def validate_step_2():
    """ Validate class selection before proceeding. """
    if user_class_input.value is None:
        user_class_input.props('error').update()
        ui.notify("Bitte wählen Sie eine Klasse aus!", type='warning')
    else:
        user_class_input.props(remove='error').update()
        stepper.next()

def validate_step_3():
    """ Validate race selection before proceeding. """
    if user_race_input.value is None:
        user_race_input.props('error').update()
        ui.notify("Bitte wählen Sie eine Rasse aus!", type='warning')
    else:
        user_race_input.props(remove='error').update()
        stepper.next()

def on_register_click():
    """ Final step: Register user, notify and close dialog """
    user.register_user(username_input.value, password_input.value, user_class_input.value, user_race_input.value)
    ui.notify("Registrierung abgeschlossen! ✅", type='positive')
    print("Registration complete!")
    dialog.close()

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

# Open Registration Dialog Button
ui.button('Open Registration Dialog', on_click=register_dialog.open)

ui.run()
