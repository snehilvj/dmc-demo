import dash_mantine_components as dmc
from dash import callback, html, Output, Input
from dash_iconify import DashIconify

component = html.Div(
    [
        dmc.ActionIcon(
            DashIconify(icon="clarity:settings-line", width=20),
            size="lg",
            variant="filled",
            id="action-icon",
            n_clicks=0,
            mb=10,
        ),
        dmc.Text(id="action-output"),
    ]
)


@callback(
    Output("action-output", "children"),
    Input("action-icon", "n_clicks"),
)
def update_clicks(n_clicks):
    return f"Clicked {n_clicks} times."
