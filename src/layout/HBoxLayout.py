'''

水平盒布局（QHBoxLayout）



'''

import sys,math
from PyQt5.QtWidgets import *


class HBoxLayout(QWidget) :
    def __init__(self):
        super(HBoxLayout,self).__init__()
        self.setWindowTitle("水平盒布局")

        hlayout = QHBoxLayout()
        hlayout.addWidget(QPushButton('按钮1'))
        hlayout.addWidget(QPushButton('按钮2'))
        hlayout.addWidget(QPushButton('按钮3'))
        hlayout.addWidget(QPushButton('按钮4'))
        hlayout.addWidget(QPushButton('按钮5'))
        hlayout.setSpacing(40)
        self.setLayout(hlayout)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = HBoxLayout()
    main.show()
    sys.exit(app.exec_())