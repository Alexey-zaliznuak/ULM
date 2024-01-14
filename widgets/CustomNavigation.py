from flet import (
    NavigationRailDestination,
    NavigationRailLabelType,
    VerticalDivider,
    NavigationRail,
    UserControl,
    Container,
    ListView,
    margin,
    Column,
    colors,
    Row,
)

from library.core.widgets.text import Text


class Title(Container):
    def __init__(self, text):
        self.value = text
        super().__init__(
            content=Text(
                value=text,
                size=24,
            ),
            margin=margin.only(bottom=10)
        )

def set_page(routes, selected_index):
    FormData = routes[selected_index]["page"]
    title =  Title(routes[selected_index]["title"])

    page = [FormData]

    if title.value:
        page = [title, FormData]

    if isinstance(FormData, UserControl):
        return Column(page, expand=True)
    return ListView(page, expand=True)


class CustomNavigation(UserControl):
    def __init__(
        self,
        *,
        routes: list = [],
        selected_index: int = 0,
    ):
        super().__init__()
        self.expand = True
        self.routes = routes
        self.selected_index = selected_index

        self.destinations = list(map(self.get_destinations, routes))

    def get_destinations(self, icons):
        return NavigationRailDestination(
            icon=icons["icon"][0],
            selected_icon=icons["icon"][1],
        )

    def navigation(self, index: str):
        self.row.controls[2] = set_page(self.routes, index)
        self.update()

    def build(self):
        self.state = set_page(self.routes, self.selected_index)

        self.rail = NavigationRail(
            selected_index=self.selected_index,
            label_type=NavigationRailLabelType.ALL,
            extended=True,
            width=70,
            destinations=self.destinations,
            on_change=lambda e: self.navigation(e.control.selected_index),
            bgcolor=colors.WHITE,
        )
        self.row = Row(
            controls=[
                self.rail,
                VerticalDivider(width=3, color=colors.GREY_200),
                self.state
            ],
        )
        return self.row
