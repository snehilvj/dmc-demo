import dash_labs as dl
import dash_mantine_components as dmc
from dash import Dash, Output, Input, callback_context as ctx
from dash_iconify import DashIconify

from lib.appshell import AppShell

app = Dash(
    __name__,
    plugins=[dl.plugins.pages],
    external_scripts=[
        "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/dayjs.min.js",
        "https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/locale/ru.min.js",
        "https://www.googletagmanager.com/gtag/js?id=G-4PJELX1C4W",
    ],
)

app.layout = AppShell(dl.plugins.page_container)
server = app.server

app.clientside_callback(
    """
    function(value) {
        if (value) {
            document.getElementById(value).click()
        }
        return value
    }
    """,
    Output("dummy-container-for-header-select", "children"),
    Input("select-component", "value"),
)

# noinspection PyProtectedMember
app.clientside_callback(
    """
    function(children) {
        return null
    }
    """,
    Output("select-component", "value"),
    Input(dl.plugins.pages._ID_CONTENT, "children"),
)

app.clientside_callback(
    """
    function(checked) {
        return {colorScheme: checked ? "dark" : "light"}
    }
    """,
    Output("theme-demo", "theme"),
    Input("dark-theme-switch", "checked"),
    prevent_initial_call=True,
)


@app.callback(
    Output("home-notifications-container", "children"),
    Input("default-notification", "n_clicks"),
    Input("green-icon-notification", "n_clicks"),
    Input("10-sec-notification", "n_clicks"),
    Input("orange-loading-notification", "n_clicks"),
    prevent_initial_call=True,
)
def notify(nc1, nc2, nc3, nc4):
    if nc1 or nc2 or nc3 or nc4:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
        props = {
            "action": "show",
            "id": button_id + "-notified",
        }

        if button_id == "default-notification":
            props["title"] = "Default Notification"
            props["message"] = "Notifications in Dash is awesome!"

        elif button_id == "green-icon-notification":
            props["title"] = "Green Icon"
            props["message"] = "Your work as been saved."
            props["icon"] = [DashIconify(icon="radix-icons:check-circled")]
            props["color"] = "green"

        elif button_id == "10-sec-notification":
            props["title"] = "10 sec timeout"
            props["message"] = "This notification will dismiss itself after 10 secs."
            props["color"] = "violet"
            props["autoClose"] = 10000

        else:
            props["title"] = "Loading data"
            props["message"] = "The app is loading data, please wait."
            props["color"] = "orange"
            props["loading"] = True

        return dmc.Notification(**props)


app.clientside_callback(
    """
    function(variant, color, radius, size, compact, loading, children) {
        return [
            `import dash_mantine_components as dmc

dmc.Button(
    "${children}",
    variant="${variant}",
    color="${window.colorMap[color]}",
    radius="${window.sizeMap[radius]}",
    size="${window.sizeMap[size]}"
    compact=${compact ? "True" : "False"},
    loading=${loading ? "True" : "False"},
)`,
        variant,
        window.colorMap[color],
        window.sizeMap[radius],
        window.sizeMap[size],
        compact,
        loading,
        children
        ];
    }
    """,
    Output("button-code-output", "children"),
    Output("button-demo", "variant"),
    Output("button-demo", "color"),
    Output("button-demo", "radius"),
    Output("button-demo", "size"),
    Output("button-demo", "compact"),
    Output("button-demo", "loading"),
    Output("button-demo", "children"),
    Input("variant-button-demo", "value"),
    Input("color-button-demo", "value"),
    Input("radius-button-demo", "value"),
    Input("size-button-demo", "value"),
    Input("compact-button-demo", "checked"),
    Input("loading-button-demo", "checked"),
    Input("children-button-demo", "value"),
)

app.clientside_callback(
    """
    function(color) {
        return [
            `import dash_mantine_components as dmc

dmc.Checkbox(
    label="Use me as a boolean input",
    checked=True,
    color="${window.colorMap[color]}"
)`,
        window.colorMap[color]
    ];
    }
    """,
    Output("checkbox-code-output", "children"),
    Output("checkbox-color", "color"),
    Input("color-checkbox-demo", "value"),
)

app.clientside_callback(
    """
    function(variant, color, radius, size, multiple, spacing) {
        return [
            `import dash_mantine_components as dmc

dmc.Chips(
    data = [
        {"value": "react", "label": "React"},
        {"value": "ng", "label": "Angular"},
        {"value": "svelte", "label": "Svelte"},
        {"value": "vue", "label": "Vue"},
    ],
    color="${window.colorMap[color]}",
    radius="${window.sizeMap[radius]}",
    size="${window.sizeMap[size]}",
    spacing="${window.sizeMap[spacing]}",
    variant="${variant}",
    multiple=${multiple ? "True" : "False"},
)`,
        variant,
        window.colorMap[color],
        window.sizeMap[radius],
        window.sizeMap[size],
        multiple,
        window.sizeMap[spacing]
        ];
    }
    """,
    Output("chips-code-output", "children"),
    Output("chips-demo", "variant"),
    Output("chips-demo", "color"),
    Output("chips-demo", "radius"),
    Output("chips-demo", "size"),
    Output("chips-demo", "multiple"),
    Output("chips-demo", "spacing"),
    Input("variant-chips-demo", "value"),
    Input("color-chips-demo", "value"),
    Input("radius-chips-demo", "value"),
    Input("size-chips-demo", "value"),
    Input("multiple-chips-demo", "checked"),
    Input("spacing-chips-demo", "value"),
)


