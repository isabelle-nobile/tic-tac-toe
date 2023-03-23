from copy import deepcopy
from ver 5 copy 2.main import TicTacToe as game

def minimax(board, depth, is_maximizing_player, current_player, ai_player):
    """
    Cette fonction implémente l'algorithme Minimax avec élagage Alpha-Bêta pour choisir le meilleur coup
    à jouer pour l'IA.
    """
    # On vérifie si le jeu est terminé ou si on atteint la profondeur maximale
    if game.check_win(board, ai_player):
        return 10
    elif game.check_win(board, current_player):
        return -10
    elif game.check_tie(board):
        return 0
    elif depth == 0:
        return 0
    
    # On initialise les variables
    best_score = float('-inf') if is_maximizing_player else float('inf')
    player = ai_player if is_maximizing_player else current_player
    
    # On boucle à travers chaque case vide du plateau
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                # On simule le coup
                board_copy = deepcopy(board)
                board_copy[i][j] = player
                
                # On récursive l'appel à la fonction minimax pour évaluer la valeur de ce coup
                score = minimax(board_copy, depth-1, not is_maximizing_player, current_player, ai_player)
                
                # On met à jour la meilleure valeur
                if is_maximizing_player:
                    best_score = max(best_score, score)
                else:
                    best_score = min(best_score, score)
    
    return best_score

def get_best_move(board, current_player, ai_player):
    """
    Cette fonction détermine le meilleur coup à jouer pour l'IA en utilisant l'algorithme Minimax.
    """
    best_score = float('-inf')
    best_move = None
    
    # On boucle à travers chaque case vide du plateau
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                # On simule le coup
                board_copy = deepcopy(board)
                board_copy[i][j] = ai_player
                
                # On évalue la valeur de ce coup en appelant la fonction minimax
                score = minimax(board_copy, 4, False, current_player, ai_player)
                
                # On met à jour le meilleur coup
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    
    return best_move
