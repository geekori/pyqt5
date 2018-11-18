'''

在表格中快速定位到特定的行

1. 数据的定位：findItems  返回一个列表
2. 如果找到了满足条件的单元格，会定位到单元格所在的行：setSliderPosition(row)

'''

import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QColor, QBrush


class DataLocation(QWidget):
    def __init__(self):
        super(DataLocation,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget 例子")
        self.resize(600, 800);

        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(40)
        tableWidget.setColumnCount(4)

        layout.addWidget(tableWidget)

        for i in range(40):
            for j in range(4):
                itemContent = '(%d,%d)' %(i,j)
                tableWidget.setItem(i,j,QTableWidgetItem(itemContent))
        self.setLayout(layout)

        # 搜索满足条件的Cell
        text = '(1'
        items = tableWidget.findItems(text,QtCore.Qt.MatchStartsWith)
        if len(items) > 0:
            item = items[0]
            item.setBackground(QBrush(QColor(0,255,0)))
            item.setForeground(QBrush(QColor(255,0,0)))

            row = item.row()

            # 定位到指定的行
            tableWidget.verticalScrollBar().setSliderPosition(row)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = DataLocation()
    example.show()
    sys.exit(app.exec_())


