import flet as ft
from forms import PersonUIModelForm


person_form = PersonUIModelForm()


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    # page.scroll = 'always'

    lv = ft.ListView(
        [person_form.DataTable()],
        expand=2, spacing=10, padding=20, auto_scroll=True, width=800,
        on_scroll_interval=30
    )

    page.add(
        ft.Text('Persons'),
        lv
    )


ft.app(target=main)
