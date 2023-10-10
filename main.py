import flet as ft
from ui_model_forms import PersonUIModelForm


person_form = PersonUIModelForm()


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    # page.scroll = 'always'

    # lv = ft.ListView(
    #     expand=1, spacing=10, padding=20, auto_scroll=True, width=700,
    #     on_scroll_interval=30,
    # )

    page.add(
        ft.Text('Persons'),
        person_form.DataTable(
            queryset=person_form.Meta.model.select
        )
    )


ft.app(target=main)
