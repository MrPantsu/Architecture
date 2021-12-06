from ui.components.sidemenu.Buttons.sidemenu_button_controller import SidemenuButtonController
from ui.components.sidemenu.sidemenu_model import SidemenuModel
from ui.components.sidemenu.sidemenu_view import SidemenuView
from ui.windows.main_window.pages import Pages


class SidemenuController:
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.sidemenu_model = SidemenuModel(self)
        self.sidemenu_view = SidemenuView(self.main_controller.get_centerlayout())
        self.button_controller = SidemenuButtonController(self) # list an button controller erstellen

    def extend_sidemenu(self):
        self.sidemenu_view.extend("here goes the names")

    def minimize_sidemenu(self):
        self.sidemenu_view.minimize()

    def getSidemenuLayout(self):
        return self.sidemenu_view.getSidemenuLayout()

    def updateMainWindowView(self, name):
        self.main_controller.setMainView(name)

    def build_button_for_page(self, name, linked_page, icon_link):
        #für jeden Button einen Controller nicht in Init
        self.button_controller.build_button_for_page(name, linked_page, icon_link)
