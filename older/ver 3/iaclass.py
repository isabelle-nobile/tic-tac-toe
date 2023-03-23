import random
from utils import check_winner
from mainclass import check_tie

class TicTacToeAI:
    def __init__(self, ai_sign):
        self.ai_sign = ai_sign
        self.human_sign = 'O' if ai_sign == 'X' else 'X'

    def get_empty_cells(self, board):
        empty_cells = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    empty_cells.append((i, j))
        return empty_cells

    def get_move(self, board):
        empty_cells = self.get_empty_cells(board)
        if empty_cells:
            return random.choice(empty_cells)
        else:
            return False

    def minimax(self, board, sign):
        if check_winner(board, self.human_sign):
            return -1
        elif check_winner(board, self.ai_sign):
            return 1
        elif check_tie(board):
            return 0

        scores = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = sign
                    scores.append(self.minimax(board, self.human_sign if sign == self.ai_sign else self.ai_sign))
                    board[i][j] = ' '

        if sign == self.ai_sign:
            return max(scores)
        else:
            return min(scores)

    def get_best_move(self, board):
        best_score = float('-inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = self.ai_sign
                    score = self.minimax(board, self.human_sign)
                    board[i][j] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move