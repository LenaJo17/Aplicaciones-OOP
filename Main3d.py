#!/usr/bin/env python3
from nicegui import app, ui
from nicegui.elements.mixins.color_elements import color

app.add_static_files('/stl', 'static')

with ui.scene(width=1024, height=800) as scene:
    scene.spot_light(distance=100, intensity=0.1).move(-10, 0, 10)
    model = scene.stl('/stl/Dragon 2.5_stl.stl').move(x=-0.5).scale(0.06)
    model.material(color = '#ba03fc')
ui.run(port=5000)

