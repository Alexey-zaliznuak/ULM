from typing import Any, List, Optional, Union
from flet_core.control import Control, OptionalNumber
from flet_core.form_field_control import InputBorder
from flet_core.ref import Ref
from flet_core.text_span import TextSpan
from flet_core.text_style import TextStyle
from flet_core.types import AnimationValue, BorderRadiusValue, FontWeight, OffsetValue, PaddingValue, ResponsiveNumber, RotateValue, ScaleValue, TextAlign
from library.core.widgets.settings import PARAGRAPH_TEXT_SIZE
from .BaseViewer import Viewer
from library.core.widgets.text import Text
from flet import KeyboardType, TextCapitalization, TextField, TextOverflow, TextThemeStyle
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
