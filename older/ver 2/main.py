import tkinter as tk
from tkinter import messagebox
from ia import ia  # importation de la fonction IA

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = "X"  # le joueur X commence
        self.board = [0] * 9  # initialise le tableau du plateau de jeu
        self.buttons = []  # initialise la liste des boutons
        self.game_over = False  # la partie n'est pas terminée
        self.create_board()  # crée le plateau de jeu
        self.window.mainloop()

    def create_board(self):
        for i in range(9):
            button = tk.Button(self.window, text="", font=("Arial", 60), width=3, height=1, command=lambda i=i: self.play(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def play(self, position):
        if not self.game_over:
            if self.board[position] == 0:  # vérifie si la case est libre
                self.board[position] = self.current_player  # place le signe du joueur sur la case
                self.buttons[position].config(text=self.current_player)  # affiche le signe sur le bouton

                if self.check_winner():  # vérifie si un joueur a gagné
                    messagebox.showinfo("Tic Tac Toe", f"Le joueur {self.current_player} a gagné !")
                    self.game_over = True

                elif self.check_draw():  # vérifie si la partie est terminée en match nul
                    messagebox.showinfo("Tic Tac Toe", "Match nul !")
                    self.game_over = True

                else:
                    self.switch_player()  # change de joueur

            else:
                messagebox.showerror("Tic Tac Toe", "Case déjà occupée !")

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def check_winner(self):
        # vérifie les alignements possibles pour les deux joueurs
        possible_alignments = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for alignment in possible_alignments:
            if self.board[alignment[0]] == self.board[alignment[1]] == self.board[alignment[2]] != 0:
                return True
        return False

    def check_draw(self):
        return all([position != 0 for position in self.board])

    def play_ia(self):
        if not self.game_over:
            position = ia(self.board, self.current_player)  # appelle la fonction IA pour obtenir la position à jouer
            if position is not False:
                self.play(position)
            else:
                messagebox.showerror("Tic Tac Toe", "Erreur dans l'IA !")


if __name__ == "__main__":
    TicTacToe()
