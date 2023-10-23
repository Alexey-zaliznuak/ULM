import flet as ft

from .BaseViewer import Viewer


class PhoneViewer(ft.Text, Viewer):
    MASK = '+X (XXX) XXX-XX-XX'

    def __init__(self, value: str = ''):
        super().__init__(
            value=self.input_mask(value),
            width=150,
            style=ft.ButtonStyle(
                color=ft.colors.BLACK87
            ),
        )

    def input_mask(self, value):
        result = self.MASK
        text = ''.join(i for i in value if i.isdigit())

        for char in text:
            result = result.replace('X', char, 1)

        result = result.replace('X', "?")
        return result
