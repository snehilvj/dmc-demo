import dash_mantine_components as dmc
from dash import Output, Input, html, callback

component = html.Div(
    [
        dmc.ColorPicker(id="color-picker", format="rgba", value="rgba(41, 96, 214, 1)"),
        dmc.Space(h=10),
        dmc.Text(id="selected-color"),
    ]
)


@callback(Output("selected-color", "children"), Input("color-picker", "value"))
def pick(color):
    return color
