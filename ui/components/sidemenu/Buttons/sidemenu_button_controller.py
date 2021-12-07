from PyQt5 import QtWidgets
from ui.components.sidemenu.Buttons.sidemenu_Button_view import SidemenuButtonView
from ui.components.sidemenu.Buttons.sidemenu_button_model import SidemenuButtonModel
from ui.windows.main_window.pages import Pages


class SidemenuButtonController:
    def __init__(self, sidemenu_controller, name, view, icon_link):
        self.sidemenu_controller = sidemenu_controller
        self.button_model = SidemenuButtonModel(name, view, icon_link)
        self.SidemenuButtonView = SidemenuButtonView(self)

    def updateMainWindowView(self, name):
        self.sidemenu_controller.updateMainWindowView(name)
        pass

    def build_button_for_page(self):
        widget_button = QtWidgets.QWidget()
        sidemenuLayout = self.sidemenu_controller.getSidemenuLayout()
        sidemenuLayout.addWidget(widget_button)
        self.SidemenuButtonView.setupUi(widget_button)




