from library.core.widgets.text import Text

class TabText(Text):
    def __init__(self, value):
        super().__init__(
            selectable=False,
            size=None,
            value=value
        )