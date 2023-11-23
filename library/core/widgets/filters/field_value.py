import flet as ft
from .filter_field import FilterField


class FilterValueFieldWidget(ft.Container, FilterField):
    def __init__(self, form, datatable):
        self.objects_ids: list[int] = []
        self.checkboxes = []

        for obj in form.Meta.model.select():
            self.objects_ids.append(obj.id)
            self.checkboxes = [
                ft.Checkbox(label=str(obj), value=True)
            ]

        super().__init__(
            content=ft.Column(controls=self.checkboxes)
        )

    @property
    def value(self) -> list[int]:
        values = []

        for index, checkbox in enumerate(self.checkboxes):
            if checkbox.value:
                values.append(self.objects_ids[index])

        return values
