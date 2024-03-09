from typing import Iterable, Union
from datetime import time

from .filter import FieldFilter, FormFilter
from library.core.widgets.filters import TimeRangeInputFieldFilterWidget
from library.model_form.fields import TimeField


class TimeRangeInputFieldFilter(FieldFilter):
    widget_ = TimeRangeInputFieldFilterWidget

    def __init__(
        self,
        field: TimeField,
        minimum: time = time(0, 0, 0),
        maximum: time = time(23, 59, 59),
    ):
        self.field = field

        self.minimum = minimum
        self.maximum = maximum

        assert self.minimum <= self.maximum

    def filter(
        self,
        queryset: Iterable,
        widget: Union[TimeRangeInputFieldFilterWidget, None] = None,
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
            ),
            self.filter
        )
