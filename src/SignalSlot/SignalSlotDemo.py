'''

信号（Signal）与槽（Slot）

'''
from PyQt5.QtWidgets import *
import sys

class SigalSlotDemo(QWidget):
    def __init__(self):
        super(SigalSlotDemo,self).__init__()
        self.initUI()

    def onClick(self):
        self.btn.setText("信号已经发出")
        self.btn.setStyleSheet("QPushButton(max-width:200px;min-width:200px")

    def initUI(self):
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('信号（Signal）与槽（Slot）')
        self.btn = QPushButton('我的按钮',self)
        self.btn.clicked.connect(self.onClick)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = SigalSlotDemo()
    gui.show()
    sys.exit(app.exec_())