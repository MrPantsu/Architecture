from PyQt5 import QtWidgets
from toolbar.Buttons.sidemenu_Button_view import SidemenuButtonView
from toolbar.Buttons.sidemenu_button_model import SidemenuButtonModel


class SidemenuButtonController:
    def __init__(self, sidemenu_controller):
        self.sidemenu_controller = sidemenu_controller
        self.button_models = SidemenuButtonModel.__subclasses__()
        self.SidemenuButtonView = SidemenuButtonView()
        self.getSidemenuButtonViews()

        # self.main_controller = main_controller
        # self.sidemenu_model = SidemenuModel(self)
        # self.sidemenu_view = SidemenuView(self.main_controller.get_centerlayout())

    def getSidemenuButtonViews(self):
        sidemenuLayout = self.sidemenu_controller.getSidemenuLayout()
        for position, ButtonModel in enumerate(SidemenuButtonModel.__subclasses__()):
            widget_button = QtWidgets.QWidget()
            sidemenuLayout.addWidget(widget_button)
            self.SidemenuButtonView.setupUi(widget_button, ButtonModel(), position)
