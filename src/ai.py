##
## Minimax Workshop, 2022
## tictactoe
## File description:
## ai
##

def playMove(board):
    x = 0
    y = 0
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if (board[i][j] == 0):
                return(j, i)
                
    return (x, y)
