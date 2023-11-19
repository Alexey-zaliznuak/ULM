import flet as ft
from .filter import Filter


class FilterWidget:
    filter_: Filter = ...

    def __init__(self, *args, **kwargs):
        pass

    def widget(self) -> ft.Control:
        self.widget_ = self.filter_()
        return self.widget_

    def filter(self, queryset):
        queryset = self.filter_.filter(queryset, filter_widget=self.widget_)
