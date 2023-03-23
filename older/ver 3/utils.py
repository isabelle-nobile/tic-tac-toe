from constants import *

def check_winner(board):
    # Check rows
    for row in range(ROWS):
        if board[row][0] != EMPTY and board[row][0] == board[row][1] == board[row][2]:
            return True
    # Check columns
    for col in range(COLS):
        if board[0][col] != EMPTY and board[0][col] == board[1][col] == board[2][col]:
            return True
    # Check diagonals
    if board[0][0] != EMPTY and board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] != EMPTY and board[0][2] == board[1][1] == board[2][0]:
        return True
    return False
