'''

使用PyQtGraph绘图

pip Install pyqtgraph
'''


from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication
import pyqtgraph as pg
from pyqtgraph_pyqt import Ui_MainWindow
import numpy as np



class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(MainWindow, self).__init__(parent)

        pg.setConfigOption('background', '#f0f0f0')
        pg.setConfigOption('foreground', 'd')


        self.setupUi(self)
        self.draw1()
        self.draw2()


    def draw1(self):

        self.pyqtgraph1.clear()

        '''第一种绘图方式'''
        print(np.random.normal(size=120))
        self.pyqtgraph1.addPlot(title="绘图单条线", y=np.random.normal(size=120), pen=pg.mkPen(color='b', width=2))

        '''第二种绘图方式'''
        plt2 = self.pyqtgraph1.addPlot(title='绘制多条线')

        plt2.plot(np.random.normal(size=150), pen=pg.mkPen(color='r', width=2),
                  name="Red curve")
        plt2.plot(np.random.normal(size=110) + 5, pen=(0, 255, 0), name="Green curve")
        plt2.plot(np.random.normal(size=120) + 10, pen=(0, 0, 255), name="Blue curve")


    def draw2(self):


        plt = self.pyqtgraph2.addPlot(title='绘制条状图')
        x = np.arange(10)
        print(x)
        y1 = np.sin(x)
        y2 = 1.1 * np.sin(x + 1)
        y3 = 1.2 * np.sin(x + 2)

        bg1 = pg.BarGraphItem(x=x, height=y1, width=0.3, brush='r')
        bg2 = pg.BarGraphItem(x=x + 0.33, height=y2, width=0.3, brush='g')
        bg3 = pg.BarGraphItem(x=x + 0.66, height=y3, width=0.3, brush='b')

        plt.addItem(bg1)
        plt.addItem(bg2)
        plt.addItem(bg3)

        self.pyqtgraph2.nextRow()

        p4 = self.pyqtgraph2.addPlot(title="参数图+显示网格")
        x = np.cos(np.linspace(0, 2 * np.pi, 1000))
        y = np.sin(np.linspace(0, 4 * np.pi, 1000))
        p4.plot(x, y, pen=pg.mkPen(color='d', width=2))
        #p4.showGrid(x=True, y=True)  # 显示网格



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
