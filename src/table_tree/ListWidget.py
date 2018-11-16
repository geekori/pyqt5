'''

扩展的列表控件（QListWidget）

QListView
'''
from PyQt5.QtWidgets import *
import sys

class ListWidgetDemo(QMainWindow):
	def __init__(self, parent=None):
		super(ListWidgetDemo, self).__init__(parent)
		self.setWindowTitle("QListWidget 例子")
		self.resize(300, 270)
		self.listwidget = QListWidget()
		self.listwidget.addItem("item1")
		self.listwidget.addItem("item2")
		self.listwidget.addItem("item3")
		self.listwidget.addItem("item4")
		self.listwidget.addItem("item5")
		self.listwidget.itemClicked.connect(self.clicked)
		self.setCentralWidget(self.listwidget)
	def clicked(self,Index):
		QMessageBox.information(self,"QListWidget","您选择了：" + self.listwidget.item(self.listwidget.row(Index)).text())



if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = ListWidgetDemo()
	win.show()
	sys.exit(app.exec_())
