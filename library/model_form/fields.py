from flet import Control
from types import FunctionType

from library.core.validators import URLValidator, PhoneValidator
from library.core.exceptions import ValidationError
from library.types import empty
from library.core.widgets.fields import (
    BooleanViewer,
    BooleanInput,
    ForeignKeyViewer,
    PhoneInput,
    PhoneViewer,
    TextViewer,
    TextEditor,
    IntegerInput,
)


class   Field:
    """Base class for all field types."""

    numeric = False

    default_validators = []
    # default_empty_value = '' TODO mb delete if useless
    default_error_messages = {
        'required': 'This field is required.',
        'null': 'This field may not be null.'
    }

    initial_empty_value = None
    edit_widget: Control = TextEditor
    display_widget: Control = TextViewer

    def __init__(
        self,
        source: str,
        read_only=False,
        write_only=False,
        required: bool = None,
        default=empty,
        label: str = '',
        help_text: str = None,
        style=None,
        error_messages: dict = None,
        validators: list = [],
        allow_null=False,
    ):
        # TODO mb model in mapping in future
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
        self.source = source
        self.label = label or source
        self.help_text = help_text
        self.style = style or {}
        self.allow_null = allow_null
        self.validators = validators.copy()
        self.validators.extend(self.default_validators)

        self.initial = self.initial_empty_value
        if default is not empty:
            self.initial = default

        self.field_name = None

        self.error_messages = error_messages

    def validate(self, value) -> list[str]:
        errors = []

        if not value and self.required:
            errors.append('Required value.')

        for validator in self.validators:
            try:
                validator(value)
            except ValidationError as e:
                errors.append(e)

        return errors

    def clear(self, value):
        return value

    def _get_db_value(self, obj):
        return getattr(obj, self.source)

    def _get_display_value(self, obj):
        return self._get_db_value(obj)

    def _get_editing_default_value(self, obj):
        return self._get_db_value(obj)

    def edit(self, *, value=empty, obj=empty) -> Control:
        value = self._get_edit_value(value=value, obj=obj)
        return self.edit_widget(value)

    def display(self, obj) -> Control:
        value = self._get_display_value(obj)
        return self.display_widget(value)

    def _get_edit_value(self, *, value, obj):
        assert not (value is not empty and obj is not empty), (
            "Only one of 'value' and 'obj' can be specified."
        )

        if obj is not empty:
            value = self._get_editing_default_value(obj)

        elif value is empty:
            value = self.initial_empty_value

        return value


class BooleanField(Field):
    display_widget = BooleanViewer
    edit_widget = BooleanInput


class CharField(Field):
    def edit(self, *, value=empty, obj=empty) -> Control:
        value = self._get_edit_value(value=value, obj=obj)
        return self.edit_widget(value=value)


class PhoneField(Field):
    initial_empty_value = ''
    display_widget = PhoneViewer
    edit_widget = PhoneInput
    default_validators = [PhoneValidator()]


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
    initial_empty_value = 0
    edit_widget = IntegerInput


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
    # TODO overriden decorator
    def _get_display_value(self, obj):
        raise AttributeError(
            'displayed value must be override in RelatedField'
        )

    def display(self, obj) -> Control:
        raise AttributeError(
            'displayed value must be override in RelatedField'
        )


class ForeignKeyField(RelatedField):
    display_widget = ForeignKeyViewer

    def __init__(
        self,
        source: str,
        foreign_form,  # form for getting fields for display object
        read_only=False,
        write_only=False,
        required: bool = None,
        default=empty,
        label: str = '',
        help_text: str = None,
        style=None,
        error_messages: dict = None,
        validators: list = [],
        allow_null=False,
        # special
    ):
        self.fields = foreign_form()._form_fields(write_only=False).values()

        super().__init__(
            source=source,
            read_only=read_only,
            write_only=write_only,
            required=required,
            default=default,
            label=label,
            help_text=help_text,
            style=style,
            error_messages=error_messages,
            validators=validators,
            allow_null=allow_null
        )

    def _get_display_value(self, obj):
        return str(self._get_db_value(obj))

    def display(self, obj) -> Control:
        # TODO mb figna
        label = self._get_display_value(obj)
        return self.display_widget(
            obj=self._get_db_value(obj), fields=self.fields, label=label
        )


class StringRelatedField(RelatedField):
    def displayed_value(self):
        return str(self.related_object)


class ManyRelatedField(Field):
    ...
