from library.model_form.filters import (
    FilterSet,
    ValueFieldFilter,
    NumericRangeInputFieldFilter,
    NumericRangeSliderFieldFilter,
    DateRangeInputFieldFilter,
    TimeRangeInputFieldFilter,
    DateTimeRangeInputFieldFilter,
)
from models import Task
from datetime import date, time, datetime, timedelta


class TasksFilterSet(FilterSet):
    work_type_filter = ValueFieldFilter(field=Task.work_type_id)
    price_numeric_slider_filter = NumericRangeSliderFieldFilter(
        field=Task.price,
        minimum=-10_000,
        maximum=100_000,
        start_value=-10_000,
        end_value=10_000,
    )
    price_numeric_input_filter = NumericRangeInputFieldFilter(
        field=Task.price,
        minimum=-100_000,
        maximum=100_000,
        notify_if_invalid=True,
    )
    deadline_filter = DateRangeInputFieldFilter(
        field=Task.deadline,
        minimum=date(2024, 1, 1),
        maximum=date(2024, 12, 31),
    )
    time_filter = TimeRangeInputFieldFilter(Task.time_field)
    date_time_filter = DateTimeRangeInputFieldFilter(
        Task.date_time_field,
    )

    class Meta:
        filters = (
            "date_time_filter",
            "work_type_filter",
            "price_numeric_input_filter",
            "price_numeric_slider_filter",
            "time_filter",
            "deadline_filter",
        )
