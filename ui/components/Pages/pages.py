from ui.components.mainContent.mainContent_Controller.mainContent_mainMenu_controller import MainMenuController
from ui.components.mainContent.mainContent_Controller.mainContent_Tarifsimulation_controller import TarifsimulationController
from ui.components.mainContent.mainContent_Views.Main_Menu_v2 import MainMenuView
from ui.components.mainContent.mainContent_Views.Tarifsimulation_v2 import Tarifsimulation_View


class Pages:
    name = ""
    icon_link = ""
    controller = object

    def __init__(self, name, icon_link, controller):
        self.name = name
        self.icon_link = icon_link
        self.controller = controller



class MainMenu(Pages):
    def __init__(self):
        super().__init__("Main Menu", "Iconpath", MainMenuController)



class Tarifvergleich(Pages):
    def __init__(self):
        super().__init__("Tarifsimulation", "Iconpath", TarifsimulationController)
