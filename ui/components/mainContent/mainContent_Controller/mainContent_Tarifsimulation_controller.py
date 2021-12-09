
from ui.components.mainContent.mainContent_Views.Tarifsimulation_v2 import Tarifsimulation_View
from ui.components.mainContent.mainContent_Models.mainContent_Tarifsimulation_model import Tarifsimulation_Model
from PyQt5 import QtWidgets


class TarifsimulationController:
    def __init__(self, main_controller, name):
        self.main_controller = main_controller
        self.mainMenu_model = Tarifsimulation_Model(self)
        self.MainMenu_view = Tarifsimulation_View()
        self.name = name
        self.build_view()

    def get_Mainview_Widget(self):
        return self.main_controller.get_Mainview_Widget()

    def build_view(self):
        page_Widget = QtWidgets.QWidget()
        page_Widget.setObjectName(self.name)
        mainview_widget = self.get_Mainview_Widget()
        mainview_widget.addWidget(page_Widget)
        self.MainMenu_view.setupUi(page_Widget, self.name)
