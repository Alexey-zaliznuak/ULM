from typing import Iterable
from .filter import FieldFilter, FormFilter
from library.core.widgets.filters import ValueFieldFilterWidget
from library.types import AllPossibleValues


class ValueFieldFilter(FieldFilter):
    widget_ = ValueFieldFilterWidget

    def __init__(self, field, value=AllPossibleValues):
        self.field = field
        self.value = value

    def filter(
        self,
        queryset: Iterable,
        widget: ValueFieldFilterWidget | None = None,
    ):
        if not queryset:
            return queryset

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

    def form_filter(self, form) -> FormFilter:
        return FormFilter(
            self.widget_(field=self.field, form=form),
            self.filter
        )
