from typing import Iterable
from datetime import datetime

from .filter import FieldFilter, FormFilter
from library.core.widgets.filters import DateTimeRangeInputFieldFilterWidget
from library.model_form.fields import DateTimeField


class DateTimeRangeInputFieldFilter(FieldFilter):
    widget_ = DateTimeRangeInputFieldFilterWidget

    def __init__(
        self,
        field: DateTimeField,
        minimum: datetime = datetime.today(),
        maximum: datetime = datetime.today(),
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
        widget: DateTimeRangeInputFieldFilterWidget | None = None,
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
