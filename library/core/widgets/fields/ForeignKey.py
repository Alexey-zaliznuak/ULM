import flet as ft
from .BaseViewer import Viewer
from library.core.widgets.actions.objects.detail import (
    DetailObjectActionDialog
)


class ForeignKeyViewer(ft.Container, Viewer):
    has_value_for_copy = False

    def __init__(
        self,
        obj,
        fields,
        label: str,
    ):
        self.obj = obj
        self.fields = fields

        super().__init__(
            content=ft.Text(label),
            on_click=self.open_detail_modal
        )

    def open_detail_modal(self, e=None):
        # TODO While open https://github.com/flet-dev/flet/issues/1670
        # don`t open NEW modal
        if not getattr(self.page.dialog, 'open', False):
            # self.page.dialog.open = False
            self.page.dialog = DetailObjectActionDialog(self.obj, self.fields)
            self.page.dialog.open = True
            self.page.update()
