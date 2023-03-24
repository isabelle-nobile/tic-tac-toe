import random
import copy
from constants import *

class MonteCarlo:
    def __init__(self, num_rollouts):
        self.num_rollouts = num_rollouts

    def get_best_move(self, board, current_player, ai_player):
        """
        Cette fonction détermine le meilleur coup à jouer pour l'IA en utilisant l'algorithme Monte Carlo.
        """
        num_wins = {}
        num_losses = {}
        
        # On boucle à travers chaque case vide du plateau
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    # On simule le coup num_rollouts fois
                    for _ in range(self.num_rollouts):
                        board_copy = copy.deepcopy(board)
                        board_copy[i][j] = ai_player
                        
                        # On joue les coups aléatoires jusqu'à la fin du jeu
                        winner = self.play_random_game(board_copy, current_player, ai_player)
                        
                        # On met à jour les statistiques pour ce coup
                        if winner == ai_player:
                            num_wins[(i, j)] = num_wins.get((i, j), 0) + 1
                        elif winner == current_player:
                            num_losses[(i, j)] = num_losses.get((i, j), 0) + 1
        
        # On choisit le meilleur coup en utilisant les statistiques
        best_score = float('-inf')
        best_move = None
        for move, wins in num_wins.items():
            losses = num_losses.get(move, 0)
            score = wins - losses
            if score > best_score:
                best_score = score
                best_move = move
        
        return best_move

    def play_random_game(self, board, current_player, ai_player):
        """
        Cette fonction joue une partie aléatoire à partir de l'état du plateau donné,
        en alternant les coups entre les joueurs aléatoires.
        """
        players = [current_player, ai_player]
        random.shuffle(players)
        while True:
            # On vérifie si le jeu est terminé
            if self.check_win(board, players[0]):
                return players[0]
            elif self.check_win(board, players[1]):
                return players[1]
            elif self.check_tie(board, players[0]):
                return None
            
            # On choisit une case vide aléatoire et on y joue le coup
            empty_spaces = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
            if empty_spaces:
                row, col = random.choice(empty_spaces)
                board[row][col] = players[0]
            
            # On alterne entre les joueurs
            players.reverse()

    def check_win(self, board, ai_player):
        # Check rows
        for row in range(ROWS):
            if board[row][0] != EMPTY and board[row][0] == board[row][1] == board[row][2] == ai_player:
                return True
        
        # Check columns
        for col in range(COLS):
            if board[0][col] != EMPTY and board[0][col] == board[1][col] == board[2][col] == ai_player:
                return True

        # Check diagonals
        if board[0][0] != EMPTY and board[0][0] == board[1][1] == board[2][2] == ai_player:
            return True
        if board[0][2] != EMPTY and board[0][2] == board[1][1] == board[2][0] == ai_player:
            return True

        return False
    
    def check_tie(self, board, ai_player):
        """
        Cette fonction vérifie si la partie est terminée avec une égalité.
        """
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == EMPTY:
                    return False
        if not self.check_win(board, ai_player) and not self.check_win(board, self.get_opponent(ai_player)):
            return True
        return False


       
