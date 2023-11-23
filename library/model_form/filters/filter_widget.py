import flet as ft
from .filter import Filter
from library.core.widgets.filters import FilterField


class FilterWidget:
    filter_class_: Filter = ...
    widget_: FilterField = ...

    def __init__(self, *args, **kwargs):
        pass

    def widget(self, form, datatable) -> ft.Control:
        self.filter_widget = self.widget_(form, datatable)
        return self.filter_widget

    def filter(self, queryset):
        queryset = self.filter_class_.filter(
            queryset, filter_widget=self.filter_widget
        )
