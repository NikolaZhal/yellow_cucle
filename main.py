import sys

from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
    QLineEdit,
    QLabel,
    QWidget,
    QMainWindow,
)
from PyQt5 import uic  # Импортируем uic
from random import randint
import sys


class Square1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.draw.clicked.connect(self.paint)
        self.do_paint = False

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle("Кружочки")

        self.draw = QPushButton("Draw", self)
        self.draw.resize(self.draw.sizeHint())
        self.draw.move(30, 30)
        self.draw.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        n = randint(2, 8)
        for i in range(n):
            color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            qp.setPen(QPen(color, 8))
            diametr = randint(8, 300)
            x, y = randint(75, 500 - diametr), randint(75, 500 - diametr)
            qp.drawEllipse(x, y, diametr, diametr)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Square1()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
