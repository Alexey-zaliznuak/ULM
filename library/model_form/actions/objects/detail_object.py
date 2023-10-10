from typing import Union

from library.core.widgets.actions.objects.detail import DetailObjectActionButtonWidget, DetailObjectActionDialog
from library.core.utils import LazyAttribute
from flet import Page

from .object_action import ObjectAction


class DetailObjectAction(ObjectAction):
    action_widget = DetailObjectActionButtonWidget

    def on_click_method(self, obj, page: Union[Page, LazyAttribute[Page]], datatable, e):
        if isinstance(page, LazyAttribute):
            page = page()

        page.dialog = DetailObjectActionDialog(obj, datatable)
        page.dialog.open = True
        page.update()
