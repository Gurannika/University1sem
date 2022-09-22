import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton

class Window(QWidget):
def __init__(self):
super(Window, self).__init__()

self.setWindowTitle("My App")

self.vbox = QVBoxLayout()

self.label = QLabel("Hello")
self.input = QLineEdit()
self.button = QPushButton("Push me!")

self.vbox.addWidget(self.input)
self.vbox.addWidget(self.label)
self.vbox.addWidget(self.button)

self.setLayout(self.vbox)

self.button.clicked.connect(self._reaction)
def _reaction(self):
inp = self.input.text()
self.label.setText(inp)

app = QApplication(sys.argv)

win = Window()
win.show()

sys.exit(app.exec_())
