# import tkinter as tk
# from tkinter import messagebox

# class Menu:

#     # Créer un widget menubar
#     menubar = tk.Menu(self.root)
#     self.root.config(menu=menubar)

#     # Créer un menu "Jeu"

#     game_menu = tk.Menu(menubar, tearoff=0)
#     menubar.add_cascade(label="Jeu", menu=game_menu)
#     game_menu.add_command(label="Relancer le jeu", command=self.reset_game)
#     game_menu.add_command(label="Play vs Player", command=self.start_pvp)
#     game_menu.add_command(label="Play vs AI", command=self.start_pvai)


from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from ver 5 copy 2.main import *
from ia import *
import ver 5 copy 2.main as main

class MyWindow():

    def __init__(self):
        self.create_menu_bar()

        # TODO: Fill the content of the window

        self.geometry("300x200")
        self.title("My First MenuBar V1.0")
        # self.start_pvp()
        self.main = main

    def create_menu_bar(self):
        menu_bar = Menu(self)

        menu_file = Menu(menu_bar, tearoff=0)

        # Un menu déroulant dans le menu Difficulty.
        menu_recent = Menu(menu_file, tearoff=0)
        menu_recent.add_command(label="Easy")
        menu_recent.add_command(label="Difficult")
        menu_file.add_cascade(label="Difficulty", underline=0, menu=menu_recent)

        menu_bar.add_cascade(label="Play vs AI", underline=0, menu=menu_file)

        # self.bind_all("<Control-n>", lambda x: self.do_something())
        # self.bind_all("<Control-o>", lambda x: self.open_file())
        # self.bind_all("<Control-s>", lambda x: self.do_something())

        menu_edit = Menu(menu_bar, tearoff=0)
        menu_bar.add_command(label="Play vs Player", command=self.start_pvp_menu)
        # menu_bar.add_cascade(label="Play vs Player", underline=0, menu=menu_edit)

        menu_help = Menu(menu_bar, tearoff=0)
        menu_help.add_command(label="About...", command=self.do_about)
        menu_bar.add_cascade(label="Help", underline=0, menu=menu_help)

        self.config(menu=menu_bar)

    def start_pvp_menu():
        return main().start_pvp()



window = MyWindow()
window.mainloop()










# def create_menu_bar(self):
    #     menu_bar = tk.Menu(self.root)
    #     menu_file = tk.Menu(menu_bar, tearoff=0)

    #     # Un menu déroulant dans le menu Difficulty.
    #     menu_recent = tk.Menu(menu_file, tearoff=0)
    #     menu_recent.add_command(label="Easy")
    #     menu_recent.add_command(label="Difficult")
    #     menu_file.add_cascade(label="Difficulty", underline=0, menu=menu_recent)

    #     menu_bar.add_cascade(label="Play vs AI", underline=0, menu=menu_file)

    #     # self.bind_all("<Control-n>", lambda x: self.do_something())
    #     # self.bind_all("<Control-o>", lambda x: self.open_file())
    #     # self.bind_all("<Control-s>", lambda x: self.do_something())

    #     menu_edit = tk.Menu(menu_bar, tearoff=0)
    #     menu_bar.add_command(label="Play vs Player", command=self.start_pvp, menu=menu_edit)
    #     # menu_bar.add_cascade(label="Play vs Player", underline=0, menu=menu_edit)

    #     menu_help = tk.Menu(menu_bar, tearoff=0)
    #     menu_help.add_command(label="About...", command=self.do_about)
    #     menu_bar.add_cascade(label="Help", underline=0, menu=menu_help)

    #     self.config(menu=menu_bar)