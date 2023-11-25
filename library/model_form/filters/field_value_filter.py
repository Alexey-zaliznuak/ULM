from typing import Iterable
from .filter import Filter
from .filter_widget import FilterWidget
from library.core.widgets.filters import FilterField, FilterValueFieldWidget
from library.types import AllPossibleValues


class FieldValueFilter(Filter):
    def __init__(self, field, value=AllPossibleValues):
        self.field = field
        self.value = value

    def filter(self, queryset: Iterable, filter_widget: FilterField = None):
        values = [self.value]

        if filter_widget:
            filter_value = filter_widget.value

            if isinstance(filter_value, list):
                values.extend(filter_value)
            else:
                values.append(filter_value)

        if len(values) == values.count(AllPossibleValues):
            return queryset

        return queryset.where(self.field.in_(values))


class FieldValueFilterWidget(FilterWidget):
    filter_class_ = FieldValueFilter
    widget_ = FilterValueFieldWidget

    def __init__(self, field):
        self.filter_class_ = self.filter_class_(field)
        super().__init__()
