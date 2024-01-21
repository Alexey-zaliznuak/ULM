from typing import Any
import flet as ft

from library.core.widgets.text import TitleText
from .filter_field import FilterFieldWidget
from peewee import ForeignKeyField


LABEL_ID = 0
KEY_ID = 1


class FieldValueFilterWidget(FilterFieldWidget):
    def __init__(self, form, field):
        super().__init__(field=field, form=form)
        self.checkboxes: list[ft.Checkbox] = self._build_checkboxes()

    def build(self):
        # todo upgrade ui
        return ft.Column([
            TitleText(value=self.form._form_fields()[self.field.name].label),
            *self.checkboxes
        ])

    def _build_checkboxes(self):
        checkboxes = []
        checkboxes_params: list[tuple[str, Any]] = []

        for obj in self.form.Meta.model.select():
            field_value = getattr(obj, self.field.name)

            if isinstance(self.field, ForeignKeyField):
                label = str(field_value)
                field_value = getattr(obj, self.field.name + '_id')
            else:
                label = field_value

            checkboxes_params.append((label, field_value))

        checkboxes_params = set(checkboxes_params)

        for param in checkboxes_params:
            checkboxes.append(
                ft.Checkbox(
                    label=param[LABEL_ID], key=param[KEY_ID], value=True
                )
            )

        return checkboxes

    @property
    def value(self) -> list[str]:
        values = []

        for chb in self.checkboxes:
            if chb.value:
                values.append(chb.key)

        return values
