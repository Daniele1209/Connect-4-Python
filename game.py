import random
import sys
import math
import numpy as np
from win import winning_move
from AI import minimax, pick_best_move
from functions import get_next_open_row, drop_piece
from valid import valid_input

row_c = 6
column_c = 7
player = 0
ai = 1
empty = 0
piece_1 = 1
piece_2 = 2
length = 4


def is_valid_location(board, col):
    return board[row_c-1][col] == 0

def create_board():
    board = np.zeros((row_c,column_c))
    return board

def print_board(board):
    print("  1  2  3  4  5  6  7")
    print(np.flip(board, 0))

board = create_board()
print_board(board)
game_over = False
turn = random.randint(player, ai)
#turn = player
square_size = 100

while not game_over:

    if turn == player:
        posx = int(input("Select a position between 1 and 7 :"))
        valid_input(posx)
        posx -= 1
        print("\n")
        #col = int(math.floor(posx/square_size))
        col = posx

        if is_valid_location(board, col):
            row = get_next_open_row(board, col, row_c)
            drop_piece(board, row, col, piece_1)

            if winning_move(board, piece_1, column_c, row_c):
                print("Congratulations !!! You win !!!")
                game_over = True

            if game_over != True :
                turn += 1
                turn = turn % 2
                print_board(board)

    if turn == ai and not game_over:

        col = pick_best_move(board, piece_2, column_c,row_c, empty, length,piece_1,piece_2)
        minimax_score = minimax(board, 5, -math.inf, math.inf, True, piece_2, piece_1, column_c, row_c, empty, length)

        if is_valid_location(board, col):

            row = get_next_open_row(board, col, row_c)
            drop_piece(board, row, col, piece_2)

            if winning_move(board, piece_2, column_c, row_c):
                print("The AI has destroyed you")
                game_over = True

            if game_over != True :
                turn += 1
                turn = turn % 2
                print_board(board)


    if game_over:
        sys.exit(0)