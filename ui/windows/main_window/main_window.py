# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\tomre\PycharmProjects\Architecture\ui\windows\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import files_rc

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMainWindow, QSizeGrip



class Ui_MainWindow(QMainWindow):

    def __init__(self, controller):

        super().__init__()

        self.main_controller = controller

        # create and setup Window from Ui_MainWindow Model

        self.setupUi(self)

        # set startsize and minimum size
        start_size = QSize(1000, 720)
        self.dragPos = QtCore.QPoint(300, 25)

        self.resize(start_size)
        self.setMinimumSize(start_size)

        # set flags to the window
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)

        #create function that handles window_drag events
        def move_window(event):
            self.main_controller.on_drag_window()

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.frame_header_top.mouseMoveEvent = move_window

        #connect frame to sizegrip
        self.sizegrip = QSizeGrip(self.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # SHOW ==> MAIN WINDOW
        self.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(887, 791)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_main)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_header = QtWidgets.QFrame(self.frame_main)
        self.frame_header.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_header.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_header.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_header.setLineWidth(0)
        self.frame_header.setObjectName("frame_header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_toogle = QtWidgets.QFrame(self.frame_header)
        self.frame_toogle.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_toogle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_toogle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toogle.setLineWidth(1)
        self.frame_toogle.setMidLineWidth(1)
        self.frame_toogle.setObjectName("frame_toogle")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_toogle)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_tgl_menu = QtWidgets.QPushButton(self.frame_toogle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_tgl_menu.sizePolicy().hasHeightForWidth())
        self.btn_tgl_menu.setSizePolicy(sizePolicy)
        self.btn_tgl_menu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_tgl_menu.setStyleSheet("QPushButton {\n"
                                        "    background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
                                        "    background-position: center;\n"
                                        "    background-repeat: no-reperat;\n"
                                        "    border: none;\n"
                                        "    background-color: rgb(80, 74, 64);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(133, 127, 114);\n"
                                        "}\n"
                                        "QPushButton:pressed {    \n"
                                        "    background-color: rgb(98, 93, 82);\n"
                                        "}")
        self.btn_tgl_menu.setText("")
        self.btn_tgl_menu.setObjectName("btn_tgl_menu")
        self.horizontalLayout_3.addWidget(self.btn_tgl_menu)
        self.horizontalLayout_2.addWidget(self.frame_toogle)
        self.frame_header_content = QtWidgets.QFrame(self.frame_header)
        self.frame_header_content.setToolTipDuration(0)
        self.frame_header_content.setStyleSheet("background-color: rgb(184, 178, 167);")
        self.frame_header_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_header_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_header_content.setObjectName("frame_header_content")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_header_content)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_header_top = QtWidgets.QFrame(self.frame_header_content)
        self.frame_header_top.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_header_top.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_header_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_header_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_header_top.setObjectName("frame_header_top")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_header_top)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_title = QtWidgets.QLabel(self.frame_header_top)
        self.label_title.setStyleSheet("background-color: rgb(80, 74, 64);")
        self.label_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_title.setLineWidth(0)
        self.label_title.setIndent(0)
        self.label_title.setObjectName("label_title")
        self.horizontalLayout_6.addWidget(self.label_title)
        self.btn_minimize = QtWidgets.QPushButton(self.frame_header_top)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy)
        self.btn_minimize.setMinimumSize(QtCore.QSize(45, 0))
        self.btn_minimize.setMaximumSize(QtCore.QSize(45, 16777215))
        self.btn_minimize.setStyleSheet("QPushButton {\n"
                                        "    background-image: url(:/16x16/icons/16x16/cil-window-minimize.png);\n"
                                        "    background-position: center;\n"
                                        "    background-repeat: no-reperat;\n"
                                        "    border: none;\n"
                                        "    background-color: rgb(80, 74, 64);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(133, 127, 114);\n"
                                        "}\n"
                                        "QPushButton:pressed {    \n"
                                        "    background-color: rgb(98, 93, 82);\n"
                                        "}")
        self.btn_minimize.setText("")
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_6.addWidget(self.btn_minimize)
        self.btn_maximise_restore = QtWidgets.QPushButton(self.frame_header_top)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_maximise_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximise_restore.setSizePolicy(sizePolicy)
        self.btn_maximise_restore.setMinimumSize(QtCore.QSize(45, 0))
        self.btn_maximise_restore.setMaximumSize(QtCore.QSize(45, 16777215))
        self.btn_maximise_restore.setStyleSheet("QPushButton {\n"
                                                "    background-image: url(:/16x16/icons/16x16/cil-window-maximize.png);\n"
                                                "    background-position: center;\n"
                                                "    background-repeat: no-reperat;\n"
                                                "    border: none;\n"
                                                "    background-color: rgb(80, 74, 64);\n"
                                                "}\n"
                                                "QPushButton:hover {\n"
                                                "    background-color: rgb(133, 127, 114);\n"
                                                "}\n"
                                                "QPushButton:pressed {    \n"
                                                "    background-color: rgb(98, 93, 82);\n"
                                                "}")
        self.btn_maximise_restore.setText("")
        self.btn_maximise_restore.setObjectName("btn_maximise_restore")
        self.horizontalLayout_6.addWidget(self.btn_maximise_restore)
        self.btn_close = QtWidgets.QPushButton(self.frame_header_top)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setMinimumSize(QtCore.QSize(45, 0))
        self.btn_close.setMaximumSize(QtCore.QSize(45, 16777215))
        self.btn_close.setStyleSheet("QPushButton {\n"
                                     "    background-image: ;\n"
                                     "    image: url(:/16x16/icons/16x16/cil-x.png);\n"
                                     "    background-position: center;\n"
                                     "    background-repeat: no-reperat;\n"
                                     "    border: none;\n"
                                     "    background-color: rgb(80, 74, 64);\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: rgb(133, 127, 114);\n"
                                     "}\n"
                                     "QPushButton:pressed {    \n"
                                     "    background-color: rgb(98, 93, 82);\n"
                                     "}")
        self.btn_close.setText("")
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_6.addWidget(self.btn_close)
        self.verticalLayout_6.addWidget(self.frame_header_top)
        self.frame_header_bottom = QtWidgets.QFrame(self.frame_header_content)
        self.frame_header_bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_header_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_header_bottom.setObjectName("frame_header_bottom")
        self.verticalLayout_6.addWidget(self.frame_header_bottom)
        self.horizontalLayout_2.addWidget(self.frame_header_content)
        self.verticalLayout_2.addWidget(self.frame_header)
        self.frame_center = QtWidgets.QFrame(self.frame_main)
        self.frame_center.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_center.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_center.setObjectName("frame_center")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_center)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_side = QtWidgets.QFrame(self.frame_center)
        self.frame_side.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_side.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_side.setObjectName("frame_side")
        self.layout_side = QtWidgets.QHBoxLayout(self.frame_side)
        self.layout_side.setContentsMargins(0, 0, 0, 0)
        self.layout_side.setSpacing(0)
        self.layout_side.setObjectName("layout_side")
        self.horizontalLayout.addWidget(self.frame_side)
        self.frame_content = QtWidgets.QFrame(self.frame_center)
        self.frame_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_content)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_main_content = QtWidgets.QFrame(self.frame_content)
        self.frame_main_content.setStyleSheet("background-color: rgb(66, 61, 51);")
        self.frame_main_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_main_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main_content.setObjectName("frame_main_content")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_main_content)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_main_content)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_color = QtWidgets.QWidget()
        self.page_color.setObjectName("page_color")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_color)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.color_palett = QtWidgets.QFrame(self.page_color)
        self.color_palett.setMaximumSize(QtCore.QSize(16777215, 60))
        self.color_palett.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.color_palett.setFrameShadow(QtWidgets.QFrame.Raised)
        self.color_palett.setObjectName("color_palett")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.color_palett)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_4 = QtWidgets.QFrame(self.color_palett)
        self.frame_4.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0.523, x2:1, y2:0.5, stop:0 rgb(250, 249, 247), stop:1 rgb(39, 36, 29));")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5.addWidget(self.frame_4)
        self.verticalLayout_5.addWidget(self.color_palett)
        self.frame_3 = QtWidgets.QFrame(self.page_color)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5.addWidget(self.frame_3)
        self.stackedWidget.addWidget(self.page_color)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout_4.addWidget(self.stackedWidget)
        self.verticalLayout_3.addWidget(self.frame_main_content)
        self.frame_footer = QtWidgets.QFrame(self.frame_content)
        self.frame_footer.setMinimumSize(QtCore.QSize(0, 25))
        self.frame_footer.setStyleSheet("background-color: rgb(80, 74, 64);")
        self.frame_footer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_footer.setObjectName("frame_footer")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_footer)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.frame = QtWidgets.QFrame(self.frame_footer)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_23.addWidget(self.frame)
        self.frame_size_grip = QtWidgets.QFrame(self.frame_footer)
        self.frame_size_grip.setMinimumSize(QtCore.QSize(25, 0))
        self.frame_size_grip.setMaximumSize(QtCore.QSize(25, 16777215))
        self.frame_size_grip.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_size_grip.setStyleSheet("background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
                                             "background-position: center;\n"
                                             "background-repeat: no-reperat;")
        self.frame_size_grip.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_size_grip.setObjectName("frame_size_grip")
        self.horizontalLayout_23.addWidget(self.frame_size_grip)
        self.verticalLayout_3.addWidget(self.frame_footer)
        self.horizontalLayout.addWidget(self.frame_content)
        self.verticalLayout_2.addWidget(self.frame_center)
        self.frame_center.raise_()
        self.frame_header.raise_()
        self.verticalLayout.addWidget(self.frame_main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def get_centerlayout(self):
        return self.layout_side

    def maximize(self):
        self.showMaximized()
        self.btn_maximise_restore.setToolTip("Restore")
        self.btn_maximise_restore.setStyleSheet("QPushButton {\n"
                                     "    background-image: ;\n"
                                     "    image: url(:/16x16/icons/16x16/cil-window-restore.png);"
                                     "    background-position: center;\n"
                                     "    background-repeat: no-reperat;\n"
                                     "    border: none;\n"
                                     "    background-color: rgb(80, 74, 64);\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: rgb(133, 127, 114);\n"
                                     "}\n"
                                     "QPushButton:pressed {    \n"
                                     "    background-color: rgb(98, 93, 82);\n"
                                     "}")

    def restore(self):
        self.showNormal()
        self.move(self.dragPos - QtCore.QPoint(300, 25))
        self.btn_maximise_restore.setToolTip("Maximize")
        self.btn_maximise_restore.setStyleSheet("QPushButton {\n"
                                     "    background-image: ;\n"
                                     "    image: url(:/16x16/icons/16x16/cil-window-maximize.png);\n"
                                     "    background-position: center;\n"
                                     "    background-repeat: no-reperat;\n"
                                     "    border: none;\n"
                                     "    background-color: rgb(80, 74, 64);\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: rgb(133, 127, 114);\n"
                                     "}\n"
                                     "QPushButton:pressed {    \n"
                                     "    background-color: rgb(98, 93, 82);\n"
                                     "}")

    def minimize(self):
        self.showMinimized()

    def change_sidemenu(self):
        self.main_controller.change_sidemenu()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
