import flet as ft


class BoolField(ft.Checkbox):
    def __init__(
        self,
        *,
        value: bool | None = False,
        tristate: bool = False,
        label_position: ft.LabelPosition = ft.LabelPosition.RIGHT,
        label: str = '',

    ):
        super().__init__(
            value=value,
            tristate=tristate,
            disabled=True,
            label_position=label_position,
            label=label
        )
