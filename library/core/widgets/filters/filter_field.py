import flet as ft


class FilterFieldWidget(ft.UserControl):
    def __init__(self, field, form):
        self.field = field
        self.form = form
        super().__init__()

    @property
    def value(self):
        ...
