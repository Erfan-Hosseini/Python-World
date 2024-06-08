import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFont
from ui_mainwindow import Ui_MainWindow
import pygame

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.time = 0
        self.timer_active = True
        self.timer_paused = False
        self.timer_interval = 1000
        self.timer_id = self.startTimer(self.timer_interval)
        self.buttons = [[self.ui.btn_1, self.ui.btn_2, self.ui.btn_3, self.ui.btn_4],
                        [self.ui.btn_5, self.ui.btn_6, self.ui.btn_7, self.ui.btn_8],
                        [self.ui.btn_9, self.ui.btn_10, self.ui.btn_11, self.ui.btn_12],
                        [self.ui.btn_13, self.ui.btn_14, self.ui.btn_15, self.ui.btn_16]]
        pygame.init()
        pygame.mixer.music.load("background_music.mp3")
        pygame.mixer.music.play(-1)
        self.move_sound = pygame.mixer.Sound("move.mp3")

        self.generate_num()
        for i in range(4):
            for j in range(4):
                self.buttons[i][j].clicked.connect(partial(self.play, i, j))
        self.ui.btn_pause.clicked.connect(self.pause_game)
        self.ui.btn_unpause.clicked.connect(self.unpause_game)
        self.ui.btn_restart.clicked.connect(self.restart_game)
        self.setStyleSheet("QMainWindow { background-image: url('wood.jpg'); background-repeat: no-repeat; background-position: center; }")

    def generate_num(self):
        nums = list(range(1, 17))  
        random.shuffle(nums)
        button_font = QFont("Segoe Script", 20)       
        for i in range(4):
            for j in range(4):
                num = nums.pop()   
                self.buttons[i][j].setText(str(num)) 
                button = self.buttons[i][j]
                button.setFont(button_font)
                button.setStyleSheet("background-color: black; color: yellow")
                if num == 16:
                    self.buttons[i][j].setVisible(False)

                    self.empty_i = i
                    self.empty_j = j

    def play(self, i, j):
        if not self.timer_active:
            return

        if (i == self.empty_i and abs(j - self.empty_j) == 1) or \
                (j == self.empty_j and abs(i - self.empty_i) == 1):
            self.buttons[self.empty_i][self.empty_j].setText(self.buttons[i][j].text())
            self.buttons[i][j].setText("16")
            self.buttons[self.empty_i][self.empty_j].setVisible(True)
            self.buttons[i][j].setVisible(False)
            self.move_sound.play()
            self.empty_i = i
            self.empty_j = j

            if self.check_win():
                self.game_won()

    def check_win(self):
        index = 1
        for i in range(4):
            for j in range(4):
                if int(self.buttons[i][j].text()) != index:
                    return False
                index += 1
        return True

    def timerEvent(self, event):
        if self.timer_active and not self.timer_paused:
            self.time += 1
            self.ui.text_box.setText(str(self.time))

    def pause_game(self):
        self.timer_paused = True
        self.ui.text_box.setText("Paused")

    def unpause_game(self):
        self.timer_paused = False
        self.ui.text_box.setText(str(self.time))

    def restart_game(self):
        self.time = 0
        self.ui.text_box.setText("0")
        for i in range(4):
            for j in range(4):
                self.buttons[i][j].setVisible(True)
        self.generate_num()

    def game_won(self):
        self.timer_active = False
        self.ui.text_box.setText("You Won!!!")

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())
