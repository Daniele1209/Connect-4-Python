from win import winning_move

def is_terminal_node(board, piece_1,piece_2, column, row):
    return winning_move(board, piece_1, column, row) or winning_move(board, piece_2, column, row) or len(get_valid_locations(board, column, row)) == 0

def score_position(board, piece, column,row, length, empty, piece_1, piece_2):
    score = 0

    #Column
    center_array = [int(i) for i in list(board[:, column//2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    #Horizontal
    for r in range(row):
        row_array = [int(i) for i in list(board[r,:])]
        for c in range(column-3):
            window = row_array[c:c+length]
            score += evaluate_window(window, piece, empty, piece_1, piece_2)

    #Vertical
    for c in range(column):
        col_array = [int(i) for i in list(board[:,c])]
        for r in range(row-3):
            window = col_array[r:r+length]
            score += evaluate_window(window, piece, empty, piece_1, piece_2)

    #Diagonal
    for r in range(row-3):
        for c in range(column-3):
            window = [board[r+i][c+i] for i in range(length)]
            score += evaluate_window(window, piece, empty, piece_1, piece_2)

    for r in range(row-3):
        for c in range(column-3):
            window = [board[r+3-i][c+i] for i in range(length)]
            score += evaluate_window(window, piece, empty, piece_1, piece_2)

    return score

def get_next_open_row(board, col, row_c):
    for r in range(row_c):
        if board[r][col] == 0:
            return r

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def evaluate_window(window, piece, empty, piece_1, piece_2):
    score = 0
    opp_piece = piece_1
    if piece == piece_1:
        opp_piece = piece_2

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(empty) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(empty) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(empty) == 1:
        score -= 4

    return score

def get_valid_locations(board, column, row):
    valid_locations = []
    for col in range(column):
        if is_valid_location(board, col, row):
            valid_locations.append(col)
    return valid_locations

def is_valid_location(board, col, row_c):
    return board[row_c-1][col] == 0