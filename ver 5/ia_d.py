from copy import deepcopy
from constants import *

class Minimax:
    def minimax(self, board, depth, is_maximizing_player, current_player, ai_player):
        """
        Cette fonction implémente l'algorithme Minimax avec élagage Alpha-Bêta pour choisir le meilleur coup
        à jouer pour l'IA.
        """
        # On vérifie si le jeu est terminé ou si on atteint la profondeur maximale
        if self.check_win(board, ai_player):
            return 10
        elif self.check_win(board, current_player):
            return -10
        elif self.check_tie(board):
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
                    score = self.minimax(board_copy, depth-1, not is_maximizing_player, current_player, ai_player)
                    
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
                    score = self.minimax(board_copy, 4, False, current_player, ai_player)
                    
                    # On met à jour le meilleur coup
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        
        return best_move

    def check_win(self):
        # Check rows
        for row in range(ROWS):
            if self.board[row][0] != EMPTY and self.board[row][0] == self.board[row][1] == self.board[row][2]:
                return True
        # Check columns
        for col in range(COLS):
            if self.board[0][col] != EMPTY and self.board[0][col] == self.board[1][col] == self.board[2][col]:
                return True
        # Check diagonals
        if self.board[0][0] != EMPTY and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True
        if self.board[0][2] != EMPTY and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True
        return False

    def check_tie(self):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] == EMPTY:
                    return False
        return True
