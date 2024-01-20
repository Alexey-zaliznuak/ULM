from typing import Iterable

import flet as ft
from .filter import FieldFilter, LiteWidgetFilter
from library.core.widgets.filters import FieldRangeFilterWidget
from peewee import fn
from library.model_form.fields import IntegerField, FloatField


Number = int | float
OptionalNumber = Number | None
NumericField = IntegerField | FloatField


class NumericRangeFieldFilter(FieldFilter):
    widget_ = FieldRangeFilterWidget

    def __init__(
        self,
        field: NumericField,
        minimum: int,
        maximum: int,
        start_value=None,
        end_value=None,
        divisions=100,
    ):
        self.field = field

        mn, mx = self.__get_field_min_max()

        self.minimum = minimum or mn
        self.maximum = maximum or mx

        self.start_value = start_value or minimum
        self.end_value = end_value or maximum

        self.divisions=divisions

    def filter(
        self,
        queryset: Iterable,
        widget: FieldRangeFilterWidget | None = None,
    ):
        if not queryset: # mb peewee feature
            return queryset

        minimum = self.start_value
        maximum = self.end_value

        if widget:
            minimum, maximum = widget.value

        return queryset.where(
            (self.field >= minimum) & (self.field <= maximum)
        )

    def lite_widget_filter(self, form) -> ft.Control:
        return LiteWidgetFilter(
            self.widget_(
                form=form,
                field=self.field,
                minimum=self.minimum,
                maximum=self.maximum,
                start_value=self.start_value,
                end_value=self.end_value,
                divisions=self.divisions,
            ),
            self.filter
        )

    def __get_field_min_max(self) -> tuple[Number]:
        return self.field.model.select(
            fn.Min(self.field),
            fn.Max(self.field),
        ).scalar(as_tuple=True)
