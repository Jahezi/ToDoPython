from nicegui import ui
from functions import Users, Database, functions, Tasks
import sqlite3

function = functions
User = Users
Databass = Database
Task = Tasks

Databass.initialize_database()



@ui.page('/')
def Startpage():
    #login
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
        """Final step: Register user, notify and close dialog"""
        if User.is_user_registered():
            ui.notify("Fehler: Ein Benutzer ist bereits registriert. Es kann nur einen Benutzer geben.", type='negative')
        else:
            user = User.register_user(username_input.value, password_input.value, user_class_input.value, user_race_input.value)
            if user:
                ui.notify(f"Registrierung abgeschlossen! Willkommen {user} ✅", type='positive')
                register_dialog.close()
            else:
                ui.notify("Fehler: Registrierung fehlgeschlagen", type='negative')


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


@ui.page('/user')
def tasks():
<<<<<<< HEAD
    user_data = User.get_user_data()
    if user_data:
        username, user_level, user_xp, user_health, user_class, user_race, user_pic = user_data
        ui.label(f'Username: {username}')
        ui.label(f'Level: {user_level}')
        ui.label(f'XP: {user_xp} / 100')
        ui.label(f'Health: {user_health}')
        ui.label(f'Class: {user_class}')
        ui.label(f'Race: {user_race}')
    else:
        ui.label('Benutzerdaten konnten nicht abgerufen werden.')
        
=======
    @ui.refreshable
    def user_data():
     user_data = User.get_user_data()
     if user_data:
         username, user_level, user_xp, user_health, user_class, user_race, user_pic = user_data
         ui.label(f'Username: {username}')
         ui.label(f'Level: {user_level}')
         ui.label(f'XP: {user_xp} / 100')
         ui.label(f'Health: {user_health}')
         ui.label(f'Class: {user_class}')
         ui.label(f'Race: {user_race}')
     else:
         ui.label('Benutzerdaten konnten nicht abgerufen werden.')
        
    user_data()


>>>>>>> 824280897b114b394b10f4f2ea0eba252f4e3922
    def close_task_with_container(card, task_name, task_difficulty):
        container.remove(card)  # Remove the specific card

        Task.close_task(task_name, task_difficulty)
<<<<<<< HEAD
=======
        user_data.refresh()

>>>>>>> 824280897b114b394b10f4f2ea0eba252f4e3922
         # Schließt den Task und aktualisiert den Status in der Datenbank
        # XP des Benutzers aktualisieren


    # Funktion zum Aktualisieren der XP des Benutzers
   
    container = ui.row()

    def add_task(task_name, task_difficulty, task_date, task_status):
        with container:
            with ui.card() as card:
                ui.label(task_name)
                ui.label(task_difficulty)
                ui.label(task_date)
                ui.label(task_status)
                ui.button('Close Task', on_click=lambda: close_task_with_container(card, task_name, task_difficulty))
    
    # Loop through the tasks and create individual cards for each task
    tasks = Task.show_tasks()
    with ui.row():  # Begin a horizontal layout
        for task in tasks:
            task_name, task_difficulty, task_xp, task_date, task_status = task
            add_task(task_name, task_difficulty, task_date, task_status)
    
    # Function to create a new task and display it in a new card
    def on_task_create_click():
        Task.create_task(task_name.value, task_difficulty.value, date.value)
        add_task(task_name.value, task_difficulty.value, date.value, 'Open')
        task_dialog.close()

    with ui.dialog() as task_dialog:  #Task creation
        with ui.card():
            ui.label('Task erstellen')
            task_name = ui.input('Taskname').classes('w-full')
            task_difficulty = ui.toggle({'Leicht': 'Leicht', 'Mittel': 'Mittel', 'Schwer': 'Schwer'}).props('required').classes('w-full')
            with ui.input('Date') as date:
                with ui.menu().props('no-parent-event') as menu:
                    with ui.date().bind_value(date):
                        with ui.row().classes('justify-end'):
                            ui.button('Close', on_click=menu.close).props('flat')
            with date.add_slot('append'):
                ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')
            ui.button('Task erstellen!', on_click=on_task_create_click)

    with ui.row():
        ui.button('Add Task', on_click=task_dialog.open)
        ui.button('Tasks anzeigen', on_click = lambda: ui.navigate.to('/tasks'))
<<<<<<< HEAD
=======
        ui.button('Refresh')
>>>>>>> 824280897b114b394b10f4f2ea0eba252f4e3922

@ui.page('/tasks')
def tasks_show():
   tasks = Task.show_all_tasks()
   with ui.row():  # Beginne eine horizontale Ausrichtung
        for task in tasks:
            with ui.card():
                ui.label(f"Task Name: {task[0]}")
                ui.label(f"Status: {task[1]}")
                ui.label(f"Difficulty: {task[2]}")
                
   ui.button('Zurück', on_click = lambda: ui.navigate.to('/user'))
    






    










ui.run()
