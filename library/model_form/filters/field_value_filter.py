from typing import Iterable

import flet as ft
from .filter import Filter, FilterWidget
from library.core.widgets.filters import FilterValueFieldWidget
from library.types import AllPossibleValues


class FieldValueFilter(Filter):
    widget_ = FilterValueFieldWidget

    def __init__(self, field, value=AllPossibleValues):
        self.field = field
        self.value = value

    def filter(
        self,
        queryset: Iterable,
        widget: FilterValueFieldWidget | None = None,
    ):
        values = [self.value]

        if widget:
            filter_value = widget.value
            if not filter_value and self.value is AllPossibleValues:
                return []

            if isinstance(filter_value, list):
                values.extend(filter_value)
            else:
                values.append(filter_value)

        if len(values) == values.count(AllPossibleValues):
            return queryset

        values = set(values)
        if AllPossibleValues in values:
            values.remove(AllPossibleValues)

        return queryset.where(self.field.in_(values))

    def widget(self, form) -> ft.Control:
        return FilterWidget(
            self.widget_(field=self.field, form=form),
            self.filter
        )
