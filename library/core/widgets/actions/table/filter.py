from flet import icons, AlertDialog, Container, Column, ElevatedButton, MainAxisAlignment, ListView, margin
from library.core.widgets.actions import ActionButton
from library.core.widgets.text import Text, TitleText


class FilterActionButton(ActionButton):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args, **kwargs,
            icon=icons.FILTER_ALT_OUTLINED,
        )


class FilterActionDialog(AlertDialog):
    def __init__(self, datatable):
        self.datatable = datatable

        super().__init__(
            content=Container(
                content=ListView(
                    [
                        TitleText('Фильтрация'),
                        datatable.filterset.widget,
                        Container(
                            content=ElevatedButton(
                            "Сохранить",
                            on_click=self._close_and_update,
                        ),
                        margin=margin.only(top=20)
                        ),
                        
                    ],
                    width=600,
                )
            ),
            modal=True,
            actions_alignment=MainAxisAlignment.END,
        )

    def _close_and_update(self, e=None):
        self.datatable.update_rows()
        self.open = False
        self.page.update()
        # self.page.overlay.remove(self)
