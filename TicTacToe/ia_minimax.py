from TicTacToe.constants import *


class Minimax:
    def minimax(self, board, depth, is_maximizing_player, current_player, ai_player):
        """
        Cette fonction implémente l'algorithme Minimax avec élagage Alpha-Bêta pour choisir le meilleur coup
        à jouer pour l'IA.

        """
        # On vérifie si le jeu est terminé ou si on atteint la profondeur maximale
        if depth < 0:
            return -1234

        if self.check_win(board, current_player, ai_player) != None:
            return self.check_win(board, current_player, ai_player)

        if self.check_tie(board):
            return 0

        if is_maximizing_player:
            player = ai_player
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        # On simule le coup
                        board[i][j] = player
                        # On récursive l'appel à la fonction minimax pour évaluer la valeur de ce coup
                        score = self.minimax(
                            board, depth - 1, not is_maximizing_player,
                            current_player, ai_player)
                        # On met à jour la meilleure valeur
                        best_score = max(best_score, score)
                        board[i][j] = ' '
        else:
            best_score = float('inf')
            player = current_player
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        # On simule le coup
                        board[i][j] = player
                        # On récursive l'appel à la fonction minimax pour évaluer la valeur de ce coup
                        score = self.minimax(
                            board, depth - 1, not is_maximizing_player,
                            current_player, ai_player)

                        # On met à jour la meilleure valeur

                        best_score = min(best_score, score)
                        board[i][j] = ' '
        # On boucle à travers chaque case vide du plateau
        return best_score

    def get_best_move(self, board, current_player, ai_player):
        """
        Cette fonction détermine le meilleur coup à jouer pour l'IA en utilisant l'algorithme Minimax.
        """
        best_score = -12345678
        best_move = None

        # On boucle à travers chaque case vide du plateau
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    # On simule le coup

                    board[i][j] = ai_player
                    # On évalue la valeur de ce coup en appelant la fonction minimax
                    score = self.minimax(
                        board, 6, False, current_player, ai_player)
                    # On met à jour le meilleur
                    board[i][j] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        return best_move

    def check_win(self, board, current_player, ai_player):
        # Check rows
        for row in range(ROWS):
            if board[row][0] != EMPTY and board[row][0] == board[row][1] == board[row][2]:
                if board[row][0] == ai_player:
                    return 10
                elif board[row][0] == current_player:
                    return -10
        # Check columns
        for col in range(COLS):
            if board[0][col] != EMPTY and board[0][col] == board[1][col] == board[2][col]:
                if board[0][col] == ai_player:
                    return 10
                elif board[0][col] == current_player:
                    return -10
        # Check diagonals
        if board[0][0] != EMPTY and board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == ai_player:
                return 10
            elif board[0][0] == current_player:
                return -10
        if board[0][2] != EMPTY and board[0][2] == board[1][1] == board[2][0]:
            if board[0][2] == ai_player:
                return 10
            elif board[0][2] == current_player:
                return -10
        # Check si le jeu est une égalité
        if self.check_tie(board):
            return 0
        # Si le jeu n'est pas terminé, return None
        return None

    def check_tie(self, board):
        for row in board:
            for cell in row:
                if cell == EMPTY:
                    return False
        return True
