from nicegui import ui

ui.icon('thumb_up')
ui.markdown('This is **Markdown**.')
ui.html('This is <strong>HTML</strong>.')
with ui.row():
    ui.label('Jolette').style('color: #9b50e6; font-weight: Arial')
    ui.label('Tailwind').classes('font-serif')
    ui.label('Quasar').classes('q-ml-xl')
ui.link('NiceGUI on GitHub', 'https://github.com/zauberzeug/nicegui')

ui.run(port=5000)