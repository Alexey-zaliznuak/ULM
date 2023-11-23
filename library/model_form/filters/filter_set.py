import flet as ft

from typing import Sequence
from functools import cached_property
from .filter import Filter
from .filter_widget import FilterWidget


class FilterSet:
    def widget(self) -> ft.Control:
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text('Фильтрация'),
                    *[f.widget() for f in self.filters]
                ]
            )
        )

    def filter(self, queryset):
        for f in self.Meta.default_filters:
            queryset = f.filter(queryset)

        for f in self.filters:
            queryset = f.filter(queryset)

        return queryset

    @cached_property
    def filters(self) -> list[FilterWidget]:
        return [getattr(self, f_name) for f_name in self.Meta.filters]

    class Meta:
        filters: Sequence[str] = ()
        default_filters: Sequence[Filter] = ()
