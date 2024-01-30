from functools import cached_property
import flet as ft
from .filter_field import FilterFieldWidget
from library.core.widgets.text import Text, TitleText
from library.core.widgets.integer_input import IntegerInput


class NumericRangeInputFieldFilterWidget(FilterFieldWidget):
    def __init__(
        self,
        form,
        field,
        minimum: int,
        maximum: int,
        *,
        notify_if_invalid: bool = False
    ):
        super().__init__(field=field, form=form)
        self.field = field
        self.form = form
        self.minimum = minimum
        self.maximum = maximum
        self.notify_if_invalid = notify_if_invalid

    def build(self):
        # todo upgrade ui
        return ft.Column([
            TitleText(value=self.form._form_fields()[self.field.name].label),
            ft.Row(
                [
                    Text("Минимум: "),
                    self._integer_inputs[0],
                ]
            ),
            ft.Row(
                [
                    Text("Максимум: "),
                    self._integer_inputs[1],
                ]
            ),
        ])

    @cached_property
    def _integer_inputs(self) -> tuple[IntegerInput, IntegerInput]:
        return IntegerInput(self.minimum), IntegerInput(self.maximum)

    @property
    def value(self) -> tuple[int]:
        minimum = (self._integer_inputs[0].clear_value or 0)
        maximum = (self._integer_inputs[1].clear_value or 0)

        if self.page and self.notify_if_invalid and minimum > maximum:
            self.page.snack_bar = ft.SnackBar(Text(f"Были введены некорректные данные для фильтров!"))
            self.page.snack_bar.open = True
            self.page.update()

        return minimum, maximum
