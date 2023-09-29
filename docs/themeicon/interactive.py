import dash_mantine_components as dmc
from dash_iconify import DashIconify

from components.configurator import Configurator

TARGET_ID = "interactive-themeicon"

target = dmc.ThemeIcon(children=DashIconify(icon="tabler:photo"), id=TARGET_ID)

configurator = Configurator(target, TARGET_ID)
configurator.add_segmented_control("variant",["filled", "light", "outline"], "filled")
configurator.add_slider("size", "sm")
configurator.add_slider("radius", "sm")
configurator.add_colorpicker("color", "indigo")

component = configurator.panel
