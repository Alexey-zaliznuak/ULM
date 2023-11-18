import flet as ft

from widgets.CustomNavigation import CustomNavigation

   
def EducationPage(EventFormDataTable, PlaceDataTable, EventTypesDataTable):
    return CustomNavigation(
                    selected_index=0,
                        routes=[
                            {
                                "icon": (
                                    ft.icons.EVENT,
                                    ft.icons.EVENT_OUTLINED,
                                ),
                                'page': 
                                    ft.ListView(controls=[EventFormDataTable])
                            },
                            {
                                "icon": (
                                    ft.icons.PLACE,
                                    ft.icons.PLACE_OUTLINED,
                                ),
                                'page': 
                                    ft.ListView(controls=[PlaceDataTable])
                            },
                            {
                                "icon": (
                                    ft.icons.NOW_WIDGETS,
                                    ft.icons.NOW_WIDGETS_OUTLINED,
                                ),
                                'page': 
                                    ft.ListView(controls=[EventTypesDataTable])
                            },
                        ]
                )


def LearningPage(EventFormDataTable, PlaceDataTable, EventTypesDataTable):
    return CustomNavigation(
                    selected_index=0,
                        routes=[
                            {
                                "icon": (
                                    ft.icons.PLACE,
                                    ft.icons.PLACE_OUTLINED,
                                ),
                                'page': 
                                    ft.ListView(controls=[PlaceDataTable])
                            },
                        ]
                )


def EntertainmentPage(EventFormDataTable, PlaceDataTable, EventTypesDataTable):
    return CustomNavigation(
                    selected_index=0,
                        routes=[
                            {
                                "icon": (
                                    ft.icons.EVENT,
                                    ft.icons.EVENT_OUTLINED,
                                ),
                                'page': 
                                    ft.ListView(controls=[EventFormDataTable])
                            },
                            {
                                "icon": (
                                    ft.icons.PLACE,
                                    ft.icons.PLACE_OUTLINED,
                                ),
                                'page': 
                                    ft.ListView(controls=[PlaceDataTable])
                            },
                            {
                                "icon": (
                                    ft.icons.NOW_WIDGETS,
                                    ft.icons.NOW_WIDGETS_OUTLINED,
                                ),
                                'page': 
                                    ft.ListView(controls=[EventTypesDataTable])
                            },
                        ]
                )