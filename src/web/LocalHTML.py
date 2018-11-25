'''

装载本地Web页面

'''

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys
import os
class WebEngineView(QMainWindow):

    def __init__(self ):
        super(WebEngineView, self).__init__()
        self.setWindowTitle('装载本地Web页面')
        self.setGeometry(5, 30, 1355, 730)
        url = os.getcwd() + '/test.html'
        self.browser = QWebEngineView()
        self.browser.load(QUrl.fromLocalFile(url))

        self.setCentralWidget(self.browser)


        print(os.getcwd())
if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = WebEngineView()
	win.show()
	sys.exit(app.exec_())
