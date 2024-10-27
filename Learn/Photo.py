import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
  QApplication,
  QMainWindow,
  QPushButton,
  QLabel,
  QLineEdit,
  QVBoxLayout
)
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')

        widget = QLabel()
        widget.setPixmap(QPixmap('Easy.png'))
        widget.setScaledContents(True)

        self.setCentralWidget(widget)
        self.setMinimumSize(QSize(100, 100))

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()