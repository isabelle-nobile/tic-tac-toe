from constants import *
from main import TicTacToe as game

def difficult_ia(board, signe):
    _, best_move = minimax(board, signe, depth=5, is_maximizing=True)
    return best_move

def minimax(board, signe, depth, is_maximizing):
    if game.has_won(board, CROSS):
        return (10 - depth, None)
    elif game.has_won(board, CIRCLE):
        return (-10 + depth, None)
    elif game.is_tie(board):
        return (0, None)

    if depth == 0:
        return (0, None)

    if is_maximizing:
        best_score = -float('inf')
        best_move = None
        for i in range(9):
            if i >= len(board):
                continue
            if board[i] == EMPTY:
                # rest of the code
                board[i] = signe
                score, _ = minimax(board, signe, depth-1, False)
                board[i] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = i
        return (best_score, best_move)
    else:
        best_score = float('inf')
        best_move = None
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = game.get_opponent(signe)
                score, _ = minimax(board, signe, depth-1, True)
                board[i] = EMPTY
                if score < best_score:
                    best_score = score
                    best_move = i
        return (best_score, best_move)
