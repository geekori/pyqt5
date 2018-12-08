'''

多窗口交互（2）：使用信号与槽

如果一个窗口A与另一个窗口B交互，那么A尽量不要直接访问B窗口中的控件，
应该访问B窗口中的信号，并指定与信号绑定的槽函数

例：如果A直接访问B窗口的控件，一旦B窗口控件发生改变，那么A和B的代码都需要变化

如果A访问的是B中的信号，那么B中的控件发生了改变，只需要修改B中的代码即可



'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from NewDateDialog import NewDateDialog

class MultiWindow2(QWidget):
    def __init__(self, parent=None):
        super(MultiWindow2, self).__init__(parent)
        self.resize(400, 90)
        self.setWindowTitle('多窗口交互（2）：使用信号与槽')

        self.open_btn = QPushButton('获取时间')
        self.lineEdit_inner = QLineEdit(self)
        self.lineEdit_emit = QLineEdit(self)
        self.open_btn.clicked.connect(self.openDialog)

        self.lineEdit_inner.setText('接收子窗口内置信号的时间')
        self.lineEdit_emit.setText('接收子窗口自定义信号的时间')

        grid = QGridLayout()
        grid.addWidget(self.lineEdit_inner)
        grid.addWidget(self.lineEdit_emit)

        grid.addWidget(self.open_btn)
        self.setLayout(grid)

    def openDialog(self):
        dialog = NewDateDialog(self)
        # 连接子窗口的内置信号与主窗口的槽函数
        dialog.datetime_inner.dateTimeChanged.connect(self.deal_inner_slot)
        # 连接子窗口的自定义信号与主窗口的槽函数
        dialog.Signal_OneParameter.connect(self.deal_emit_slot)
        dialog.show()

    def deal_inner_slot(self, date):
        self.lineEdit_inner.setText(date.toString())


    def deal_emit_slot(self, dateStr):
        self.lineEdit_emit.setText(dateStr)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MultiWindow2()
    form.show()
    sys.exit(app.exec_())
