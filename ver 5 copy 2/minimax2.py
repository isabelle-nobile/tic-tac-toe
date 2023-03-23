
from constants import *

def minimax_ia(board, signe):
    # Vérification des paramètres
    # if not isinstance(board, list) or len(board) != 3 or not all(isinstance(row, list) and len(row) == 3 for row in board):
    #     return False
    if signe not in ['X', 'O']:
        return False

    # Récupérer le joueur adverse
    if signe == 'X':
        opponent = 'O'
    else:
        opponent = 'X'

    # Définir la profondeur maximale de l'arbre de recherche
    depth = 9 - sum(row.count(EMPTY) for row in board)

    # Appeler la méthode minimax pour obtenir le meilleur coup
    _, row, col = minimax(board, depth, signe, opponent, True)

    return [row, col]


def minimax(board, depth, player, opponent, maximizing_player):
    """
    Renvoie le score et le coup optimal pour le joueur en cours.
    """
    # Vérifier si le jeu est terminé ou si la profondeur maximale est atteinte
    if depth == 0 or check_game_over(board):
        score = evaluate(board, player)
        return score, None, None

    # Initialiser les variables
    best_row, best_col = None, None

    # Si c'est le tour du joueur qui maximise le score
    if maximizing_player:
        best_score = -float('inf')
        # Parcourir les cases vides
        for row, col in get_empty_cells(board):
            # Placer le prochain coup pour le joueur en cours
            board[row][col] = player
            # Appeler récursivement minimax pour le joueur adverse
            score, _, _ = minimax(board, depth-1, player=opponent, opponent=player, maximizing_player=False)
            # Mettre à jour le meilleur score
            if score > best_score:
                best_score = score
                best_row, best_col = row, col
            # Annuler le coup
            board[row][col] = EMPTY

        return best_score, best_row, best_col

    # Si c'est le tour du joueur qui minimise le score
    else:
        best_score = float('inf')
        # Parcourir les cases vides
        for row, col in get_empty_cells(board):
            # Placer le prochain coup pour le joueur en cours
            board[row][col] = player
            # Appeler récursivement minimax pour le joueur adverse
            score, _, _ = minimax(board, depth-1, player=opponent, opponent=player, maximizing_player=True)
            # Mettre à jour le meilleur score
            if score < best_score:
                best_score = score
                best_row, best_col = row, col
            # Annuler le coup
            board[row][col] = EMPTY

        return best_score, best_row, best_col

            
def evaluate(board, player):
    """
    Évalue la position actuelle du plateau de jeu pour le joueur en cours.
    """
    if check_win(board, player):
        return 1
    elif check_win(board, get_opponent(player)):
        return -1
    else:
        return 0

def get_opponent(player):
    """
    Renvoie le joueur adverse.
    """
    if player == 'X':
        return 'O'
    else:
        return 'X'

def get_empty_cells(board):
    """
    Renvoie les coordonnées des cases vides du plateau de jeu.
    """
    cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                cells.append((row, col))
    return cells

def check_win(board, player):
    """
    Vérifie si le joueur en cours a gagné la partie.
    """
    # Vérification des lignes
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    # Vérification des colonnes
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    # Vérification des diagonales
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    # Si aucune condition n'est remplie, le joueur n'a pas gagné
    return False


def check_game_over(board):
    """
    Vérifie si la partie est terminée.
    """
    # Vérification des lignes
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != EMPTY:
            return True
    # Vérification des colonnes
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return True
    # Vérification des diagonales
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return True
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return True
    # Vérification s'il y a des cases vides
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                return False
    # Si aucune condition n'est remplie, la partie est terminée
    return True
