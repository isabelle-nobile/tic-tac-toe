import tkinter as tk
from tkinter import messagebox
from constants import *
from ia import ia

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
        self.canvas.pack()
        self.draw_lines()
        self.canvas.bind("<Button-1>", self.click_handler)
        self.board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
        self.current_player = CROSS
        self.game_over = False
        self.ai_player = CIRCLE
        self.root.iconbitmap('icon_tic_tac_toe.ico')

         # Créer un widget menubar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Créer un menu "Jeu"
        # https://koor.fr/Python/Tutoriel_Tkinter/tkinter_menu.wp
        game_menu = tk.Menu(menubar, tearoff=0)
        # menubar.add_cascade(label="Jeu", menu=game_menu)
        # game_menu.add_command(label="Lancer le jeu", command=self.start_game)
        # game_menu.add_command(label="Relancer le jeu", command=self.reset_game)
        game_menu.add_command(label="Play vs Player", command=self.start_pvp)
        game_menu.add_command(label="Play vs AI", command=self.start_pvai)
        # game_menu.add_command(label="Quitter", command=self.quit_game)

        # Create buttons
        # self.pvp_button = tk.Button(self.root, text="Play vs Player", command=self.start_pvp)
        # self.pvp_button.pack(side=tk.LEFT, padx=5, pady=5)
        # self.pvai_button = tk.Button(self.root, text="Play vs AI", command=self.start_pvai)
        # self.pvai_button.pack(side=tk.RIGHT, padx=5, pady=5)

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
            self.canvas.create_line(x, 0, x, HEIGHT, width=LINE_WIDTH, fill=LINE_COLOR)
        for i in range(1, ROWS):
            y = i * HEIGHT // ROWS
            self.canvas.create_line(0, y, WIDTH, y, width=LINE_WIDTH, fill=LINE_COLOR)

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
        self.canvas.create_line(x1, y1, x2, y2, width=CROSS_WIDTH, fill=CROSS_COLOR)
        x1 = (col + 1) * WIDTH // COLS - OFFSET
        y1 = row * HEIGHT // ROWS + OFFSET
        x2 = col * WIDTH // COLS + OFFSET
        y2 = (row + 1) * HEIGHT // ROWS - OFFSET
        self.canvas.create_line(x1, y1, x2, y2, width=CROSS_WIDTH, fill=CROSS_COLOR)


    def draw_circle(self, row, col):
        x1 = col * WIDTH // COLS + OFFSET
        y1 = row * HEIGHT // ROWS + OFFSET
        x2 = (col + 1) * WIDTH // COLS - OFFSET
        y2 = (row + 1) * HEIGHT // ROWS - OFFSET
        self.canvas.create_oval(x1, y1, x2, y2, width=CIRCLE_WIDTH, outline=CIRCLE_COLOR)

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
        row, col = ia(self.board, self.ai_player)
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


if __name__ == "__main__":
    game = TicTacToe()
    game.root.mainloop()

