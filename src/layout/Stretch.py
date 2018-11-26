'''

设置伸缩量（addStretch）



'''

import sys,math
from PyQt5.QtWidgets import *


class Stretch(QWidget) :
    def __init__(self):
        super(Stretch,self).__init__()
        self.setWindowTitle("设置伸缩量")
        btn1 = QPushButton(self)
        btn2 = QPushButton(self)
        btn3 = QPushButton(self)
        btn1.setText("按钮1")
        btn2.setText("按钮2")
        btn3.setText("按钮3")

        layout = QHBoxLayout()

        layout.addStretch(1)
        layout.addWidget(btn1)

        layout.addStretch(2)
        layout.addWidget(btn2)
        layout.addStretch(3)
        layout.addWidget(btn3)

        self.setLayout(layout)







if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Stretch()
    main.show()
    sys.exit(app.exec_())