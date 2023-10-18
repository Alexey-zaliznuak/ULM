from flet import (
    icons,
    AlertDialog,
    ElevatedButton,
    Text,
    MainAxisAlignment,
    Control,
    Column
)
from library.core.widgets.actions import ActionButton
from library.model_form.ui_fields import Field


class CreateObjectActionButtonWidget(ActionButton):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args, **kwargs,
            icon=icons.ADD,
        )


class CreateObjectActionDialog(AlertDialog):
    def __init__(self, datatable):
        self.datatable = datatable
        fields_list_widget, self.fields = self.make_fields()

        super().__init__(
            modal=True,
            title=Text("Create new."),
            content=Column(
                fields_list_widget,
                tight=True,
                width=300
            ),
            actions=[
                ElevatedButton("Cancel", on_click=self.close_dlg),
                ElevatedButton("Save", on_click=self.save_obj),
            ],
            actions_alignment=MainAxisAlignment.END,
        )

    def close_dlg(self, e=None):
        self.open = False
        self.page.update()

    def save_obj(self, e=None):
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

    # TODO : mb cached property
    # TODO noraml annotate - list of widget[column(fields)], list fields

    def make_fields(self) -> tuple[list[Column], list[Control]]:
        fields: dict[Field, Control] = {}
        widgets = []

        for field in self.datatable.fields:
            if field.read_only:
                widgets.append(Text(field.label + ' - read only.'))
                continue

            f = field.edit()
            fields[field] = f

            widgets.append(
                Column([
                    Text(field.label),
                    f
                ])
            )

        return widgets, fields
