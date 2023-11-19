import flet as ft
from typing import Iterable


class FieldValueFilter:
    def __init__(self, field, value):
        self.field = field
        self.value = value

    def filter(self, queryset: Iterable, filter_widget: ft.Control = None):
        print(queryset, self.field, self.value)
        print(queryset.where(self.field==self.value))
        return queryset.where(self.field==self.value)