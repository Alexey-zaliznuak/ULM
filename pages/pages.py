import flet as ft

from widgets.CustomNavigation import CustomNavigation


def WorkPage(WorkTypesFormDataTable, TaskFormDataTable):
    return CustomNavigation(
        selected_index=0,
        routes=[
            {
                "icon": (
                    ft.icons.REQUEST_QUOTE,
                    ft.icons.REQUEST_QUOTE_OUTLINED,
                ),
                'page':
                    ft.ListView(controls=[TaskFormDataTable]),
                'title': 'Заявки'
            },
            {
                "icon": (
                    ft.icons.NOW_WIDGETS,
                    ft.icons.NOW_WIDGETS_OUTLINED,
                ),
                'page':
                    ft.ListView(controls=[WorkTypesFormDataTable]),
                'title': 'Виды работ'
            },
        ],
    )


def EducationPage(
    EventFormDataTable,
    PlaceDataTable,
    EventTypesDataTable,
    WorkTypesFormDataTable,
    TaskFormDataTable
):
    return CustomNavigation(
        selected_index=3,
        routes=[
            {
                "icon": (
                    ft.icons.EVENT,
                    ft.icons.EVENT_OUTLINED,
                ),
                'page':
                    ft.ListView(controls=[EventFormDataTable]),
                'title': 'Мероприятия'
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
                    WorkPage(WorkTypesFormDataTable, TaskFormDataTable),
                'title': ''
            },
        ],
    )


def LearningPage(
    EventFormDataTable,
    PlaceDataTable,
    EventTypesDataTable,
    WorkTypesFormDataTable,
    TaskFormDataTable
):
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
                'title': 'Мероприятия'
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
                    WorkPage(WorkTypesFormDataTable, TaskFormDataTable),
                'title': ''
            },
        ]
    )


def EntertainmentPage(PlaceDataTable):
    return CustomNavigation(
        selected_index=0,
        routes=[
            {
                "icon": (
                    ft.icons.WORK,
                    ft.icons.WORK_OUTLINED,
                ),
                'page':
                    ft.ListView(controls=[PlaceDataTable]),
                'title': 'К выполнению'
            },
        ]
    )


def WorkTablePage(WorkTable):
    return CustomNavigation(
        selected_index=0,
        routes=[
            {
                "icon": (
                    ft.icons.WORK,
                    ft.icons.WORK_OUTLINED,
                ),
                'page':
                    ft.ListView(controls=[WorkTable]),
                'title': 'Заявки'
            },
        ]
    )