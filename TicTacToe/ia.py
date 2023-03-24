import random

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