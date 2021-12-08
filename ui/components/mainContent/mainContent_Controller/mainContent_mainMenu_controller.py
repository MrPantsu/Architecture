
from ui.components.mainContent.mainContent_Views.MainMenu import MainMenuView
from ui.components.mainContent.mainContent_Models.mainContent_MainMenu_model import MainMenu_Model
from PyQt5 import QtWidgets


class MainMenuController:
    def __init__(self, main_controller, name):
        self.main_controller = main_controller
        self.mainMenu_model = MainMenu_Model(self)
        self.MainMenu_view = MainMenuView()
        self.name = name
        self.build_view()

    def get_Mainview_Widget(self):
        return self.main_controller.get_Mainview_Widget()

    def build_view(self):
        page_Widget = QtWidgets.QWidget()
        page_Widget.setObjectName(self.name)
        mainview_widget = self.get_Mainview_Widget()
        mainview_widget.addWidget(page_Widget)
        self.MainMenu_view.setupUi(mainview_widget, self.name)
