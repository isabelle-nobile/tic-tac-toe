import tkinter as tk
from tkinter import messagebox
from constants import *
from ia import ia
# from ia_d import Minimax
# from minimax import Minimax
# from minimax2 import minimax_ia
from minimaxAI import MinimaxAI

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
        self.canvas.pack()
        self.create_menu_bar()
        self.draw_lines()
        self.canvas.bind("<Button-1>", self.click_handler)
        self.board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
        self.current_player = CROSS
        self.game_over = False
        self.ai_player = CIRCLE
        self.ai = MinimaxAI(player=self.ai_player)

        # self.minimax = Minimax(player=self.current_player, opponent=self.ai_player)
        self.root.iconbitmap('icon_tic_tac_toe.ico')

    def create_menu_bar(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        menu_file = tk.Menu(menu_bar, tearoff=0)

        # Un menu déroulant dans le menu Difficulty.
        menu_recent = tk.Menu(menu_file, tearoff=0)
        menu_recent.add_command(label="Easy", command=self.play_easy)
        menu_recent.add_command(label="Difficult",  command=self.play_difficult)
        menu_file.add_cascade(label="Difficulty", underline=0, menu=menu_recent)
        menu_bar.add_cascade(label="Play vs AI", underline=0, menu=menu_file)

        menu_edit = tk.Menu(menu_bar, tearoff=0)
        menu_edit.add_command(label="PvP", command=self.start_pvp)
        menu_bar.add_cascade(label="Play vs Player", menu=menu_edit)


        menu_reset = tk.Menu(menu_bar, tearoff=0)
        menu_reset.add_command(label="New Game", command=self.reset_game)
        menu_bar.add_cascade(label="Relancer une partie ?", menu=menu_reset)

    def play_easy(self):
        self.difficulty = 'easy'  # ajout de la difficulté choisie
        event = tk.Event()  # create dummy event object
        event.x = WIDTH // 2  # set x and y to center of the canvas
        event.y = HEIGHT // 2
        self.click_handler(event)  # call click_handler with the dummy event
        self.reset_game()

    def play_difficult(self):
        self.difficulty = 'difficult'  # ajout de la difficulté choisie
        event = tk.Event()  # create dummy event object
        event.x = WIDTH // 2  # set x and y to center of the canvas
        event.y = HEIGHT // 2
        self.click_handler(event)  # call click_handler with the dummy event
        self.reset_game()

    def start_pvp(self):
        # self.ai_player = None
        self.difficulty = None
        self.reset_game()
        
    def reset_game(self):
        self.board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
        self.current_player = CROSS
        self.game_over = False
        self.canvas.delete("all")
        self.draw_lines()
        self.ia_difficulty = None


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
            if self.difficulty == 'easy' and self.current_player == self.ai_player:
                self.ai_move_easy()
            elif self.difficulty == 'difficult' and self.current_player == self.ai_player:
                # self.ai_move_difficult()
                self.choose_move_with_minimax()



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

    def ai_move_easy(self):
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


    # def ai_move_difficult(self):

    #     row, col = minimax_ia(self.board, self.ai_player)
    #     self.board[row][col] = self.ai_player
    #     return row, col

    def choose_move_with_minimax(self, player=2):
        ai = MinimaxAI(player=player)
        return ai.eval(self.board)



if __name__ == "__main__":
    game = TicTacToe()
    game.root.mainloop()
