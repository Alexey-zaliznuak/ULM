from typing import Callable

from flet import (
    AlertDialog,
    ElevatedButton,
    MainAxisAlignment,
    SnackBar,
    Text,
    colors,
    icons
)

from library.core.widgets.actions import ActionButton


class CreateObjectActionButtonWidget(ActionButton):
    def __init__(self, on_click: Callable):
        super().__init__(
            on_click=on_click,
            bgcolor=colors.BLUE_400,
            icon=icons.DELETE_OUTLINED,
        )


class CreateObjectActionDialog(AlertDialog):
    SNACK_BAR_DURATION = 1600

    def __init__(self, obj, datatable=None):
        self.obj = obj
        self.datatable = datatable

        super().__init__(
            modal=True,
            title=Text("Please confirm"),
            content=Text("Do you really want to delete this object?"),
            actions=[
                ElevatedButton("Delete", on_click=self.del_obj, color='red'),
                ElevatedButton("Cancel", on_click=self.close_dlg),
            ],
            actions_alignment=MainAxisAlignment.END,
        )

    def close_dlg(self, e=None):
        self.open = False
        self.page.update()

    def del_obj(self, e):
        self.obj.delete_instance()
        if self.datatable:
            self.datatable.update_rows()
        self.close_dlg()

        self.page.snack_bar = SnackBar(
            Text("Success deleted object"),
            duration=self.SNACK_BAR_DURATION,
            open=True
        )

        self.page.update()
