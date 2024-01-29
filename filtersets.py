from library.model_form.filters import (
    FilterSet,
    ValueFieldFilter,
    NumericRangeInputFieldFilter
)
from models import Task


class TasksFilterSet(FilterSet):
    work_type_filter = ValueFieldFilter(field=Task.work_type_id)
    # price_numeric_filter = NumericRangeSliderFieldFilter(
    #     field=Task.price,
    #     minimum=0,
    #     maximum=100_000
    # )
    price_numeric_filter = NumericRangeInputFieldFilter(
        field=Task.price,
        minimum=0,
        maximum=100_000,
        notify_if_invalid=True,
    )

    class Meta:
        filters = (
            "work_type_filter",
            "price_numeric_filter",
        )
