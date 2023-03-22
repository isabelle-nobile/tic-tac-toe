import copy
from constants import *

# class difficult_ia:
#     def __init__(self, board, ai_player):
#         self.board = board
#         self.ai_player = ai_player

#     def get_best_move(self):
#         best_score = float('-inf')
#         best_move = None

#         for row in range(len(self.board)):
#             for col in range(len(self.board[row])):
#                 if self.board[row][col] == EMPTY:
#                     board_copy = copy.deepcopy(self.board)
#                     board_copy[row][col] = self.ai_player
#                     score = self.minimax(board_copy, 0, False)
#                     if score > best_score:
#                         best_score = score
#                         best_move = (row, col)
#         return best_move

#     def minimax(self, board, depth, is_maximizing):
#         if self.check_winner(board, CROSS):
#             return -10 + depth
#         elif self.check_winner(board, CIRCLE):
#             return 10 - depth
#         elif self.check_tie(board):
#             return 0

#         if is_maximizing:
#             best_score = float('-inf')
#             for row in range(len(board)):
#                 for col in range(len(board[row])):
#                     if board[row][col] == EMPTY:
#                         board_copy = copy.deepcopy(board)
#                         board_copy[row][col] = CIRCLE
#                         score = self.minimax(board_copy, depth + 1, False)
#                         best_score = max(score, best_score)
#             return best_score

#         else:
#             best_score = float('inf')
#             for row in range(len(board)):
#                 for col in range(len(board[row])):
#                     if board[row][col] == EMPTY:
#                         board_copy = copy.deepcopy(board)
#                         board_copy[row][col] = CROSS
#                         score = self.minimax(board_copy, depth + 1, True)
#                         best_score = min(score, best_score)
#             return best_score

#     def check_winner(self, board, player):
#         win_states = [[board[0][0], board[0][1], board[0][2]],
#                       [board[1][0], board[1][1], board[1][2]],
#                       [board[2][0], board[2][1], board[2][2]],
#                       [board[0][0], board[1][0], board[2][0]],
#                       [board[0][1], board[1][1], board[2][1]],
#                       [board[0][2], board[1][2], board[2][2]],
#                       [board[0][0], board[1][1], board[2][2]],
#                       [board[0][2], board[1][1], board[2][0]]]

#         return [player, player, player] in win_states

#     def check_tie(self, board):
#         for row in range(len(board)):
#             for col in range(len(board[row])):
#                 if board[row][col] == EMPTY:
#                     return False
#         return True



def minimax_alpha_beta(board, player, depth, alpha, beta):
    # vérifier si la partie est terminée ou si la profondeur maximale est atteinte
    if board.game_over() or depth == 0:
        score = evaluate(board, player)
        return score

    # maximiser le score pour le joueur en cours
    if player == 'X':
        best_score = -np.inf
        for move in board.get_legal_moves():
            board.make_move(move, player)
            score = minimax_alpha_beta(board, 'O', depth-1, alpha, beta)
            board.undo_move(move)
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if alpha >= beta:
                break
        return best_score
    
    # minimiser le score pour le joueur en cours
    else:
        best_score = np.inf
        for move in board.get_legal_moves():
            board.make_move(move, player)
            score = minimax_alpha_beta(board, 'X', depth-1, alpha, beta)
            board.undo_move(move)
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if alpha >= beta:
                break
        return best_score

def evaluate(board, player):
    # évaluer le plateau de jeu pour le joueur donné
    # une fonction d'évaluation simple est de compter le nombre de lignes, colonnes et diagonales avec deux symboles du joueur donné et aucun symbole de l'autre joueur
    score = 0
    for row in board.get_rows():
        if row.count(player) == 2 and row.count(board.get_opponent(player)) == 0:
            score += 1
    for col in board.get_cols():
        if col.count(player) == 2 and col.count(board.get_opponent(player)) == 0:
            score += 1
    for diag in board.get_diagonals():
        if diag.count(player) == 2 and diag.count(board.get_opponent(player)) == 0:
            score += 1
    return score

def get_best_move(board, player, depth):
    # déterminer le meilleur coup possible pour le joueur en utilisant l'algorithme Minimax avec élagage alpha-bêta
    best_score = -np.inf
    best_move = None
    alpha = -np.inf
    beta = np.inf
    for move in board.get_legal_moves():
        board.make_move(move, player)
        score = minimax_alpha_beta(board, board.get_opponent(player), depth-1, alpha, beta)
        board.undo_move(move)
        if score > best_score:
            best_score = score
            best_move = move
        alpha = max(alpha, best_score)
    return best_move
