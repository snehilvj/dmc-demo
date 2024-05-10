import dash_mantine_components as dmc

from lib.configurator import Configurator

data = [
  { "name": "USA", "value": 400, "color": "indigo.6" },
  { "name": "India", "value": 300, "color": "yellow.6" },
  { "name": "Japan", "value": 100, "color": "teal.6" },
  { "name": "Other", "value": 200, "color": "gray.6" }
]


target = dmc.DonutChart(
    data=data,
    size=160,
    thickness=20
)

configurator = Configurator(target)
configurator.add_number_slider("size", 275, min=80, max=300)
configurator.add_number_slider("thickness", 20, min=2, max=30)

component = configurator.panel

