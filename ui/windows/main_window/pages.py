class Pages:
    name = ""
    linked_page = ""
    icon_link = ""

    def __init__(self, name, linked_page, icon_link):
        self.name = name
        self.linked_page = linked_page
        self.icon_link = icon_link


class Tarifsimulation(Pages):
    def __init__(self):
        super().__init__("Tarifsimulator", "StackedWidget", "Iconpath")


class Tarifvergleich(Pages):
    def __init__(self):
        super().__init__("Tarifvergleich", "StackedWidget", "Iconpath")
