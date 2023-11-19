from .BaseViewer import Viewer
from library.core.widgets.text import Text
from flet import TextField
from .BaseInput import InputField


class TextViewer(Text, Viewer):
    "View content as Text."


class TextEditor(TextField, InputField):
    pass


class MultiLineTextViewer(TextField, InputField):
    # todo dsytcnb ukj,fkmytq
    defaults = {
        'multiline': True,
    }

    def __init__(self, *args, **kwargs):
        kwargs = kwargs | self.defaults
        super().__init__(*args, **kwargs)
