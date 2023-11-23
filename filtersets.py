from library.model_form.filters import (
    FilterSet,
    FieldValueFilterWidget
)
from models import Task


class TasksFilterSet(FilterSet):
    work_type_filter = FieldValueFilterWidget(field=Task.work_type)
    class Meta:
        filters = ('work_type_filter', )
