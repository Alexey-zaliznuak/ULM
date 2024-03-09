from typing import Iterable, Union

from .filter import FieldFilter, FormFilter
from library.core.widgets.filters import NumericRangeInputFieldFilterWidget
from library.model_form.fields import IntegerField


Number = Union[ int, float]
OptionalNumber = Union[Number, None]


class NumericRangeInputFieldFilter(FieldFilter):
    widget_ = NumericRangeInputFieldFilterWidget

    def __init__(
        self,
        field: IntegerField,
        minimum=0,
        maximum=0,
        *,
        notify_if_invalid: bool = False
    ):
        self.field = field

        self.minimum = minimum
        self.maximum = maximum

        assert self.minimum <= self.maximum

        self.notify_if_invalid = notify_if_invalid

    def filter(
        self,
        queryset: Iterable,
        widget: Union[NumericRangeInputFieldFilterWidget, None] = None,
    ):
        if not queryset:  # mb peewee feature
            return queryset

        minimum = self.minimum
        maximum = self.maximum

        if widget:
            minimum, maximum = widget.value

        return queryset.where(
            (self.field >= minimum) & (self.field <= maximum)
        )

    def form_filter(self, form) -> FormFilter:
        return FormFilter(
            self.widget_(
                form=form,
                field=self.field,
                minimum=self.minimum,
                maximum=self.maximum,
                notify_if_invalid=self.notify_if_invalid
            ),
            self.filter
        )
