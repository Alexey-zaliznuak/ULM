import flet as ft
from filtersets import TasksFilterSet

from pages.pages import EntertainmentPage, LearningPage, EducationPage
# from widgets.CustomNavigation import CustomNavigation

from models import Event, Categories, Place, init_tables, TasksStatuses, Task
init_tables()

from forms import (
    EventTypesForm,
    EventForm,
    PlaceForm,
    CategoriesForm,
    WorkTypeForm,
    TasksForm
)

from models import Event, Categories, Place, init_tables
init_tables()

from library.model_form.filters import FieldValueFilter




place_catagories_form = CategoriesForm()
place_form = PlaceForm()
events_types_form = EventTypesForm()
events_form = EventForm()
work_types_form = WorkTypeForm()
task_form = TasksForm()


def main(page: ft.Page):
    # TODO global context class
    page.theme_mode = ft.ThemeMode.LIGHT
    page.datatables = []

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

    t = ft.Tabs(
        selected_index=0,
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
                        TaskFormDataTablePr
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
                        TaskFormDataTableRa
                    )
                ),
            ),
            ft.Tab(
                text="Образование",
                content=ft.Container(
                    content=EntertainmentPage(
                        PlaceDataTableOb,
                    )
                ),
            ),
            ft.Tab(
                text="Активные заявки",
                content=ft.Container(
                    content=EntertainmentPage(
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