@app.callback(
    Output("chips-demo", "value"),
    Input("multiple-chips-demo", "checked"),
)
def multiple_chips_demo(multiple):
    return ["vue", "react"] if multiple else "react"


app.clientside_callback(
    """
    function(variant, color, size) {
        return [
            `import dash_mantine_components as dmc

dmc.Loader(
    variant="${variant}",
    color="${window.colorMap[color]}",
    size="${window.sizeMap[size]}"
)`,
        variant,
        window.colorMap[color],
        window.sizeMap[size],
        ];
    }
    """,
    Output("loader-code-output", "children"),
    Output("loader-demo", "variant"),
    Output("loader-demo", "color"),
    Output("loader-demo", "size"),
    Input("variant-loader-demo", "value"),
    Input("color-loader-demo", "value"),
    Input("size-loader-demo", "value"),
)

app.clientside_callback(
    """
    function(size, thickness, roundCaps) {
        return [
            `import dash_mantine_components as dmc

dmc.RingProgress(
    size=${size},
    thickness=${thickness},
    roundCaps=${roundCaps ? "True" : "False"},
    sections=[
        {"value": 40, "color": "red"},
        {"value": 15, "color": "yellow"},
        {"value": 15, "color": "violet"},
    ],
)`,
        size,
        thickness,
        roundCaps,
        ];
    }
    """,
    Output("ringprogress-code-output", "children"),
    Output("ringprogress-demo", "size"),
    Output("ringprogress-demo", "thickness"),
    Output("ringprogress-demo", "roundCaps"),
    Input("size-ringprogress-demo", "value"),
    Input("thickness-ringprogress-demo", "value"),
    Input("caps-ringprogress-demo", "checked"),
)

app.clientside_callback(
    """
    function(radius, p, shadow, withBorder) {
        return [
            `import dash_mantine_components as dmc

dmc.Paper(
    children=[
        dmc.Text(
            "Paper is the most basic ui component. Use it to create cards, dropdowns, "
            "modals and other components that require background with shadow "
        )
    ],
    radius="${window.sizeMap[radius]}",
    p="${window.sizeMap[p]}",
    shadow="${window.sizeMap[shadow]}",
    withBorder=${withBorder ? "True" : "False"},
)`,
        window.sizeMap[radius],
        window.sizeMap[p],
        window.sizeMap[shadow],
        withBorder
        ];
    }
    """,
    Output("paper-code-output", "children"),
    Output("paper-demo", "radius"),
    Output("paper-demo", "p"),
    Output("paper-demo", "shadow"),
    Output("paper-demo", "withBorder"),
    Input("radius-paper-demo", "value"),
    Input("padding-paper-demo", "value"),
    Input("shadow-paper-demo", "value"),
    Input("border-paper-demo", "checked"),
)

app.clientside_callback(
    """
    function(color, radius, position, placement, withArrow) {
        return [
            `import dash_mantine_components as dmc

dmc.Tooltip(
    label="Tooltip",
    withArrow=${withArrow ? "True" : "False"},
    position="${position}",
    placement="${placement}",
    color="${window.colorMap[color]}",
    children=[
        dmc.Button(
            "Tooltip",
            variant="outline",
            size="xl",
        )
    ],
)`,
        window.colorMap[color],
        window.sizeMap[radius],
        position,
        placement,
        withArrow
        ];
    }
    """,
    Output("tooltip-code-output", "children"),
    Output("tooltip-demo", "color"),
    Output("tooltip-demo", "radius"),
    Output("tooltip-demo", "position"),
    Output("tooltip-demo", "placement"),
    Output("tooltip-demo", "withArrow"),
    Input("color-tooltip-demo", "value"),
    Input("radius-tooltip-demo", "value"),
    Input("position-tooltip-demo", "value"),
    Input("placement-tooltip-demo", "value"),
    Input("arrow-tooltip-demo", "checked"),
)

