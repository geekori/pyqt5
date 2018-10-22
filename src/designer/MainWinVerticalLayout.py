# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWinVerticalLayout.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(460, 60, 251, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 30, 261, 271))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))

