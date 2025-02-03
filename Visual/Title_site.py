from nicegui import ui


ui.add_head_html('<style>body { overflow: hidden; }</style>')
ui.add_head_html('<style>body { background-color: grey;  }</style>')
ui.add_head_html('<style>.centered-label { position: absolute; top: 20px; left: 50%; transform: translateX(-50%); font-size: 48px; font-weight: bold; color: white; }</style>')
ui.add_head_html('<style>.ui-card { background-color: lightgrey; }</style>')

# Überschrift
ui.add_body_html('<div class="centered-label">Quest-RPG</div>')

with ui.label().style('position: fixed; bottom: 0; left: 0; width: 100%;'):
    ui.label('Erstellt von Jan Zimmerle und Leon Hein').style('margin-left: 10px; color: black;')

def open_anmelden_site():
    ui.navigate.to('Anmelden_Site.py')

with ui.card().classes('absolute-center ui-card'):  # Fügt hier die Klasse ui-card hinzu
    ui.button('Anmelden', on_click=open_anmelden_site)
    ui.button('Caracter erstellen')

ui.run()