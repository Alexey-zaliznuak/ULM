from library.model_form.filters import (
    FilterSet,
    FieldValueFilter
)
from models import Task


class TasksFilterSet(FilterSet):
    work_type_filter = FieldValueFilter(field=Task.work_type_id)

    class Meta:
        filters = ('work_type_filter', )
