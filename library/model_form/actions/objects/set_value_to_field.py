from typing import Union
from functools import partial

from library.core.widgets.actions.objects.set_value import (
    SetValueObjectActionButtonWidget
)
from library.utils import LazyAttribute
from library.core.widgets import ConfirmActionDialog
from flet import Page

from .object_action import DataTableObjectAction


class SetValueObjectAction(DataTableObjectAction):
    action_widget = SetValueObjectActionButtonWidget

    def __init__(
        self,
        field,
        value,
        *,
        request_confirm: bool = True,
    ):
        """
        request_confirm: - call ConfirmDialog for action confirm
        """
        self.field = field
        self.value = value
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

        def change_obj(obj, page, datatable):
            value = self.value

            if callable(value):
                value = value(obj)

            setattr(obj, self.field.name, value)
            obj.save()

            if datatable:
                datatable.update_rows()

            page.update()

        action = partial(change_obj, obj, page, datatable)

        if self.request_confirm:
            confirm_action_dialog = ConfirmActionDialog(
                action
            )
            page.overlay.append(confirm_action_dialog)
            confirm_action_dialog.open = True
            page.update()

        else:
            action()
