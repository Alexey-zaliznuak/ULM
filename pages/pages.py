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
                    ft.ListView(controls=[page1]),
                'title': 'Виды работ'
            },
            {
                "icon": (
                    ft.icons.ROOM,
                    ft.icons.ROOM_OUTLINED,
                ),
                'page':
                    ft.ListView(controls=[page1]),
                'title': 'Помещение'
            },
            {
                "icon": (
                    ft.icons.REQUEST_QUOTE,
                    ft.icons.REQUEST_QUOTE_OUTLINED,
                ),
                'page':
                    ft.ListView(controls=[page1]),
                'title': 'Заявки'
            },
        ],
    )

def EntertainmentWorkPage(page1):
    return CustomNavigation(
        selected_index=0,
        routes=[
            {
                "icon": (
                    ft.icons.ROOM,
                    ft.icons.ROOM_OUTLINED,
                ),
                'page':
                    ft.ListView(controls=[page1]),
                'title': 'Помещение'
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
                    ft.ListView(controls=[EventFormDataTable]),
                'title': 'События'
            },
            {
                "icon": (
                    ft.icons.PLACE,
                    ft.icons.PLACE_OUTLINED,
                ),
                'page':
                    ft.ListView(controls=[PlaceDataTable]),
                'title': 'Пространства'
            },
            {
                "icon": (
                    ft.icons.NOW_WIDGETS,
                    ft.icons.NOW_WIDGETS_OUTLINED,
                ),
                'page':
                    ft.ListView(controls=[EventTypesDataTable]),
                'title': 'Виды мероприятий'
            },
            {
                "icon": (
                    ft.icons.WORK,
                    ft.icons.WORK_OUTLINED,
                ),
                'page':
                    WorkPage(EventTypesDataTable),
                'title': ''
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
                    ft.ListView(controls=[EventFormDataTable]),
                'title': 'События'
            },
            {
                "icon": (
                    ft.icons.PLACE,
                    ft.icons.PLACE_OUTLINED,
                ),
                'page':
                    ft.ListView(controls=[PlaceDataTable]),
                'title': 'Пространства'
            },
            {
                "icon": (
                    ft.icons.NOW_WIDGETS,
                    ft.icons.NOW_WIDGETS_OUTLINED,
                ),
                'page':
                    ft.ListView(controls=[EventTypesDataTable]),
                'title': 'Виды мероприятий'
            },
            {
                "icon": (
                    ft.icons.WORK,
                    ft.icons.WORK_OUTLINED,
                ),
                'page':
                    WorkPage(EventTypesDataTable),
                'title': ''
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
                    ft.ListView(controls=[PlaceDataTable]),
                'title': 'Пространства'
            },
            {
                "icon": (
                    ft.icons.WORK,
                    ft.icons.WORK_OUTLINED,
                ),
                'page':
                    EntertainmentWorkPage(EventTypesDataTable),
                'title': ''
            },
        ]
    )
