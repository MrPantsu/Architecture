from PyQt5 import QtWidgets
from ui.components.sidemenu.Buttons.sidemenu_Button_view import SidemenuButtonView
from ui.components.sidemenu.Buttons.sidemenu_button_model import SidemenuButtonModel
from ui.windows.main_window.pages import Pages


class SidemenuButtonController:
    def __init__(self, sidemenu_controller):
        self.sidemenu_controller = sidemenu_controller
        self.button_models = SidemenuButtonModel.__subclasses__()
        self.SidemenuButtonView = SidemenuButtonView(self)

    # def getSidemenuButtonViews(self):
    #     sidemenuLayout = self.sidemenu_controller.getSidemenuLayout()
    #     for position, ButtonModel in enumerate(SidemenuButtonModel.__subclasses__()):
    #         widget_button = QtWidgets.QWidget()
    #         sidemenuLayout.addWidget(widget_button)
    #         self.SidemenuButtonView.setupUi(widget_button, ButtonModel(), position)

    def updateMainWindowView(self, name):
        self.sidemenu_controller.updateMainWindowView(name)
        pass

    def build_button_for_page(self, name, linked_page, icon_link):
        ButtonModel = SidemenuButtonModel(name, linked_page, icon_link)
        widget_button = QtWidgets.QWidget()
        sidemenuLayout = self.sidemenu_controller.getSidemenuLayout()
        sidemenuLayout.addWidget(widget_button)
        self.SidemenuButtonView.setupUi(widget_button, ButtonModel)




