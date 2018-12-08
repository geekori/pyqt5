'''
用代码控制窗口的最大化和最小化

'''


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


### 自定义窗口类
class WindowMaxMin(QWidget):


    ###  构造函数
    def __init__(self, parent=None):
        '''构造函数'''
        # 调用父类构造函数
        super(WindowMaxMin, self).__init__(parent)
        self.resize(300,400)
        self.setWindowTitle("用代码控制窗口的最大化和最小化")
        self.setWindowFlags(Qt.WindowMaximizeButtonHint)

        layout = QVBoxLayout()
        maxButton1 = QPushButton()
        maxButton1.setText('窗口最大化1')
        maxButton1.clicked.connect(self.maximized1)


        maxButton2 = QPushButton()
        maxButton2.setText('窗口最大化2')
        maxButton2.clicked.connect(self.showMaximized)

        minButton = QPushButton()
        minButton.setText('窗口最小化')
        minButton.clicked.connect(self.showMinimized)


        layout.addWidget(maxButton1)
        layout.addWidget(maxButton2)
        layout.addWidget(minButton)
        self.setLayout(layout)



    def maximized1(self):
        desktop = QApplication.desktop()
        # 获取桌面可用尺寸
        rect = desktop.availableGeometry()

        self.setGeometry(rect)



if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = WindowMaxMin()
    window.show()
    # 应用程序事件循环
    sys.exit(app.exec_())
