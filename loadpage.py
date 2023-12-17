from time import time
import flet as ft
from time import sleep
import random


load_quotes = [
    'Чудесный день',
    'Выгляните в окно',
    '☆*: .｡. o(≧▽≦)o .｡.:*☆',
    'Как дела?',
    'Отдохните пять минут',
    'Ты заработался, разомнись',
]


class LoadPage(ft.UserControl):
    def __init__(self):
        super().__init__()

        self.c1 = ft.Container(
            width=10,
            height=10,
            bgcolor="green",
            border_radius=50,
            scale=1,
            rotate=ft.transform.Rotate(0, alignment=ft.alignment.center),
            offset=ft.transform.Offset(0, 0),
            animate_offset=ft.animation.Animation(600, ft.AnimationCurve.EASE),
        )
        self.c2 = ft.Container(
            width=10,
            height=10,
            bgcolor="blue",
            border_radius=50,
            scale=1,
            rotate=ft.transform.Rotate(0, alignment=ft.alignment.center),
            offset=ft.transform.Offset(0, 0),
            animate_offset=ft.animation.Animation(600, ft.AnimationCurve.EASE),
        )
        self.c3 = ft.Container(
            width=10,
            height=10,
            bgcolor="red",
            border_radius=50,
            scale=1,
            rotate=ft.transform.Rotate(0, alignment=ft.alignment.center),
            offset=ft.transform.Offset(0, 0),
            animate_offset=ft.animation.Animation(600, ft.AnimationCurve.EASE),
        )
        self.c4 = ft.Container(
            width=10,
            height=10,
            bgcolor="yellow",
            border_radius=50,
            scale=1,
            rotate=ft.transform.Rotate(0, alignment=ft.alignment.center),
            offset=ft.transform.Offset(0, 0),
            animate_offset=ft.animation.Animation(600, ft.AnimationCurve.EASE),
        )
        t = ft.Text(random.choice(load_quotes), size=24)
        c = ft.Row([self.c1, self.c2, self.c3, self.c4], alignment='center')
        cont = ft.Container(
            content=ft.Column(
                [
                    c,
                    t
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=45
            )
        )
        one = ft.Row([
            ft.Icon(
                name=ft.icons.CIRCLE,
                color=ft.colors.CYAN_400,
                scale=10,
                offset=ft.transform.Offset(0, 9.5),
            ),
        ])
        three = ft.Row([
            ft.Icon(
                name=ft.icons.CIRCLE,
                color=ft.colors.CYAN_400,
                scale=6,
                offset=ft.transform.Offset(26, -6),
            ),
        ])
        self.column = ft.Column(
            height=450,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                one,
                cont,
                three
            ]
        )

    def animate_me(self):
        now = time()
        while time() - now < 2:
            self.c1.offset = ft.transform.Offset(1, 0)  # -2 0
            self.c2.offset = ft.transform.Offset(1, 1)  # 0 0
            self.c3.offset = ft.transform.Offset(1, 0)  # 2 0
            self.c4.offset = ft.transform.Offset(-3, -1)  # 0 0
            self.update()
            sleep(.6)

            self.c1.offset = ft.transform.Offset(3, -1)  # 0 0
            self.c2.offset = ft.transform.Offset(3, 0)  # 2 0
            self.c3.offset = ft.transform.Offset(-1, 1)  # 0 0
            self.c4.offset = ft.transform.Offset(-5, 0)  # -2 0
            self.update()
            sleep(.6)

            self.c1.offset = ft.transform.Offset(5, 0)  # 2 0
            self.c2.offset = ft.transform.Offset(1, -1)  # 0 0
            self.c3.offset = ft.transform.Offset(-3, 0)  # -2 0
            self.c4.offset = ft.transform.Offset(-3, 1)  # 0 0
            self.update()
            sleep(.6)

            self.c1.offset = ft.transform.Offset(3, 1)  # 0 0
            self.c2.offset = ft.transform.Offset(-1, 0)  # -2 0
            self.c3.offset = ft.transform.Offset(-1, -1)  # 0 0
            self.c4.offset = ft.transform.Offset(-1, 0)  # 2 0
            self.update()
            sleep(.6)

        return True

    def build(self):
        return ft.Container(
            content=ft.Column(
                scroll="adaptive",
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    self.column
                ]
            ),
        )
