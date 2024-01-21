from flet import (
    app,
    Page,
    ThemeMode,
    Tabs,
    Tab,
    Row,
    colors,
    Container,
)

from widgets.TabText import TabText
from core.TimeLineTable.TimeLineTable import TimeLineTable
from filtersets import TasksFilterSet
from loadpage import LoadPage

from pages.pages import (
    EntertainmentPage,
    LearningPage,
    EducationPage,
    ScheduleTablePage,
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
    Club
)

init_tables()

from core.ScheduleTable.schedule_table import ScheduleDataTable

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


def main(page: Page):
    # TODO global context class
    page.theme_mode = ThemeMode.LIGHT
    page.datatables = []
    page.title = 'Fletty birds'
    page.fonts = {
        "Comfortaa-Variable": "/fonts/Comfortaa-Variable.ttf",
        "DidactGothic-Regular": "/fonts/DidactGothic-Regular.ttf",
        "Pacifico-Regular": "/fonts/Pacifico-Regular.ttf",
        "MarckScript-Regular": "/fonts/MarckScript-Regular.ttf",
        
    }

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

    # ---------------ScheduleTableData---------------
    ScheduleTableOb = ScheduleDataTable(
        clubs=Club.select
    )

    t = Tabs(
        selected_index=0,
        animation_duration=50,
        overlay_color=colors.BLUE_100,
        tabs=[
            Tab(
                tab_content=TabText("Просвещение"),
                content=Container(
                    content=EducationPage(
                        EventFormDataTablePr,
                        PlaceDataTablePr,
                        EventTypesDataTablePr,
                        WorkTypesFormDataTablePr,
                        TaskFormDataTablePr,
                        BookingFormDataTablePr,
                        TimeLineTablePr,
                    ),
                ),

            ),
            Tab(
                tab_content=TabText("Развлечение"),
                content=Container(
                    content=LearningPage(
                        EventFormDataTableRa,
                        PlaceDataTableRa,
                        EventTypesDataTableRa,
                        WorkTypesFormDataTableRa,
                        TaskFormDataTableRa,
                        BookingFormDataTableRa,
                        TimeLineTableRa,
                    )
                ),
            ),
            Tab(
                tab_content=TabText("Образование"),
                content=Container(
                    content=EntertainmentPage(
                        PlaceDataTableOb,
                        TeacherFormDataTableOb,
                        ClubFormDataTableOb,
                        ClubTypeFormDataTableOb,
                    )
                ),
            ),
            Tab(
                tab_content=TabText("Активные заявки"),
                content=Container(
                    content=WorkTablePage(
                        WorkTableFormDataTable,
                    )
                ),
            ),
            Tab(
                tab_content=TabText("Расписание занятий"),
                content=Container(
                    content=ScheduleTablePage(
                        ScheduleTableOb,
                    )
                ),
            ),
        ],
        on_change=lambda _: ScheduleTableOb.update(),
        expand=True,
    )

    page.window_center()
    page.window_width = 700
    page.window_height = 450
    page.window_resizable = False
    page.horizontal_alignment = "center"
    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True
    page.padding = 0

    loadpage = LoadPage()
    page.add(
        loadpage
    )

    if loadpage.animate_me():
        page.controls.pop()

        page.window_width = 1265.6
        page.window_height = 682.4
        page.window_resizable = True
        page.horizontal_alignment = ''
        page.window_center()
        page.window_maximized = True
        page.window_title_bar_hidden = False
        page.window_title_bar_buttons_hidden = False
        page.padding = None

        page.add(
            Row(
                controls=[
                    t
                ],
                expand=True,
            )
        )
    page.update()


app(target=main)