app.clientside_callback(
    """
    function(variant, radius, size, withSeconds, disabled, required) {
        return [
            `import dash_mantine_components as dmc

dmc.TimeInput(
    variant="${variant}",    
    radius="${window.sizeMap[radius]}",
    size="${window.sizeMap[size]}"
    withSeconds=${withSeconds ? "True" : "False"},
    disabled=${disabled ? "True" : "False"},
    required=${required ? "True" : "False"},
)`,
        variant,    
        window.sizeMap[radius],
        window.sizeMap[size],
        withSeconds,
        disabled,
        required
        ];
    }
    """,
    Output("timeinput-code-output", "children"),
    Output("timeinput-demo", "variant"),
    Output("timeinput-demo", "radius"),
    Output("timeinput-demo", "size"),
    Output("timeinput-demo", "withSeconds"),
    Output("timeinput-demo", "disabled"),
    Output("timeinput-demo", "required"),
    Input("variant-timeinput-demo", "value"),
    Input("radius-timeinput-demo", "value"),
    Input("size-timeinput-demo", "value"),
    Input("seconds-timeinput-demo", "checked"),
    Input("disabled-timeinput-demo", "checked"),
    Input("required-timeinput-demo", "checked"),
)

app.clientside_callback(
    """
    function(orientation, spacing, size, color, required) {
        return [
            `import dash_mantine_components as dmc

dmc.RadioGroup(
    data=[
        {"value": "react", "label": "React"},
        {"value": "ng", "label": "Angular"},
        {"value": "svelte", "label": "Svelte"},
        {"value": "vue", "label": "Vue"},
    ],
    color="${window.colorMap[color]}",
    size="${window.sizeMap[size]}",
    spacing="${window.sizeMap[spacing]}",
    orientation="${orientation}",
    label="Select your favorite framework/library",
    description="This is anonymous",
    required=${required ? "True" : "False"},
)`,
        orientation,
        window.sizeMap[spacing],
        window.sizeMap[size],
        window.colorMap[color],
        required
        ];
    }
    """,
    Output("radio-code-output", "children"),
    Output("radio-demo", "orientation"),
    Output("radio-demo", "spacing"),
    Output("radio-demo", "size"),
    Output("radio-demo", "color"),
    Output("radio-demo", "required"),
    Input("variant-radio-demo", "value"),
    Input("spacing-radio-demo", "value"),
    Input("size-radio-demo", "value"),
    Input("color-radio-demo", "value"),
    Input("required-radio-demo", "checked"),
)


app.clientside_callback(
    """
    function(color, variant, tabPadding, orientation, position, grow) {
        return [
            `import dash_mantine_components as dmc

dmc.Tabs(
    [
        dmc.Tab("Gallery tab content", label="Gallery"),
        dmc.Tab("Messages tab content", label="Messages"),
        dmc.Tab("Settings tab content", label="Settings"),
    ],
    color="${window.colorMap[color]}",
    variant="${variant}",
    tabPadding="${window.sizeMap[tabPadding]}",
    orientation="${orientation}",
    position="${position}",
    grow=${grow ? "True" : "False"},
)`,
        window.colorMap[color],
        variant,
        window.sizeMap[tabPadding],
        orientation,
        position,
        grow
        ];
    }
    """,
    Output("tabs-code-output", "children"),
    Output("tabs-demo", "color"),
    Output("tabs-demo", "variant"),
    Output("tabs-demo", "tabPadding"),
    Output("tabs-demo", "orientation"),
    Output("tabs-demo", "position"),
    Output("tabs-demo", "grow"),
    Input("color-tabs-demo", "value"),
    Input("variant-tabs-demo", "value"),
    Input("padding-tabs-demo", "value"),
    Input("orientation-tabs-demo", "value"),
    Input("position-tabs-demo", "value"),
    Input("grow-tabs-demo", "checked"),
)


app.clientside_callback(
    """
    function(position, direction, spacing, grow) {
        return [
            `import dash_mantine_components as dmc

dmc.Group(
    [
        dmc.Button(val, variant="outline", fullWidth=True)
        for val in ["1", "2", "3"]
    ],
    position="${position}",
    direction="${direction}",
    spacing="${window.sizeMap[spacing]}",
    grow=${grow ? "True" : "False"},
)`,
        position,
        direction,
        window.sizeMap[spacing],
        grow
        ];
    }
    """,
    Output("group-code-output", "children"),
    Output("group-demo", "position"),
    Output("group-demo", "direction"),
    Output("group-demo", "spacing"),
    Output("group-demo", "grow"),
    Input("position-group-demo", "value"),
    Input("direction-group-demo", "value"),
    Input("spacing-group-demo", "value"),
    Input("grow-group-demo", "checked"),
)


app.clientside_callback(
    """
    function(color, radius, size) {
        return [
            `import dash_mantine_components as dmc

dmc.Switch(
    label="I agree to sell my privacy.",
    color="${window.colorMap[color]}",
    radius="${window.sizeMap[radius]}",
    size="${window.sizeMap[size]}"
)`,
        window.colorMap[color],
        window.sizeMap[radius],
        window.sizeMap[size],
        ];
    }
    """,
    Output("switch-code-output", "children"),
    Output("switch-demo", "color"),
    Output("switch-demo", "radius"),
    Output("switch-demo", "size"),
    Input("color-switch-demo", "value"),
    Input("radius-switch-demo", "value"),
    Input("size-switch-demo", "value"),
)


if __name__ == "__main__":
    app.run_server(debug=True, dev_tools_hot_reload=False)
