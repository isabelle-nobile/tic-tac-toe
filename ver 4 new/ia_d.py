import copy
from constants import *

class difficult_ia:
    def __init__(self, board, ai_player):
        self.board = board
        self.ai_player = ai_player

    def get_best_move(self):
        best_score = float('-inf')
        best_move = None

        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == EMPTY:
                    board_copy = copy.deepcopy(self.board)
                    board_copy[row][col] = self.ai_player
                    score = self.minimax(board_copy, 0, False)
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        return best_move

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner(board, CROSS):
            return -10 + depth
        elif self.check_winner(board, CIRCLE):
            return 10 - depth
        elif self.check_tie(board):
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for row in range(len(board)):
                for col in range(len(board[row])):
                    if board[row][col] == EMPTY:
                        board_copy = copy.deepcopy(board)
                        board_copy[row][col] = CIRCLE
                        score = self.minimax(board_copy, depth + 1, False)
                        best_score = max(score, best_score)
            return best_score

        else:
            best_score = float('inf')
            for row in range(len(board)):
                for col in range(len(board[row])):
                    if board[row][col] == EMPTY:
                        board_copy = copy.deepcopy(board)
                        board_copy[row][col] = CROSS
                        score = self.minimax(board_copy, depth + 1, True)
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self, board, player):
        win_states = [[board[0][0], board[0][1], board[0][2]],
                      [board[1][0], board[1][1], board[1][2]],
                      [board[2][0], board[2][1], board[2][2]],
                      [board[0][0], board[1][0], board[2][0]],
                      [board[0][1], board[1][1], board[2][1]],
                      [board[0][2], board[1][2], board[2][2]],
                      [board[0][0], board[1][1], board[2][2]],
                      [board[0][2], board[1][1], board[2][0]]]

        return [player, player, player] in win_states

    def check_tie(self, board):
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == EMPTY:
                    return False
        return True
