'''

缩放图片

QImage.scaled

'''

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
import sys


class ScaleImage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("图片大小缩放例子")
        filename = './images/Cloudy_72px.png'
        img = QImage(filename)
        label1 = QLabel(self)
        label1.setFixedWidth(200)
        label1.setFixedHeight(200)

        result = img.scaled(label1.width(),label1.height(),Qt.IgnoreAspectRatio,Qt.SmoothTransformation)
        label1.setPixmap(QPixmap.fromImage(result))

        vbox = QVBoxLayout()
        vbox.addWidget(label1)

        self.setLayout(vbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ScaleImage()
    win.show()
    sys.exit(app.exec_())

