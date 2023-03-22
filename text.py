Créez une fonction easy_ia(board, signe) qui prend le tableau board et le signe du joueur (CROSS ou CIRCLE) en entrée et retourne une position aléatoire dans le tableau où le signe peut être placé.

Créez une fonction minimax(board, signe, depth, is_maximizing) qui utilise l'algorithme Minimax pour déterminer la meilleure position pour l'IA. Cette fonction prend en entrée le tableau board, le signe de l'IA, la profondeur actuelle de l'arbre Minimax et un booléen is_maximizing qui indique si c'est le tour de l'IA ou de l'adversaire. La fonction doit retourner un tuple (score, position) où score est le score attribué à la position et position est la position recommandée pour l'IA.

Modifiez votre fonction ia(board, signe) pour appeler soit easy_ia(board, signe) soit minimax(board, signe, depth, is_maximizing) en fonction du niveau de difficulté choisi.

Ajoutez un menu déroulant dans votre interface utilisateur pour permettre à l'utilisateur de choisir le niveau de difficulté de l'IA.

Voici un exemple de code pour vous aider à démarrer :


import random
from constants import *
from main import TicTacToe as game

def ia(board, signe, level):
    if level == "facile":
        return easy_ia(board, signe)
    elif level == "difficile":
        return minimax(board, signe, 0, True)
    else:
        return False, False



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


def minimax(board, signe, depth, is_maximizing):

    if game.has_won(board, CROSS):
        return (10-depth, None)
    elif game.has_won(board, CIRCLE):
        return (-10+depth, None)
    elif game.is_tie(board):
        return (0, None)

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = signe
                score, _ = minimax(board, signe, depth+1, False)
                board[i] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = i
        return (best_score, best_move)
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = game.get_opponent(signe)
                score, _ = minimax(board, signe, depth+1, True)
                board[i] = EMPTY
                if score < best_score:
                    best_score = score
                    best_move = i
        return (best_score, best_move)



import tkinter as tk
from tkinter import messagebox
from constants import *
from ia import *


