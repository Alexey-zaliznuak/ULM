import inspect
from functools import cached_property
from typing import Callable, Iterable

import peewee
from flet import Control, DataColumn, Text

from library.core.validators import LengthValidator
from library.core.widgets.data_table import (
    UIModelFormDataTable,
    UIModelFormDataTableColumn
)

from .actions import DataTableAction, ObjectAction
from .meta import UIModelFormMetaClass
from .ui_fields import BooleanField, CharField
from .ui_fields import Field as UIField
from .ui_fields import IntegerField


class UIModelForm(metaclass=UIModelFormMetaClass):
    # TODO classmethods

    ModelField = peewee.Field
    auto_fields: list[ModelField] = [peewee.AutoField]
    form_fields_mapping: dict[ModelField, UIField] = {
        peewee.AutoField: IntegerField,
        peewee.BooleanField: BooleanField,
        peewee.CharField: CharField,
        peewee.IntegerField: IntegerField,
    }
    # db_attr_name: ui_attr_name
    fields_attrs_mapping: dict[str, str] = {
        'null': 'allow_null',
        'default': 'default',
        'help_text': 'help_text',
        'column_name': 'label',
        'choices': 'choices',
    }

    # TODO Filter Widget
    # choose displaying fields

    def DataTable(
        self,
        *args,
        queryset: Callable = None,
        table_actions: list[DataTableAction] = [],
        objects_actions: list[ObjectAction] = [],
        **kwargs,
    ) -> UIModelFormDataTable:
        queryset = self.get_queryset(queryset)
        fields = self._get_fields(write_only=False)

        table_actions = getattr(
            self.Meta, 'table_actions', table_actions
        )
        objects_actions = getattr(
            self.Meta, 'objects_actions', objects_actions
        )

        objects_actions_column_name = getattr(
            self.Meta, 'actions_column_name', "Actions"
        )

        columns = [
            UIModelFormDataTableColumn(field_name, field)
            for field_name, field in fields.items()
        ]

        return UIModelFormDataTable(
            columns=columns,
            queryset=queryset,
            fields=fields.values(),
            table_actions=table_actions,
            objects_actions=objects_actions,
            action_column=DataColumn(Text(objects_actions_column_name)),
            *args, **kwargs,
        )

    def EditWindow(self, pk) -> Control:
        pass

    def _get_fields(
        self,
        read_only: bool = True,
        write_only: bool = True
    ) -> dict[str, UIField]:

        fields = {}

        assert hasattr(self.Meta, 'fields'), (
            'Meta class must have list of fields.'
        )

        for field_name in self.Meta.fields:
            field = self._ui_fields[field_name]

            if not read_only and getattr(field, 'read_only', False):
                continue
            if not write_only and getattr(field, 'write_only', False):
                continue

            fields[field_name] = field

        return fields

    def _build_attrs(
        self,
        model_field: ModelField,
        ui_field: UIField,
        field_name: str,
    ) -> dict[str]:

        attrs = {}
        db_field_attrs = inspect.getfullargspec(model_field.__init__).args
        ui_field_attrs = inspect.getfullargspec(ui_field.__init__).args

        for db_attr_name in db_field_attrs:
            ui_attr_name = self.fields_attrs_mapping.get(db_attr_name)

            if ui_attr_name and ui_attr_name in ui_field_attrs:
                attrs[ui_attr_name] = getattr(model_field, db_attr_name)

        if 'source' not in attrs.keys():
            attrs['source'] = field_name

        max_length = getattr(model_field, 'max_length', None)
        min_length = getattr(model_field, 'min_length', None)

        if min_length or max_length:
            validators = attrs.get('validators', [])
            validators.append(LengthValidator(mn=min_length, mx=max_length))
            attrs['validators'] = validators

        if model_field.__class__ in self.auto_fields:
            attrs['read_only'] = True

        if field_name in getattr(self.Meta, 'read_only_fields', ()):
            attrs['read_only'] = True
        if field_name in getattr(self.Meta, 'write_only_fields', ()):
            attrs['write_only'] = True

        return attrs

    def get_queryset(self, q=None) -> Callable:
        # TODO filters widget
        # TODO filter_widget.get_queryset: Calable
        return q or self.Meta.model.select

    @cached_property
    def _ui_fields(self) -> dict[str, UIField]:
        ui_fields = {}

        for field_name in self.Meta.fields:
            # TODO ClassLookupDict
            field = getattr(self, field_name, None)
            if field:
                return field

            model_field = getattr(self.Meta.model, field_name)
            ui_field = self.form_fields_mapping[model_field.__class__]

            attrs = self._build_attrs(model_field, ui_field, field_name)
            ui_fields[field_name] = ui_field(**attrs)

        return ui_fields

    class Meta:
        model: peewee.Model = None
        fields: Iterable[str] = ()
        read_only_fields: Iterable[str] = ''
        write_only_fields: Iterable[str] = ''
        table_actions: list[DataTableAction] = []
        objects_actions: list[ObjectAction] = []
