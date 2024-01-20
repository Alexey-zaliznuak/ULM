from time import time
from flet import (
    MainAxisAlignment,
    CrossAxisAlignment,
    AnimationCurve,
    TextOverflow,
    TextThemeStyle,
    UserControl,    
    alignment,  
    transform,  
    Container,
    animation,  
    Column,
    colors,
    icons,
    Icon,
    Row,
)
from flet_core.control import OptionalNumber
from flet_core.ref import Ref
from flet_core.text_span import TextSpan
from flet_core.types import AnimationValue, FontWeight, OffsetValue, ResponsiveNumber, RotateValue, ScaleValue, TextAlign
from library.core.widgets.settings import PARAGRAPH_TEXT_SIZE

from library.core.widgets.text import Text as DefaultText

from time import sleep
import random



load_quotes = [
    '',
]


class Text(DefaultText):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class LoadPage(UserControl):
    def __init__(self):
        super().__init__()

        self.c1 = Container(
            width=10,
            height=10,
            bgcolor="green",
            border_radius=50,
            scale=1,
            rotate=transform.Rotate(0, alignment=alignment.center),
            offset=transform.Offset(0, 0),
            animate_offset=animation.Animation(600, AnimationCurve.EASE),
        )
        self.c2 = Container(
            width=10,
            height=10,
            bgcolor="blue",
            border_radius=50,
            scale=1,
            rotate=transform.Rotate(0, alignment=alignment.center),
            offset=transform.Offset(0, 0),
            animate_offset=animation.Animation(600, AnimationCurve.EASE),
        )
        self.c3 = Container(
            width=10,
            height=10,
            bgcolor="red",
            border_radius=50,
            scale=1,
            rotate=transform.Rotate(0, alignment=alignment.center),
            offset=transform.Offset(0, 0),
            animate_offset=animation.Animation(600, AnimationCurve.EASE),
        )
        self.c4 = Container(
            width=10,
            height=10,
            bgcolor="yellow",
            border_radius=50,
            scale=1,
            rotate=transform.Rotate(0, alignment=alignment.center),
            offset=transform.Offset(0, 0),
            animate_offset=animation.Animation(600, AnimationCurve.EASE),
        )
        t = Text(random.choice(load_quotes), size=24)
        c = Row([self.c1, self.c2, self.c3, self.c4], alignment='center')
        cont = Container(
            content=Column(
                [
                    c,
                    t
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=45
            )
        )
        one = Row([
            Icon(
                name=icons.CIRCLE,
                color=colors.CYAN_400,
                scale=10,
                offset=transform.Offset(0, 9.5),
            ),
        ])
        three = Row([
            Icon(
                name=icons.CIRCLE,
                color=colors.CYAN_400,
                scale=6,
                offset=transform.Offset(26, -6),
            ),
        ])
        self.column = Column(
            height=450,
            alignment=MainAxisAlignment.CENTER,
            controls=[
                one,
                cont,
                three
            ]
        )

    def animate_me(self):
        now = time()
        while time() - now < 2:
            self.c1.offset = transform.Offset(1, 0)  # -2 0
            self.c2.offset = transform.Offset(1, 1)  # 0 0
            self.c3.offset = transform.Offset(1, 0)  # 2 0
            self.c4.offset = transform.Offset(-3, -1)  # 0 0
            self.update()
            sleep(.6)

            self.c1.offset = transform.Offset(3, -1)  # 0 0
            self.c2.offset = transform.Offset(3, 0)  # 2 0
            self.c3.offset = transform.Offset(-1, 1)  # 0 0
            self.c4.offset = transform.Offset(-5, 0)  # -2 0
            self.update()
            sleep(.6)

            self.c1.offset = transform.Offset(5, 0)  # 2 0
            self.c2.offset = transform.Offset(1, -1)  # 0 0
            self.c3.offset = transform.Offset(-3, 0)  # -2 0
            self.c4.offset = transform.Offset(-3, 1)  # 0 0
            self.update()
            sleep(.6)

            self.c1.offset = transform.Offset(3, 1)  # 0 0
            self.c2.offset = transform.Offset(-1, 0)  # -2 0
            self.c3.offset = transform.Offset(-1, -1)  # 0 0
            self.c4.offset = transform.Offset(-1, 0)  # 2 0
            self.update()
            sleep(.6)

        return True

    def build(self):
        return Container(
            content=Column(
                scroll="adaptive",
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    self.column
                ]
            ),
        )
