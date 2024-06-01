from functools import partial
import random
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtGui import QFont
from PySide6.QtUiTools import QUiLoader

player = 1
win = False
game_mode = "Player vs Player"

colors = ["red", "blue", "green", "yellow", "white", "orange", "cyan", "pink"]

def click(row, col):
    global player
    global btns
    global game_mode

    if btns[row][col].text() == "": 
        if player == 1:
            main_window.text_box.setText("Turn: Player 2")
            btns[row][col].setText("X")
            player = 2
            check_win()

            if game_mode == "Player vs CPU" and not win:
                cpu_move()
        elif player == 2:
            main_window.text_box.setText("Turn: Player 1")
            btns[row][col].setText("O")
            player = 1
            check_win()

def cpu_move():
    global player
    empty_cells = [(i, j) for i in range(3) for j in range(3) if btns[i][j].text() == ""]
    if empty_cells:
        row, col = random.choice(empty_cells)
        btns[row][col].setText("O")
        player = 1
        main_window.text_box.setText("Turn: Player 1")
        check_win()

def check_win():
    global win
    win = False
    for i in range(3):
        if btns[i][0].text() == btns[i][1].text() == btns[i][2].text() != "":
            announce_winner(btns[i][0].text())
            return
        if btns[0][i].text() == btns[1][i].text() == btns[2][i].text() != "":
            announce_winner(btns[0][i].text())
            return

    if btns[0][0].text() == btns[1][1].text() == btns[2][2].text() != "":
        announce_winner(btns[0][0].text())
        return
    if btns[0][2].text() == btns[1][1].text() == btns[2][0].text() != "":
        announce_winner(btns[0][2].text())
        return

    if all(btns[i][j].text() != "" for i in range(3) for j in range(3)):
        msg_box = QMessageBox(text="It's a draw!")
        msg_box.exec()
        restart_game()

def announce_winner(player_text):
    global win
    win = True
    msg_box = QMessageBox(text=f"Player {'1' if player_text == 'X' else '2'} Won!!!")
    msg_box.exec()
    restart_game()

def change_color():
    for i in range(3):
        for j in range(3):
            random_color = random.choice(colors)
            btns[i][j].setStyleSheet(f"background-color: {random_color};")
            btns[i][j].setFont(QFont("Viner Hand ITC", 50))

def restart_game():
    global player
    global win
    player = 1
    win = False
    main_window.text_box.setText("Turn: Player 1")
    font = QFont("Viner Hand ITC", 50)
    for i in range(3):
        for j in range(3):
            btns[i][j].setText("")
            btns[i][j].setStyleSheet("background-color: black; color: yellow")
            btns[i][j].setFont(font)

def set_game_mode():
    global game_mode
    if main_window.radio_pvp.isChecked():
        game_mode = "Player vs Player"
    elif main_window.radio_pvc.isChecked():
        game_mode = "Player vs CPU"
    restart_game()

def about():
    msg_box = QMessageBox(text="Created by Erfan Hosseini\ngmail: erfanhosseini2001@gmail.com\nTelegram: @Mykween")
    msg_box.exec()

loader = QUiLoader()
app = QApplication([])
main_window = loader.load("window.ui")
main_window.show()
main_window.text_box.setText("Turn: Player 1")

btns = [[main_window.btn_1, main_window.btn_2, main_window.btn_3],
        [main_window.btn_4, main_window.btn_5, main_window.btn_6],
        [main_window.btn_7, main_window.btn_8, main_window.btn_9]]

for i in range(3):
    for j in range(3):
        btns[i][j].clicked.connect(partial(click, i, j))
main_window.btn_restart.clicked.connect(restart_game)
main_window.btn_change_color.clicked.connect(change_color)
main_window.radio_pvp.toggled.connect(set_game_mode)
main_window.radio_pvc.toggled.connect(set_game_mode)
main_window.btn_about.clicked.connect(about)

app.exec()