class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.canvas = tk.Canvas(self.root, width=WIDTH,
                                height=HEIGHT, bg=BG_COLOR)
        self.canvas.pack()
        self.create_menu_bar()
        self.difficulty = tk.StringVar()
        self.draw_lines()
        self.canvas.bind("<Button-1>", self.click_handler)
        self.board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
        self.current_player = CROSS
        self.game_over = False
        self.ai_player = CIRCLE
        self.root.iconbitmap('icon_tic_tac_toe.ico')

        #  # Créer un widget menubar
        # menubar = tk.Menu(self.root)
        # self.root.config(menu=menubar)

        # # Créer un menu "Jeu"

        # game_menu = tk.Menu(menubar, tearoff=0)
        # menubar.add_cascade(label="Jeu", menu=game_menu)
        # game_menu.add_command(label="Relancer le jeu", command=self.reset_game)
        # game_menu.add_command(label="Play vs Player", command=self.start_pvp)
        # game_menu.add_command(label="Play vs AI", command=self.start_pvai)

    def create_menu_bar(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        menu_file = tk.Menu(menu_bar, tearoff=0)

        # Un menu déroulant dans le menu Difficulty.
        menu_recent = tk.Menu(menu_file, tearoff=0)
        menu_recent.add_command(label="Easy")
        menu_recent.add_command(label="Difficult")
        menu_file.add_cascade(label="Difficulty", underline=0, menu=menu_recent)
        menu_bar.add_cascade(label="Play vs AI", underline=0, menu=menu_file)

        menu_edit = tk.Menu(menu_bar, tearoff=0)
        menu_edit.add_command(label="PvP", command=self.start_pvp)
        menu_bar.add_cascade(label="Play vs Player", menu=menu_edit)


        menu_reset = tk.Menu(menu_bar, tearoff=0)
        menu_reset.add_command(label="New Game", command=self.reset_game)
        menu_bar.add_cascade(label="Relancer une partie ?", menu=menu_reset)


    def start_pvp(self):
        self.ai_player = None
        self.reset_game()

    def start_pvai(self):
        self.ai_player = CIRCLE if self.current_player == CROSS else CROSS
        self.reset_game()
        if self.current_player == self.ai_player:
            self.ai_move()

    def reset_game(self):
        self.board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
        self.current_player = CROSS
        self.game_over = False
        self.canvas.delete("all")
        self.draw_lines()

    def draw_lines(self):
        for i in range(1, COLS):
            x = i * WIDTH // COLS
            self.canvas.create_line(
                x, 0, x, HEIGHT, width=LINE_WIDTH, fill=LINE_COLOR)
        for i in range(1, ROWS):
            y = i * HEIGHT // ROWS
            self.canvas.create_line(
                0, y, WIDTH, y, width=LINE_WIDTH, fill=LINE_COLOR)

    def click_handler(self, event):
        if self.game_over:
            return
        row = event.y // (HEIGHT // ROWS)
        col = event.x // (WIDTH // COLS)
        if self.board[row][col] != EMPTY:
            return
        self.board[row][col] = self.current_player
        if self.current_player == CROSS:
            self.draw_cross(row, col)
        else:
            self.draw_circle(row, col)
        if self.check_win():
            self.show_win_message()
        elif self.check_tie():
            self.show_tie_message()
        else:
            self.switch_player()
            if self.current_player == self.ai_player:
                self.ai_move()

    def draw_cross(self, row, col):
        x1 = col * WIDTH // COLS + OFFSET
        y1 = row * HEIGHT // ROWS + OFFSET
        x2 = (col + 1) * WIDTH // COLS - OFFSET
        y2 = (row + 1) * HEIGHT // ROWS - OFFSET
        self.canvas.create_line(
            x1, y1, x2, y2, width=CROSS_WIDTH, fill=CROSS_COLOR)
        x1 = (col + 1) * WIDTH // COLS - OFFSET
        y1 = row * HEIGHT // ROWS + OFFSET
        x2 = col * WIDTH // COLS + OFFSET
        y2 = (row + 1) * HEIGHT // ROWS - OFFSET
        self.canvas.create_line(
            x1, y1, x2, y2, width=CROSS_WIDTH, fill=CROSS_COLOR)

    def draw_circle(self, row, col):
        x1 = col * WIDTH // COLS + OFFSET
        y1 = row * HEIGHT // ROWS + OFFSET
        x2 = (col + 1) * WIDTH // COLS - OFFSET
        y2 = (row + 1) * HEIGHT // ROWS - OFFSET
        self.canvas.create_oval(
            x1, y1, x2, y2, width=CIRCLE_WIDTH, outline=CIRCLE_COLOR)

    def switch_player(self):
        if self.current_player == CROSS:
            self.current_player = CIRCLE
        else:
            self.current_player = CROSS

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

    def show_win_message(self):
        messagebox.showinfo("Game Over", f"{self.current_player} wins!")
        self.game_over = True

    def show_tie_message(self):
        messagebox.showinfo("Game Over", "Tie game!")
        self.game_over = True

    def ai_move(self):
        level = self.difficulty.get()  # get the selected difficulty level
        # pass the level to the function call
        row, col = ia(self.board, self.ai_player, level)
        # row, col = ia(self.board, self.ai_player)
        if row is not False and col is not False:
            self.board[row][col] = self.ai_player
            self.draw_circle(row, col)
            if self.check_win():
                self.show_win_message()
            elif self.check_tie():
                self.show_tie_message()
            else:
                self.switch_player()
        else:
            print("Error: AI couldn't make a move")

    def has_won(self, player):
        # Check rows
        for row in range(ROWS):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] == player:
                return True
        # Check columns
        for col in range(COLS):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == player:
                return True
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

    def is_tie(self):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] == EMPTY:
                    return False
        return True

    def get_opponent(self, player):
        return CROSS if player == CIRCLE else CIRCLE


if __name__ == "__main__":
    game = TicTacToe()
    game.root.mainloop()


i have this error, every difficulty of the ia :
Error: AI couldn't make a move