import flet as ft

from .BaseViewer import Viewer


class PhoneParent():
    MASK = '+X (XXX) XXX-XX-XX'

    def input_mask(self, value):
        result = self.MASK
        text = ''.join(i for i in value if i.isdigit())

        for char in text:
            result = result.replace('X', char, 1)

        result = result.replace('X', "?")
        return result


class PhoneViewer(ft.Text, Viewer, PhoneParent):
    def __init__(self, value: str = ''):
        super().__init__(
            value=self.input_mask(value),
            width=150,
            style=ft.ButtonStyle(
                color=ft.colors.BLACK87
            ),
        )


class PhoneInput(ft.TextField, PhoneParent):

    MASK = '(XXX) XXX-XX-XX'

    def __init__(self, default_value: str = ''):
        super().__init__(
            value=self.input_mask(default_value),
            icon=ft.icons.PHONE,
            hint_text='(123) 456-78-90',
            prefix_text='+7 ',
            label="Your phone number",
            keyboard_type=ft.KeyboardType.PHONE,
            on_change=self.broker_input,
        )

    def broker_input(self, e):
        mask = self.MASK
        result = ''
        text = ''.join(i for i in e.control.value if i.isdigit())

        for w in mask:
            if w == 'X':
                if not text:
                    break
                mask = mask.replace('X', text[0], 1)
                result += text[0]
                text = text[1:]
            else:
                if not text:
                    break
                result += w

        self.value = result
        self.update()
