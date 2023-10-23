import flet as ft

from library.core.widgets.fields.temp import Viewer


class IntegerViewer(ft.Text, Viewer):
    def __init__(self, value: int = 0):
        super().__init__(
            size=16,
            value=str(value),
        )
