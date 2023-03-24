from constants import *
from minimaxAI import MinimaxAI

class Game:
    def __init__(self):
        self.board = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
        self.current_player = CROSS
        self.ai_player = CIRCLE

    def make_move(self, row, col):
        if self.board[row][col] == EMPTY:
            self.board[row][col] = self.current_player
            self.current_player = CIRCLE if self.current_player == CROSS else CROSS
            return True
        else:
            return False

    def choose_move_with_minimax(self):
        ai = MinimaxAI(self.ai_player, self.current_player)
        return ai.eval(self.board)

    def play(self):
        while True:
            print(self.board)
            if self.current_player == self.ai_player:
                row, col = self.choose_move_with_minimax()
            else:
                row, col = input("Enter row and column: ").split()
                row, col = int(row), int(col)

            if self.make_move(row, col):
                if self.final_state() != -1:
                    print(self.board)
                    print("Game over.")
                    break
            else:
                print("Invalid move. Try again.")
                continue

    def final_state(self):
        # check rows
        for row in range(ROWS):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] and self.board[row][0] != EMPTY:
                return self.board[row][0]

        # check columns
        for col in range(COLS):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != EMPTY:
                return self.board[0][col]

        # check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != EMPTY:
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != EMPTY:
            return self.board[0][2]

        # check for a tie
        if self.isfull():
            return 0

        # game is still ongoing
        return -1

    def isfull(self):
        """
        Returns True if the board is full (no more empty squares), False otherwise.
        """
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] == EMPTY:
                    return False
        return True
