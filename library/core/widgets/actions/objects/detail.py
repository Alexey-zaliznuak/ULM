from flet import (
    icons,
    AlertDialog,
    ElevatedButton,
    Text,
    MainAxisAlignment,
    Row,
    Control,
    Column
)
from library.core.widgets.actions import ActionButton
from library.model_form.actions.objects import DeleteObjectAction
from library.core.utils import LazyAttribute


class DetailObjectActionButtonWidget(ActionButton):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args, **kwargs,
            icon=icons.REMOVE_RED_EYE_OUTLINED,
        )


class DetailObjectActionDialog(AlertDialog):
    def __init__(self, obj, datatable):
        self.obj = obj
        self.datatable=datatable

        super().__init__(
            modal=True,
            title=Text("Details"),
            content=Column(
                [
                    *self.fields_row(),
                    # DeleteObjectAction()(
                    #     obj=obj,
                    #     page=LazyAttribute(self, 'page'),
                    #     datatable=datatable
                    # )
                ],
                tight=True,
                width=300
            ),
            actions=[
                ElevatedButton("Close", on_click=self.close_dlg),
            ],
            actions_alignment=MainAxisAlignment.END,
        )

    def close_dlg(self, e=None):
        self.open = False
        self.page.update()

    def fields_row(self) -> list[Control]:
        result = []

        for field in self.datatable.fields:
            result.append(
                Row([
                    Text(field.label + " - "),
                    field.display_widget(self.obj)
                ])
            )

        return result
