from flet import (
    colors,
    SnackBar,
    icons,
    AlertDialog,
    ElevatedButton,
    Text,
    MainAxisAlignment,
)


from library.core.widgets.actions import ActionButton


class DeleteObjectActionButtonWidget(ActionButton):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args, **kwargs,
            icon=icons.DELETE_OUTLINED,
        )


class DeleteObjectActionDialog(AlertDialog):
    SNACK_BAR_DURATION = 1600

    def __init__(self, obj, datatable):
        self.obj=obj
        self.datatable=datatable

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
            Text(f"Success deleted object", size=18),
            duration=self.SNACK_BAR_DURATION,
            bgcolor=colors.GREY,
            open=True
        )

        self.page.update()
