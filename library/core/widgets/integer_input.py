from flet import Row, TextField, TextAlign
from functools import cached_property


class IntegerInput(Row):
    def __init__(
        self,
        default_value: int = 0,
    ):
        self.default_value = default_value

        super().__init__([self.picker])

    @property
    def clear_value(self):
        cleared = ''.join(
            s for s in self.picker.value if s.isdigit() or s == "-"
        )

        if cleared:
            cleared = cleared[0] + cleared[1:].replace("-", "")

            if self.page:
                self.picker.value = str(int(cleared))
                self.picker.update()

            return int(cleared)

        return ''

    @cached_property
    def picker(self) -> TextField:
        return TextField(
            value=str(self.default_value),
            text_align=TextAlign.RIGHT,
            width=100
        )
