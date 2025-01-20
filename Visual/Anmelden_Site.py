from nicegui import ui

ui.add_head_html('<style>body { overflow: hidden; }</style>')
ui.add_head_html('<style>body { background-color: grey;}</style>')

# Fügt die Überschrift hinzu
ui.add_head_html('<style>.title { text-align: center; font-size: 36px; font-weight: bold; margin-top: 20px; color: white; }</style>')
ui.add_body_html('<div class="title">Quest-RPG</div>')

with ui.card().classes('absolute-center'):
    ui.input('Benutzername')
    ui.input('Kennwort', password=True)
    ui.button('Anmelden')

ui.run()
