import random
from constants import *
from main import TicTacToe as game

class EasyIA:
    def ia(board, signe):
        # Vérification des paramètres
        if not isinstance(board, list) or len(board) != 3 or not all(isinstance(row, list) and len(row) == 3 for row in board):
            return False
        if signe not in ['X', 'O']:
            return False

        # On renvoie un emplacement aléatoire qui n'est pas déjà pris
        empty_cells = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    empty_cells.append((i, j))
        if empty_cells:
            return random.choice(empty_cells)
        else:
            return False
        

class DifficultIA:
    def difficult_ia(board, signe):
        _, best_move = self.minimax(board, signe, depth=5, is_maximizing=True)
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
                if board[i] == EMPTY:
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
