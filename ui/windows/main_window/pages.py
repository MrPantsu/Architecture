from ui.windows.main_window.UI_Designer_pages.MainMenu import MainMenuView
from ui.windows.main_window.UI_Designer_pages.Tarifsimulation import Tarifsimulation_View

class Pages:
    name = ""
    view = object
    icon_link = ""

    def __init__(self, name, view, icon_link):
        self.name = name
        self.view = view
        self.icon_link = icon_link


class MainMenu(Pages):
    def __init__(self):

        super().__init__("Main Menu", MainMenuView, "Iconpath")



class Tarifvergleich(Pages):
    def __init__(self):
        super().__init__("Tarifsimulation", Tarifsimulation_View, "Iconpath")
