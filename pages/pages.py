import flet as ft

from widgets.CustomNavigation import CustomNavigation


def WorkPage(page1):
    return CustomNavigation(
        selected_index=0,
        routes=[
            {
                "icon": (
                    ft.icons.NOW_WIDGETS,
                    ft.icons.NOW_WIDGETS_OUTLINED,
                ),
                'page':
                    ft.ListView(controls=[page1])
            },
            {
                "icon": (
                    ft.icons.ROOM,
                    ft.icons.ROOM_OUTLINED,
                ),
                'page':
                    ft.ListView(controls=[page1])
            },
            {
                "icon": (
                    ft.icons.REQUEST_QUOTE,
                    ft.icons.REQUEST_QUOTE_OUTLINED,
                ),
                'page':
                    ft.ListView(controls=[page1])
            },
        ],
    )


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
            {
                "icon": (
                    ft.icons.WORK,
                    ft.icons.WORK_OUTLINED,
                ),
                'page':
                    WorkPage(EventTypesDataTable)
            },
        ],
    )


def LearningPage(EventFormDataTable, PlaceDataTable, EventTypesDataTable):
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
            {
                "icon": (
                    ft.icons.WORK,
                    ft.icons.WORK_OUTLINED,
                ),
                'page':
                    WorkPage(EventTypesDataTable)
            },
        ]
    )


def EntertainmentPage(EventFormDataTable, PlaceDataTable, EventTypesDataTable):
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
