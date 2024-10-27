import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QLineEdit,
    QVBoxLayout, QWidget
)
from PyQt6.QtGui import QPixmap, QColor, QPalette
from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        color1 = Color('red')
        color2 = Color('blue')
        color3 = Color('green')

        layout = QVBoxLayout()
        layout.addWidget(color1)
        layout.addWidget(color2)
        layout.addWidget(color3)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
win_ow = MainWindow()
win_ow.show()
app.exec()