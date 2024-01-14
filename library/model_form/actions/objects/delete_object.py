from typing import Union
from functools import partial

from library.core.widgets.actions.objects.delete import (
    DeleteObjectActionButtonWidget
)
from library.utils import LazyAttribute
from library.core.widgets import ConfirmActionDialog
from flet import Page

from .object_action import DataTableObjectAction


class DeleteObjectAction(DataTableObjectAction):
    action_widget = DeleteObjectActionButtonWidget

    def __init__(self, request_confirm: bool = True):
        """
        request_confirm: - call ConfirmDialog for action confirm
        """
        self.request_confirm = request_confirm
        super().__init__()

    def on_click_method(
        self,
        obj,
        page: Union[Page, LazyAttribute[Page]],
        datatable,
        e
    ):
        if isinstance(page, LazyAttribute):
            page = page()

        def del_obj(obj, page, datatable):
            obj.delete_instance()
            if datatable:
                datatable.update_rows()

            page.update()

        action = partial(del_obj, obj, page, datatable)

        if self.request_confirm:
            confirm_action_dialog = ConfirmActionDialog(
                action
            )
            page.overlay.append(confirm_action_dialog)
            confirm_action_dialog.open = True
            page.update()

        else:
            action()
