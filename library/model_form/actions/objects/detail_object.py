from typing import Union

from library.core.widgets.actions.objects.detail import (
    DetailObjectActionButtonWidget,
    DetailObjectActionDialog
)
from library.utils import LazyAttribute
from flet import Page

from .object_action import DataTableObjectAction


class DataTableDetailObjectAction(DataTableObjectAction):
    action_widget = DetailObjectActionButtonWidget

    def on_click_method(
        self,
        obj,
        page: Union[Page, LazyAttribute[Page]],
        datatable,
        e
    ):
        if isinstance(page, LazyAttribute):
            page = page()

        detail_object_action_dialog = DetailObjectActionDialog(
            obj=obj,
            fields=datatable.fields
        )
        page.overlay.append(detail_object_action_dialog)
        detail_object_action_dialog.open = True
        page.update()


class DetailObjectAction(DataTableObjectAction):
    action_widget = DetailObjectActionButtonWidget

    def on_click_method(
        self,
        obj,
        page: Union[Page, LazyAttribute[Page]],
        fields,
        e
    ):
        if isinstance(page, LazyAttribute):
            page = page()

        detail_object_action_dialog = DetailObjectActionDialog(
            obj=obj,
            fields=fields
        )
        page.overlay.append(detail_object_action_dialog)
        detail_object_action_dialog.open = True
        page.update()
