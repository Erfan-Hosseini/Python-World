import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.kind = "normal"
        self.password = ""
        self.lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', ':', ';', '"', "'", '<', '>', ',', '.', '/', '?']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        self.ui.btn_generate.clicked.connect(self.generate)

    def generate(self):
        self.password = ""
        if self.ui.radio_1.isChecked():
            self.kind = "normal"
            self.password += random.choice(self.uppercase_letters)
            self.password += random.choice(self.special_characters)  
            self.password += random.choice(self.numbers) 
            password_length = 8
        elif self.ui.radio_2.isChecked():
            self.kind = "strong"
            self.password += random.choice(self.uppercase_letters) 
            self.password += random.choice(self.special_characters) 
            self.password += random.choice(self.special_characters) 
            self.password += random.choice(self.numbers)
            password_length = 12
        elif self.ui.radio_3.isChecked():
            self.kind = "super"
            password_length = 20
        
        for _ in range(password_length - 4): 
            self.password += random.choice(self.lowercase_letters + self.uppercase_letters + self.special_characters + self.numbers)
        
        self.ui.text_box.setText(self.password)

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())
