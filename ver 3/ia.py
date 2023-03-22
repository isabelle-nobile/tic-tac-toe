import random
from utils import check_winner
from main import check_tie 


def ia(board, signe):
    # Vérification des paramètres
    if not isinstance(board, list) or len(board) != 3 or not all(isinstance(row, list) and len(row) == 3 for row in board):
        return False
    if signe not in ['X', 'O']:
        return False
    
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty_cells.append((i, j))
    if empty_cells:
        return random.choice(empty_cells)
    else:
        return False
    
# fonction récursive minimax
def minimax(board, signe):
    if check_winner(board, signe):
        if signe == 'X':
            return -1
        else:
            return 1
    elif check_tie(board):
        return 0
    
    scores = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = signe
                scores.append(minimax(board, 'O' if signe == 'X' else 'X'))
                board[i][j] = ' '
    
    if signe == 'X':
        return max(scores)
    else:
        return min(scores)
    





    

    # On renvoie un emplacement aléatoire qui n'est pas déjà pris
    # empty_cells = []
    # for i in range(3):
    #     for j in range(3):
    #         if board[i][j] == ' ':
    #             empty_cells.append((i, j))
    
    # if difficulty == 'easy':
    #     if empty_cells:
    #         return random.choice(empty_cells)
            
    #     else:
    #         return False
    # elif difficulty == 'hard':
    #     return minimax(board, signe)
    # else:
    #     return False


# def minimax(self, board, maximizing):
        
#         # terminal case
#         case = board.final_state()

#         # player 1 wins
#         if case == 1:
#             return 1, None # eval, move

#         # player 2 wins
#         if case == 2:
#             return -1, None

#         # draw
#         elif board.isfull():
#             return 0, None

#         if maximizing:
#             max_eval = -100
#             best_move = None
#             empty_sqrs = board.get_empty_sqrs()

#             for (row, col) in empty_sqrs:
#                 temp_board = copy.deepcopy(board)
#                 temp_board.mark_sqr(row, col, 1)
#                 eval = self.minimax(temp_board, False)[0]
#                 if eval > max_eval:
#                     max_eval = eval
#                     best_move = (row, col)

#             return max_eval, best_move

#         elif not maximizing:
#             min_eval = 100
#             best_move = None
#             empty_sqrs = board.get_empty_sqrs()

#             for (row, col) in empty_sqrs:
#                 temp_board = copy.deepcopy(board)
#                 temp_board.mark_sqr(row, col, self.player)
#                 eval = self.minimax(temp_board, True)[0]
#                 if eval < min_eval:
#                     min_eval = eval
#                     best_move = (row, col)

#             return min_eval, best_move
        