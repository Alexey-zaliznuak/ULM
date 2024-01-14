from library.core.widgets.actions.table import (
    FilterActionButton,
    FilterActionDialog
)

from .table_action import DataTableAction


class FilterAction(DataTableAction):
    action_widget = FilterActionButton

    def on_click_method(self, *args, datatable, **kwargs):
        filter_action_dialog = FilterActionDialog(
            datatable=datatable,
        )
        datatable.page.overlay.append(filter_action_dialog)
        filter_action_dialog.open = True
        datatable.page.update()
