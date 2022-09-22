import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from math import sqrt


class Window(QWidget):
    numbers = []
    signs = []

    def add_digit(self, digit: str):
        if len(self.numbers) == 0:
            self.numbers.append("")
        number = self.numbers[-1]
        number += digit
        self.numbers[-1] = number
        self.update_label()

    def add_sign(self, sign: str):
        self.signs.append(sign)
        self.numbers.append("")
        self.update_label()

    def update_label(self) -> None:
        result = []
        maxlen = max(len(self.numbers), len(self.signs))
        for i in range(maxlen):
            if i < len(self.numbers):
                result.append(self.numbers[i])
            if i < len(self.signs):
                result.append(self.signs[i])
        self.label.setText(" ".join(result))

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Calc")

        self.vbox = QVBoxLayout()
        self.hbox0 = QHBoxLayout()
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.hbox3 = QHBoxLayout()
        self.hbox4 = QHBoxLayout()
        self.hbox5 = QHBoxLayout()
        self.hbox6 = QHBoxLayout()

        self.label = QLabel()
        self.result = QLabel()

        # Создание кнопок
        # line 6
        self.btn_score = QPushButton("=")
        self.hbox6.addWidget(self.btn_score)
        self.btn_score.clicked.connect(self._score)

        # line 5
        self.btn_7 = QPushButton("7")
        self.hbox5.addWidget(self.btn_7)
        self.btn_7.clicked.connect(self._7)

        self.btn_8 = QPushButton("8")
        self.hbox5.addWidget(self.btn_8)
        self.btn_8.clicked.connect(self._8)

        self.btn_9 = QPushButton("9")
        self.hbox5.addWidget(self.btn_9)
        self.btn_9.clicked.connect(self._9)

        self.btn_0 = QPushButton("0")
        self.hbox5.addWidget(self.btn_0)
        self.btn_0.clicked.connect(self._0)

        # line 4
        self.btn_4 = QPushButton("4")
        self.hbox4.addWidget(self.btn_4)
        self.btn_4.clicked.connect(self._4)

        self.btn_5 = QPushButton("5")
        self.hbox4.addWidget(self.btn_5)
        self.btn_5.clicked.connect(self._5)

        self.btn_6 = QPushButton("6")
        self.hbox4.addWidget(self.btn_6)
        self.btn_6.clicked.connect(self._6)

        self.btn_C = QPushButton("C")
        self.hbox4.addWidget(self.btn_C)
        self.btn_C.clicked.connect(self._C)

        # line 3
        self.btn_1 = QPushButton("1")
        self.hbox3.addWidget(self.btn_1)
        self.btn_1.clicked.connect(self._1)

        self.btn_2 = QPushButton("2")
        self.hbox3.addWidget(self.btn_2)
        self.btn_2.clicked.connect(self._2)

        self.btn_3 = QPushButton("3")
        self.hbox3.addWidget(self.btn_3)
        self.btn_3.clicked.connect(self._3)

        self.btn_comma = QPushButton(",")
        self.hbox3.addWidget(self.btn_comma)
        self.btn_comma.clicked.connect(self._comma)

        # line 2
        self.btn_plus = QPushButton("+")
        self.hbox2.addWidget(self.btn_plus)
        self.btn_plus.clicked.connect(self._plus)

        self.btn_minus = QPushButton("-")
        self.hbox2.addWidget(self.btn_minus)
        self.btn_minus.clicked.connect(self._minus)

        self.btn_multyplication = QPushButton("*")
        self.hbox2.addWidget(self.btn_multyplication)
        self.btn_multyplication.clicked.connect(self._multyplication)

        self.btn_division = QPushButton(":")
        self.hbox2.addWidget(self.btn_division)
        self.btn_division.clicked.connect(self._division)

        # line 1
        self.hbox1.addWidget(self.label)

        # line 0
        self.hbox0.addWidget(self.result)
        # Конец создания кнопок

        self.setLayout(self.vbox)
        self.vbox.addLayout(self.hbox0)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox5)
        self.vbox.addLayout(self.hbox6)

    # Объявление функций кнопок
    def _score(self):
        if len(self.numbers) == 0 and len(self.signs) == 0:
            return
        self.update_label()
        score = self.label.text()
        try:
            result = eval(score)
        except Exception as e:
            result = str(e)
        self.result.setText(str(result))

    def _7(self):
        self.add_digit("7")

    def _8(self):
        self.add_digit("8")

    def _9(self):
        self.add_digit("9")

    def _0(self):
        self.add_digit("0")

    def _4(self):
        self.add_digit("4")

    def _5(self):
        self.add_digit("5")

    def _6(self):
        self.add_digit("6")

    def _C(self):
        self.numbers = []
        self.signs = []
        self.label.setText("")
        self.result.setText("")

    def _1(self):
        self.add_digit("1")

    def _2(self):
        self.add_digit("2")

    def _3(self):
        self.add_digit("3")

    def _comma(self):
        self.add_digit(".")

    def _plus(self):
        self.add_sign("+")

    def _minus(self):
        self.add_sign("-")

    def _multyplication(self):
        self.add_sign("*")

    def _division(self):
        self.add_sign("/")


# Конец объявления функций кнопок


# Конец окна
app = QApplication(sys.argv)

win = Window()

win.show()

sys.exit(app.exec_())
