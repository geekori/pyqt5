'''

在单元格中放置控件

setItem：将文本放到单元格中
setCellWidget：将控件放到单元格中
setStyleSheet：设置控件的样式（QSS）

'''

import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem, QAbstractItemView,
                              QComboBox, QPushButton)


class PlaceControlInCell(QWidget):
    def __init__(self):
        super(PlaceControlInCell,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("在单元格中放置控件")
        self.resize(430, 300);
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)

        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['姓名','性别','体重（kg）'])
        textItem = QTableWidgetItem('小明')
        tableWidget.setItem(0,0,textItem)

        combox = QComboBox()
        combox.addItem('男')
        combox.addItem('女')
        # QSS Qt StyleSheet
        combox.setStyleSheet('QComboBox{margin:3px};')
        tableWidget.setCellWidget(0,1,combox)

        modifyButton = QPushButton('修改')
        modifyButton.setDown(True)
        modifyButton.setStyleSheet('QPushButton{margin:3px};')
        tableWidget.setCellWidget(0,2,modifyButton)

        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = PlaceControlInCell()
    example.show()
    sys.exit(app.exec_())
