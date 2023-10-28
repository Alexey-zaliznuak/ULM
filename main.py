import flet as ft
from forms import PersonUIModelForm

from flet_core.types import ScrollMode
from library.core.widgets.fields.DateTime import DateTimePicker, DateTimeViewer

from library.core.widgets.fields.Phone import PhoneInput


person_form = PersonUIModelForm()


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    # page.scroll = 'always'

    c = ft.Column(
        [person_form.DataTable()],
        expand=2, spacing=10, width=800,
        on_scroll_interval=30, scroll=ScrollMode.AUTO
    )

    page.add(
        c,
    )


ft.app(target=main)
