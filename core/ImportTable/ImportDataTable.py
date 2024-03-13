import flet as ft
from library.core.widgets.text import Text

from generators import generate_exhibits, generate_places, generate_studios, generate_teachers


class ImportDataTable(ft.Row):
    def button_clicked(self, e):

        export_method = {
            'Пространства': generate_places,
            'Экспонаты': generate_exhibits,
            'Студия': generate_studios,
            'Преподаватели': generate_teachers,
        }
        export_method[self.dd.value]()  

        self.controls[2].value = f"Данные для: «{self.dd.value}» загружены. Проверьте таблицу"
        self.page.datatables[0].update_rows()
        self.update()

    def __init__(self):
        self.t = Text()
        self.b = ft.ElevatedButton(text="Загрузить", on_click=self.button_clicked)
        self.dd = ft.Dropdown(
            options=[
                ft.dropdown.Option("Пространства"),
                ft.dropdown.Option("Экспонаты"),
                ft.dropdown.Option("Студия"),
                ft.dropdown.Option("Преподаватели"),
            ],
        )
        super().__init__(
            [
                self.dd,
                self.b,
                self.t
            ],
            scroll=True
        )
