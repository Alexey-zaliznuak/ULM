import flet as ft

from pages.pages import EntertainmentPage, LearningPage, EducationPage
from widgets.CustomNavigation import CustomNavigation

from forms import EventTypesForm, EventForm, PlaceForm, CategoriesForm
from models import Event, Categories, Place


place_catagories_form = CategoriesForm()
place_form = PlaceForm()
events_types_form = EventTypesForm()
events_form = EventForm()


def main(page: ft.Page):
    # TODO global context class
    page.theme_mode = ft.ThemeMode.LIGHT
    page.datatables = []


    PlaceDataTablePr, place_dtPr = place_form.DataTable(queryset=lambda: Place.select().where(Place.category==Categories.get(name='Просветительское')))
    page.datatables.append(place_dtPr)

    PlaceDataTableOb, place_dtOb = place_form.DataTable(queryset=lambda: Place.select().where(Place.category==Categories.get(name='Образовательное')))
    page.datatables.append(place_dtOb)

    PlaceDataTableRa, place_dtRa = place_form.DataTable(queryset=lambda: Place.select().where(Place.category==Categories.get(name='Развлекательное')))
    page.datatables.append(place_dtRa)



    EventTypesDataTablePr, events_types_form_dtPr = events_types_form.DataTable()
    page.datatables.append(events_types_form_dtPr)

    EventTypesDataTableOb, events_types_form_dtOb = events_types_form.DataTable()
    page.datatables.append(events_types_form_dtOb)

    EventTypesDataTableRa, events_types_form_dtRa = events_types_form.DataTable()
    page.datatables.append(events_types_form_dtRa)



    EventFormDataTablePr, events_dtPr = events_form.DataTable(queryset=lambda: Event.select().where(Event.category==Categories.get(name='Просветительское')))
    page.datatables.append(events_dtPr)

    EventFormDataTableOb, events_dtOb = events_form.DataTable(queryset=lambda: Event.select().where(Event.category==Categories.get(name='Образовательное')))
    page.datatables.append(events_dtOb)

    EventFormDataTableRa, events_dtRa = events_form.DataTable(queryset=lambda: Event.select().where(Event.category==Categories.get(name='Развлекательное')))
    page.datatables.append(events_dtRa)


    t = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Просвещение",
                content=ft.Container(
                    content=EducationPage(EventFormDataTablePr, PlaceDataTablePr, EventTypesDataTablePr),
                ),
            ),
            ft.Tab(
                text="Развлечение",
                content=ft.Container(
                    content=LearningPage(EventFormDataTableRa, PlaceDataTableRa, EventTypesDataTableRa)
                ),
            ),
            ft.Tab(
                text="Образование",
                content=ft.Container(
                    content=EntertainmentPage(EventFormDataTableOb, PlaceDataTableOb, EventTypesDataTableOb)
                ),
            ),
        ],
        expand=1,
    )

    page.add(
        ft.Row(
            controls=[
                t
            ],
            expand=True,
        )
    )


ft.app(target=main)
