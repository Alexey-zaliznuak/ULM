import flet as ft

CELL_WIDTH = 60
FIRST_COLUMN_WIDTH = 100


class TimeLineTable(ft.UserControl):
    def __init__(
        self,
        matrix,
    ):
        super().__init__()
        self.matrix = matrix

    def make_rectangles(self, data):
        row = []
        for rect in data:
            row.append(
                ft.cv.Rect(
                    rect['start'], 
                    rect['floor'],
                    rect['end'], 
                    rect['height']
                )
            )
        return row      

    def make_rows(self):
        rows = []
        for row in self.matrix:
            rows.append(
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Text(row['name']),
                            width=FIRST_COLUMN_WIDTH,
                        ),
                        ft.Container(
                            content=ft.canvas.Canvas(
                                self.make_rectangles(row['data']),
                                width=float("inf"),
                                expand=True,
                            ),
                            height=40,
                            bgcolor=ft.colors.BLUE_400
                        ),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        return rows


    def build(self):
        return ft.ListView(
            [
                ft.Column([
                    ft.Row(
                        [
                            ft.Container(
                                content=ft.Text(f'Помещение'),
                                width=FIRST_COLUMN_WIDTH,
                                alignment=ft.alignment.center
                            ),
                            *[ft.Container(content=ft.Text(f'{hour:02}:00'), width=CELL_WIDTH) for hour in range(24)]
                        ],
                        vertical_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    ft.Column(self.make_rows())
                ])
            ],
            horizontal=True
        )