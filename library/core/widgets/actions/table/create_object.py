from flet import (
    icons,
    AlertDialog,
    ElevatedButton,
    Text,
    MainAxisAlignment,
    Control,
    Container,
    Column
)
from library.core.widgets.actions import ActionButton
from library.core.widgets import ErrorText
from library.model_form.ui_fields import Field


class CreateObjectActionButtonWidget(ActionButton):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args, **kwargs,
            icon=icons.ADD,
        )


class EditFieldWidget(Container):
    def __init__(self, label, editing_field: Control = None, errors: list[str] = []):
        super().__init__(
            content=Column([
                Text(label),
                editing_field,
                Column(
                    [ErrorText(text) for text in errors]
                )]
            ),
            width=600,
    )


class CreateObjectActionDialog(AlertDialog):
    def __init__(self, datatable):
        self.datatable = datatable
        self.errors: dict[str, list[str]] = {}
        self.fields: dict[Field, Control] = {}
        self.widgets: list[Control] = []
        self.errors = {'name': ['hello!']}


        super().__init__(
            modal=True,
            title=Text("Create new."),
            content=Column(self._get_content()),
            actions=[
                ElevatedButton("Cancel", on_click=self._close_dlg),
                ElevatedButton("Save", on_click=self._save_obj),
            ],
            actions_alignment=MainAxisAlignment.END,
        )

    # TODO : mb cached property
    # TODO noraml annotate - list of widget[column(fields)], list fields

    def _get_content(self) -> list[Control]:
        print('get content called')
        controls = []

        for field in self.datatable.fields:

            if field.read_only:
                edit_field = Text(field.label + ' - read only.')
            else:
                edit_field = field.edit()
                self.fields[field] = edit_field

            controls.append(
                EditFieldWidget(
                    field.label, edit_field, self.errors.get(field.label, [])
                )
            )

        return controls

    def _close_dlg(self, e=None):
        self.open = False
        self.page.update()

    def _save_obj(self, e=None):
        new_obj = {}
        self.errors = {'name': ['world!']}

        # help please
        self.update()
        self.page.update()
        for child in self._get_children():
            child.update()
        self.update()
        self.page.update()

        return

        # TODO validators, some checks
        for ui_field, input_widget in self.fields.items():
            if not (input_widget.value or ui_field.allow_null):
                # error msg
                break

            new_obj[ui_field.source] = input_widget.value

        self.datatable.model.create(**new_obj)
        self.datatable.update_rows()

        self.open = False
        self.page.update()
