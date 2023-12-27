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
        uic.loadUi("UI.ui", self)  # Загружаем дизайн
        self.draw.clicked.connect(self.paint)
        self.do_paint = False
        self.color = QColor(255, 255, 0)

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
        qp.setPen(QPen(self.color, 8))
        for i in range(n):
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
