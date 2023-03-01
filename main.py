import time
import random
import typing as T
import numpy as np

COLOR_BG = (10,10,10)
COLOR_GRID = (50,50,50)
COLOR_DUE_NEXT = (170,170,170)
COLOR_ALIVE_NEXT = (255,255,255)


# Game of Life

#screeen : screen size 
#cells : state of the individual cells
#size   : size of the cells
#with_progress=False : show the progress of the game



class glife:
    # Original  | New   | State
    # 0         | 0     | 0
    # 1         | 0     | 1
    # 0         | 1     | 2
    # 1         | 1     | 3
    def count_neighbors(r, c):
        # count the number of neighbors for a cell
        # r, c are the row and column of the cell
        # returns the number of neighbors
        count = 0
        # start top left corner and go clockwise to the bottom right corner
        for i in range(-1, 2):
            for j in range(-1, 2):
                #shipping all positions out of bounds
                if ((i==r and j==c) or i < 0 or j < 0 or i >= ROWS or j >= COLS):
                    continue
                if board[i][j] in [1, 3]:
                    # increment the count if the neighbor is alive
                    count += 1
        return count

    # type hinting for the board
    # type hinting none is not returnning anything
    # everything is passing by reference
    def run_life(self, board: T.List[T.List[np.int64]]) -> None:
    # update board in place
        ROWS, COLS = 100, 100
        # iterate through each cell of the board
        for r in range(ROWS):
            for c in range(COLS):
                neighbors = self.count_neighbors(r, c)
                # apply the rules of the game
                if board[r][c]:
                    # check the neighbors of a live cell if 2 or 3 neighbors are alive, the cell stays alive
                    if neighbors in [2, 3]:
                        # cell stays alive with 2 or 3 neighbors
                        # 1 is not changed
                        board[r][c] = 3
                    elif neighbors == 3:
                        # cell 3 neighbors alive
                        board[r][c] = 2
        # update the board into the next state
        for r in range(ROWS):
            for c in range(COLS):
                # if the cell is a 1 will turn into a 0
                if board[r][c] == 1:
                    board[r][c] = 0
                elif board[r][c] in [2, 3]:
                    # if the cell is a 2 or 3 will turn into a 1
                    board[r][c] = 1
    
def run(n):
    #print('hello world' + str(n))
    print('hello world')
    print(n)


if __name__ == '__main__':
    #n = int(input().strip())
    n = np.zeros((100,100), dtype=np.int64)

    run(n)