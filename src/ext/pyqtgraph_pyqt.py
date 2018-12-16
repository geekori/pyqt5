# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqtgraph_pyqt.ui'
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
        self.pyqtgraph1 = GraphicsLayoutWidget(self.centralwidget)
        self.pyqtgraph1.setGeometry(QtCore.QRect(10, 10, 721, 251))
        self.pyqtgraph1.setObjectName("pyqtgraph1")
        self.pyqtgraph2 = GraphicsLayoutWidget(self.centralwidget)
        self.pyqtgraph2.setGeometry(QtCore.QRect(10, 290, 501, 281))
        self.pyqtgraph2.setObjectName("pyqtgraph2")
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

from pyqtgraph import GraphicsLayoutWidget
