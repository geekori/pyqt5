'''

使用QSS选择器设置控件样式

'''

from PyQt5.QtWidgets import *
import sys
import qdarkstyle
class QSSSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSS样式")
        btn1 = QPushButton(self)
        btn1.setText("按钮1")
        btn2 = QPushButton(self)
        btn2.setProperty('name','btn2')
        btn2.setText("按钮2")

        btn3 = QPushButton(self)
        btn3.setProperty('name','btn3')
        btn3.setText("按钮3")

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QSSSelector()
    # 选择器
    qssStyle = '''
        QPushButton[name="btn2"] {
            background-color:red;
            color:yellow;
            height:120;
            font-size:60px;
        }
        QPushButton[name="btn3"] {
            background-color:blue;
            color:yellow;
            height:60;
            font-size:30px;
        }
    '''
    #form.setStyleSheet(qssStyle)
    form.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    form.show()
    sys.exit(app.exec_())