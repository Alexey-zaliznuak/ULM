from flet import UserControl



class DataTableAction(UserControl):
    """Base class for doing smth with all data."""

    def __init__(self, *args, **kwargs):
        ...

    def widget(self) -> UserControl:
        ...

