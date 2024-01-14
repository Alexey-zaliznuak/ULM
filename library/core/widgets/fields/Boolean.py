from flet import (
    Checkbox,
    LabelPosition,
)

from .BaseViewer import Viewer
from .BaseInput import InputField


class BooleanViewer(Checkbox, Viewer):
    has_value_for_copy = False

    def __init__(
        self,
        value,
        tristate: bool = False,
        label_position: LabelPosition = LabelPosition.RIGHT,
        label: str = '',

    ):
        super().__init__(
            value=bool(value),
            tristate=tristate,
            disabled=True,
            label_position=label_position,
            label=label,
        )


class BooleanInput(Checkbox, InputField):
    has_value_for_copy = False

    def __init__(
        self,
        value: bool,
        tristate: bool = False,
        label_position: LabelPosition = LabelPosition.RIGHT,
        label: str = '',
    ):
        super().__init__(
            value=bool(value),
            tristate=tristate,
            label_position=label_position,
            label=label,
        )
