from typing import Iterable, Union
from datetime import date

from .filter import FieldFilter, FormFilter
from library.core.widgets.filters import DateRangeInputFieldFilterWidget
from library.model_form.fields import DateField


class DateRangeInputFieldFilter(FieldFilter):
    widget_ = DateRangeInputFieldFilterWidget

    def __init__(
        self,
        field: DateField,
        minimum: date = date(1970, 1, 1),
        maximum: date = date(3000, 12, 31),
    ):
        self.field = field

        self.minimum = minimum
        self.maximum = maximum

        assert self.minimum <= self.maximum

    def filter(
        self,
        queryset: Iterable,
        widget: Union[DateRangeInputFieldFilterWidget, None] = None,
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
