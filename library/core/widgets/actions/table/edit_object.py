from flet import (
    AlertDialog,
    BottomSheet,
    ElevatedButton,
    Text,
    MainAxisAlignment,
    Control,
    Row,
    Container,
    Column,
    MainAxisAlignment,
    colors,
    border_radius,
    BoxShadow,
    ShadowBlurStyle,
    Offset,
    ListView
)
from typing import Callable
from library.core.widgets.text import Text, TitleText
from library.utils import LazyAttribute
from library.core.widgets import ErrorText
from library.model_form.fields import Field, empty


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


class ObjectErrorBottomSheet(BottomSheet):
    def __init__(self, error_text: str):
        # todo max size? mb list view
        super().__init__(
            Container(
                Column([
                    Container(
                        Column([
                            TitleText("Invalid data:"),
                            Text(error_text)
                        ]),
                        padding=8,
                        bgcolor=colors.WHITE,
                        border_radius=16,
                        shadow=BoxShadow(
                            blur_radius=15,
                            color=colors.WHITE,
                            offset=Offset(0, 0),
                            blur_style=ShadowBlurStyle.OUTER,
                        )
                    ),
                    Row(
                        [
                            ElevatedButton("OK", on_click=self.close, width=95, height=45, bgcolor=colors.AMBER_ACCENT_200)
                        ],
                        alignment=MainAxisAlignment.END
                    ),
                ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                ),
                padding=30,
                expand=True,
                bgcolor=colors.BLUE_400,
                border_radius=border_radius.vertical(top = 26, bottom = 0),
            ),
            open=True,
            enable_drag=True,
            
        )

    def close(self, e=None):
        self.open = False
        self.update()


class EditObjectActionDialog(AlertDialog):
    def __init__(
        self,
        obj: dict = {},
        datatable=None,
        form=None,
        *args,
        **kwargs
    ):
        self.obj = obj
        self.form = form
        self.datatable = datatable
        self.errors: dict[str, list[str]] = {}
        self.fields: dict[Field, Control] = {}
        self.fields_widgets: list[Control] = self._get_content()

        super().__init__(
            modal=True,
            # title=,
            content=Container(
                content=ListView([
                        TitleText("Create new."),
                        Column(self.fields_widgets),
                        Container(
                            content= Row(
                                [
                                    ElevatedButton("Cancel", on_click=self._close_dlg),
                                    ElevatedButton("Save", on_click=self._save_obj),
                                ],
                                alignment=MainAxisAlignment.END,
                                
                            ),
                            margin=10
                        ),
                       
                    ],
                    # scroll="adaptive",
                    width=600,
                    padding=15
                    # alignment=MainAxisAlignment.SPACE_BETWEEN,
                    
                ),
                
                # bgcolor=colors.AMBER,
                border_radius=26,
                padding=30,
                
            ),
            title_padding=0,
            actions_padding=0,
            content_padding=0,
            # actions=[
            #     ElevatedButton("Cancel", on_click=self._close_dlg),
            #     ElevatedButton("Save", on_click=self._save_obj),
            # ],
            actions_alignment=MainAxisAlignment.END,
        )

    def _get_content(self) -> list[Control]:
        # TODO : mb cached property
        # TODO noraml annotate - list of widget[column(fields)], list fields
        controls = []

        for field in self.form._form_fields(read_only=False).values():

            # if field.read_only:
            #     edit_field = Text(field.label + ' - read only.')
            # else:
            edit_field = field.edit(value=self.obj.get(field.label, empty))
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
            new_obj[ui_field.source] = input_widget.clear_value

        _, object_error, self.errors = self.form.create(new_obj)

        if not (self.errors or object_error):
            self.datatable.update_rows()
            self.open = False
            self.page.update()
            return

        if object_error:
            self.page.overlay.append(ObjectErrorBottomSheet(object_error))
            self.page.update()

        self.update()

    def update(self):
        for widget in self.fields_widgets:
            widget.update()

        return super().update()
