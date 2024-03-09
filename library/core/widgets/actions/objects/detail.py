from flet import (
    icons,
    AlertDialog,
    ElevatedButton,
    Text,
    MainAxisAlignment,
    Row,
    Control,
    Column,
    Container,
)
from library.core.widgets.actions import ActionButton
from library.core.widgets.text import Text


class DetailObjectActionButtonWidget(ActionButton):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args, **kwargs,
            icon=icons.REMOVE_RED_EYE_OUTLINED,
        )


class DetailObjectWidget(Container):
    def __init__(self, obj, fields):
        content = Column(
            [*self.fields_row(obj, fields)],
            tight=True,
        )

        super().__init__(content=content)

    def fields_row(self, obj, fields) -> list[Control]:
        result = []

        for field in fields:
            result.append(
                Row([
                    Text((field.datatable_column_title or field.help_text or field.label) + " - "),
                    field.display(obj)
                ])
            )

        return result


class DetailObjectActionDialog(AlertDialog):
    def __init__(self, obj, fields):
        self.obj = obj

        super().__init__(
            modal=True,
            title=Text("Детали"),
            content=DetailObjectWidget(obj, fields),
            actions=[
                ElevatedButton("Закрыть", on_click=self.close_dlg),
            ],
            actions_alignment=MainAxisAlignment.END,
            open=True,
        )

    def close_dlg(self, e=None):
        self.open = False
        self.page.update()
