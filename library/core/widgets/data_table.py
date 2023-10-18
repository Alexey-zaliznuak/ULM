from typing import Callable, Iterable

from peewee import Model
from flet import (
    border,
    DataTable,
    DataColumn,
    DataCell,
    DataRow,
    Text,
    Row,
)

from library.model_form.ui_fields import Field
from library.model_form.actions import DataTableAction, ObjectAction
from library.utils import LazyAttribute


class UIModelFormDataTableCell(DataCell):
    def __init__(self, obj, field: Field, *args, **kwargs):
        # TODO paddings
        super().__init__(field.display(obj), *args, **kwargs)


class UIModelFormDataTableObjectActionCell(DataCell):
    def __init__(self, actions: list[ObjectAction], *args, **kwargs):
        super().__init__(Row(actions), *args, **kwargs)


class UIModelFormDataTableObjectActionColumn(DataColumn):
    def __init__(self, col_name: str, *args, **kwargs):
        super().__init__(Text(col_name), *args, **kwargs)


class UIModelFormDataTableRow(DataRow):
    def __init__(
        self,
        obj,
        fields: list[Field],
        actions: list[ObjectAction],
        datatable: 'UIModelFormDataTable',
        *args,
        **kwargs
    ):
        cells = [UIModelFormDataTableCell(obj, field) for field in fields]

        if actions:
            cells.append(DataCell(Row([
                action()(
                    obj=obj,
                    datatable=datatable,
                    page=LazyAttribute(self, 'page'),
                ) for action in actions
            ])))

        super().__init__(cells, *args, **kwargs)


class UIModelFormDataTableColumn(DataColumn):
    def __init__(self, label: str, field: Field, *args, **kwargs):
        numeric = getattr(field, 'numeric', False)
        tooltip = getattr(field, 'help_text', None) or label

        # TODO modal window with details of column type
        super().__init__(
            Text(label),
            numeric=numeric,
            tooltip=tooltip,
            *args,
            **kwargs
        )


class UIModelFormDataTable(DataTable):
    default = {
        'border': border.all(0.5, "dark"),
        'border_radius': 3,
        'horizontal_lines': border.BorderSide(1, "dark"),
        'vertical_lines': border.BorderSide(0.5, "dark"),
    }

    def __init__(
        self,
        columns: list[UIModelFormDataTableColumn],
        fields: list[Field],
        queryset: Callable,
        model: Model,
        *args,
        action_column: DataColumn = DataColumn(Text('Actions')),
        objects_actions: list[ObjectAction] = [],
        table_actions: list[DataTableAction] = [],
        **kwargs,
    ):
        self.fields = fields
        self.model = model
        self.objects_actions = objects_actions
        self.queryset = queryset
        self.table_actions = table_actions

        self.update_rows()

        if action_column and objects_actions:
            columns.append(action_column)

        kwargs = (self.default | kwargs)
        super().__init__(*args, columns=columns, rows=self.rows, **kwargs)

    def update_rows(self, queryset: Iterable = None):
        self.rows = [
            UIModelFormDataTableRow(
                obj=obj,
                fields=self.fields,
                actions=self.objects_actions,
                datatable=self
            )
            for obj in (queryset or self.queryset())
        ]

        if hasattr(self, 'page'):
            self.update()
