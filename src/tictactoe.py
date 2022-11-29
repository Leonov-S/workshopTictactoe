##
## Minimax Workshop, 2022
## tictactoe
## File description:
## tictactoe
##

from ai import playMove

import pygame as pg
import sys

## init display settings
background_colour = (220, 220, 220)
width = 800
height = 800
screen = pg.display.set_mode((width, height), 0, 32)
pg.display.set_caption('Workshop Minimax')
screen.fill(background_colour)

## board size for every difficulty
difficulties = {
    "1": 3,
    "2": 5,
    "3": 15
}

class Board:
    def __init__(self, difficulty):
        self.__size = difficulties[difficulty]
        self.__square_size = int(800 / self.__size)
        self.__padd = 0
        self.__board = [[0 for _ in range(self.__size)] for _ in range(self.__size)]
        self.__draw_board()
    
    def __draw_board(self):
        screen.fill(background_colour)
        self.__square_size = 800 / self.__size
        self.__padd = int((5 * (self.__size - 1)) / 2)
        x_pos = self.__padd
        y_pos = self.__padd
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                pg.draw.rect(screen, (0, 0, 0), pg.Rect(x_pos, y_pos, self.__square_size, self.__square_size), 5)
                x_pos += (self.__square_size - 5)
            x_pos = self.__padd
            y_pos += (self.__square_size - 5)
        pg.display.update()
    
    ## draw last player move
    def __draw_play(self, y, x, player):
        size = self.__square_size - 5
        x_pos = (x * size + self.__padd + size / 2)
        y_pos = (y * size + self.__padd + size / 2)
        if (player == 1):
            pg.draw.circle(screen, (255, 0, 0), (x_pos, y_pos), size / 3, 20)
        if (player == 2):

            pg.draw.line(screen, (0, 0, 255), (x_pos - size / 4, y_pos - size / 4),
            (x_pos + size / 4, y_pos + size / 4) , 20)

            pg.draw.line(screen, (0, 0, 255), (x_pos - size / 4, y_pos + size / 4),
            (x_pos + size / 4, y_pos - size / 4) , 20)

        pg.display.update()
    
    ## get mouse pos on board
    def coords_from_mouse(self, coord):
        (x, y) = coord
        if (x > (800 - self.__padd)) or (x < self.__padd):
            print("ERROR: Out of bound")
            return -1
        if (y > (800 - self.__padd)) or (y < self.__padd):
            print("ERROR: Out of bound")
            return -1
        size = self.__square_size - 5
        x_pos = int((x - (self.__padd)) / size)
        y_pos = int((y - (self.__padd)) / size)

        return (self.__set_value(x_pos, y_pos, 1))
    
    ## check win around the last move
    def __check_win(self, last_move):
        (x, y) = last_move
        player = self.get_value(x, y)

        # horizontal
        if (self.get_value(x + 1, y) == player):
            if (self.get_value(x + 2, y) == player):
                return True
            if (self.get_value(x - 1, y) == player):
                return True
        if (self.get_value(x - 1, y) == player):
            if (self.get_value(x - 2, y) == player):
                return True
        
        # vertical
        if (self.get_value(x, y + 1) == player):
            if (self.get_value(x, y + 2) == player):
                return True
            if (self.get_value(x, y - 1) == player):
                return True
        if (self.get_value(x, y - 1) == player):
            if (self.get_value(x, y - 2) == player):
                return True
        
        # diagonal_left
        if (self.get_value(x + 1, y + 1) == player):
            if (self.get_value(x + 2, y + 2) == player):
                return True
            if (self.get_value(x - 1, y - 1) == player):
                return True
        if (self.get_value(x - 1, y - 1) == player):
            if (self.get_value(x - 2, y - 2) == player):
                return True

        # diagonal_right
        if (self.get_value(x + 1, y - 1) == player):
            if (self.get_value(x + 2, y - 2) == player):
                return True
            if (self.get_value(x - 1, y + 1) == player):
                return True
        if (self.get_value(x - 1, y + 1) == player):
            if (self.get_value(x - 2, y + 2) == player):
                return True
        return False

    ## set the last move on the board if the move is permited,
    #   then checks if it's a winning   move
    def __set_value(self, x, y, player):
        if (x < 0 or x > (self.__size - 1)):
            print("ERROR: Out of bound", "x:", x," y:", y)
            return -1
        if (y < 0 or y > (self.__size - 1)):
            print("ERROR: Out of bound", "x:", x," y:", y)
            return -1
        if self.__board[y][x] != 0:
            print("ERROR: Case not empty")
            return -1
        self.__board[y][x] = player
        self.__draw_play(y, x, player)
        if (self.__check_win((x, y))):
            return 1
        return 0



    ## get board value at x, y
    def get_value(self, x, y):
        if (x < 0 or x > (self.__size - 1)):
            return -1
        if (y < 0 or y > (self.__size - 1)):
            return -1
        return self.__board[y][x]

    
    def game_loop(self):
        running = True
        player = 1
        turn = 0
        while running:
            for event in pg.event.get():
                if (event.type == pg.QUIT):
                    running = False
                if ((event.type == pg.KEYDOWN) and (event.key == pg.K_r)):
                    print("RESTART")
                    return True
                if (player == 1):
                    if ((event.type == pg.MOUSEBUTTONDOWN) and pg.mouse.get_pressed()[0]):
                        play = self.coords_from_mouse(pg.mouse.get_pos())
                        if (play == 1):
                            print("Human win")
                            player = -1
                        elif (play == 0):
                            turn += 1
                            if (turn == (self.__size ** 2)):
                                player = -1
                                print("DRAW")
                            else:
                                player = 2
            if (player == 2):
                (x, y) = playMove(self.__board)
                play = self.__set_value(x, y, 2)
                if (play == 1):
                    print("Bot win")
                    player = -1
                elif (play == 0):
                    turn += 1
                    if (turn == (self.__size ** 2)):
                        player = -1
                        print("DRAW")
                    else:
                        player = 1
                else:
                    player = -1
        return False

def print_help():
    print("\n./tictactoe <difficulty> \n Difficulties:")
    print(" 1: 3x3 \n 2: 5x5 \n 3: 15x15")

def main():
    args = sys.argv[1:]
    if len(args) > 1:
        print_help()
        return 84
    if (len(args) != 0):
        if (not args[0].isdigit()):
            print_help()
            return 84
        if (int(args[0]) > 3 or int(args[0]) < 1):
            print_help()
            return 84
    if (len(args) != 0):
        difficulty = args[0]
    else:
        difficulty = '1'
    game = True
    print("START")
    while(game):
        board = Board(difficulty)
        game = board.game_loop()
    print("END")

if __name__=="__main__":
    main()