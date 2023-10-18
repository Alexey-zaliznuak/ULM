import flet as ft
from ..datepicker.datepicker import DatePicker
from ..datepicker.selection_type import SelectionType
from datetime import datetime


class DateViewer(ft.Container):
    def __init__(
            self,
            width: ft.OptionalNumber = None,
            hour_minute: bool = False,
            show_three_months: bool = False,
            hide_no_month: bool = False,
            datepicker_type: int = 0,
            value: str = None
    ):
        super().__init__(
            content=self.st,
        )
        self.value = self._to_datetime(value)
        self.type = SelectionType.SINGLE.value
        self.datepicker = None
        self.width = width
        self.holidays = [
            datetime(2023, 4, 25),
            datetime(2023, 5, 1),
            datetime(2023, 6, 2)
        ]
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

        self.tf = ft.TextField(
            value=self.value,
            disabled=True,
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
            ))

        self.st = ft.Stack(
            [
                self.tf,
                self.cal_ico,
            ]
        )

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
