from datetime import datetime

import dash_mantine_components as dmc

component = dmc.DatePicker(
    value=datetime.now().date(),
    hideOutsideDates=True
)