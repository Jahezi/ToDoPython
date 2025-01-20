from nicegui import ui

with ui.column().style('max-width: 500px; margin: auto; padding: 10px;'):
    ui.label('Aufgabe erstellen')
    task_name = ui.input('Name der Aufgabe').props('outlined')
    task_difficulty = ui.select(['Leicht', 'Mittel', 'Schwer']).props('label="Schwierigkeit der Aufgabe" outlined')
    date = ui.input('Datum der Aufgabe').props('outlined')
    ui.button('Erstellen')

    ui.separator()
    ui.label('Alle Aufgaben')
    with ui.table(rows=[]).props('rows-per-page-options="5" dense'):
        with ui.row():
            ui.label('Taskname: Beispielaufgabe')
            ui.label('Schwierigkeit: Mittel')
            ui.label('XP: 250')
            ui.label('Datum: 15.01.2025')
            ui.label('Status: offen')

ui.run()
