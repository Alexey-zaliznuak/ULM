import flet as ft


class IntViewer(ft.Text):
    def __init__(
        self,
        *,
        value: int = 0,
    ):
        super().__init__(
            size=24,
            value=str(value),
        )
