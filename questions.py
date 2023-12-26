import sys

from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QLabel, QWidget


class Square1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.color = QColor(255, 0, 0)

    def initUI(self):
        self.setGeometry(300, 300, 800, 900)
        self.setWindowTitle("Квадрат объектив 1")

        self.label = QLabel(self)
        self.label.setText("side")
        self.label.move(300, 20)

        self.label1 = QLabel(self)
        self.label1.setText("coeff")
        self.label1.move(300, 50)

        self.label2 = QLabel(self)
        self.label2.setText("n")
        self.label2.move(300, 80)

        self.btn = QPushButton("Показать", self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(30, 60)
        self.btn.clicked.connect(self.paint)

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setText("300")
        self.lineEdit.move(370, 20)

        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.setText("0.9")
        self.lineEdit_2.move(370, 50)

        self.lineEdit_3 = QLineEdit(self)
        self.lineEdit_3.setText("10")
        self.lineEdit_3.move(370, 80)
        self.do_paint = False

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
        side, coeff, n = (
            int(self.lineEdit.text()),
            float(self.lineEdit_2.text()),
            int(self.lineEdit_3.text()),
        )
        qp.setPen(self.color)
        for i in range(n):
            qp.drawRect(
                QRectF(
                    50 + (side - side * coeff**i) / 2,
                    130 + (side - side * coeff**i) / 2,
                    side * coeff**i,
                    side * coeff**i,
                )
            )


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Square1()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
