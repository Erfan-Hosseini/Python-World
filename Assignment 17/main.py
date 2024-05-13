import math
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader



global flg_empty
flg_empty=0

def zero():
    if my_window.txt_1.text() == "":
        my_window.txt_1.setText('0')
    else:
        my_window.txt_1.setText(my_window.txt_1.text() + '0')

def one():
    global flg_empty
    if flg_empty:
        my_window.txt_1.setText('1')
        flg_empty=0
    else:
        my_window.txt_1.setText(my_window.txt_1.text()+'1')

def two():
    global flg_empty
    if flg_empty :
        my_window.txt_1.setText('2')
        flg_empty=0
    else:
        my_window.txt_1.setText(my_window.txt_1.text()+'2')

def three():
    global flg_empty
    if flg_empty:
        my_window.txt_1.setText('3')
        flg_empty=0
    else:
        my_window.txt_1.setText(my_window.txt_1.text()+'3')

def four():
    global flg_empty
    if flg_empty:
        my_window.txt_1.setText('4')
        flg_empty=0
    else:
        my_window.txt_1.setText(my_window.txt_1.text()+'4')

def five():
    global flg_empty
    if flg_empty:
        my_window.txt_1.setText('5')
        flg_empty=0
    else:
        my_window.txt_1.setText(my_window.txt_1.text()+'5')

def six():
    global flg_empty
    if flg_empty:
        my_window.txt_1.setText('6')
        flg_empty=0
    else:
        my_window.txt_1.setText(my_window.txt_1.text()+'6')

def seven():
    global flg_empty
    if flg_empty:
        my_window.txt_1.setText('7')
        flg_empty=0
    else:
        my_window.txt_1.setText(my_window.txt_1.text()+'7')

def eight():
    global flg_empty
    if flg_empty:
        my_window.txt_1.setText('8')
        flg_empty=0
    else:
        my_window.txt_1.setText(my_window.txt_1.text()+'8')

def nine():
    global flg_empty
    if flg_empty:
        my_window.txt_1.setText('9')
        flg_empty=0
    else:
        my_window.txt_1.setText(my_window.txt_1.text()+'9')
    
def decimal_point():
    my_window.txt_1.setText(my_window.txt_1.text()+'.')

def sub():
    global A,O
    if my_window.txt_1.text()=="":
        my_window.txt_1.setText("0")
    A=float(my_window.txt_1.text())
    my_window.txt_1.setText("")
    O="-"

def sum():
    global A,O
    if my_window.txt_1.text()=="":
        my_window.txt_1.setText("0")
    A=float(my_window.txt_1.text())
    my_window.txt_1.setText("")
    O="+"

def mul():
    global A,O
    if my_window.txt_1.text()=="":
        my_window.txt_1.setText("0")
    A=float(my_window.txt_1.text())
    my_window.txt_1.setText("")
    O="*"

def div():
    global A,O
    if my_window.txt_1.text()=="":
        my_window.txt_1.setText("0")
    A=float(my_window.txt_1.text())
    my_window.txt_1.setText("")
    O="/"


def sqrt():
    global flg_empty
    my_window.txt_1.setText(str(math.sqrt(float(my_window.txt_1.text()))))
    flg_empty=1

def log():
    global flg_empty
    my_window.txt_1.setText(str(math.log(float(my_window.txt_1.text()))))
    flg_empty=1

def sin():
    global flg_empty
    my_window.txt_1.setText(str(math.sin(float(my_window.txt_1.text()))))
    flg_empty=1

def cos():
    global flg_empty
    my_window.txt_1.setText(str(math.cos(float(my_window.txt_1.text()))))
    flg_empty=1

def tan():
    global flg_empty
    my_window.txt_1.setText(str(math.tan(float(my_window.txt_1.text()))))
    flg_empty=1

def cot():
    global flg_empty
    my_window.txt_1.setText(str(1/math.sin(float(my_window.txt_1.text()))))
    flg_empty=1



def Result():
        global flg_empty
        B=float(my_window.txt_1.text())
        if(O=="+"):        
            result=A+B 
        elif(O=="-"):
            result=A-B 
        elif(O=="*"):
            result=A*B 
        elif(O=="/"):
            while(B==0):
                B=float(my_window.txt_1.text())
            result=A/B 
        elif(O=="^"):
            result=(A)**(B )
        my_window.txt_1.setText(str(result))

        flg_empty=1


def clear():
    my_window.txt_1.setText("")


loader=QUiLoader()

my_app=QApplication([])

my_window=loader.load("mainwindow.ui")

my_window.show()
my_window.btn_sub.clicked.connect(sub)
my_window.btn_sum.clicked.connect(sum)
my_window.btn_multiply.clicked.connect(mul)
my_window.btn_divide.clicked.connect(div)
my_window.btn_sqrt.clicked.connect(sqrt)
my_window.btn_log.clicked.connect(log)
my_window.btn_sin.clicked.connect(sin)
my_window.btn_cos.clicked.connect(cos)
my_window.btn_tan.clicked.connect(tan)
my_window.btn_cot.clicked.connect(cot)
my_window.btn_clear.clicked.connect(clear)
my_window.btn_equal.clicked.connect(Result)
my_window.btn_0.clicked.connect(zero)
my_window.btn_1.clicked.connect(one)
my_window.btn_2.clicked.connect(two)
my_window.btn_3.clicked.connect(three)
my_window.btn_4.clicked.connect(four)
my_window.btn_5.clicked.connect(five)
my_window.btn_6.clicked.connect(six)
my_window.btn_7.clicked.connect(seven)
my_window.btn_8.clicked.connect(eight)
my_window.btn_9.clicked.connect(nine)
my_window.btn_dot.clicked.connect(decimal_point)


my_app.exec()