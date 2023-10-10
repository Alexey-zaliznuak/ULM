from typing import Callable

from flet import FloatingActionButton


class ActionButton(FloatingActionButton):
    defaults = dict(
        width=80,
    )

    def __init__(
        self,
        on_click: Callable,
        *args,
        **kwargs
    ):
        kwargs = self.defaults | kwargs
        super().__init__(on_click=on_click, *args, **kwargs)
