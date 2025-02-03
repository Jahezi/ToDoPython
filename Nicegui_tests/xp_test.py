from nicegui import ui
from functions import Users, Database, functions, Tasks
import sqlite3

Task = Tasks
User = Users

@ui.page('/')
def tasks():
    global user_xp
    user_xp = 0

    def close_task_with_container(card, task_name):
        container.remove(card)  # Remove the specific card

        Task.close_task(task_name)  # Schließt den Task und aktualisiert den Status in der Datenbank
        xp_points = 10  # Anzahl der XP-Punkte, die der Benutzer erhalten soll
        update_user_xp(xp_points)

    def update_user_xp(xp_points):
        global user_xp
        user_xp += xp_points
        xp_bar.set_value(user_xp)
        connection = sqlite3.connect('Database.db')
        cursor = connection.cursor()
        cursor.execute('''
            UPDATE users SET xp = xp + ? WHERE user_id = ?
        ''', (xp_points,))
        connection.commit()
        connection.close()

    container = ui.row()

    def add_task(task_name, task_difficulty, task_date, task_status):
        with container:
            with ui.card() as card:
                ui.label(task_name)
                ui.label(task_difficulty)
                ui.label(task_date)
                ui.label(task_status)
                ui.button('Close Task', on_click=lambda: close_task_with_container(card, task_name))

    tasks = Task.show_tasks()
    with ui.row():  # Begin a horizontal layout
        for task in tasks:
            task_name, task_difficulty, task_xp, task_date, task_status = task
            add_task(task_name, task_difficulty, task_date, task_status)

    def on_task_create_click():
        Task.create_task(task_name.value, task_difficulty.value, date.value)
        add_task(task_name.value, task_difficulty.value, date.value, 'Open')
        task_dialog.close()

    with ui.dialog() as task_dialog:
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


    xp_value = 
    
   
    User.get_user_data(usernae)
    ui.label(f'Username:'{username})

ui.run()


    with ui.row():
        ui.button('Add Task', on_click=task_dialog.open)
        ui.button('Clear Tasks', on_click=container.clear)
        ui.button('zurück', on_click=lambda: ui.navigate.to('/user'))
        slider = ui.slider(min=0, max=1, step=0.01, value=0.5)
        ui.linear_progress().bind_value_from(slider, 'value')
        progress_bar = ui.linear_progress().set_value(xp_value)

ui.run()
