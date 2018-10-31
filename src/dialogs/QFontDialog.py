'''

字体对话框：QFontDialog



'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class QFontDialogDemo(QWidget):
    def __init__(self):
        super(QFontDialogDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Font Dialog例子')
        layout = QVBoxLayout()
        self.fontButton = QPushButton('选择字体')
        self.fontButton.clicked.connect(self.getFont)
        layout.addWidget(self.fontButton)

        self.fontLabel = QLabel('Hello，测试字体例子')
        layout.addWidget(self.fontLabel)

        self.setLayout(layout)
    def getFont(self):
        font, ok = QFontDialog.getFont()
        if ok :
            self.fontLabel.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFontDialogDemo()
    main.show()
    sys.exit(app.exec_())

