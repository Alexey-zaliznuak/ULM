import flet as ft

from pages.pages import EntertainmentPage, LearningPage, EducationPage
from widgets.CustomNavigation import CustomNavigation

from forms import EventTypesForm, EventForm, PlaceForm, CategoriesForm
from models import Event, Categories


place_catagories_form = CategoriesForm()
place_form = PlaceForm()
events_types_form = EventTypesForm()
events_form = EventForm()


def main(page: ft.Page):
    # TODO global context class
    page.theme_mode = ft.ThemeMode.LIGHT
    page.datatables = []


    PlaceDataTable, place_dt = place_form.DataTable()
    page.datatables.append(place_dt)

    EventTypesDataTable, events_types_form_dt = events_types_form.DataTable()
    page.datatables.append(events_types_form_dt)

    EventFormDataTable, events_dt = events_form.DataTable(queryset=lambda: Event.select().where(Event.category==Categories.get(name='Просветительское')))
    page.datatables.append(events_dt)


    t = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Просвещение",
                content=ft.Container(
                    content=EducationPage(EventFormDataTable, PlaceDataTable, EventTypesDataTable)  
                ),
            ),
            # ft.Tab(
            #     text="Развлечение",
            #     content=ft.Container(
            #         content=LearningPage(EventFormDataTable, PlaceDataTable, EventTypesDataTable)
            #     ),
            # ),
            # ft.Tab(
            #     text="Образование",
            #     content=ft.Container(
            #         content=EntertainmentPage(EventFormDataTable, PlaceDataTable, EventTypesDataTable)
            #     ),
            # ),
        ],
        expand=1,

    )

    page.add(
        ft.Row(
            controls=[
                CustomNavigation(
                    selected_index=3,
                        routes=[
                            {
                                "icon": (
                                    ft.icons.FAVORITE,
                                    ft.icons.FAVORITE_BORDER,
                                ),
                                'page': ft.ListView(controls=[PlaceCategoriesDataTable])
                            },
                            {
                                "icon": (
                                    ft.icons.SETTINGS,
                                    ft.icons.SETTINGS_OUTLINED,
                                ),
                                'page': 
                                    ft.ListView(controls=[PlaceDataTable])
                            },
                            {
                                "icon": (
                                    ft.icons.ACCOUNT_BOX,
                                    ft.icons.ACCOUNT_BOX_OUTLINED,
                                ),
                                'page': 
                                    ft.ListView(controls=[EventTypesDataTable])
                            },
                            {
                                "icon": (
                                    ft.icons.EXPAND_LESS,
                                    ft.icons.EXPAND_LESS_OUTLINED,
                                ),
                                'page': 
                                    ft.ListView(controls=[EventFormDataTable])
                            },
                        ]
                )
            ],
            expand=True,
        )
    )


ft.app(target=main)
