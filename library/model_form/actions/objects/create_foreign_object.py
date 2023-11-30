from typing import Union

from library.core.widgets.actions.table.edit_object import (
    EditObjectActionDialog,
    ActionButton,
)
from library.utils import LazyAttribute
from flet import Page, icons

from .object_action import ObjectAction


class CreateForeignObjectAction(ObjectAction):
    action_widget = ActionButton
    params = dict(
        icon=icons.EDGESENSOR_HIGH_OUTLINED
    )

    def __init__(self, foreign_form, foreign_field):
        self.foreign_form = foreign_form
        self.foreign_field = foreign_field

    def on_click_method(
        self,
        obj,
        page: Union[Page, LazyAttribute[Page]],
        datatable,
        e
    ):
        if isinstance(page, LazyAttribute):
            page = page()

        page.dialog = EditObjectActionDialog(
            form=self.foreign_form,
            obj={self.foreign_field.label: obj.id},
        )
        page.dialog.open = True
        page.update()
