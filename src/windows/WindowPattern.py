'''

设置窗口样式（主要是窗口边框、标题栏以及窗口本身的样式）

'''

from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import *

class WindowPattern(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500,260)
        self.setWindowTitle('设置窗口的样式')

        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowStaysOnTopHint )
        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow{border-image:url(images/python.jpg);}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WindowPattern()
    form.show()
    sys.exit(app.exec_())
