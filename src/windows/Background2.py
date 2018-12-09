'''

使用多种方式设置窗口背景色和背景图片

1.  QSS
2.  QPalette
3.  直接绘制

'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Background2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("绘制背景图片")
    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap('./images/screen1.jpg')

        painter.drawPixmap(self.rect(),pixmap)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Background2()

    form.show()
    sys.exit(app.exec_())