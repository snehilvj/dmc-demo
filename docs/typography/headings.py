import dash_mantine_components as dmc

theme = {
    "components": {
        "Title": {
            "classNames": {
                "root": "heading",
            },
        },
    },
}

dmc.MantineProvider(
    theme=theme,
    children=[
        dmc.Title("Heading 1", order=1),
        dmc.Title("Heading 2", order=2),
        dmc.Title("Heading 3", order=3),
        dmc.Title("Heading 4", order=4),
        dmc.Title("Heading 5", order=5),
        dmc.Title("Heading 6", order=6),
    ],
)
