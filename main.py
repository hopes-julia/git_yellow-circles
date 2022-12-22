import sys

from random import randrange
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QLineEdit, QComboBox
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QInputDialog, QPushButton, QWidget, QTableView, QPlainTextEdit


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        self.do_paint = False
        self.ch = 0
        self.coords = []
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.do_paint = True
        self.ch += 1
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.ch != 0:
            # Создаем объект QPainter для рисования
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            self.draw(qp)
            # Завершаем рисование
            qp.end()

    def draw(self, qp):
        # Задаем кисть
        if self.ch == len(self.coords) + 1:
            x = randrange(600)
            y = randrange(500)
            d = randrange(15, 60)
            self.coords.append([x, y, d])
        qp.setBrush(QColor(238, 234, 140))
        for i in self.coords:
            # Рисуем прямоугольник заданной кистью
            qp.drawEllipse(i[0], i[1], i[2], i[2])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
