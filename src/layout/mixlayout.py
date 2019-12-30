from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QApplication, QHBoxLayout, QWidget, QPushButton, QLineEdit
from PyQt5 import QtWidgets
import sys

class RadioButton(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setUI()

    def setUI(self):
        # button
        self.btn1 = QPushButton('button1')
        self.btn2 = QPushButton('button2')
        self.btn3 = QPushButton('button3')
        self.btn4 = QPushButton('button4')

        # 新建一个栅格布局，并且将按钮添加进去
        self.grid = QGridLayout()
        self.grid.addWidget(self.btn1, 0, 0)
        self.grid.addWidget(self.btn2, 0, 1)
        self.grid.addWidget(self.btn3, 1, 0)
        self.grid.addWidget(self.btn4, 1, 1)

        # 新建左边容器
        self.widget1 = QWidget()
        self.widget1.setStyleSheet("QWidget{border: 1px solid #FF0000;}")  # 设置样式
        self.widget1.setLayout(self.grid)

        # 输入行
        self.lineEdit1 = QLineEdit('lineEdit1')
        self.lineEdit2 = QLineEdit('lineEdit2')
        self.lineEdit3 = QLineEdit('lineEdit3')
        self.lineEdit4 = QLineEdit('lineEdit4')

        # 新建一个垂直布局，并且将输入行添加进去
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.lineEdit1)
        self.vbox.addWidget(self.lineEdit2)
        self.vbox.addWidget(self.lineEdit3)
        self.vbox.addWidget(self.lineEdit4)

        # 新建右边容器
        self.widget2 = QWidget()
        self.widget2.setStyleSheet("QWidget{border: 1px solid #FF0000;}")  # 设置样式
        self.widget2.setLayout(self.vbox)

        '''layout'''
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.widget1)
        self.hbox.addWidget(self.widget2)
        self.setLayout(self.hbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    qb = RadioButton()
    qb.show()
    sys.exit(app.exec_())
