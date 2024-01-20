from library.model_form.filters import (
    FilterSet,
    ValueFieldFilter,
    NumericRangeFieldFilter
)
from models import Task


class TasksFilterSet(FilterSet):
    work_type_filter = ValueFieldFilter(field=Task.work_type_id)
    price_filter = NumericRangeFieldFilter(
        field=Task.price,
        minimum=0,
        maximum=100_000
    )

    class Meta:
        filters = (
            "work_type_filter",
            "price_filter",
        )
