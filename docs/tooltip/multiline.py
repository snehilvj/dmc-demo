import dash_mantine_components as dmc

component = dmc.Center(
    [
        dmc.Tooltip(
            multiline=True,
            width=220,
            withArrow=True,
            transition="fade",
            transitionDuration=200,
            label="Use this button to save this information in your profile,"
            " after that you will be able to access it any time and share"
            " it via email.",
            children=[dmc.Button("Multiline Tooltip", variant="outline")],
        )
    ]
)
