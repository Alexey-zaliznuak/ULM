from flet import Text, TextStyle, colors


class ErrorText(Text):
    def __init__(self, text: str, *args, **kwargs):
        super().__init__(text, style=TextStyle(16, color=colors.RED_400))
