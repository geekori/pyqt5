'''

使用Partial对象为槽函数传递参数


'''

from PyQt5.QtWidgets import *
import sys
from functools import partial

class PartialSlotArg(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("使用Partial表达式为槽函数传递参数")

        button1 = QPushButton("按钮1")
        button2 = QPushButton("按钮2")
        x = 20
        y = -123
        button1.clicked.connect(partial(self.onButtonClick,10,20))
        button2.clicked.connect(partial(self.onButtonClick, x, y))

        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)
    def onButtonClick(self,m,n):
        print("m + n =",m + n )
        QMessageBox.information(self,"结果",str(m+n))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = PartialSlotArg()
    form.show()
    sys.exit(app.exec_())