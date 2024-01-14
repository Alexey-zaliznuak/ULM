from typing import Union

from library.core.widgets.actions.table.edit_object import (
    EditObjectActionDialog,
    EditObjectActionButton,
)
from library.utils import LazyAttribute
from flet import Page

from .object_action import DataTableObjectAction


class EditObjectAction(DataTableObjectAction):
    action_widget = EditObjectActionButton

    def on_click_method(
        self,
        obj,
        page: Union[Page, LazyAttribute[Page]],
        datatable,
        e
    ):
        if isinstance(page, LazyAttribute):
            page = page()

        edit_object_action_dialog = EditObjectActionDialog(
            obj=obj,
            datatable=datatable,
            form=datatable.form
        )
        page.overlay.append(edit_object_action_dialog)
        edit_object_action_dialog.open = True
        page.update()
