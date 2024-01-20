from typing import Iterable
import flet as ft
from types import FunctionType
from library.core.widgets.filters import FilterFieldWidget, FilterTableWidget


# todo what a hell.....
# todo provide form in filter func

class LiteWidgetFilter:
    def __init__(self, widget: FilterFieldWidget, filter_: FunctionType):
        self.widget = widget
        self.__filter = filter_

    def filter(self, queryset):
        return self.__filter(queryset=queryset, widget=self.widget)


class FieldFilter:
    _widget: FilterFieldWidget = ...

    def __init__(self, field):
        self.field = field

    def lite_widget_filter(self, form) -> ft.Control:
        return LiteWidgetFilter(
            self._widget(field=self.field, form=form),
            self.filter
        )

    def filter(
        self,
        queryset: Iterable,
        widget: FilterFieldWidget | None = None,
    ):
        ...


class TableFilter:
    _widget: FilterTableWidget = ...

    def lite_widget_filter(self, form) -> ft.Control:
        return LiteWidgetFilter(
            self._widget(form=form),
            self.filter
        )

    def filter(
        self,
        queryset: Iterable,
        widget: FilterTableWidget | None = None
    ):
        ...
