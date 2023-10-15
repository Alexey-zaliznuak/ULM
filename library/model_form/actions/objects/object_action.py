from functools import partial
from typing import Union

from flet import Control, Page


from library.utils import LazyAttribute
from library.core.widgets.actions import ActionButton


class ObjectAction():
    """Base Action class for doing smth with one object."""
    action_widget: ActionButton = None

    def __call__(
        self,
        obj,
        page: Union[Page, LazyAttribute[Page]],
        datatable=None
    ) -> Control:
        return self.action_widget(
            partial(self.on_click_method, obj, page, datatable)
        )

    def on_click_method(self, *args, **kwargs):
        ...
