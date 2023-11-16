import flet as ft
from forms import EventTypesForm, EventForm

from flet_core.types import ScrollMode


person_form = EventTypesForm()
place_form = EventForm()


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.datatables = []

    # TODO global context class

    PersonDataTable, person_dt = person_form.DataTable()
    page.datatables.append(person_dt)

    PlaceDataTable, place_dt = place_form.DataTable()
    page.datatables.append(place_dt)

    c = ft.Column(
        [
            PersonDataTable,
            PlaceDataTable,
        ],
        expand=2, spacing=10,
        on_scroll_interval=30, scroll=ScrollMode.AUTO
    )

    page.add(
        c
    )


ft.app(target=main)
