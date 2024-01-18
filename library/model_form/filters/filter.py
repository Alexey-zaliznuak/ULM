from typing import Iterable
import flet as ft
from types import FunctionType
from library.core.widgets.filters import FilterFieldWidget


# todo what a hell.....
class FilterWidget:
    def __init__(self, widget: FilterFieldWidget, filter_: FunctionType):
        self.widget = widget
        self.__filter = filter_

    def filter(self, queryset):
        return self.__filter(widget=self.widget, queryset=queryset)


class Filter:
    _widget: FilterFieldWidget = ...

    def __init__(self, field):
        self.field = field

    def widget(self, form) -> ft.Control:
        return FilterWidget(
            self._widget(field=self.field, form=form),
            self.filter
        )

    def filter(
        self,
        queryset: Iterable,
        widget: FilterFieldWidget | None = None
    ):
        ...
