import flet as ft
from ..datepicker.datepicker import DatePicker
from ..datepicker.selection_type import SelectionType
from datetime import datetime, date
from .BaseViewer import Viewer
from .BaseInput import InputField


class DateTimeField(ft.UserControl):
    holidays = [
        datetime(2023, 4, 25),
        datetime(2023, 5, 1),
        datetime(2023, 6, 2),
    ]

    def __init__(
        self,
        value: str,
        width: ft.OptionalNumber = None,
        hour_minute: bool = False,
        show_three_months: bool = False,
        hide_no_month: bool = False,
        datepicker_type: int = 0,
    ):
        super().__init__()

        self.value = self._to_datetime(value)
        # print(self.value)
        self.type = SelectionType.SINGLE.value
        self.datepicker = None
        self.width = width
        self.selected_locale = None
        self.datepicker_type = datepicker_type
        self.hour_minute = hour_minute
        self.show_three_months = show_three_months
        self.hide_no_month = hide_no_month

        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Date picker"),
            actions=[
                ft.TextButton("Cancel", on_click=self.cancel_dlg),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            actions_padding=5,
            content_padding=0
        )

        self.tf = ft.Container(
                content=ft.Text(
                value=self.value.strftime("%Y-%m-%d"),
            ),
            width=120,
            height=50,
            alignment=ft.alignment.center_left,
        )
        

        self.cal_ico = ft.TextButton(
            icon=ft.icons.CALENDAR_MONTH,
            on_click=self.open_dlg_modal,
            height=50,
            width=40,
            right=0,
            style=ft.ButtonStyle(
                shape={
                    ft.MaterialState.DEFAULT:
                    ft.RoundedRectangleBorder(radius=1),
                },
            ))

        self.st = ft.Stack(
            [
                self.tf,
                self.cal_ico,
            ],
            width=120
        )

    def build(self):
        return ft.Container(
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
        self.page.dialog.open = False
        self.page.update()

    def open_dlg_modal(self, e):
        self.datepicker = DatePicker(
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
        if not (self.page.dialog and self.page.dialog.open):
            self.page.dialog = self.dlg_modal
            self.dlg_modal.content = self.datepicker
            self.dlg_modal.open = True
        self.page.update()
        self.update()

    def _to_datetime(self, dt=None):
        if not dt:
            return None

        if isinstance(dt, (datetime, date)):
            return dt

        return datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S")

    def set_locale(self, e):
        self.selected_locale = self.dd.value or None


class DateTimeViewer(DateTimeField, Viewer):
    pass


class DateTimePicker(DateTimeField, InputField):
    def __init__(
        self,
        value: datetime,
        hour_minute: bool = False,
        show_three_months: bool = False,
        hide_no_month: bool = False,
        datepicker_type: int = 0,
    ):
        super().__init__(value=value)

        self.value = self._to_datetime(value)
        self.datepicker_type = datepicker_type
        self.hour_minute = hour_minute
        self.show_three_months = show_three_months
        self.hide_no_month = hide_no_month

        self.dlg_modal.actions = [
            ft.TextButton("Cancel", on_click=self.cancel_dlg),
            ft.TextButton("Confirm", on_click=self.confirm_dlg),
        ]

        self.tf = ft.TextField(
            value=self.value,
            label="Select Date",
            dense=True,
            hint_text="yyyy-mm-ddThh:mm:ss",
            width=260,
            height=60
        )
        self.st = ft.Stack(
            [
                self.tf,
                self.cal_ico,
            ]
        )

    def build(self):
        # self.widget = ft.Container(
        #     content=self.st,
        # )
        # return self.widget

        self.datepicker = DatePicker(
            hour_minute=self.hour_minute,
            show_three_months=self.show_three_months,
            hide_prev_next_month_days=False,
            selected_date=[self.tf.value] if self.tf.value else None,
            selection_type=self.datepicker_type,
            holidays=self.holidays,
            # disable_to=self._to_datetime(self.tf1.value),
            # disable_from=self._to_datetime(self.tf2.value),
            # locale=self.selected_locale,
        )

        return self.datepicker

    @property
    def clear_value(self):
        return self.datepicker.selected_data[0]
