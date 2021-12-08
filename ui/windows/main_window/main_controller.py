import sys

from ui.components.sidemenu.sidemenu_controller import SidemenuController
from ui.windows.main_window.Main_Menu_from_FH_v4 import Ui_MainWindow
# from ui.windows.main_window.main_window import Ui_MainWindow
from ui.windows.main_window.main_window_model import MainWindowModel
from ui.windows.main_window.pages import Pages, MainMenu

from PyQt5 import QtWidgets


class MainWindowController:
    def __init__(self, app):
        self.app = app
        self.main_window_model = MainWindowModel(self)
        self.main_window_ui = Ui_MainWindow(self)
        self.sidemenu_controller = SidemenuController(self)
        self.mainContentController_List = list()
        self.build_pages()


        # connenct the buttons
        self.main_window_ui.btn_close.clicked.connect(lambda: self.close_app())
        self.main_window_ui.btn_maximise_restore.clicked.connect(lambda: self.change_window_format())
        self.main_window_ui.btn_minimize.clicked.connect(lambda: self.minimize_window())
        self.main_window_ui.btn_tgl_menu.clicked.connect(lambda: self.change_sidemenu())

    def get_centerlayout(self):
        return self.main_window_ui.get_centerlayout()

    def get_Mainview_Widget(self):
        return self.main_window_ui.get_Mainview_Widget()

    def build_toolbutton(self):
        pass

    def toogle_toolbar(self):
        pass

    def close_app(self):
        sys.exit(self.app.exec_())  # ToDo is this right?

    def change_window_format(self):
        self.main_window_model.state.move_to_next_format()

    def restore_window(self):
        self.main_window_ui.restore()

    def maximize_window(self):
        self.main_window_ui.maximize()

    def minimize_window(self):
        self.main_window_ui.minimize()

    def on_drag_window(self):
        self.main_window_model.state.on_drag()

    def change_model_state(self, state):
        self.main_window_model.set_state(state)

    def change_sidemenu(self):
        self.sidemenu_controller.sidemenu_model.sidemenu_state.move_to_next_visibility_state()  # ToDo Frage: kann ich direkt auf die zugreifen oder soll ich in jeder klasse eine eigene Funktion einbinden die weiterleitet??

    def build_pages(self):
        for Page in Pages.__subclasses__():
            Page = Page()
            controller = Page.controller(self, Page.name)
            self.mainContentController_List.append(controller)
            self.sidemenu_controller.build_button_for_page(Page.name, Page.view, Page.icon_link)
            # initialise Qwidget to put in Frame
            # this should be in an MainContent_Controller
            # page_Widget = QtWidgets.QWidget()
            # page_Widget.setObjectName(Page.name)
            # mainMenuLayout = self.get_Mainview_Widget()
            # mainMenuLayout.addWidget(page_Widget)
            # view = Page.view()
            # view.setupUi(page_Widget, Page.name)
        self.setMainView(MainMenu().name)

    def setMainView(self, name):
        mainMenuLayout = self.get_Mainview_Widget()
        # for count, Page in enumerate(Pages.__subclasses__()):
        try:
            for i in range(0, 100):
                widget = mainMenuLayout.widget(i)
                print(widget.objectName())
                if mainMenuLayout.widget(i).objectName() == name:
                    mainMenuLayout.setCurrentWidget(widget)
                    break
        except:
            print("no Page found in StackedWidget")
