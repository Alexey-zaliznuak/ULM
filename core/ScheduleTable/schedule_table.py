import flet as ft

from models import Club
from forms import ClubForm

from library.core.widgets.text import Text

DAYS = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']


class ScheduleFormatter():
    def __init__(
        self,
        clubs: list[Club],
    ):
        clubs = clubs

        rows = []

        for club in clubs:
            working_days = club.working_days.split(':')[1].split(';')
            row = []
            for day in DAYS:
                row.append(club if day in working_days else '')

            rows.append(
                {
                    'name': club.name,
                    'data': row
                }
            )
        self.rows = rows


class ScheduleTable(ft.DataTable):
    def __init__(self, data):
        super().__init__(
            # data_row_min_height=160,
            data_row_max_height=130,
            vertical_lines=ft.BorderSide(.1),
            columns=[
                ft.DataColumn(Text("")),
                ft.DataColumn(
                    ft.Container(
                        Text("Понедельник"),
                        alignment=ft.alignment.center
                    )
                ),
                ft.DataColumn(
                    ft.Container(
                        Text("Вторник"),
                        alignment=ft.alignment.center
                    )
                ),
                ft.DataColumn(
                    ft.Container(
                        Text("Среда"),
                        alignment=ft.alignment.center
                    )
                ),
                ft.DataColumn(
                    ft.Container(
                        Text("Четверг"),
                        alignment=ft.alignment.center
                    )
                ),
                ft.DataColumn(
                    ft.Container(
                        Text("Пятница"),
                        alignment=ft.alignment.center
                    )
                ),
                ft.DataColumn(
                    ft.Container(
                        Text("Суббота"),
                        alignment=ft.alignment.center
                    )
                ),
                ft.DataColumn(
                    ft.Container(
                        Text("Воскресение"),
                        alignment=ft.alignment.center
                    )
                ),
            ],
            rows=[
                ft.DataRow(
                    [
                        ft.DataCell(Text(row['name'])),
                        *[
                            ft.DataCell(Text('')) if not obj else (
                                self.get_cell_by_obj(obj)
                            ) for obj in row['data']
                        ]
                    ],
                ) for row in data
            ],
        )

    def get_cell_by_obj(self, obj):
        return ft.DataCell(
            ft.Container(
                ft.Column(
                    [
                        ClubForm.teacher.display(obj),
                        ClubForm.place.display(obj),
                        Text(
                            f"{obj.start_lesson_time.hour:02}:"
                            f"{obj.start_lesson_time.minute:02} — "
                            f"{obj.end_lesson_time.hour:02}:"
                            f"{obj.end_lesson_time.minute:02}"
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                width=125
            )
        )


class ScheduleDataTable(ft.Row):
    def __init__(self, clubs):
        self.clubs = clubs
        self.formatted_clubs = ScheduleFormatter(self.clubs()).rows
        super().__init__(
            [
                ScheduleTable(self.formatted_clubs)
            ],
            scroll=True
        )

    def update(self):
        self.formatted_clubs = ScheduleFormatter(self.clubs()).rows
        self.controls[0] = ScheduleTable(self.formatted_clubs)
        return super().update()
