from functools import cached_property
import flet as ft
from .filter_field import FilterFieldWidget
from library.core.widgets.text import TitleText


class FieldRangeFilterWidget(FilterFieldWidget):
    def __init__(
        self,
        form,
        field,
        minimum,
        maximum,
        start_value,
        end_value,
        divisions: int = 100,
        label="{value}",
    ):
        super().__init__(field=field, form=form)
        self.field = field
        self.form = form
        self.minimum = minimum
        self.maximum = maximum
        self.start_value = start_value
        self.end_value = end_value
        self.divisions = divisions
        self.label = label

    def build(self):
        # todo upgrade ui
        return ft.Column([
            TitleText(value=self.form._form_fields()[self.field.name].label),
            self._range_slider
        ])

    @cached_property
    def _range_slider(self):
        return ft.RangeSlider(
            min=self.minimum,
            max=self.maximum,
            start_value=self.start_value,
            end_value=self.end_value,
            divisions=self.divisions,
            label=self.label
        )

    @property
    def value(self) -> tuple[float]:
        return self._range_slider.start_value, self._range_slider.end_value
