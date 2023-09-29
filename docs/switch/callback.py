import dash_mantine_components as dmc
from dash import html, Output, Input, callback

component = html.Div(
    [
        dmc.Switch(id="switch-example", label="Use default settings.", checked=True),
        dmc.Space(h=10),
        dmc.Text(id="switch-settings"),
    ]
)


@callback(Output("switch-settings", "children"), Input("switch-example", "checked"))
def settings(checked):
    return f"Using {'default' if checked else 'custom'} settings"
