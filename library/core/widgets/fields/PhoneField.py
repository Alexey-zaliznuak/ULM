import flet as ft


class PhoneViewer(ft.Text):
    def __init__(self, value: str = ''):
        super().__init__(
            value=self.input_mask(value),
            max_lines=1
        )

    def input_mask(self, value):
        mask = '+X (XXX) XXX-XX-XX'
        result = ''
        text = ''.join(i for i in value if i.isdigit())

        for w in mask:
            if not text:
                break
            if w == 'X':
                mask = mask.replace('X', text[0], 1)
                result += text[0]
                text = text[1:]
            else:
                result += w

        return result
