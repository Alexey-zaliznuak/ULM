from flet import (
    ElevatedButton,
    UserControl,
    icons,
    DatePicker as FtDatePicker,
    TimePicker as FtTimePicker,
    DatePickerEntryMode,
    Row,
)
from datetime import datetime, date, time
from .Text import TextViewer
from .BaseViewer import Viewer
from .BaseInput import InputField


class DateViewer(UserControl, Viewer):
    def __init__(self, value):
        self.value = value
        
        self.date_picker = FtDatePicker(
            value=self.value,
            disabled=True,
            on_dismiss=self.on_dismiss,
            date_picker_entry_mode=DatePickerEntryMode.CALENDAR_ONLY,
        )
        super().__init__()
    
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

    def on_dismiss(self, e):
        self.page.overlay.remove(self.date_picker)

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
        if self.on_change: self.on_change(self.date_picker.value.date())

    def on_dismiss(self, e):
        self.page.overlay.remove(self.date_picker)

    @property
    def clear_value(self):
        return self.date_picker.value.date()


class DateTimeViewer(UserControl, Viewer):
    def __init__(self, value):
        self.value = value

        self.text = self.value.strftime("%d.%m.%y %H:%M")

        self.value = value
        self.date_picker = FtDatePicker(
            value=self.value,
            disabled=True,
            on_dismiss=self.on_dismiss,
            date_picker_entry_mode=DatePickerEntryMode.CALENDAR_ONLY,
        )
        super().__init__()

    def pick_date(self, e):
        self.page.overlay.append(self.date_picker)
        self.page.update()
        self.date_picker.pick_date()

    def on_dismiss(self, e):
        self.page.overlay.remove(self.date_picker)

    def build(self):
        self.date_button = ElevatedButton(
            text=self.text,
            icon=icons.CALENDAR_MONTH,
            on_click=self.pick_date,
        )

        return self.date_button


class DateTimePicker(UserControl, Viewer):
    def __init__(self, value):
        self.value = value or datetime.now()

        self.time_text = self.value.strftime("%H:%M")
        self.date_text = self.value.strftime("%Y-%m-%d")

        self.time_picker = FtTimePicker(
            confirm_text="Готово",
            cancel_text="Отмена",
            error_invalid_text="Неправильное время",
            help_text="Выбери время",
            on_change=self.on_change_time,
            value=value,
            on_dismiss=self.on_dismiss_time
        )

        self.date_picker = FtDatePicker(
            value=self.value,
            on_change=self.on_change_date,
            open=True,
            on_dismiss=self.on_dismiss_date,
        )

        super().__init__()

    def pick_date(self, e):
        self.page.overlay.append(self.date_picker)
        self.page.update()
        self.date_picker.pick_date()

    def on_change_date(self, e):
        self.value = self.value.replace(year=self.date_picker.value.year, month=self.date_picker.value.month, day=self.date_picker.value.day)
        self.date_text = self.date_picker.value.strftime("%Y-%m-%d")
        self.date_button.text = self.date_text
        self.update()

    def on_dismiss_date(self, e):
        self.page.overlay.remove(self.date_picker)

    def pick_time(self, e):
        self.page.overlay.append(self.time_picker)
        self.page.update()
        self.time_picker.pick_time()

    def on_dismiss_time(self, e):
        self.page.overlay.remove(self.time_picker)

    def on_change_time(self, e):
        self.value = self.value.replace(hour = self.time_picker.value.hour,  minute =self.time_picker.value.minute )
        self.time_text = self.time_picker.value.strftime("%H:%M")
        self.time_button.text = self.time_text
        self.update()

    def build(self):
        self.date_button = ElevatedButton(
            text=self.date_text,
            icon=icons.CALENDAR_MONTH,
            on_click=self.pick_date,
        )
        self.time_button = ElevatedButton(
            self.time_text,
            icon=icons.ACCESS_TIME,
            on_click=self.pick_time,
        )
        return Row([
            self.date_button,
            self.time_button
        ])
    
    @property
    def clear_value(self):
        return self.value
    

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
            on_click=self.pick_time,
        )


    def pick_time(self, e):
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
        value = f"{value[0]}:{value[1]}"

        super().__init__(value=value)
