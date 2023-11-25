import flet as ft
from .filter import Filter
from library.core.widgets.filters import FilterField


class FilterWidget:
    filter_class_: Filter = ...
    widget_: FilterField = ...

    def __init__(self, *args, **kwargs):
        self.filter_widget: ft.Control = None

    def widget(self, form, datatable) -> ft.Control:
        self.filter_widget = self.widget_(form, datatable)
        return self.filter_widget

    def filter(self, queryset):
        if self.filter_widget:
            queryset = self.filter_class_.filter(
                queryset, filter_widget=self.filter_widget
            )

        return queryset
