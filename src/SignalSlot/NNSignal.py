'''

信号槽N对N连接与断开连接



'''

from PyQt5.QtCore import *

class NNSignal(QObject):
    signal1 = pyqtSignal()
    signal2 = pyqtSignal(int)
    signal3 = pyqtSignal()
    def __init__(self):
        super(NNSignal,self).__init__()

        self.signal1.connect(self.call1)
        self.signal1.connect(self.call11)

        self.signal3.connect(self.call1)
        self.signal1.emit()
        self.signal3.emit()
        '''
        self.signal2.connect(self.signal1)

        self.signal2.emit(2)   # 触发了信号1

        self.signal1.disconnect(self.call1)
        self.signal1.disconnect(self.call11)
        self.signal2.disconnect(self.signal1)

        self.signal1.connect(self.call1)
        self.signal2.connect(self.call2)

        self.signal1.emit()
        self.signal2.emit(100)
        '''
    def call1(self):
        print("call1 emit")

    def call11(self):
        print("call11 emit")

    def call2(self,val):
        print("call2 emit:",val)
if __name__ == '__main__':
    nnSignal = NNSignal()