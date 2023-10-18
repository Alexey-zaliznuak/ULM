import flet as ft


class PhoneViewer(ft.Text):
    MASK = '+X (XXX) XXX-XX-XX'

    def __init__(self, value: str = ''):
        super().__init__(
            value=self.input_mask(value),
            max_lines=1
        )

    def input_mask(self, value):
        result = self.MASK
        text = ''.join(i for i in value if i.isdigit())

        for char in text:
            result = result.replace('X', char, 1)

        result = result.replace('X', "?")
        return result
