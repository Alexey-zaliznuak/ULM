import flet as ft

from core.ExportTable.ExportDataTable import ExportDataTable
from widgets.CustomNavigation import CustomNavigation
from core.ImportTable.ImportDataTable import ImportDataTable


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


def BookingPage(BookingFormDataTable, TimeLineTable):
    return CustomNavigation(
        selected_index=0,
        routes=[
            {
                "icon": (
                    ft.icons.FACT_CHECK,
                    ft.icons.FACT_CHECK_OUTLINED,
                ),
                'page':
                    ft.ListView(controls=[BookingFormDataTable]),
                'title': 'Бронь'
            },
            {
                "icon": (
                    ft.icons.CALENDAR_VIEW_DAY,
                    ft.icons.CALENDAR_VIEW_DAY_OUTLINED,
                ),
                'page':
                    ft.ListView(controls=[TimeLineTable]),
                'title': 'Календарь бронирования'
            },
        ],
    )


def EducationPage(
    ExhibitFormDataTable,
):
    return CustomNavigation(
        selected_index=0,
        routes=[
            {
                "icon": (
                    ft.icons.FORT,
                    ft.icons.FORT_OUTLINED,
                ),
                'page':
                    ft.ListView(controls=[ExhibitFormDataTable]),
                'title': 'Экспонаты'
            }
        ],
    )


def LearningPage(
    PlaceDataTable,
):
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
            }
        ]
    )


def EntertainmentPage(
    StudioDataTable,
    ClubFormDataTable
):
    return CustomNavigation(
        selected_index=0,
        routes=[
            {
                "icon": (
                    ft.icons.PLACE,
                    ft.icons.PLACE_OUTLINED,
                ),
                'page':
                    ft.ListView(controls=[StudioDataTable]),
                'title': 'Студии'
            },
            {
                "icon": (
                    ft.icons.MAN_4,
                    ft.icons.MAN_4_OUTLINED,
                ),
                'page':
                    ft.ListView(controls=[ClubFormDataTable]),
                'title': 'Преподаватели'
            }
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


def ScheduleTablePage(ScheduleTable):
    return CustomNavigation(
        selected_index=0,
        routes=[
            {
                "icon": (
                    ft.icons.CALENDAR_MONTH,
                    ft.icons.CALENDAR_MONTH_OUTLINED,
                ),
                'page':
                    ft.ListView(controls=[ScheduleTable]),
                'title': 'Расписание'
            }
        ]
    )

def EntertainmentPage(
    StudioDataTable,
    TeacherDataTable
):
    return CustomNavigation(
        selected_index=0,
        routes=[
            {
                "icon": (
                    ft.icons.PLACE,
                    ft.icons.PLACE_OUTLINED,
                ),
                'page':
                   ft.ListView(controls=[StudioDataTable]),
                'title': 'Студии'
            },
            {
                "icon": (
                    ft.icons.MAN_4,
                    ft.icons.MAN_4_OUTLINED,
                ),
                'page':
                    ft.ListView(controls=[TeacherDataTable]),
                'title': 'Преподаватели'
            }
        ]
    )


def ExcelPage():
    return CustomNavigation(
        selected_index=0,
        routes=[
            {
                "icon": (
                    ft.icons.DOWNLOAD,
                    ft.icons.DOWNLOAD,
                ),
                'page':
                    ft.ListView(controls=[
                        ImportDataTable()
                        ]),
                'title': 'Загрузка данных из Excel'
            },
            {
                "icon": (
                    ft.icons.UPLOAD,
                    ft.icons.UPLOAD,
                ),
                'page':
                    ft.ListView(controls=[
                        ExportDataTable()
                        ]),
                'title': 'Экспорт данных из Excel'
            },
        ]
    )