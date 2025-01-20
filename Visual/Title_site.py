from nicegui import ui

ui.add_head_html('<style>body { overflow: hidden; }</style>')
ui.add_head_html('<style>body { background-color: grey; /* Beispiel: Grauer Hintergrund */ }</style>')
ui.add_head_html('<style>.centered-label { position: absolute; top: 20px; left: 50%; transform: translateX(-50%); font-size: 48px; font-weight: bold; color: white; }</style>')
ui.add_head_html('<style>.ui-card { background-color: lightgrey; /* Beispiel: Hellgrauer Hintergrund für Karten */ }</style>')

# Fügt die größere Überschrift hinzu
ui.add_body_html('<div class="centered-label">Quest-RPG</div>')

with ui.label().style('position: fixed; bottom: 0; left: 0; width: 100%;'):
    ui.label('Erstellt von Jan Zimmerle und Leon Hein').style('margin-left: 10px; color: black;')

with ui.card().classes('absolute-center ui-card'):  # Fügt hier die Klasse ui-card hinzu
    ui.button('Anmelden')
    ui.button('Caracter erstellen')

ui.run()
