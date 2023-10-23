from flet import Control, Text, TextField
from types import FunctionType

from library.core.validators import URLValidator
from library.core.widgets.fields import (
    BooleanViewer,
    PhoneViewer,
)
from library.core.widgets.fields.IntField import IntegerViewer


class empty:
    """
    This class is used to represent no data being provided for a given input
    or output value.

    It is required because `None` may be a valid input or output value.
    """
    pass


class Field:
    """Base class for all field types."""

    numeric = False

    default_validators = []
    # default_empty_value = '' TODO mb delete if useless
    default_error_messages = {
        'required': 'This field is required.',
        'null': 'This field may not be null.'
    }

    edit_widget: Control = TextField
    display_widget: Control = Text

    def __init__(
        self,
        source: str,
        read_only=False,
        write_only=False,
        required: bool = None,
        initial=None,
        default=empty,
        label: str = '',
        help_text: str = None,
        style=None,
        error_messages: dict = None,
        validators: list = [],
        allow_null=False,
    ):

        # If `required` is unset, then use `True` unless a default is provided.
        if required is None:
            required = default is empty and not read_only

        # Some combinations of keyword arguments do not make sense.
        assert not (read_only and write_only), (
            'Invalid combination of fields values: '
            f'read_only - {read_only} and write_only - {write_only}'
        )
        assert not (read_only and required), (
            'Invalid combination of fields values: read_only and required'
            f'read_only - {read_only} and required - {required}'
        )
        assert not (required and default is not empty), (
            'Invalid combination of fields values: required and default'
            f'required - {required} and default - {default}'
        )

        self.read_only = read_only
        self.write_only = write_only
        self.required = required
        self.default = default
        self.source = source
        self.initial = initial
        self.label = label or source
        self.help_text = help_text
        self.style = style or {}
        self.allow_null = allow_null
        self.validators = validators
        self.validators.extend(self.default_validators)

        self.field_name = None

        self.error_messages = error_messages

    def validate(self, value) -> list[str]:
        errors = []

        for validator in self.validators:
            errors.extend(validator(value))

        return errors

    def _get_db_value(self, obj):
        return getattr(obj, self.source)

    def _get_display_value(self, obj):
        return self._get_db_value(obj)

    def _get_editing_default_value(self, obj):
        return self._get_db_value(obj)

    def edit(self, obj=empty) -> Control:
        value = empty

        if obj is not empty:
            value = self._get_editing_default_value(obj)

        return self.edit_widget(value if not isinstance(value, empty) else '')

    def display(self, obj) -> Control:
        value = self._get_display_value(obj)
        return self.display_widget(value)


class BooleanField(Field):
    display_widget = BooleanViewer


class CharField(Field):
    ...  # hide_input_value,


class PhoneField(CharField):
    display_widget = PhoneViewer


class ChooseField(Field):  # ???? ValueValidator?
    ...


class DateField(Field):
    ...


class DateTimeField(Field):
    ...


class DecimalField(Field):  # not in priority
    ...


class DurationField(Field):  # ?????
    ...  # from date time to date time


class EmailField(Field):  # ?????
    ...


class FloatField(Field):
    ...


class IntegerField(Field):
    display_widget = IntegerViewer


class MultipleChoiceField(Field):
    ...


class RegexField(Field):
    ...


class TimeField(Field):
    ...


class URLField(Field):
    default_validators = [URLValidator]


class MethodField(Field):
    def __init__(self, method: FunctionType, *args, **kwargs):
        self.method: FunctionType = method

        assert kwargs.get('read_only') is not False, (
            'MethodField must be read_only'
        )

        super().__init__(*args, **kwargs)

    def _get_display_value(self, obj):
        return self.method(obj)

    def _get_db_value(self, obj):
        raise AttributeError(
            'MethodField doesn`t provide get db values functional.'
        )

    def get_editing_default_value(self, obj):
        raise AttributeError(
            'MethodField doesn`t provide object editing functional.'
        )

    def _editing_form_widget(self, value, action: str = None):
        raise AttributeError(
            'MethodField doesn`t provide object editing functional.'
        )


class RelatedField(Field):
    ...

    def displayed_value(self):
        raise AttributeError(
            'displayed value must be override in RelatedField'
        )


class StringRelatedField(RelatedField):
    def displayed_value(self):
        return str(self.related_object)


class ManyRelatedField(Field):
    ...
