import pyfiglet
import time
import random

start_time = time.time()

def show_board():
    print("\n-----------------")
    for row in game_board:
        for col in row:
            print("|",col, end=" | ")
        print("\n-----------------")
        
def check_win(game_board, symbol):
    for row in game_board:
        count = 0
        for cell in row:
            if cell == symbol:
                count += 1
        if count == 3:
            return True,True
    
    for col in range(3):
        count = 0
        for row in range(3):
            if game_board[row][col] == symbol:
                count += 1
        if count == 3:
            return True,True
    
    count = 0
    for i in range(3):
        if game_board[i][i] == symbol:
            count += 1
    if count == 3:
        return True,True
    
    count = 0
    for i in range(3):
        if game_board[i][2-i] == symbol:
            count += 1
    if count == 3:
        return True,True

    return False,False

def check_draw(game_board):
    for row in game_board:
        for col in row:
            if isinstance(col, int):
                return False
    return True



againts = "player"
player1 = "Player 1"
player2 = "Player 2"
computer_name = "Computer"
symbol1 = "X"
symbol2 = "O"
n = 0
draw = False
check_game = False

print(pyfiglet.figlet_format("        Welcome \n                      to \n Tic Tak Toe", font="Doom"))
print("----------------------------------------------------------------------------------------------")

while True:
    print("\nEnter your desired input.")
    answer = input("start/setting/exit: ").lower()
    
    if answer == "setting":
        print("\nHere, you can change the symbols of X and O to something you like. select if you want to play againts another")
        print("player or computer. change the name of player 1, player 2 or computer.\n")
        answer = input("symbol/againts/name: ").lower()
        
        if answer == "symbol":
            while True:
                symbol1 = input("Enter the symbol for player 1: ")
                if len(symbol1) != 1:
                    print("Enter only one symbol.")
                    continue
                
                symbol2 = input("Enter the symbol for player 2: ")
                if len(symbol2) != 1:
                    print("Enter only one symbol.")
                    continue
                
                print("Changes were made.")
                break
            
        elif answer == "againts":
            while True:
                print("Do you want to play againts another player or computer? (The default was player.)")
                againts = input("player/computer: ").lower()
                
                if againts == "player":
                    againts = "player"
                    print("Changes were made.")
                    break
                
                elif againts == "computer":
                    againts = "computer"
                    print("Changes were made.")
                    break
                
                else:
                    print("Invalid input")
                    
        elif answer == "name":
            player1 = input("Enter the name of player 1: ")
            player2 = input("Enter the name of player 2: ")
            computer_name = input("Enter the name of the computer: ")
            print("Changes were made.")
            
        else:
            print("Invalid input, let's go to main menu.")
            
    elif answer == "start":
        game_board = [[1,2,3]
             ,[4,5,6]              
             ,[7,8,9]]
        print("Let's go, you are againts:", againts)
        
        if againts == "player":
            show_board()
            while True:
                #player 1
                while True:
                    print("\nGo",player1)
                    player1_answer = input("\nWhere do you want to put your symbol? ")
                                       
                    if  1>int(player1_answer) or 9<int(player1_answer):
                        print("enter a number from the board.")
                        continue
                    
                    for row_idx, row in enumerate(game_board):
                        for col_idx, col in enumerate(row):
                            if col == int(player1_answer):
                                game_board[row_idx][col_idx] = symbol1
                                show_board()
                                n = 1
                                break
                        else:
                                continue
                        break  
                    else:
                        print("There is a symbol there, try again.")
                        
                    check_game,m = check_win(game_board, symbol1)
                    if check_game:
                        print(player1, "wins!")
                        break
                    if n == 1:
                        n = 0
                        break
                if m:
                    break
                
                if check_draw(game_board):
                    print("It's a draw!")
                    break
                #player 2
                while True:
                    print("\nGo",player2)
                    player2_answer = input("\nWhere do you want to put your symbol? ")
                                       
                    if  1>int(player2_answer) or 9<int(player2_answer):
                        print("enter a number from the board.")
                        continue
                    
                    for row_idx, row in enumerate(game_board):
                        for col_idx, col in enumerate(row):
                            if col == int(player2_answer):
                                game_board[row_idx][col_idx] = symbol2
                                show_board()
                                n = 1
                                break
                        else:
                                continue
                        break  
                    else:
                        print("There is a symbol there, try again.")
                        
                    check_game,m = check_win(game_board, symbol2)
                    if check_game:
                        print(player2, "wins!")
                        break    
                    if n == 1:
                        n = 0
                        break
                if m:
                    break
        
        elif againts == "computer":
            show_board()
            while True:
                #player
                while True:
                    print("\nGo",player1)
                    player1_answer = input("\nWhere do you want to put your symbol? ")
                                       
                    if  1>int(player1_answer) or 9<int(player1_answer):
                        print("enter a number from the board.")
                        continue
                    
                    for row_idx, row in enumerate(game_board):
                        for col_idx, col in enumerate(row):
                            if col == int(player1_answer):
                                game_board[row_idx][col_idx] = symbol1
                                show_board()
                                n = 1
                                break
                        else:
                                continue
                        break  
                    else:
                        print("There is a symbol there, try again.")
                        
                    check_game,m = check_win(game_board, symbol1)
                    if check_game:
                        print(player1, "wins!")
                        break
                    if n == 1:
                        n = 0
                        break
                if m:
                    break
                if check_draw(game_board):
                    print("It's a draw!")
                    break
                #computer
                print(computer_name, "turn:")
                while True:
                    row, col = random.randint(0, 2), random.randint(0, 2)
                    if isinstance(game_board[row][col], int):
                        game_board[row][col] = symbol2
                        break
                show_board()
                check_game,m = check_win(game_board, symbol2)
                if check_game:
                    print(computer_name,"wins!")
                    break
                if m:
                    break
      
        
    elif answer == "exit":
        elapsed_time = time.time() - start_time
        print("You have been here for: ",elapsed_time,"seconds")
        print("Have a good day, Bye")
        break
    
    else:
        print("Invalid input, give me a more straightforward answer.")