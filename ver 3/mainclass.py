import tkinter as tk
from tkinter import messagebox
from constants import *
from iaclass import *
from utils import check_winner


class TicTacToeGame:
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
        self.ai_player = None
        self.ai_difficulty = 2  # Default difficulty is "hard".
        self.root.iconbitmap('icon_tic_tac_toe.ico')

        # Create a menu bar.
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Create a "Game" menu.
        game_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Game", menu=game_menu)
        game_menu.add_command(label="Restart game", command=self.reset_game)
        game_menu.add_command(label="Play vs Player", command=self.start_pvp)
        game_menu.add_command(label="Play vs AI", command=self.start_pvai)
        game_menu.add_command(label="Select difficulty", command=self.select_difficulty)

    def select_difficulty(self):
        # Show a dialog box with difficulty options.
        options = [
            ("Easy", 1),
            ("Hard", 2)
        ]
        var = tk.StringVar()
        var.set(str(self.ai_difficulty))
        for text, mode in options:
            tk.Radiobutton(self.root, text=text, variable=var, value=mode).pack(anchor=tk.W)
        tk.Button(self.root, text="OK", command=lambda: self.set_difficulty(var.get())).pack()
    
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
        if check_winner():
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

    def ai_move(self):
        # Check if it's AI's turn and difficulty is set
        if self.ai_player == self.current_player and hasattr(self, 'difficulty'):
            if self.difficulty == 1:
            # Select a random empty cell
                move = ia(self.board, self.ai_player)
            elif self.difficulty == 2:
            # Find the best move using minimax algorithm
                move = self.find_best_move()
            else:
                raise ValueError("Invalid difficulty level")
                    # Make the move
        if move:
            self.board[move[0]][move[1]] = self.ai_player
            row, col = move
            if self.ai_player == CROSS:
                self.draw_cross(row, col)
            else:
                self.draw_circle(row, col)
            
            # Check if AI has won or game is tied
            if self.check_win():
                self.show_win_message()
            elif self.check_tie():
                self.show_tie_message()
            else:
                self.switch_player()

def find_best_move(self):
    # Find the best move for AI using minimax algorithm
    scores = []
    for i in range(3):
        for j in range(3):
            if self.board[i][j] == EMPTY:
                self.board[i][j] = self.ai_player
                score = minimax(self.board, self.current_player)
                self.board[i][j] = EMPTY
                scores.append(score)
            else:
                scores.append(None)
    
    # Choose the move with the highest score
    best_score = -2 if self.ai_player == CROSS else 2
    best_move = None
    for i in range(len(scores)):
        if scores[i] is not None:
            if self.ai_player == CROSS and scores[i] > best_score:
                best_score = scores[i]
                best_move = (i // 3, i % 3)
            elif self.ai_player == CIRCLE and scores[i] < best_score:
                best_score = scores[i]
                best_move = (i // 3, i % 3)
    
    return best_move

def switch_player(self):
    # Switch player
    self.current_player = CROSS if self.current_player == CIRCLE else CIRCLE

def check_tie(self):
    # Check if the game is tied
    for row in self.board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True

def show_win_message(self):
    # Show message box with the winner
    winner = self.current_player
    if winner == CROSS:
        messagebox.showinfo("Tic Tac Toe", "X a gagné!")
    else:
        messagebox.showinfo("Tic Tac Toe", "O a gagné!")
    self.game_over = True

def show_tie_message(self):
    # Show message box with tie message
    messagebox.showinfo("Tic Tac Toe", "Match nul!")
    self.game_over = True


if __name__ == "__main__":
    game = TicTacToeGame()
    game.root.mainloop()
