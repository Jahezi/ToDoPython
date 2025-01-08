from nicegui import ui

ui.add_head_html('<style>body { background-image: url("https://i.redd.it/51r6w0a9v1a81.png"); background-size: cover; }</style>')
ui.add_head_html('<style>.centered-label { position: absolute; top: 20px; left: 50%; transform: translateX(-50%); font-size: 36px; color: Black; }</style>')
ui.label('Willkommen zu Quest-Rpg').classes('centered-label')

with ui.label().style('position: fixed; bottom: 0; left: 0; width: 100%;'):
    ui.label('Erstellt von Jan Zimmerle und Leon Hein').style('margin-left: 10px; color: white;')

with ui.row().style('height: 100vh; display: flex; align-items: center; justify-content: center; color: Black;'):
    with ui.column().style('align-items: center;'):
        ui.button('Anmelden', color='red')
        ui.button('Neuen Charakter erstellen', color='red')

ui.run()