import flet as ft
from typing import Union


class BooleanViewer(ft.Checkbox):
    def __init__(
        self,
        value: Union[bool, None] = False,
        tristate: bool = False,
        label_position: ft.LabelPosition = ft.LabelPosition.RIGHT,
        label: str = '',

    ):
        super().__init__(
            value=bool(value),
            tristate=tristate,
            disabled=True,
            label_position=label_position,
            label=label,
        )
