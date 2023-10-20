from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
import math


app = QApplication([])  # Создание приложения
mw = QWidget() # Создание окна
mw.setWindowTitle('калькулятор')
mw.resize(500, 200)
mw.move(520,300)

def plus_action():
    a = float(first.text())
    b = float(second.text())
    result.setText(f'Результат: {a+b}')
def minus_action():
    a = float(first.text())
    b = float(second.text())
    result.setText(f'Результат: {a-b}')
def div_action():
    a = float(first.text())
    b = float(second.text())
    result.setText(f'Результат: {a%b}')
def mul_action():
    a = float(first.text())
    b = float(second.text())
    result.setText(f'Результат: {a*b}')
def step_action():
    a = float(first.text())
    b = float(second.text())
    result.setText(f'Результат: {a**b}')
def koren():
    a = float(first.text())
    result.setText(f'Результат: {math.sqrt(a)}')

v_line = QVBoxLayout()
first = QLineEdit()
v_line.addWidget(first)


h_line = QHBoxLayout()
plus = QPushButton('+')
plus.clicked.connect(plus_action)

min = QPushButton('─︎')
min.clicked.connect(minus_action)

div = QPushButton('÷')
div.clicked.connect(div_action)

mul = QPushButton('⨉')
mul.clicked.connect(mul_action)

step = QPushButton('^')
step.clicked.connect(step_action)

kor = QPushButton('√')
kor.clicked.connect(koren)

h_line.addWidget(plus)
h_line.addWidget(min)
h_line.addWidget(div)
h_line.addWidget(mul)
h_line.addWidget(step)
h_line.addWidget(kor)
v_line.addLayout(h_line)

second = QLineEdit()
v_line.addWidget(second)

result = QLabel('Результат: ')
v_line.addWidget(result)

mw.setLayout(v_line)  # Закрепляем направляющую на окне
mw.show()  # Показать окно
app.exec_()
