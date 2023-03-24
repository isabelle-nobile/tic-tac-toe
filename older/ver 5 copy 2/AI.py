import math
import random

class TicTacToeAI:
    def __init__(self, ai_player):
        self.ai_player = ai_player

    def get_move(self, board):
        if board is None:
            board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        if self.is_first_move(board):
            return self.make_random_move(board)
        elif self.is_ai_turn(board):
            return self.minimax(board)
        else:
            # Let the other player make their move
            return None


    def is_first_move(self, board):
        return all(all(cell == 0 for cell in row) for row in board)

    def make_random_move(self, board):
        empty_cells = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    empty_cells.append((i, j))
        return random.choice(empty_cells)

    def is_ai_turn(self, board):
        count_x = sum(row.count(1) for row in board)
        count_o = sum(row.count(2) for row in board)
        return count_x == count_o if self.ai_player == 1 else count_x > count_o

    def minimax(self, board):
        if self.is_terminal(board):
            return None

        best_move = (-1, -1)
        best_score = -math.inf if self.ai_player == 1 else math.inf

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    board[i][j] = self.ai_player
                    score = self.minimax_score(board, depth=0, is_maximizing_player=False)
                    board[i][j] = 0  # undo move

                    if (self.ai_player == 1 and score > best_score) or (self.ai_player == 2 and score < best_score):
                        best_score = score
                        best_move = (i, j)

        return best_move



    def minimax_score(self, board, depth, is_maximizing_player):
        if self.is_terminal(board):
            return self.get_terminal_score(board, depth)

        if is_maximizing_player:
            best_score = -math.inf
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == 0:
                        board[i][j] = self.ai_player
                        score = self.minimax_score(board, depth+1, is_maximizing_player=False)
                        board[i][j] = 0  # undo move
                        best_score = max(best_score, score)
            return best_score

        else:  # minimizing player
            best_score = math.inf
            other_player = 2 if self.ai_player == 1 else 1
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == 0:
                        board[i][j] = other_player
                        score = self.minimax_score(board, depth+1, is_maximizing_player=True)
                        board[i][j] = 0  # undo move
                        best_score = min(best_score, score)
            return best_score

    def is_terminal(self, board):
        return self.check_win(board) or self.check_tie(board)

    def check_win(self, board):
        for i in range(len(board)):
            if board[i][0] == board[i][1] == board[i][2] != 0:
                return True
            if board[0][i] == board[1][i] == board[2][i] != 0:
                return True
