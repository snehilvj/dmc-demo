import dash_mantine_components as dmc
from .data import data

component = dmc.DonutChart(
  data=data,
  withTooltip=False
)
