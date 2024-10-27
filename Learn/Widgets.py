import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
  QApplication,
  QMainWindow,
  QPushButton,
  QLabel,
  QLineEdit,
  QVBoxLayout,
  QWidget,
  QSlider,
  QSpinBox,
  QDial,
) 

from random import choice


window_title = [
    'My_App',
    'My_App',
    'Still_My_App',
    'What_On_Earth',
    'This_Is_Surprising',
    'Something_Went_Wrong'
]

class MainWindow(QMainWindow):
    def button_close(self):
      self.button.setText('You Already Clicked Me!')
      self.button.setEnabled(False)

      self.setWindowTitle("My OneShot App")

    def button_toggle(self, checked):
      self.button_checked = checked
      print(self.button_checked)

    def button_released(self):
      self.button_checked = self.button.isChecked()
      print(self.button_checked)

    def button_clicked(self):
      print('Clicked!')
      win_tit = choice(window_title)
      self.setWindowTitle(win_tit)

      if win_tit == 'Something_Went_Wrong':
        self.button.setEnabled(False)
        self.button.setText("Can't Press Me Anymore")

    def change_txt(self, lbl):
      text = choice(window_title)
      self.lbl.setText(text)


    def __init__(self):
      super().__init__() 
      
      self.button_checked = True

      self.setWindowTitle("My App")
    
      self.button = QPushButton("Press Me!")
      # self.button.setCheckable(True)
      self.button.clicked.connect(self.change_txt)
      # self.button.clicked.connect(self.button_close)
      # self.button.clicked.connect(self.button_toggle)
      # self.button.released.connect(self.button_released)
      # self.button.clicked.connect(self.button_clicked)
      # self.button.setChecked(self.button_checked)

      self.label = QLabel()
      self.input = QLineEdit()
      self.input.textChanged.connect(self.label.setText)
      self.lbl = QLabel('1')
      font = self.label.font()
      fon = self.lbl.font()
      font.setPointSize(30)
      fon.setPointSize(30)
      self.label.setFont(font)
      self.lbl.setFont(font)
      self.label.setAlignment(
        Qt.AlignmentFlag.AlignHCenter
        | Qt.AlignmentFlag.AlignVCenter
      )
      self.lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

      layout1 = QVBoxLayout()
      layout1.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignHCenter)
      # layout1.addWidget(self.input)
      # layout1.addWidget(self.label)

      layout_p = QVBoxLayout()
      layout_p.addLayout(layout1)
      layout_p.addWidget(self.lbl)

      container = QWidget()
      container.setLayout(layout_p)

      self.slider = QSlider()
      self.dial = QDial()
      self.spin = QSpinBox()

      # self.setCentralWidget(self.button)
      self.setCentralWidget(container)
      # self.setCentralWidget(self.dial)
      
      self.button.setFixedSize(QSize(100,100))
      self.setFixedSize(QSize(450,450))



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()