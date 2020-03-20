import random
import math
from functions import is_terminal_node, score_position, get_next_open_row, drop_piece, get_valid_locations
from win import winning_move


def minimax(board, depth, alpha, beta, maximizingPlayer, piece_2, piece_1, column_c, row_c , length, empty):

    valid_locations = get_valid_locations(board, column_c, row_c)
    is_terminal = is_terminal_node(board, column_c, piece_2, column_c, row_c)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, piece_2, column_c, row_c):
                return (None, 100000000000000)
            elif winning_move(board, piece_1, column_c, row_c):
                return (None, -10000000000000)
            else:
                return (None, 0)
        else:
            return (None, score_position(board, piece_2, column_c, row_c, length, empty, piece_1,piece_2))
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col, row_c)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, piece_2)
            new_score = minimax(b_copy, depth-1, alpha, beta, False, piece_2, piece_1, column_c, row_c, length, empty)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col, row_c)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, piece_1)
            new_score = minimax(b_copy, depth-1, alpha, beta, True, piece_2, piece_1, column_c, row_c, length, empty)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value

def pick_best_move(board, piece, column_c, row_c, length, empty, piece_1, piece_2):

    valid_locations = get_valid_locations(board, column_c, row_c)
    best_score = -10000
    best_col = random.choice(valid_locations)
    for col in valid_locations:
        row = get_next_open_row(board, col, row_c)
        temp_board = board.copy()
        drop_piece(temp_board, row, col, piece)
        score = score_position(temp_board, piece, column_c, row_c, length, empty, piece_1, piece_2)
        if score > best_score:
            best_score = score
            best_col = col

    return best_col