import flet as ft
from datetime import time
def main(page: ft.Page):
    page.title = "AlertDialog examples"

    def change_time(e):
        date_button.text = time_picker.value
        print(f"Time picker changed, value (minute) is {time_picker.value.minute}")

    def dismissed(e):
        print(f"Time picker dismissed, value is {time_picker.value}")

    time_picker = ft.TimePicker(
        confirm_text="Готово",
        cancel_text="Отмена",
        error_invalid_text="Неправильно время",
        help_text="Выбери время",
        on_change=change_time,
        on_dismiss=dismissed,
        value=time(hour=1, minute=1)
    )

    page.overlay.append(time_picker)

    date_button = ft.ElevatedButton(
        'asd',
        icon=ft.icons.TIME_TO_LEAVE,
        on_click=lambda _: time_picker.pick_time(),
    )
    
    dlg = ft.AlertDialog(
        title=date_button, on_dismiss=lambda e: print("Dialog dismissed!")
    )

    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you really want to delete all those files?"),
        actions=[
            ft.TextButton("Yes", on_click=close_dlg),
            ft.TextButton("No", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    page.add(
        ft.ElevatedButton("Open dialog", on_click=open_dlg),
        ft.ElevatedButton("Open modal dialog", on_click=open_dlg_modal),
    )

ft.app(target=main)
