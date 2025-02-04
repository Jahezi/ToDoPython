from nicegui import ui
from datetime import datetime

# Funktion zur Aktualisierung der Uhrzeit
def update_time(label):
    label.set_text(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

ui.colors(background='gray')

# Hauptspalte für das gesamte Layout
ui.page('/')
with ui.column().style('padding: 20px;'):
    # Taste (Button) unten links
    with ui.row().style('position: fixed; bottom: 20px; left: 20px;'):
        ui.button('Taste')

    # XP-Leiste unten in der Mitte, vergrößert und auf 10% eingestellt
    with ui.row().style('position: fixed; bottom: 60px; left: 50%; transform: translateX(-50%); width: 50%;'):
        ui.linear_progress(value=0.01).props('color="blue" height="30px"')

    # Lebensleiste unten in der Mitte, vergrößert und auf 1% eingestellt
    with ui.row().style('position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%); width: 50%;'):
        ui.linear_progress(value=0.01).props('color="green" height="30px"')

    
    with ui.row().style('position: fixed; top: 20px; right: 20px;'):
        time_label = ui.label(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).style('font-size: 18px; font-weight: bold;')
        ui.timer(1.0, lambda: update_time(time_label))

ui.run()
