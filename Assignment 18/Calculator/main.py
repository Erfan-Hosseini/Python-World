import math
from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

global flg_empty, A, O
flg_empty = 0

def number_click(digit):
    global flg_empty
    if flg_empty:
        my_window.txt_1.setText(str(digit))
        flg_empty = 0
    else:
        my_window.txt_1.setText(my_window.txt_1.text() + str(digit))

def decimal_point():
    my_window.txt_1.setText(my_window.txt_1.text() + '.')

def operation(op):
    global A, O
    if my_window.txt_1.text() == "":
        my_window.txt_1.setText("0")
    A = float(my_window.txt_1.text())
    my_window.txt_1.setText("")
    O = op

def sqrt():
    global flg_empty
    my_window.txt_1.setText(str(math.sqrt(float(my_window.txt_1.text()))))
    flg_empty = 1

def log():
    global flg_empty
    my_window.txt_1.setText(str(math.log(float(my_window.txt_1.text()))))
    flg_empty = 1

def sin():
    global flg_empty
    my_window.txt_1.setText(str(math.sin(float(my_window.txt_1.text()))))
    flg_empty = 1

def cos():
    global flg_empty
    my_window.txt_1.setText(str(math.cos(float(my_window.txt_1.text()))))
    flg_empty = 1

def tan():
    global flg_empty
    my_window.txt_1.setText(str(math.tan(float(my_window.txt_1.text()))))
    flg_empty = 1

def cot():
    global flg_empty
    my_window.txt_1.setText(str(1 / math.tan(float(my_window.txt_1.text()))))
    flg_empty = 1

def result():
    global flg_empty, A, O
    B = float(my_window.txt_1.text())
    if O == "+":
        res = A + B
    elif O == "-":
        res = A - B
    elif O == "*":
        res = A * B
    elif O == "/":
        res = A / B if B != 0 else float('inf')
    elif O == "^":
        res = A ** B
    my_window.txt_1.setText(str(res))
    flg_empty = 1

def clear():
    my_window.txt_1.setText("")

loader = QUiLoader()
my_app = QApplication([])
my_window = loader.load("mainwindow.ui")
my_window.show()

for i in range(10):
    getattr(my_window, f'btn_{i}').clicked.connect(partial(number_click, i))

my_window.btn_dot.clicked.connect(decimal_point)
my_window.btn_sub.clicked.connect(partial(operation, "-"))
my_window.btn_sum.clicked.connect(partial(operation, "+"))
my_window.btn_multiply.clicked.connect(partial(operation, "*"))
my_window.btn_divide.clicked.connect(partial(operation, "/"))
my_window.btn_sqrt.clicked.connect(sqrt)
my_window.btn_log.clicked.connect(log)
my_window.btn_sin.clicked.connect(sin)
my_window.btn_cos.clicked.connect(cos)
my_window.btn_tan.clicked.connect(tan)
my_window.btn_cot.clicked.connect(cot)
my_window.btn_clear.clicked.connect(clear)
my_window.btn_equal.clicked.connect(result)

my_app.exec()