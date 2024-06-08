import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon, QPixmap, QTransform
from ui_mainwindow import Ui_MainWindow
import pygame

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.buttons = [self.ui.btn_rock, self.ui.btn_paper, self.ui.btn_scissors]
        self.player_score = 0
        self.computer_score = 0
        self.setStyleSheet("QMainWindow { background-image: url('background.jpg'); background-repeat: no-repeat; background-position: center; }")
        pygame.init()

        pygame.mixer.music.load("sound/background_music.mp3")
        pygame.mixer.music.play(-1)
        self.rock_sound = pygame.mixer.Sound("sound/rock.mp3")
        self.paper_sound = pygame.mixer.Sound("sound/paper.mp3")
        self.scissors_sound = pygame.mixer.Sound("sound/scissors.mp3")
        self.win_sound = pygame.mixer.Sound("sound/win.mp3")
        self.lose_sound = pygame.mixer.Sound("sound/lose.mp3")
        self.tie_sound = pygame.mixer.Sound("sound/tie.mp3")


        pixmap = QPixmap("rock.png")
        scaled_pixmap = pixmap.scaled(202, 167)
        icon = QIcon(scaled_pixmap)
        self.ui.btn_rock.setStyleSheet("background-color: black;")
        self.ui.btn_rock.setIcon(icon)
        self.ui.btn_rock.setIconSize(scaled_pixmap.size())  

        pixmap = QPixmap("paper.png")
        scaled_pixmap = pixmap.scaled(202, 167)
        icon = QIcon(scaled_pixmap)
        self.ui.btn_paper.setStyleSheet("background-color: black;")
        self.ui.btn_paper.setIcon(icon)
        self.ui.btn_paper.setIconSize(scaled_pixmap.size())  

        pixmap = QPixmap("scissors.png")
        scaled_pixmap = pixmap.scaled(202, 167)
        icon = QIcon(scaled_pixmap)
        self.ui.btn_scissors.setStyleSheet("background-color: black;")
        self.ui.btn_scissors.setIcon(icon)
        self.ui.btn_scissors.setIconSize(scaled_pixmap.size())  

        for i in range(3):
            self.buttons[i].clicked.connect(lambda _, i=i: self.play(i))
        
        self.ui.text_player.setText("Player: 0")
        self.ui.text_computer.setText("Computer: 0")
        self.ui.btn_restart.clicked.connect(self.restart_scores)
        
        self.choice_to_icon = {
            0: "rock.png",
            1: "paper.png",
            2: "scissors.png"
        }
        

    def play(self, player_choice):
        computer_choice = random.randint(0, 2) 
        self.update_button_icon(self.ui.btn_player, player_choice)
        self.update_button_icon(self.ui.btn_computer, computer_choice, flip=True)
        
        if player_choice == computer_choice:
            self.ui.text_box.setText("It's a tie!")
            self.tie_sound.play()
        elif (player_choice - computer_choice) % 3 == 1:
            self.ui.text_box.setText("You win!")
            self.win_sound.play()
            self.player_score += 1
        else:
            self.ui.text_box.setText("Computer wins!")
            self.lose_sound.play()
            self.computer_score += 1

        self.update_scores()

        if player_choice == 0:
            self.rock_sound.play()
        elif player_choice == 1:
            self.paper_sound.play()
        elif player_choice == 2:
            self.scissors_sound.play()

    def update_button_icon(self, button, choice, flip=False):
        pixmap = QPixmap(self.choice_to_icon[choice])
        if flip:
            pixmap = pixmap.transformed(QTransform().rotate(180))
        scaled_pixmap = pixmap.scaled(202, 167)
        icon = QIcon(scaled_pixmap)
        button.setStyleSheet("background-color: black;")
        button.setIcon(icon)
        button.setIconSize(scaled_pixmap.size())  
        self.update_scores()

    def update_scores(self):
        self.ui.text_player.setText(f"Player: {self.player_score}")
        self.ui.text_computer.setText(f"Computer: {self.computer_score}")


    def restart_scores(self):
        self.player_score = 0
        self.computer_score = 0
        self.update_scores()

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())
