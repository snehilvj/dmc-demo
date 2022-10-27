from datetime import datetime, date

import dash_mantine_components as dmc
from dash import Input, Output, html, callback
from dash.exceptions import PreventUpdate

component = html.Div(
    [
        dmc.DatePicker(
            id="date-picker",
            label="Start Date",
            description="You can also provide a description",
            minDate=date(2020, 8, 5),
            value=datetime.now().date(),
            style={"width": 200},
        ),
        dmc.Space(h=10),
        dmc.Text(id="selected-date"),
    ]
)


@callback(Output("selected-date", "children"), Input("date-picker", "value"))
def update_output(d):
    prefix = "You have selected: "
    if d:
        return prefix + d
    else:
        raise PreventUpdate
