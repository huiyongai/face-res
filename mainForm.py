# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt_create_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_1125(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(859, 474)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnOpenCamera = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenCamera.setGeometry(QtCore.QRect(60, 370, 100, 30))
        self.btnOpenCamera.setObjectName("btnOpenCamera")
        self.btnCaptureImg = QtWidgets.QPushButton(self.centralwidget)
        self.btnCaptureImg.setGeometry(QtCore.QRect(220, 370, 100, 30))
        self.btnCaptureImg.setObjectName("btnCaptureImg")
        self.btnOpenImg = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenImg.setGeometry(QtCore.QRect(370, 370, 93, 28))
        self.btnOpenImg.setObjectName("btnOpenImg")
        self.btnGraying = QtWidgets.QPushButton(self.centralwidget)
        self.btnGraying.setGeometry(QtCore.QRect(520, 370, 100, 30))
        self.btnGraying.setObjectName("btnGraying")
        self.btnThresholdSegment = QtWidgets.QPushButton(self.centralwidget)
        self.btnThresholdSegment.setGeometry(QtCore.QRect(670, 370, 150, 30))
        self.btnThresholdSegment.setObjectName("btnThresholdSegment")
        self.labelCamera = QtWidgets.QLabel(self.centralwidget)
        self.labelCamera.setGeometry(QtCore.QRect(70, 100, 150, 150))
        self.labelCamera.setObjectName("labelCamera")
        self.labelCapture = QtWidgets.QLabel(self.centralwidget)
        self.labelCapture.setGeometry(QtCore.QRect(330, 100, 150, 150))
        self.labelCapture.setObjectName("labelCapture")
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setGeometry(QtCore.QRect(630, 100, 150, 150))
        self.labelResult.setObjectName("labelResult")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 859, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btnOpenCamera.clicked.connect(MainWindow.btnOpenCamera_Clicked)
        self.btnCaptureImg.clicked.connect(MainWindow.btnCaptureImg_Clicked)
        self.btnOpenImg.clicked.connect(MainWindow.btnOpenImg_Clicked)
        self.btnGraying.clicked.connect(MainWindow.btnGrayingImg_Clicked)
        self.btnThresholdSegment.clicked.connect(MainWindow.btnThresholdSegment_Clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnOpenCamera.setText(_translate("MainWindow", "Open Camera"))
        self.btnCaptureImg.setText(_translate("MainWindow", "Capture Image"))
        self.btnOpenImg.setText(_translate("MainWindow", "Open Image"))
        self.btnGraying.setText(_translate("MainWindow", "Graying"))
        self.btnThresholdSegment.setText(_translate("MainWindow", "Threshold Segmentation"))
        self.labelCamera.setText(_translate("MainWindow", "Camera"))
        self.labelCapture.setText(_translate("MainWindow", "Captured Image"))
        self.labelResult.setText(_translate("MainWindow", "Result Image"))