'''

实现不规则窗口（异形窗口）

通过mask实现异形窗口

需要一张透明的png图，透明部分被扣出，形成一个非矩形的区域


移动和关闭不规则窗口
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class AbnormityWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("异形窗口")
        self.pix = QBitmap('./images/mask.png')
        self.resize(self.pix.size())
        self.setMask(self.pix)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True

            self.m_DragPosition = event.globalPos() - self.pos()
            self.setCursor(QCursor(Qt.OpenHandCursor))
            print(event.globalPos())  #
            print(event.pos())
            print(self.pos())
        if event.button() == Qt.RightButton:
            self.close()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            # 当左键移动窗体修改偏移值
            # QPoint
            # 实时计算窗口左上角坐标
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)


    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0,0,self.pix.width(),self.pix.height(),QPixmap('./images/screen1.jpg'))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = AbnormityWindow()
    form.show()
    sys.exit(app.exec_())
