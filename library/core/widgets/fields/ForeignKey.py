from flet import (
    Container,
    dropdown,
    Dropdown,
    TextAlign,
    TextButton,
    TextOverflow,
)

from library.core.widgets.text import Text
from .BaseInput import InputField
from .BaseViewer import Viewer
from library.core.widgets.actions.objects.detail import (
    DetailObjectActionDialog
)



class ForeignKeyViewer(Container, Viewer):
    has_value_for_copy = False

    def __init__(
        self,
        obj,
        fields,
        label: str,
    ):
        self.obj = obj
        self.fields = fields

        if len(label) > 25:
            label = label[:22] + "..."

        super().__init__(
            content=TextButton(
                content=Text(
                    label,
                    max_lines=2,
                    overflow=TextOverflow.ELLIPSIS,
                    text_align=TextAlign.CENTER,
                    size=None,
                    selectable=False
                ),
                on_click=self.open_detail_modal
            ),
        )

    def open_detail_modal(self, e=None):
        if not getattr(self.page.dialog, 'open', False):

            detail_object_action_dialog = DetailObjectActionDialog(
                obj=self.obj,
                fields=self.fields
            )
            self.page.overlay.append(detail_object_action_dialog)
            detail_object_action_dialog.open = True
            self.page.update()


class ForeignKeyEditor(Dropdown, InputField):
    defaults = {
        'width': 300,
        'hint_text': 'Выберете',
    }

    def __init__(self, queryset, default_key=None):  # TODO filters
        return super().__init__(
            options=[
                dropdown.Option(text=str(obj), key=obj.id)
                for obj in queryset()
            ],
            value=default_key,
            **self.defaults
        )
