"""Program to play a game of minesweeper"""
from __future__ import print_function
import random

class Tile(object):
    """Class for minesweeper tiles"""
    def __init__(self, isBomb, board):
        self.isbomb = isBomb
        self.neighbours = []
        self.number = 0
        self.visible = False
        self.board = board

    def add_neighbour(self, neighbour):
        "Adds a tile as a neighbour"
        if neighbour.isbomb:
            self.number += 1
        self.neighbours.append(neighbour)

    def expose(self):
        "Sets itself to visible and if self is not a bomb and number == 0 then expose neighbours"
        if self.visible:
            return
        self.visible = True
        self.board.visiblecnt += 1
        if self.number == 0 and not self.isbomb:
            for neighbour in self.neighbours:
                neighbour.expose()

    def cheat(self):
        "Return str as if visible for debugging purposes"
        old_visible = self.visible
        self.visible = True
        ret_val = self.__str__()
        self.visible = old_visible
        return ret_val

    def __str__(self):
        if not self.visible:
            return '?'
        if self.isbomb:
            return 'X'
        if self.number == 0:
            return ' '
        return '{}'.format(self.number)

class Board(object):
    """Class for minesweeper board"""
    def __init__(self, width, height, bombpct):
        self.height = height
        self.width = width
        self.game_state = 0 # 0 = in play, 1 = lose, 2 = win
        self.bombcnt = 0
        self.visiblecnt = 0
        self.tiles = [[Tile(True if random.random() < bombpct else False, self) for y in range(height)] for x in range(width)]

        # For each tile, add neighbouring tiles to itself
        # Opposed to for each tile, add itself to neighbouring tiles
        for y in range(height):
            for x in range(width):
                if self.tiles[x][y].isbomb:
                    self.bombcnt += 1
                if x - 1 >= 0:
                    self.tiles[x][y].add_neighbour(self.tiles[x-1][y])
                if x - 1 >= 0 and y - 1 >= 0:
                    self.tiles[x][y].add_neighbour(self.tiles[x-1][y-1])
                if y - 1 >= 0:
                    self.tiles[x][y].add_neighbour(self.tiles[x][y-1])
                if x + 1 < width and y - 1 >= 0:
                    self.tiles[x][y].add_neighbour(self.tiles[x+1][y-1])
                if x + 1 < width:
                    self.tiles[x][y].add_neighbour(self.tiles[x+1][y])
                if x + 1 < width and y + 1 < height:
                    self.tiles[x][y].add_neighbour(self.tiles[x+1][y+1])
                if y + 1 < height:
                    self.tiles[x][y].add_neighbour(self.tiles[x][y+1])
                if x - 1 >= 0 and y + 1 < height:
                    self.tiles[x][y].add_neighbour(self.tiles[x-1][y+1])

    def print_board(self):
        "Prints the game board"
        print('----' * self.width + '-')
        for y in range(self.height):
            for x in range(self.width):
                print('| {} '.format(self.tiles[x][y]), end='')
            print('| {}'.format(y + 1))
            print('----' * self.width + '-')
        for x in range(self.width):
            print('  {} '.format(x + 1), end='')
        print('')

    def cheat_board(self):
        "Prints the revealed game board, for debugging purposes"
        print('----' * self.width + '-')
        for y in range(self.height):
            for x in range(self.width):
                print('| {} '.format(self.tiles[x][y].cheat()), end='')
            print('|')
            print('----' * self.width + '-')

    def check_win(self):
        "Checks to see if win"
        if self.bombcnt + self.visiblecnt == self.width * self.height:
            self.game_state = 2

    # Call only if x and y are valid
    def make_move(self, x_coord, y_coord):
        "Performs the move"
        assert x_coord >= 0 and x_coord < self.width and y_coord >= 0 and y_coord < self.height
        self.tiles[x_coord][y_coord].expose()
        if self.tiles[x_coord][y_coord].isbomb:
            self.game_state = 1
        self.check_win()

    def play(self):
        "Main game logic"
        self.print_board()
        while not self.game_state:
            x = int(raw_input('Enter your x: ')) - 1
            y = int(raw_input('Enter your y: ')) - 1
            if x < 0 or x >= self.width or y < 0 or y >= self.height:
                print('Please enter valid x and y coordinates')
                continue
            self.make_move(x, y)
            self.print_board()
        if self.game_state == 1:
            print('You lost! Revealing game board')
            self.cheat_board()
        elif self.game_state == 2:
            print('You won!')

def main():
    "Main function"
    while True:
        board = Board(8, 6, .3)
        board.play()
        while True:
            play_again = raw_input('Play again? (y/n)')
            if play_again == 'y':
                break
            elif play_again == 'n':
                print('Thanks for playing!')
                raw_input()
                return
            else:
                print('Please enter y/n')

if __name__ == '__main__':
    main()