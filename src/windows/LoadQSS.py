'''

装载QSS文件

'''

import sys
from PyQt5.QtWidgets import *
from CommonHelper import CommonHelper

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(477, 258)
        self.setWindowTitle("加载QSS文件")
        btn = QPushButton()
        btn.setText('装载QSS文件')
        btn.setToolTip('提示文本')

        vbox = QVBoxLayout()
        vbox.addWidget(btn)
        btn.clicked.connect(self.onClick)
        self.setLayout(vbox)

        widget  = QWidget(self)
        self.setCentralWidget(widget)
        widget.setLayout(vbox)

    def onClick(self):
        styleFile = './style.qss'
        qssStyle = CommonHelper.readQSS(styleFile)
        win.setStyleSheet(qssStyle)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()

    win.show()
    sys.exit(app.exec_())