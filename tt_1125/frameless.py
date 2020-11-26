# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frameless.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(482, 424)
        Dialog.setStyleSheet("#Dialog {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"#widget {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 20px;\n"
"}\n"
"#closeButton {\n"
"    border: none;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"#closeButton:hover {\n"
"    color: white;\n"
"    background-color: rgb(232, 16, 16);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        # spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.closeButton = QtWidgets.QPushButton(self.widget)
        self.closeButton.setMinimumSize(QtCore.QSize(30, 30))
        self.closeButton.setObjectName("closeButton")
        self.gridLayout.addWidget(self.closeButton, 0, 1, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 1, 0, 1, 2)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.closeButton.setText(_translate("Dialog", "X"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "其他内容"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

