import flet as ft
from datetime import time
from functools import cached_property
from .filter_field import FilterFieldWidget
from library.core.widgets.text import Text, TitleText
from library.core.widgets.fields import TimePicker


class TimeRangeInputFieldFilterWidget(FilterFieldWidget):
    def __init__(
        self,
        form,
        field,
        minimum: time,
        maximum: time,
    ):
        super().__init__(field=field, form=form)
        self.field = field
        self.form = form
        self.minimum = minimum
        self.maximum = maximum

    def build(self):
        # todo upgrade ui
        return ft.Column([
            TitleText(value=self.form._form_fields()[self.field.name].label),
            ft.Row(
                [
                    Text("C: "),
                    self._time_inputs[0],
                ]
            ),
            ft.Row(
                [
                    Text("По: "),
                    self._time_inputs[1],
                ]
            ),
        ])

    @cached_property
    def _time_inputs(self) -> tuple[TimePicker, TimePicker]:
        return TimePicker(self.minimum), TimePicker(self.maximum)

    @property
    def value(self) -> tuple[time]:
        minimum = (self._time_inputs[0].clear_value or 0)
        maximum = (self._time_inputs[1].clear_value or 0)

        return minimum, maximum
