from typing import Union

from library.core.widgets.actions.objects.delete import DeleteObjectActionButtonWidget, DeleteObjectActionDialog
from library.core.utils import LazyAttribute
from flet import Page

from .object_action import ObjectAction


class DeleteObjectAction(ObjectAction):
    action_widget = DeleteObjectActionButtonWidget

    def on_click_method(self, obj, page: Union[Page, LazyAttribute[Page]], datatable, e):
        if isinstance(page, LazyAttribute):
            page = page()

        page.dialog = DeleteObjectActionDialog(obj, datatable)
        page.dialog.open = True
        page.update()
