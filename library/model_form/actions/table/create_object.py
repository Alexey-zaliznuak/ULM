from library.core.widgets.actions.table.create_object import (
    CreateObjectActionButtonWidget,
    CreateObjectActionDialog
)

from .table_action import DataTableAction


class CreateObjectAction(DataTableAction):
    action_widget = CreateObjectActionButtonWidget

    def on_click_method(self, datatable, e=None):
        datatable.page.dialog = CreateObjectActionDialog(datatable)
        datatable.page.dialog.open = True
        datatable.page.update()
