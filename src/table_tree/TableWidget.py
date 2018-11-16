'''

扩展的表格控件（QTableWidget）

QTableView

每一个Cell（单元格）是一个QTableWidgetItem

'''

import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem, QAbstractItemView)


class TableWidgetDemo(QWidget):
    def __init__(self):
        super(TableWidgetDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget演示")
        self.resize(430, 230);
        layout = QHBoxLayout()
        tablewidget = QTableWidget()
        tablewidget.setRowCount(4)
        tablewidget.setColumnCount(3)

        layout.addWidget(tablewidget)

        tablewidget.setHorizontalHeaderLabels(['姓名','年龄','籍贯'])
        nameItem = QTableWidgetItem("小明")
        tablewidget.setItem(0,0,nameItem)

        ageItem = QTableWidgetItem("24")
        tablewidget.setItem(0,1,ageItem)

        jgItem = QTableWidgetItem("北京")
        tablewidget.setItem(0,2,jgItem)

        # 禁止编辑
        tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 整行选择
        tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 调整列和行
        tablewidget.resizeColumnsToContents()
        tablewidget.resizeRowsToContents()

        tablewidget.horizontalHeader().setVisible(False)
     #   tablewidget.verticalHeader().setVisible(False)

        tablewidget.setVerticalHeaderLabels(["a","b"])

        # 隐藏表格线
        tablewidget.setShowGrid(False)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = TableWidgetDemo()
    example.show()
    sys.exit(app.exec_())
