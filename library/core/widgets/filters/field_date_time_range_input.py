import flet as ft
from datetime import datetime
from functools import cached_property
from .filter_field import FilterFieldWidget
from library.core.widgets.text import Text, TitleText
from library.core.widgets.fields import DateTimePicker


class DateTimeRangeInputFieldFilterWidget(FilterFieldWidget):
    def __init__(
        self,
        form,
        field,
        minimum: datetime,
        maximum: datetime,
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
                    self._date_time_inputs[0],
                ]
            ),
            ft.Row(
                [
                    Text("По: "),
                    self._date_time_inputs[1],
                ]
            ),
        ])

    @cached_property
    def _date_time_inputs(self) -> tuple[DateTimePicker, DateTimePicker]:
        return DateTimePicker(self.minimum), DateTimePicker(self.maximum)

    @property
    def value(self) -> tuple[datetime]:
        minimum = (self._date_time_inputs[0].clear_value or 0)
        maximum = (self._date_time_inputs[1].clear_value or 0)

        return minimum, maximum
