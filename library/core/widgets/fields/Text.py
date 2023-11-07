from .BaseViewer import Viewer
from library.core.widgets.text import Text
from flet import TextField
from .BaseInput import InputField


class TextViewer(Text, Viewer):
    "View content as Text."


class TextEditor(TextField, InputField):
    pass
