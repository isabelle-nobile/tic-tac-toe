import random

def ia(board, signe):
    # Vérifie si l'IA peut gagner en jouant une case
    for i in range(9):
        if board[i] == 0:
            board[i] = signe
            if check_win(board, signe):
                return i
            board[i] = 0

    # Vérifie si le joueur peut gagner en jouant une case
    other_signe = "X" if signe == "O" else "O"
    for i in range(9):
        if board[i] == 0:
            board[i] = other_signe
            if check_win(board, other_signe):
                board[i] = signe
                return i
            board[i] = 0

    # Si aucune victoire possible, joue aléatoirement
    available_moves = [i for i in range(9) if board[i] == 0]
    if available_moves:
        return random.choice(available_moves)

    # Si aucune case disponible, retourne False
    return False

def check_win(board, signe):
    winning_combinations = (
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colonnes
        [0, 4, 8], [2, 4, 6]             # diagonales
    )
    for combo in winning_combinations:
        if all(board[i] == signe for i in combo):
            return True
    return False
