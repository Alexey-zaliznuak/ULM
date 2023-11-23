import inspect
from functools import cached_property
from typing import Callable, Sequence, Optional

import peewee
from flet import Control, DataColumn, Text, Column, Row, ListView, ScrollMode

from library.core.validators import LengthValidator
from library.utils import Singleton
from library.core.exceptions import ValidationError
from library.core.widgets.data_table import (
    UIModelFormDataTable,
    UIModelFormDataTableColumn
)

from .actions import DataTableAction, ObjectAction
from .fields import (
    BooleanField,
    CharField,
    ForeignKeyField,
    FloatField,
    DateTimeField
)
from .fields import Field as UIField
from .fields import IntegerField
from .filters import FilterSet, Filter


class UIModelForm(metaclass=Singleton):
    # TODO classMethods

    ModelField = peewee.Field
    auto_fields: list[ModelField] = [peewee.AutoField]
    form_fields_mapping: dict[ModelField, UIField] = {
        peewee.AutoField: IntegerField,
        peewee.BooleanField: BooleanField,
        peewee.CharField: CharField,
        peewee.TextField: CharField,
        peewee.DateTimeField: DateTimeField,
        peewee.IntegerField: IntegerField,
        peewee.ForeignKeyField: ForeignKeyField,
        peewee.FloatField: FloatField
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
        queryset: Callable = None,
        table_actions: list[DataTableAction] = [],
        objects_actions: list[ObjectAction] = [],
        filterset: FilterSet = None,
        default_filters: Sequence[Filter] = (),
        **kwargs,
    ) -> UIModelFormDataTable:
        # todo in class

        queryset = self.get_queryset(queryset)
        fields = self._form_fields(write_only=False)
        filterset = getattr(self.Meta, 'filterset', filterset)
        default_filters = getattr(
            self.Meta, 'default_filters', default_filters
        )

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

        data_table = UIModelFormDataTable(
            action_column=DataColumn(Text(objects_actions_column_name)),
            columns=columns,
            fields=fields.values(),
            filterset=filterset,
            default_filters=default_filters,
            form=self,
            model=self.Meta.model,
            objects_actions=objects_actions,
            queryset=queryset,
            table_actions=table_actions,
            get_row_params=self.get_row_params,
            **kwargs,
        )
        data_table_actions_row = Row(
            [
                action()(datatable=data_table, form=self)
                for action in table_actions
            ],
        )

        return Column(
            [
                data_table_actions_row,
                Row([data_table],scroll=ScrollMode.AUTO), 
            ]
        ), data_table

    def EditWindow(self, pk) -> Control:
        pass

    def clear(self, obj: dict) -> dict:
        new_obj = {}

        for field_name, field in self._form_fields(read_only=False).items():
            new_obj[field_name] = field.clear(obj[field_name])

            if hasattr(self, f'clear_{field_name}'):
                new_obj[field_name] = getattr(self, f'clear_{field_name}')(obj)

        return new_obj

    def create(self, obj: dict) -> tuple[bool, str, dict[str, list[str]]]:
        obj = self.clear(obj)
        created = False

        object_error, fields_errors = self._run_validators(obj, create=True)

        if not (object_error or fields_errors):
            self.Meta.model.create(**obj)
            created = True

        return created, object_error, fields_errors

    def update(
        self, obj: peewee.Model, update: dict
    ) -> tuple[bool, str, dict[str, list[str]]]:
        update = self.clear(update)
        success = False

        object_error, fields_errors = self._run_validators(
            update, create=False
        )

        if not (object_error or fields_errors):
            self.Meta.model.update(
                **update
            ).where(
                self.Meta.model.id == obj.id
            ).execute()
            success = True

        return success, object_error, fields_errors

    def validate(self, obj: dict, create: bool = False) -> Optional[str]:
        ...

    def get_queryset(self, q=None) -> Callable:
        # TODO filters widget
        # TODO filter_widget.get_queryset: Callable
        return q or self.Meta.model.select

    def get_row_params(self, obj, form, datatable) -> dict:
        return {}

    def _run_validators(
        self, obj: dict, create: bool = False
    ) -> tuple[str, dict[str, list[str]]]:
        fields_errors = {}

        for field_name, field in self._form_fields(read_only=False).items():
            e = field.validate(obj[field_name])
            if e:
                fields_errors[field_name] = e

        object_error = self.validate(obj, create=create)

        if not object_error:
            try:
                if hasattr(self.Meta.model, 'validate'):
                    self.Meta.model(**obj).validate()
            except ValidationError as e:
                object_error = str(e)

        return object_error, fields_errors

    def _form_fields(
        self,
        read_only: bool = True,
        write_only: bool = True
    ) -> dict[str, UIField]:

        fields = {}

        assert hasattr(self.Meta, 'fields'), (
            'Meta class must have a list of fields.'
        )

        for field_name in self.Meta.fields:
            field = self._all_form_fields[field_name]

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

    @cached_property
    def _all_form_fields(self) -> dict[str, UIField]:
        ui_fields = {}

        for field_name in self.Meta.fields:
            # TODO ClassLookupDict
            field = getattr(self, field_name, None)
            if field:
                ui_fields[field_name] = field
                continue

            model_field = getattr(self.Meta.model, field_name)
            ui_field = self.form_fields_mapping[model_field.__class__]

            attrs = self._build_attrs(model_field, ui_field, field_name)
            ui_fields[field_name] = ui_field(**attrs)

        return ui_fields

    class Meta:
        model: peewee.Model = None
        fields: Sequence[str] = ()
        read_only_fields: Sequence[str] = ''
        write_only_fields: Sequence[str] = ''
        table_actions: list[DataTableAction] = []
        objects_actions: list[ObjectAction] = []
        filterset: FilterSet = None
        default_filters: Sequence[Filter] = ()
