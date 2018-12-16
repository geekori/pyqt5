'''

用动画效果一不同速度移动窗口

'''

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)

window1 = QMainWindow()
window1.show()
window2 = QMainWindow()
window2.show()

animation1 = QPropertyAnimation(window1, b'geometry')
animation2 = QPropertyAnimation(window2, b'geometry')

group = QParallelAnimationGroup()  # 并行
group = QSequentialAnimationGroup()  # 串行

group.addAnimation(animation1)
group.addAnimation(animation2)

animation1.setDuration(3000)
animation1.setStartValue(QRect(0,0,100,30))
animation1.setEndValue(QRect(250,250,100,30))
animation1.setEasingCurve(QEasingCurve.OutBounce)

animation2.setDuration(4000)
animation2.setStartValue(QRect(250,150,100,30))
animation2.setEndValue(QRect(850,250,100,30))
animation2.setEasingCurve(QEasingCurve.CosineCurve)

group.start()

sys.exit(app.exec())

