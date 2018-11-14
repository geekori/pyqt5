'''

创建和使用状态栏

'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class StatusBar(QMainWindow) :
    def __init__(self):
        super(StatusBar,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("状态栏演示")
        self.resize(300,200)

        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("show")
        file.triggered.connect(self.processTrigger)
        self.setCentralWidget(QTextEdit())
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)


    def processTrigger(self,q):
        if q.text() == "show" :
            self.statusBar.showMessage(q.text() + " 菜单被点击了",5000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = StatusBar()
    main.show()
    sys.exit(app.exec_())