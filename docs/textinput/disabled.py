import dash_mantine_components as dmc

component = dmc.Group(
    children=[
        dmc.TextInput(
            label="Disabled without value:",
            style={"width": 150},
            disabled=True
        ),

        dmc.TextInput(
            label="Disabled with value:",
            style={"width": 150},
            disabled='With Value'
        ),
    ],
    direction="center",
)
