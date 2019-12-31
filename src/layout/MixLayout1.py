import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, \
                            QGridLayout, QFormLayout, QPushButton

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('嵌套布局')
        self.resize(700, 200)

        # 全局控件（注意参数self），用于承载全局布局
        wwg = QWidget(self)

        # 全局布局
        wl = QHBoxLayout(wwg)
        hlayout = QHBoxLayout()
        vlayout = QVBoxLayout()
        glayout = QGridLayout()
        flayout = QFormLayout()

        # 为局部布局添加控件
        hlayout.addWidget(QPushButton(str(1)))
        hlayout.addWidget(QPushButton(str(2)))
        vlayout.addWidget(QPushButton(str(3)))
        vlayout.addWidget(QPushButton(str(4)))
        glayout.addWidget(QPushButton(str(5)), 0, 0)
        glayout.addWidget(QPushButton(str(6)), 0, 1)
        glayout.addWidget(QPushButton(str(7)), 1, 0)
        glayout.addWidget(QPushButton(str(8)), 1, 1)
        flayout.addWidget(QPushButton(str(9)))
        flayout.addWidget(QPushButton(str(10)))
        flayout.addWidget(QPushButton(str(11)))
        flayout.addWidget(QPushButton(str(12)))

        # 在布局布局wl中添加局部布局
        wl.addLayout(hlayout)
        wl.addLayout(vlayout)
        wl.addLayout(glayout)
        wl.addLayout(flayout)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())
