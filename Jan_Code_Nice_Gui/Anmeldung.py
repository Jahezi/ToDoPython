from nicegui import ui
from Tasks import create_task, show_tasks, end_task, delete_task
from Users import register_user, login_user, show_user_status, delete_user


def start_app():
    def login():
        username = username_input
        password = password_input
        user = login_user(username, password)
        if user:
            ui.notify(f"Willkommen {username}!")
            show_logged_in_menu(username)
        else:
            ui.notify("Benutzername oder Passwort falsch.", color='red')

    def register():
        def submit():
            username = username_input
            password = password_input
            user_race = user_race_input
            user_class = user_class_input
            user_pic = "default"  # This can be extended for profile picture selection.
            register_user(username, password, user_class, user_race, user_pic)
            ui.notify(f"Benutzer {username} erfolgreich registriert!")
            dialog.close()

        with ui.dialog() as dialog:
            with ui.card():
                username_input = ui.input("Benutzername").bind_value()
                password_input = ui.input("Passwort", password=True).bind_value()
                user_race_input = ui.select(["Mensch", "Elf", "Zwerg"], label="Rasse").bind_value()
                user_class_input = ui.select(["Ritter", "Bogenschütze", "Magier"], label="Klasse").bind_value()
                ui.button("Registrieren", on_click=submit)

    ui.label("Willkommen im Hero Quest!").classes("text-2xl text-center")
    with ui.row():
        username_input = ui.input("Benutzername").bind_value()
        password_input = ui.input("Passwort", password=True).bind_value()
        ui.button("Einloggen", on_click=login)
        ui.button("Registrieren", on_click=register)


def show_logged_in_menu(username):
    ui.clear()
    ui.label(f"Willkommen, {username}").classes("text-2xl text-center")

    def create_task_ui():
        def submit():
            create_task(username)
            ui.notify("Task erfolgreich erstellt!")
            dialog.close()

        with ui.dialog() as dialog:
            with ui.card():
                ui.input("Name der Aufgabe").bind_value()
                ui.select(["Leicht", "Mittel", "Schwer"], label="Schwierigkeit").bind_value()
                ui.input("Datum der Aufgabe").bind_value()
                ui.button("Erstellen", on_click=submit)

    def display_tasks():
        ui.clear()
        tasks = show_tasks(username)
        with ui.table():
            for task in tasks:
                ui.row(*task)

    ui.button("Task erstellen", on_click=create_task_ui)
    ui.button("Tasks anzeigen", on_click=display_tasks)
    ui.button("Status anzeigen", on_click=lambda: show_user_status(username))
    ui.button("Ausloggen", on_click=start_app)


if __name__ == "__main__":
    start_app()
    ui.run(port=8080)
