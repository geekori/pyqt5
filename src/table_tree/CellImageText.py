'''

在单元格中实现图文混排的效果

'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class CellImageText(QWidget):

    def __init__(self):
        super(CellImageText,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("在单元格中实现图文混排的效果")
        self.resize(500, 300);
        layout = QHBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(4)
        layout.addWidget(self.tableWidget)

        self.tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重', '显示图片'])

        newItem = QTableWidgetItem('李宁')
        self.tableWidget.setItem(0,0,newItem)

        newItem = QTableWidgetItem('男')
        self.tableWidget.setItem(0,1,newItem)
        newItem = QTableWidgetItem('160')
        self.tableWidget.setItem(0,2,newItem)

        newItem = QTableWidgetItem(QIcon('./images/bao1.png'),'背包')
        self.tableWidget.setItem(0,3,newItem)



        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = CellImageText()
    example.show()
    sys.exit(app.exec_())
