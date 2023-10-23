import flet as ft
import pyperclip3 as pc


class Копировальщик(ft.Container):
    def __init__(self, content):
        super().__init__(
            content=content,
            copy_to_clipboard=self.copy_to_clipboard
        )
        self.content = content

    def copy_to_clipboard(self, e):
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text("copy to clipboard!"),
            action="Alright!",
        )
        self.page.snack_bar.open = True
        self.page.update()

        pc.copy(self.content.copy_value())


class Viewer():
    @property
    def copy_value(self):
        return None
