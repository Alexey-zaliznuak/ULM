from typing import Iterable
from .filter import Filter
from .filter_widget import FilterWidget
from library.core.widgets.filters import FilterField, FilterValueFieldWidget


class FieldValueFilter(Filter):
    def __init__(self, field, value=None):
        self.field = field
        self.value = value

    def filter(self, queryset: Iterable, filter_widget: FilterField = None):
        values = []

        if self.value:
            values.append(self.value)

        if filter_widget:
            value = filter_widget.value

            if isinstance(value, list):
                values.extend(value)
            else:
                values.append(self.value)

        return queryset.where(self.field._in(values))


class FieldValueFilterWidget(FilterWidget):
    filter_class_ = FieldValueFilter
    widget_ = FilterValueFieldWidget

    def __init__(self, field):
        self.filter_class_ = self.filter_class_(field)
