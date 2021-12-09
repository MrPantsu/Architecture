from ui.components.mainContent.mainContent_Controller.mainContent_mainMenu_controller import MainMenuController
from ui.components.mainContent.mainContent_Controller.mainContent_Tarifsimulation_controller import TarifsimulationController
from ui.components.mainContent.mainContent_Views.Main_Menu_v2 import MainMenuView
from ui.components.mainContent.mainContent_Views.Tarifsimulation_v2 import Tarifsimulation_View


class Pages:
    name = ""
    view = object # Todo: braucht man nicht, weil in Controller
    icon_link = ""
    controller = object

    def __init__(self, name, view, icon_link, controller):
        self.name = name
        self.view = view # Todo: braucht man nicht, weil in Controller
        self.icon_link = icon_link
        self.controller = controller



class MainMenu(Pages):
    def __init__(self):

        super().__init__("Main Menu", MainMenuView, "Iconpath", MainMenuController)



class Tarifvergleich(Pages):
    def __init__(self):
        super().__init__("Tarifsimulation", Tarifsimulation_View, "Iconpath", TarifsimulationController)
