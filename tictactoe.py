board = ["-", "-", "-", "-", "-", "-", "-", "-", "-",]
flag = True

winner = None
currentPlayer = "X"

def displayBoard():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])   

def checkRows():
    global flag
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    if row1 or row2 or row3:
        flag = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

def checkColumns():
    global flag
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"
    if column1 or column2 or column3:
        flag = False
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    return

def checkDiagnols():
    global flag
    diagnol1 = board[0] == board[4] == board[8] != "-"
    diagnol2 = board[2] == board[4] == board[6] != "-"
    if diagnol1 or diagnol2:
        flag = False
    if diagnol1:
        return board[0]
    elif diagnol2:
        return board[2]
    return

def checkWin():
    global winner
    row = checkRows()
    column = checkColumns()
    diagnol = checkDiagnols()
    if row:
        winner = row
    elif column:
        winner = column
    elif diagnol:
        winner = diagnol
    return

def checkTie():
    global flag
    if "-" not in board:
        flag = False
    return

def changePlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    elif currentPlayer == "O":
        currentPlayer = "X"
    return

def play(currentPlayer):
    valid = False
    while not valid:
        if currentPlayer == "X":
            print("Player 1's turn: ")
        elif currentPlayer == "O":
            print("Player 2's turn: ")
        position = input("Choose a number from 1-9: ")
        if position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("invalid input, try again")
            continue
        position = int(position) -1
        if board[position] != "-":
            print("Position is already filled, try again")
        else:
            valid = True
        
    
    board[position] = currentPlayer

def checkIfGameOver():
    checkWin()
    checkTie()

def start():
    displayBoard()
    while flag:
        play(currentPlayer)
        checkIfGameOver()
        displayBoard()
        changePlayer()
    if winner == "X":
        print("Winner is player 1")
    elif winner == "O":
        print("Winner is player 2")
    elif winner == None:
        print("Tie")
    


start()