import flet as ft
from library.core.widgets.text import Text

from forms import ExhibitForm, StudioForm, PlaceForm, TeacherForm

class ExportDataTable(ft.Row):
    def button_clicked(self, e):
        retranslate = {
            'Пространства': 'SpacesData',
            'Экспонаты': 'ExhibitsData',
            'Студия': 'StudiosData',
            'Преподаватели': 'TeachersData',
        }
        export_method = {
            'SpacesData': lambda: PlaceForm().to_excel(write_file='SpacesData'),
            'ExhibitsData': lambda: ExhibitForm().to_excel(write_file='ExhibitsData'),
            'StudiosData': lambda: StudioForm().to_excel(write_file='StudiosData'),
            'TeachersData': lambda: TeacherForm().to_excel(write_file='TeachersData'),
        }
        filename = retranslate[self.dd.value]
        export_method[filename]()        

        self.controls[2].value = f"Файл с данными загружен как {filename}.xls. В папку с проектом"
        self.update()

    def __init__(self):
        self.t = Text()
        self.b = ft.ElevatedButton(text="Выгрузить", on_click=self.button_clicked)
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
