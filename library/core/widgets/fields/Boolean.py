import flet as ft
from typing import Union
from .BaseViewer import Viewer


class BooleanViewer(ft.Checkbox, Viewer):
    has_value_for_copy = False

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


class BooleanInput(ft.Checkbox, Viewer):
    has_value_for_copy = False

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
            label_position=label_position,
            label=label,
        )
