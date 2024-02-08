from typing import Iterable

from .filter import FieldFilter, FormFilter
from library.core.widgets.filters import NumericRangeSliderFieldFilterWidget
from peewee import fn
from library.model_form.fields import IntegerField, FloatField


Number = int | float
OptionalNumber = Number | None
NumericField = IntegerField | FloatField


class NumericRangeSliderFieldFilter(FieldFilter):
    widget_ = NumericRangeSliderFieldFilterWidget

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

        assert self.minimum <= self.maximum

        self.start_value = start_value or minimum
        self.end_value = end_value or maximum

        assert self.start_value <= self.end_value

        assert self.start_value >= self.minimum
        assert self.end_value <= self.maximum

        self.divisions = divisions

    def filter(
        self,
        queryset: Iterable,
        widget: NumericRangeSliderFieldFilterWidget | None = None,
    ):
        if not queryset:  # mb peewee feature
            return queryset

        minimum = self.start_value
        maximum = self.end_value

        if widget:
            minimum, maximum = widget.value

        maximum = float(maximum)
        minimum = float(minimum)

        if self.maximum != maximum:
            queryset = queryset.where(self.field <= maximum)

        if not queryset:  # mb peewee feature
            return queryset

        if self.minimum != minimum:
            queryset = queryset.where(self.field >= minimum)

        return queryset

    def form_filter(self, form) -> FormFilter:
        return FormFilter(
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
