import random
import copy
from constants import *

class MinimaxAI:
    def __init__(self, player=2):
        self.player = player

    def rnd(self, board):
        empty_sqrs = self.get_empty_sqrs(board)
        idx = random.randrange(0, len(empty_sqrs))
        return empty_sqrs[idx]  # (row, col)

    def minimax(self, board, maximizing):
        # Terminal cases
        case = self.final_state(board)
        if case == 1:
            return 1, None  # Player 1 wins
        elif case == 2:
            return -1, None  # Player 2 wins
        elif self.isfull(board):
            return 0, None  # Draw

        # Non-terminal cases
        if maximizing:
            max_eval = -100
            best_move = None
            empty_sqrs = self.get_empty_sqrs(board)

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board = self.mark_sqr(row, col, 1, temp_board) # for maximizing player 1
                eval = self.minimax(temp_board, False)[0]
                if eval > max_eval:
                    max_eval = eval
                    best_move = (row, col)

            return max_eval, best_move

        else:  # minimizing
            min_eval = 100
            best_move = None
            empty_sqrs = self.get_empty_sqrs(board)

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board = self.mark_sqr(row, col, self.player, temp_board) # for minimizing player 2
                eval = self.minimax(temp_board, True)[0]
                if eval < min_eval:
                    min_eval = eval
                    best_move = (row, col)

            return min_eval, best_move


    def eval(self, main_board):
    # Minimax algo choice
        if self.player == 1:  # maximizing player goes first
            _, move = self.minimax(main_board, True)
        else:
            _, move = self.minimax(main_board, False)
            
        return move


    def get_empty_sqrs(self, board):
        """
        Returns a list of empty squares, where each element is a tuple of row and column indices
        """
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == EMPTY:
                    empty_sqrs.append((row, col))
        return empty_sqrs
    
    def final_state(self, board):
    # check rows
        for row in range(ROWS):
            if board[row][0] == board[row][1] == board[row][2] and board[row][0] != EMPTY:
                return board[row][0]

        # check columns
        for col in range(COLS):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
                return board[0][col]

        # check diagonals
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
            return board[0][0]

        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
            return board[0][2]

        # check for a tie
        if self.isfull(board):
            return 0

        # game is still ongoing
        return -1


    def isfull(self, board):
        """
        Returns True if the board is full (no more empty squares), False otherwise.
        """
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == EMPTY:
                    return False
        return True
    
    def mark_sqr(self, row, col, mark, board):
        board[row][col] = mark