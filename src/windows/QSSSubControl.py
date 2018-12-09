'''

QSS子控件选择器

QComboBox

'''

from PyQt5.QtWidgets import *
import sys

class QSSSubControl(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSS子控件选择器")
        combo = QComboBox(self)
        combo.setObjectName("myComboBox")
        combo.addItem("Window")
        combo.addItem("Linux")
        combo.addItem("Mac OS X")

        combo.move(50,50)

        self.setGeometry(250,200,320,150)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QSSSubControl()
    qssStyle = '''
       QComboBox#myComboBox::drop-down {
           image:url(./images/dropdown.png)
       }
    '''
    form.setStyleSheet(qssStyle)
    form.show()
    sys.exit(app.exec_())