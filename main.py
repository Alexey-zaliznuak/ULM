import flet as ft
from core.TimeLineTable.TimeLineTable import TimeLineTable
from filtersets import TasksFilterSet

from pages.pages import (
    EntertainmentPage,
    LearningPage,
    EducationPage,
    WorkTablePage
)
# from widgets.CustomNavigation import CustomNavigation

from models import (
    Event,
    Categories,
    Place,
    init_tables,
    TasksStatuses,
    Task,
    Booking,
)

init_tables()

from forms import (
    EventTypesForm,
    EventForm,
    PlaceForm,
    CategoriesForm,
    WorkTypeForm,
    TasksForm,
    BookingForm,
    TeacherForm,
    ClubForm,
    ClubTypeForm
)

from library.model_form.filters import FieldValueFilter


place_catagories_form = CategoriesForm()
place_form = PlaceForm()
events_types_form = EventTypesForm()
events_form = EventForm()
work_types_form = WorkTypeForm()
task_form = TasksForm()
booking_form = BookingForm()
teacher_form = TeacherForm()
club_form = ClubForm()
club_type_form = ClubTypeForm()


def main(page: ft.Page):
    # TODO global context class
    page.theme_mode = ft.ThemeMode.LIGHT
    page.datatables = []
    page.title = 'Fletty birds'
    # ---------------PlaceData---------------
    PlaceDataTablePr, place_dtPr = place_form.DataTable(
        default_filters=[
            FieldValueFilter(
                Place.category,
                Categories.get(name='Просветительское')
            )
        ]
    )
    page.datatables.append(place_dtPr)

    PlaceDataTableOb, place_dtOb = place_form.DataTable(
        default_filters=[
            FieldValueFilter(
                Place.category,
                Categories.get(name='Образовательное')
            )
        ]
    )
    page.datatables.append(place_dtOb)

    PlaceDataTableRa, place_dtRa = place_form.DataTable(
        default_filters=[
            FieldValueFilter(
                Place.category,
                Categories.get(name='Развлекательное')
            )
        ]
    )
    page.datatables.append(place_dtRa)
    # ---------------EventTypesData---------------
    EventTypesDataTablePr, events_types_form_dtPr = (
        events_types_form.DataTable()
    )
    page.datatables.append(events_types_form_dtPr)

    EventTypesDataTableOb, events_types_form_dtOb = (
        events_types_form.DataTable()
    )
    page.datatables.append(events_types_form_dtOb)

    EventTypesDataTableRa, events_types_form_dtRa = (
        events_types_form.DataTable()
    )
    page.datatables.append(events_types_form_dtRa)

    # ---------------EventData---------------
    EventFormDataTablePr, events_dtPr = events_form.DataTable(
        default_filters=[
            FieldValueFilter(
                Event.category,
                Categories.get(name='Просветительское')
            )
        ]
    )
    page.datatables.append(events_dtPr)

    EventFormDataTableOb, events_dtOb = events_form.DataTable(
        default_filters=[
            FieldValueFilter(
                Event.category,
                Categories.get(name='Образовательное')
            )
        ]
    )
    page.datatables.append(events_dtOb)

    EventFormDataTableRa, events_dtRa = events_form.DataTable(
        default_filters=[
            FieldValueFilter(
                Event.category,
                Categories.get(name='Развлекательное')
            )
        ]
    )
    page.datatables.append(events_dtRa)

    # ---------------WorkTypesData---------------
    WorkTypesFormDataTablePr, work_types_events_dtPr = (
        work_types_form.DataTable()
    )
    page.datatables.append(work_types_events_dtPr)

    WorkTypesFormDataTableOb, work_types_events_dtOb = (
        work_types_form.DataTable()
    )
    page.datatables.append(work_types_events_dtOb)

    WorkTypesFormDataTableRa, work_types_events_dtRa = (
        work_types_form.DataTable()
    )
    page.datatables.append(work_types_events_dtRa)

    # ---------------TaskData---------------
    TaskFormDataTablePr, task_events_dtPr = (
        task_form.DataTable()
    )
    page.datatables.append(task_events_dtPr)

    TaskFormDataTableOb, task_events_dtOb = (
        task_form.DataTable()
    )
    page.datatables.append(task_events_dtOb)

    TaskFormDataTableRa, task_events_dtRa = (
        task_form.DataTable()
    )
    page.datatables.append(task_events_dtRa)

    # ---------------WorkTableData---------------
    WorkTableFormDataTable, work_table_dt = (
        task_form.DataTable(
            default_filters=[
                FieldValueFilter(
                    Task.status,
                    TasksStatuses.get(status_name='К выполнению')
                )
            ],
            filterset=TasksFilterSet
        )
    )
    page.datatables.append(work_table_dt)

    # ---------------BookingTableData---------------
    BookingFormDataTableRa, booking_events_dtRa = (
        booking_form.DataTable()
    )
    page.datatables.append(booking_events_dtRa)

    BookingFormDataTablePr, booking_events_dtPr = (
        booking_form.DataTable()
    )
    page.datatables.append(booking_events_dtPr)

    # ---------------TimeLineTableData---------------

    TimeLineTableRa = TimeLineTablePr = TimeLineTable(
        get_bookings=Booking.select,
        get_places=Place.select
    )

    # ---------------TeacherTableData---------------
    TeacherFormDataTableOb, teacher_events_dtOb = (
        teacher_form.DataTable()
    )
    page.datatables.append(teacher_events_dtOb)

    # ---------------ClubTableData---------------
    ClubFormDataTableOb, club_events_dtOb = (
        club_form.DataTable()
    )
    page.datatables.append(club_events_dtOb)

    # ---------------ClubTypeTableData---------------
    ClubTypeFormDataTableOb, club_type_events_dtOb = (
        club_type_form.DataTable()
    )
    page.datatables.append(club_type_events_dtOb)

    t = ft.Tabs(
        selected_index=2,
        animation_duration=50,
        tabs=[
            ft.Tab(
                text="Просвещение",
                content=ft.Container(
                    content=EducationPage(
                        EventFormDataTablePr,
                        PlaceDataTablePr,
                        EventTypesDataTablePr,
                        WorkTypesFormDataTablePr,
                        TaskFormDataTablePr,
                        BookingFormDataTablePr,
                        TimeLineTablePr
                    ),
                ),

            ),
            ft.Tab(
                text="Развлечение",
                content=ft.Container(
                    content=LearningPage(
                        EventFormDataTableRa,
                        PlaceDataTableRa,
                        EventTypesDataTableRa,
                        WorkTypesFormDataTableRa,
                        TaskFormDataTableRa,
                        BookingFormDataTableRa,
                        TimeLineTableRa
                    )
                ),
            ),
            ft.Tab(
                text="Образование",
                content=ft.Container(
                    content=EntertainmentPage(
                        PlaceDataTableOb,
                        TeacherFormDataTableOb,
                        ClubFormDataTableOb,
                        ClubTypeFormDataTableOb,
                    )
                ),
            ),
            ft.Tab(
                text="Активные заявки",
                content=ft.Container(
                    content=WorkTablePage(
                        WorkTableFormDataTable,
                    )
                ),
            ),
        ],
        expand=True,
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
