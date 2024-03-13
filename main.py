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

from models import (
    Place,
    Studio,
    Exhibit,
    Teacher,
    manage_db,
)

manage_db()

from widgets.TabText import TabText
from loadpage import LoadPage

from pages.pages import (
    EntertainmentPage,
    LearningPage,
    EducationPage,
    ExcelPage
)
# from widgets.CustomNavigation import CustomNavigation

# from core.ScheduleTable.schedule_table import ScheduleDataTable

from forms import (
    PlaceForm,
    StudioForm,
    ExhibitForm,
    TeacherForm,
)

from library.model_form.filters import ValueFieldFilter
import locale

locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))
locale.setlocale(
    category=locale.LC_ALL,
    locale="Russian"
)

place_form = PlaceForm()
teacher_form = TeacherForm()
studio_form = StudioForm()
exhibit_form = ExhibitForm()


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
    PlaceDataTable, place_dt = place_form.DataTable()

    page.datatables.append(place_dt)
    
    # ---------------PlaceData---------------
    TeacherDataTable, teach_dt = teacher_form.DataTable()

    page.datatables.append(teach_dt)

    # ---------------PlaceData---------------
    StudioDataTable, studio_dt = studio_form.DataTable()

    page.datatables.append(studio_dt)

    # ---------------PlaceData---------------
    ExhibitDataTable, exhibit_dt = exhibit_form.DataTable()

    page.datatables.append(exhibit_dt)

    

    


    t = Tabs(
        selected_index=0,
        animation_duration=50,
        overlay_color=colors.BLUE_100,
        tabs=[
            Tab(
                tab_content=TabText("Развлекательная деятельность"),
                content=Container(
                    content=LearningPage(
                        PlaceDataTable,
                    )
                ),
            ),
            Tab(
                tab_content=TabText("Культурно-просветительская деятельность"),
                content=Container(
                    content=EducationPage(
                        ExhibitDataTable,
                    ),
                ),
            ),
            Tab(
                tab_content=TabText("Образовательная деятельность"),
                content=Container(
                    content=EntertainmentPage(
                        StudioDataTable,
                        TeacherDataTable
                    )
                ),
            ),
            Tab(
                tab_content=TabText("Загрузка"),
                content=Container(
                    content=ExcelPage()
                ),
            )

        ],
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
