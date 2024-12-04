from nicegui import ui

class Demo:
    def __init__(self):
        self.number = 1

demo = Demo()
v = ui.checkbox('visible', value=True)
with ui.column().bind_visibility_from(v, 'value'):
    ui.slider(min=1, max=3).bind_value(demo, 'number')
    ui.toggle({1: 'Sol', 2: 'Luna', 3: 'Eclipse'}).bind_value(demo, 'number')
    ui.number().bind_value(demo, 'number')

ui.run(port=5000)