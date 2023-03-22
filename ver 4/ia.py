import random
from constants import *
from main import TicTacToe as game

def ia(board, signe, level):
    if level == "facile":
        return easy_ia(board, signe)
    elif level == "difficile":
        _, best_move = minimax(board, signe, depth=5, is_maximizing=True, level=level)
        return best_move
    else:
        # Return (0, 0) or any other valid move as a tuple of row and column indices
        return (0, 0)




def easy_ia(board, signe):
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


def minimax(board, signe, depth, is_maximizing, level):
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
                score, _ = minimax(board, signe, depth-1, False, level)
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
                score, _ = minimax(board, signe, depth-1, True, level)
                board[i] = EMPTY
                if score < best_score:
                    best_score = score
                    best_move = i
        return (best_score, best_move)



# import random
# from constants import *
# from main import TicTacToe

# game = TicTacToe()


# def ia(board, signe, level):
#     if level == "facile":
#         return easy_ia(board, signe)
#     elif level == "difficile":
#         return minimax(board, signe, 0, True)
#     else:
#         # raise ValueError("Niveau de difficulté invalide.")
#         return False, False 


# def easy_ia(board, signe):
#     # Vérification des paramètres
#     if not isinstance(board, list) or len(board) != 3 or not all(isinstance(row, list) and len(row) == 3 for row in board):
#         return False
#     if signe not in ['X', 'O']:
#         return False

#     # On renvoie un emplacement aléatoire qui n'est pas déjà pris
#     empty_cells = []
#     for i in range(3):
#         for j in range(3):
#             if board[i][j] == ' ':
#                 empty_cells.append((i, j))
#     if empty_cells:
#         return random.choice(empty_cells)
#     else:
#         return False

# def minimax(board, signe, depth, is_maximizing):
#     if game.has_won(board, CROSS):
#         return (10-depth, None)
#     elif game.has_won(board, CIRCLE):
#         return (-10+depth, None)
#     elif game.is_tie(board):
#         return (0, None)

#     if is_maximizing:
#         best_score = -float('inf')
#         for i in range(9):
#             if board[i] == EMPTY:
#                 board[i] = signe
#                 score, _ = minimax(board, signe, depth+1, False)
#                 board[i] = EMPTY
#                 if score > best_score:
#                     best_score = score
#                     best_move = i
#         return (best_score, best_move)
#     else:
#         best_score = float('inf')
#         for i in range(9):
#             if board[i] == EMPTY:
#                 board[i] = game.get_opponent(signe)
#                 score, _ = minimax(board, signe, depth+1, True)
#                 board[i] = EMPTY
#                 if score < best_score:
#                     best_score = score
#                     best_move = i
#         return (best_score, best_move)
    
# def has_won(self, player):
#     # Check rows
#     for row in range(ROWS):
#         if self.board[row][0] == self.board[row][1] == self.board[row][2] == player:
#             return True
#     # Check columns
#     for col in range(COLS):
#         if self.board[0][col] == self.board[1][col] == self.board[2][col] == player:
#             return True
#     # Check diagonals
#     if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
#         return True
#     if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
#         return True
#     return False

# def is_tie(self):
#     for row in range(ROWS):
#         for col in range(COLS):
#             if self.board[row][col] == EMPTY:
#                 return False
#     return True

# def get_opponent(self, player):
#     return CROSS if player == CIRCLE else CIRCLE