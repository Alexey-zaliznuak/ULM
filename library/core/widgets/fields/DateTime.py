from flet import (
    MainAxisAlignment,
    ElevatedButton,
    ButtonStyle,
    UserControl,
    TextButton,
    Container,
    icons,
    OptionalNumber,
    AlertDialog,
    alignment,
    MaterialState,
    RoundedRectangleBorder,
    Stack,
    DatePicker as FtDatePicker,
    TimePicker as FtTimePicker
)

from library.core.widgets.text import Text

from ..datepicker.datepicker import DateWidget
from ..datepicker.selection_type import SelectionType
from datetime import datetime, date, time
from .Text import TextViewer
from .BaseViewer import Viewer
from .BaseInput import InputField


class DateTimeClass(UserControl):
    holidays = [
        datetime(2023, 4, 25),
        datetime(2023, 5, 1),
        datetime(2023, 6, 2),
    ]

    def __init__(
        self,
        value: str,
        width: OptionalNumber = None,
        hour_minute: bool = False,
        show_three_months: bool = False,
        hide_no_month: bool = False,
        datepicker_type: int = 0,
    ):
        super().__init__()

        self.value = self._to_datetime(value)
        self.type = SelectionType.SINGLE.value
        self.datepicker = None
        self.width = width
        self.selected_locale = None
        self.datepicker_type = datepicker_type
        self.hour_minute = hour_minute
        self.show_three_months = show_three_months
        self.hide_no_month = hide_no_month

        self.dlg_modal = AlertDialog(
            modal=True,
            title=Text("Календарь"),
            actions=[
                TextButton("Закрыть", on_click=self.cancel_dlg),
            ],
            actions_alignment=MainAxisAlignment.END,
            actions_padding=5,
            content_padding=0
        )

        if value is None:
            value = datetime.now()

        if not isinstance(value, str):
            if self.hour_minute:
                value = datetime.strftime(value, "%Y-%m-%d\n%H:%M")
            else:
                value = datetime.strftime(value, "%Y-%m-%d")

        self.tf = Container(
            content=Text(
                value=value,
            ),
            width=120,
            height=50,
            alignment=alignment.center_left,
        )

        self.cal_ico = TextButton(
            icon=icons.CALENDAR_MONTH,
            on_click=self.open_dlg_modal,
            height=50,
            width=40,
            right=0,
            style=ButtonStyle(
                shape={
                    MaterialState.DEFAULT:
                    RoundedRectangleBorder(radius=1),
                },
            ))

        self.st = Stack(
            [
                self.tf,
                self.cal_ico,
            ],
            width=120
        )

    def build(self):
        return Container(
            content=self.st,
        )

    def confirm_dlg(self, e):
        if int(self.type) == SelectionType.SINGLE.value:
            self.tf.value = self.datepicker.selected_data[0] if len(
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

    def cancel_dlg(self, e):
        self.dlg_modal.open = False
        self.dlg_modal.update()
        self.page.overlay.remove(self.dlg_modal)

    def open_dlg_modal(self, e):
        self.datepicker = DateWidget(
            hour_minute=self.hour_minute,
            show_three_months=self.show_three_months,
            hide_prev_next_month_days=False,
            selected_date=[self.value] if self.value else None,
            selection_type=self.datepicker_type,
            holidays=self.holidays,
            # disable_to=self._to_datetime(self.tf1.value),
            # disable_from=self._to_datetime(self.tf2.value),
            # locale=self.selected_locale,
        )
        self.dlg_modal.content = self.datepicker
        self.page.overlay.append(self.dlg_modal)
        self.dlg_modal.open = True

        self.page.update()

    def _to_datetime(self, dt):
        if isinstance(dt, (datetime, date)):
            return dt

        if not dt:
            if getattr(self, 'hour_minute', False):
                return datetime.now()
            else:
                return date.today()

        if getattr(self, 'hour_minute', False):
            return datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S")

        return datetime.strptime(dt, "%Y-%m-%d")

    def set_locale(self, e):
        self.selected_locale = self.dd.value or None


class DateViewer(DateTimeClass, Viewer):
    pass


class DateTimeViewer(DateViewer):
    defaults = {
        'hour_minute': True,
    }

    def __init__(self, *args, **kwargs):
        kwargs = kwargs | self.defaults
        super().__init__(*args, **kwargs)


class DatePicker(UserControl, InputField):
    def __init__(
        self,
        value: date,
        on_change=None
    ):
        super().__init__()

        self.value = value
        self.on_change = on_change
        self.date_picker = FtDatePicker(
            value=self.value,
            on_change=self.picker_change,
            open=True,
            on_dismiss=self.on_dismiss,
        )

    def build(self):
        self.date_button = ElevatedButton(
            text=self.value,
            icon=icons.CALENDAR_MONTH,
            on_click=self.pick_date,
        )

        return self.date_button

    def pick_date(self, e):
        self.page.overlay.append(self.date_picker)
        self.page.update()
        self.date_picker.pick_date()

    def picker_change(self, e):
        self.date_button.text = self.date_picker.value.date()
        self.update()
        if self.on_change: self.on_change()

    def on_dismiss(self, e):
        self.page.overlay.remove(self.date_picker)

    @property
    def clear_value(self):
        return self.date_picker.value.date()


class DateTimePicker(DateWidget, InputField):
    defaults = {
        'hour_minute': True,
    }

    def __init__(self, *args, **kwargs):
        kwargs = kwargs | self.defaults | {'selected_date': [args[0]]}
        super().__init__(**kwargs)
    
    @property
    def clear_value(self):
        return self.selected_data[0]
    


class TimePicker(ElevatedButton, InputField):
    def __init__(
        self,
        value: time
    ):
        value = value or time(hour=0, minute=0)
        self.time_picker = FtTimePicker(
            confirm_text="Готово",
            cancel_text="Отмена",
            error_invalid_text="Неправильное время",
            help_text="Выбери время",
            on_change=self.on_change,
            value=value,
            on_dismiss=self.on_dismiss
        )
        
        super().__init__(
            self.time_to_text(value),
            icon=icons.ACCESS_TIME,
            on_click=lambda _: self.pick_time(),
        )


    def pick_time(self):
        self.page.overlay.append(self.time_picker)
        self.page.update()
        self.time_picker.pick_time()

    def on_dismiss(self, e):
        self.page.overlay.remove(self.time_picker)

    def on_change(self, e):
        self.text = self.time_to_text(self.time_picker.value)
        self.update()

    def time_to_text(self, time):
        return f"{time.hour:02}:{time.minute:02}"
    
    @property
    def clear_value(self):
        return self.time_picker.value


class TimeViewer(TextViewer, Viewer):
    def __init__(self, value):
        value = str(value).split(':')
        value = f"{value[0]:02}:{value[1]:02}"

        super().__init__(value=value)
