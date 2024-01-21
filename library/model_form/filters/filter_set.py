import flet as ft

from typing import Sequence
from functools import cached_property
from .filter import FieldFilter, TableFilter, LiteWidgetFilter


# todo group field
class FilterSet:
    def __init__(self, form, datatable):
        self.form = form
        self.datatable = datatable
        self.filters_widgets: list[ft.Control] = []

    @cached_property
    def widget(self) -> ft.Control:
        return ft.Container(
            content=ft.Column(
                [
                    f.widget
                    for f in self.filters
                ]
            ),
            width=500
        )

    def filter(self, queryset):
        for f in getattr(self.Meta, 'default_filters', ()):
            queryset = f.filter(queryset)

        for f in self.filters:
            queryset = f.filter(queryset)

        return queryset

    @cached_property
    def filters(self) -> list[LiteWidgetFilter]:
        return [
            getattr(self, f_name).lite_widget_filter(self.form)
            for f_name in self.Meta.filters
        ]

    class Meta:
        filters: Sequence[str] = ()
        default_filters: Sequence[FieldFilter | TableFilter] = ()
