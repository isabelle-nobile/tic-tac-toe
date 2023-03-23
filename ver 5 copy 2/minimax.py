class Minimax:
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent

    def get_best_move(self, board):
        best_score = float('-inf')
        best_move = None
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '-':
                    board[i][j] = self.player
                    score = self.minimax(board, False)
                    board[i][j] = '-'
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        if best_move is None:  # No valid moves left
            return (-1, -1)
        else:
            return best_move

    def minimax(self, board, is_maximizing):
        if self.check_win(board, self.player):
            return 1
        elif self.check_win(board, self.opponent):
            return -1
        elif self.check_tie(board):
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == '-':
                        board[i][j] = self.player
                        score = self.minimax(board, False)
                        board[i][j] = '-'
                        best_score = max(score, best_score)
            return best_score

        else:
            best_score = float('inf')
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == '-':
                        board[i][j] = self.opponent
                        score = self.minimax(board, True)
                        board[i][j] = '-'
                        best_score = min(score, best_score)
            return best_score
    
    
    def check_win(self, board, player):
        win_states = [
            [board[0][0], board[0][1], board[0][2]],
            [board[1][0], board[1][1], board[1][2]],
            [board[2][0], board[2][1], board[2][2]],
            [board[0][0], board[1][0], board[2][0]],
            [board[0][1], board[1][1], board[2][1]],
            [board[0][2], board[1][2], board[2][2]],
            [board[0][0], board[1][1], board[2][2]],
            [board[2][0], board[1][1], board[0][2]],
        ]
        for state in win_states:
            if state.count(player) == 3:
                return True
        return False

    def check_tie(self, board):
        for row in board:
            if '-' in row:
                return False
        return True

