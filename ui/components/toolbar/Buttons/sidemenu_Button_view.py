# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\tomre\PycharmProjects\Architecture\ui\Components\toolbar\sidemenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


from toolbar.Buttons.sidemenuButton import Ui_Form
from toolbar.Buttons.sidemenu_button_model import SidemenuButtonModel


class SidemenuButtonView(object):

    def setupUi(self, Form, ButtonModel:SidemenuButtonModel, position:int):
        Form.setObjectName("Form")
        Form.resize(94, 70)
        self.sidemenuButton = QtWidgets.QPushButton(Form)
        self.sidemenuButton.setGeometry(QtCore.QRect(0, 0+position*10, 70, 70)) #y increase by 70 for each initialisation
        self.sidemenuButton.setMinimumSize(QtCore.QSize(70, 70))
        self.sidemenuButton.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setKerning(True)
        self.sidemenuButton.setFont(font)
        self.sidemenuButton.setObjectName("sidemenuButton")

        self.retranslateUi(Form, ButtonModel)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form, ButtonModel):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.sidemenuButton.setText(_translate("Form", ButtonModel.buttonName))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
