import flet as ft


class CustomNavigation(ft.UserControl):
    def __init__(
        self,
        *,
        routes: list = [],
        selected_index: int = 0

    ):
        super().__init__()
        self.expand = True
        self.routes = routes
        self.selected_index = selected_index

        self.destinations = list(map(self.get_destinations, routes))

    def get_destinations(self, icons):
        return ft.NavigationRailDestination(
            icon=icons["icon"][0],
            selected_icon=icons["icon"][1],
        )

    def navigation(self, index: str):
        self.row.controls[2] = self.routes[index]["page"]
        self.row.controls[2].expand = True
        self.update()

    def build(self):
        self.state = self.routes[self.selected_index]["page"]
        self.state.expand = True
        
        self.rail = ft.NavigationRail(
            selected_index=self.selected_index,
            label_type=ft.NavigationRailLabelType.ALL,
            extended=True,
            width=70,
            destinations=self.destinations,
            on_change=lambda e: self.navigation(e.control.selected_index),
        )
        self.row = ft.Row(  
            controls=[
                self.rail,
                ft.VerticalDivider(width=1),
                self.state
            ],
        )
        return self.row
