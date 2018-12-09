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

app = QApplication(sys.argv)
win = QMainWindow()
win.setWindowTitle("背景图片")
win.resize(350,250)
win.setObjectName("MainWindow")
'''
# 通过QSS动态修改窗口的背景颜色和背景图片
#win.setStyleSheet("#MainWindow{border-image:url(./images/python.jpg);}")
win.setStyleSheet("#MainWindow{background-color:yellow}")
'''

# 通过QPalette设置背景图片和背景颜色
#palette = QPalette()
#palette.setBrush(QPalette.Background,QBrush(QPixmap("./images/python.jpg")))
#palette.setColor(QPalette.Background,Qt.red)
#win.setPalette(palette)

win.show()
sys.exit(app.exec())

