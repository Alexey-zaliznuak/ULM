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
from typing import Callable
from library.core.widgets.actions import ActionButton
from library.utils import LazyAttribute
from library.core.widgets import ErrorText
from library.model_form.ui_fields import Field


class CreateObjectActionButtonWidget(ActionButton):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args, **kwargs,
            icon=icons.ADD,
        )


class EditFieldWidget(Container):
    def __init__(
        self,
        label,
        editing_field: Control = None,
        errors: Callable[[], list[str]] = None
    ):
        self.label = label
        self._get_errors = errors
        self.column_errors = Column(self._get_column_errors())

        super().__init__(
            content=Column(
                [
                    Text(label),
                    editing_field,
                    self.column_errors
                ]
            ),
            width=600,
        )

    def update(self):
        for child in self.content.controls:
            if child is self.column_errors:
                child.controls = self._get_column_errors()

        return super().update()

    def _get_column_errors(self) -> list[Control]:
        return [ErrorText(text) for text in self._get_errors()()]


class CreateObjectActionDialog(AlertDialog):
    def __init__(self, datatable):
        self.datatable = datatable
        self.errors: dict[str, list[str]] = {}
        self.fields: dict[Field, Control] = {}
        self.fields_widgets: list[Control] = self._get_content()

        super().__init__(
            modal=True,
            title=Text("Create new."),
            content=Column(self.fields_widgets),
            actions=[
                ElevatedButton("Cancel", on_click=self._close_dlg),
                ElevatedButton("Save", on_click=self._save_obj),
            ],
            actions_alignment=MainAxisAlignment.END,
        )

    def _get_content(self) -> list[Control]:
        # TODO : mb cached property
        # TODO noraml annotate - list of widget[column(fields)], list fields
        controls = []

        for field in self.datatable.fields:

            if field.read_only:
                edit_field = Text(field.label + ' - read only.')
            else:
                edit_field = field.edit()
                self.fields[field] = edit_field

            controls.append(
                EditFieldWidget(
                    field.label, edit_field, LazyAttribute(
                        obj=self,
                        attr='errors.get',
                        args=(field.label, []),
                    ))
            )

        return controls

    def _close_dlg(self, e=None):
        self.open = False
        self.page.update()

    def _save_obj(self, e=None):
        new_obj = {}

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

    def update(self):
        for widget in self.fields_widgets:
            widget.update()

        return super().update()
