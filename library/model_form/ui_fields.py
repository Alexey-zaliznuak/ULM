import flet as ft

from flet import Control, Text, TextField, Checkbox, LabelPosition
from datetime import datetime
from types import FunctionType

from library.core.validators import URLValidator
from library.model_form.datepicker.datepicker import DatePicker
from library.model_form.datepicker.selection_type import SelectionType


class empty:
    """
    This class is used to represent no data being provided for a given input
    or output value.

    It is required because `None` may be a valid input or output value.
    """
    pass


class Field:
    """Base class for all field types."""

    default_validators = []
    default_empty_value = ''
    default_error_messages = {
        'required': 'This field is required.',
        'null': 'This field may not be null.'
    }
    numeric = False

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
            f'read_only - {read_only} and wrte_only - {write_only}'
        )
        assert not (read_only and required), (
            'Invalid combination of fields values: read_obly and required'
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
        self.style = {} if style is None else style
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

    def _display_form_widget(self, value) -> Control:
        return Text(value, size=15)

    def editing_widget(self, obj) -> Control:
        value = self._get_editing_default_value(obj)
        return TextField(value)

    def display_widget(self, obj) -> Control:
        value = self._get_display_value(obj)
        return self._display_form_widget(value)


class BooleanField(Field):
    def __init__(
        self,
        *,
        value: bool = False,
        tristate: bool = False,
        label_position: LabelPosition = LabelPosition.RIGHT,
        label: str = '',

    ):
        super().__init__()

        if self.page:
            self.page.update()

        self.value = value
        self.tristate = tristate
        self.label_position = label_position
        self.label = label

    def build(self):
        return Checkbox(
            value=self.value,
            tristate=self.tristate,
            disabled=True,
            label_position=self.label_position,
            label=self.label,
        )


class CharField(Field):
    ...  # hide_input_value,


class ChoseField(Field):
    ...


class DateField(Field):
    def __init__(
            self,
            hour_minute: bool = False,
            show_three_months: bool = False,
            hide_no_month: bool = False,
            datepicker_type: int = 0,
            value: str = None
    ):
        super().__init__()
        self.value = self._to_datetime(value)
        self.type = SelectionType.SINGLE.value
        self.datepicker = None
        self.holidays = [datetime(2023, 4, 25), datetime(
            2023, 5, 1), datetime(2023, 6, 2)]
        self.selected_locale = None
        self.datepicker_type = datepicker_type
        self.hour_minute = hour_minute
        self.show_three_months = show_three_months
        self.hide_no_month = hide_no_month

        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=Text("Date picker"),
            actions=[
                ft.TextButton("Cancel", on_click=self.cancel_dlg),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            actions_padding=5,
            content_padding=0
        )

        self.tf = TextField(
            value=self.value,
            label="Select Date",
            dense=True,
            hint_text="yyyy-mm-ddThh:mm:ss",
            width=260,
            height=40
        )
        self.cal_ico = ft.TextButton(
            icon=ft.icons.CALENDAR_MONTH,
            on_click=self.open_dlg_modal,
            height=40,
            width=40,
            right=0,
            style=ft.ButtonStyle(
                padding=ft.Padding(4, 0, 0, 0),
                shape={
                    ft.MaterialState.DEFAULT:
                    ft.RoundedRectangleBorder(radius=1),
                },
            )
        )

        self.st = ft.Stack(
            [
                self.tf,
                self.cal_ico,
            ]
        )

    def build(self):
        return self.st

    def confirm_dlg(self, e):
        if int(self.type) == SelectionType.SINGLE.value:
            self.value = self.datepicker.selected_data[0] if len(
                self.datepicker.selected_data) > 0 else None
        elif (
            int(self.type) == SelectionType.MULTIPLE.value
            and len(self.datepicker.selected_data) > 0
        ):
            self.from_to_text.value = "[" + ", ".join(
                [d.isoformat() for d in self.datepicker.selected_data]) + "]"
            self.from_to_text.visible = True
        elif (
            int(self.type) == SelectionType.RANGE.value
            and len(self.datepicker.selected_data) > 0
        ):
            self.from_to_text.value = (
                f"From: {self.datepicker.selected_data[0]} "
                f"To: {self.datepicker.selected_data[1]}"
            )
            self.from_to_text.visible = True

        self.dlg_modal.open = False
        self.update()
        self.page.update()

    def cancel_dlg(self, e):
        self.dlg_modal.open = False
        self.page.update()

    def open_dlg_modal(self, e):
        self.datepicker = DatePicker(
            hour_minute=self.hour_minute,  # Time
            show_three_months=self.show_three_months,  # 3 Months
            hide_prev_next_month_days=False,  # Not Month Days
            # Selected Date
            selected_date=[self.tf.value] if self.tf.value else None,
            selection_type=self.datepicker_type,  # 0-SINGLE 1-MULTIPLE 2-RANGE
            holidays=self.holidays,  # ?
            # disable_to=self._to_datetime(self.tf1.value),
            # disable_from=self._to_datetime(self.tf2.value),
            # locale=self.selected_locale,
        )
        self.page.dialog = self.dlg_modal
        self.dlg_modal.content = self.datepicker
        self.dlg_modal.open = True
        self.page.update()

    def _to_datetime(self, date_str=None):
        if date_str:
            print(date_str)
            return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
        else:
            return None

    def set_locale(self, e):
        self.selected_locale = self.dd.value if self.dd.value else None


class DateTimeField(Field):
    ...


class DecimalField(Field):
    ...


class DurationField(Field):
    ...  # from date time to date time


class EmailField(Field):
    def __init__(
        self,
        *,
        value: str = '',

    ):
        super().__init__()

        if self.page:
            self.page.update()

        self.value = value

    def build(self):
        self.text_field = ft.Text(
            value=self.value,
        )
        return self.text_field


class FloatField(Field):
    def __init__(
        self,
        *,
        value: float = '',
    ):
        super().__init__()

        if self.page:
            self.page.update()

        self.value = value

    def build(self):
        number = str(self.value).split('.')
        if len(number) < 2:
            number.append('00')
        print(number)

        self.dot = ft.TextSpan(
            text='.',
            style=ft.TextStyle(size=18),

        )
        self.text_float = ft.TextSpan(
            text=str(number[1]),
            style=ft.TextStyle(size=18),
        )
        self.text_int = ft.Text(
            value=str(number[0]),
            size=24,
            spans=[
                self.dot,
                (self.text_float if number[1]
                 else None),
            ]
        )

        return self.text_int


class IntegerField(Field):
    def __init__(
        self,
        *,
        value: int = '',
    ):
        super().__init__()

        if self.page:
            self.page.update()

        self.value = value

    def build(self):
        self.wrap_my_text = ft.Text(
            value=str(self.value),
            size=24
        )

        return self.wrap_my_text


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
