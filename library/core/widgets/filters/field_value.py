import flet as ft
from .filter_field import FilterField


# todo multiple select
class FilterValueFieldWidget(ft.UserControl, FilterField):
    def __init__(self, form, datatable):
        self.objects_ids: list[int] = []
        self.checkboxes = []
        self.form = form

    def build(self):
        return ft.Container(
            content=ft.Column(controls=self.checkboxes)
        )

    def update(self):
        # todo filters updates
        for obj in self.form.Meta.model.select():
            self.objects_ids.append(obj.id)
            self.checkboxes = [
                ft.Checkbox(label=str(obj), value=True)
            ]

        return super().update()

    @property
    def value(self) -> list[int]:
        values = []

        for index, checkbox in enumerate(self.checkboxes):
            if checkbox.value:
                values.append(self.objects_ids[index])

        return values
