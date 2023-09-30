import dash_mantine_components as dmc


component = dmc.Stack(
    [
        dmc.PasswordInput(
            label="Your password",
            placeholder="Your password",
            style={"width": 250},
            error=True,
        ),
        dmc.PasswordInput(
            label="Your password",
            placeholder="Your password",
            style={"width": 250},
            error="Invalid Password",
        ),
    ],
)
