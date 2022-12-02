##
## Minimax Workshop, 2022
## tictactoe
## File description:
## ai
##

def isMovesLeft(board):
    for row in range(3):
        for col in range(3):
            if (board[row][col] == 0):
                return (True)
    return (False)

def evaluate(board):

    for row in range(3):
        if (board[row][0] == board[row][1] and board[row][1] == board[row][2]):
            return (board[row][0] * 10)
 
    for col in range(3):
        if (board[0][col] == board[1][col] and board[1][col] == board[2][col]):
            return (board[0][col] * 10)
 
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        if (board[0][0] == 1):
            return (10)
        elif (board[0][0] == -1):
            return (-10)

    if (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        if (board[0][2] == 1):
            return (10)
        elif (board[0][2] == -1):
            return (-10)
    return (0)
 
def minimax(board, depth, isMax) :
    score = evaluate(board)
 
    if (score == 10):
        return (score)

    if (score == -10):
        return (score)
 
    if (isMovesLeft(board) == False):
        return (0)

    if (isMax):
        best = -1000
        for row in range(3):
            for col in range(3):
                if (board[row][col] == 0):
                    board[row][col] = 1
                    best = max(best, minimax(board, depth + 1, not isMax))
 
                    board[row][col] = 0
        return (best - depth)
    else :
        best = 1000
        for row in range(3):
            for col in range(3):
                if (board[row][col] == 0) :
                    board[row][col] = -1
                    best = min(best, minimax(board, depth + 1, not isMax))
                    board[row][col] = 0
        return (best + depth)
 
def findBestMove(board):
    bestVal = -1000
    bestMove = (-1, -1)
 
    for row in range(3):
        for col in range(3):
            if (board[row][col] == 0):
                board[row][col] = 1
                moveVal = minimax(board, 0, False)
                board[row][col] = 0
                if (moveVal > bestVal) :               
                    bestMove = (row, col)
                    bestVal = moveVal
    return (bestMove)

def playMove(board):
    x = 0
    y = 0
    for i in range(3):
        for j in range(3):
            if (board[i][j] == 1):
                board[i][j] = -1
            elif (board[i][j] == 2):
                board[i][j] = 1
    (y, x) = findBestMove(board)
    for i in range(3):
        for j in range(3):
            if (board[i][j] == -1):
                board[i][j] = 1
            elif (board[i][j] == 1):
                board[i][j] = 2
    return (x, y)
