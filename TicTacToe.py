import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
cur_player = "X"
game_run = True
winner = True


def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--------- ")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


def playerInput(board):
    inp = int(input("Enter a number (1-9) : "))
    if 1 <= inp <= 9 and board[inp - 1] == '-':
        board[inp - 1] = cur_player
    else:
        print("Oops player is already in the position !")


def CheckHorizontle(board):
    global winner
    if board[0] == board[1] and board[1] == board[2] and board[2] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[5] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[8] != "-":
        winner = board[6]
        return True


def CheckRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[6] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[7] != "-":
        winner = board[7]
        return True
    elif board[2] == board[5] == board[8] and board[8] != "-":
        winner = board[8]
        return True


def CheckDia(board):
    global winner
    if board[0] == board[4] == board[8] and board[8] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[6] != "-":
        winner = board[2]
        return True


def CheckWin():
    global game_run
    if CheckDia(board) or CheckHorizontle(board) or CheckRow(board):
        printBoard(board)
        print(f"The Winner is {winner}")
        game_run = False


def CheckTie(board):
    global game_run
    if "-" not in board:
        printBoard(board)
        print("Game is Tie !")
        game_run = False


def Computer(board):
    while cur_player == "O":
        pos = random.randint(0, 8)
        if board[pos] == "-":
            board[pos] = "O"
            SwitchPlayer()


def SwitchPlayer():
    global cur_player
    if cur_player == "X":
        cur_player = "O"
    else:
        cur_player = "X"


while game_run:
    printBoard(board)
    playerInput(board)
    CheckWin()
    CheckTie(board)
    SwitchPlayer()
    Computer(board)
    CheckWin()
    CheckTie(board)

# Name : Md Tushar Ahmed
# Python TicTacToe Game
