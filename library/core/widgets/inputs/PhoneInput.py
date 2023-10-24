import flet as ft


class PhoneInput(ft.TextField):

    MASK = '(XXX) XXX-XX-XX'

    def __init__(self, value: str = ''):
        super().__init__(
            icon=ft.icons.PHONE,
            hint_text='(XXX) XXX-XX-XX',
            prefix_text='+7 ',
            label="Your phone number",
            keyboard_type=ft.KeyboardType.PHONE,
            on_change=self.input_mask,
        )

    def input_mask(self, e):
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
