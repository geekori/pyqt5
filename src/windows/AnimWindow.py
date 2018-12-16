'''

用动画效果改变窗口尺寸


QPropertyAnimation




'''

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class AnimWindow(QWidget):
    def __init__(self):
        super(AnimWindow, self).__init__()
        self.OrigHeight = 50
        self.ChangeHeight = 150
        self.setGeometry(QRect(500, 400, 150, self.OrigHeight))
        self.btn = QPushButton('展开', self)
        self.btn.setGeometry(10, 10, 60, 35)
        self.btn.clicked.connect(self.change)
    def change(self):
        currentHeight = self.height()
        if self.OrigHeight == currentHeight:
            startHeight = self.OrigHeight
            endHeight = self.ChangeHeight
            self.btn.setText('收缩')
        else:
            startHeight = self.ChangeHeight
            endHeight= self.OrigHeight
            self.btn.setText('展开')

        self.animation = QPropertyAnimation(self,b'geometry')
        self.animation.setDuration(500)
        self.animation.setStartValue(QRect(500,400,150,startHeight))
        self.animation.setEndValue(QRect(500,400,150,endHeight))
        self.animation.start()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AnimWindow()
    window.show()
    sys.exit(app.exec_())