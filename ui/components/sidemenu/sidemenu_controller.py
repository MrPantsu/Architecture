from ui.components.sidemenu.Buttons.sidemenu_button_controller import SidemenuButtonController
from ui.components.sidemenu.sidemenu_model import SidemenuModel
from ui.components.sidemenu.sidemenu_view import SidemenuView


class SidemenuController:
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.sidemenu_model = SidemenuModel(self)
        self.sidemenu_view = SidemenuView(self.main_controller.get_centerlayout())
        self.button_controller_list = list()

    def extend_sidemenu(self):
        self.sidemenu_view.extend("here goes the names")

    def minimize_sidemenu(self):
        self.sidemenu_view.minimize()

    def getSidemenuLayout(self):
        return self.sidemenu_view.getSidemenuLayout()

    def updateMainWindowView(self, name):
        self.main_controller.setMainView(name)

    def build_button_for_page(self, name, icon_link):
        buttonController = SidemenuButtonController(self, name, icon_link)
        self.button_controller_list.append(SidemenuButtonController)
        buttonController.build_button_for_page()
