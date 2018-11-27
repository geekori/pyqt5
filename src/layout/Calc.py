'''

栅格布局：实现计算器UI

'''

import sys,math
from PyQt5.QtWidgets import *


class Calc(QWidget) :
    def __init__(self):
        super(Calc,self).__init__()
        self.setWindowTitle("栅格布局")

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls','Back','','Close',
                 '7','8','9','/',
                 '4','5','6','*',
                 '1','2','3','-',
                 '0','.','=','+']

        positions = [(i,j) for i in range(5) for j in range(4)]
        print(positions)

        for position,name in zip(positions,names):
            if name == '':
                continue
            button = QPushButton(name)
           # print(position)
            grid.addWidget(button,*position)









if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Calc()
    main.show()
    sys.exit(app.exec_())