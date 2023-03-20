from tkinter import *
root = Tk()
player_character = ''
positions = ['-','-','-','-','-','-','-','-','-']

def x_select():
    global player_character
    player_character = 'X'
    player_label = Label(root, text=' You have selected ' + player_character ).grid(row=3, column=0)
    start_button = Button(root, text='Start!', command=draw_board).grid(row=4, column=0)


def o_select():
    global player_character
    player_character = 'O'
    player_label = Label(root, text=' You have selected ' + player_character ).grid(row=3, column=0)
    start_button = Button(root, text='Start!', command=draw_board).grid(row=4, column=0)

def player_pos(position):
    if 0 <= position <= 2:
        r = 0
    elif 3 <= position <= 5:
        r = 6
    else:
        r = 7
    if position == 0 or position == 3 or position == 6:
        c = 0 
    elif position == 1 or position == 4 or position == 7:
        c = 1
    else:
        c = 2

    positions[position] = player_character
    new_button = Button(root, text=positions[position]).grid(row=r, column=c)

def draw_board():
    global positions
    positions = ['-','-','-','-','-','-','-','-','-']
    t_l = Button(root, text=positions[0], command=lambda: player_pos(0)).grid(row=5, column=0)
    t_m = Button(root, text=positions[1], command=lambda: player_pos(1)).grid(row=5, column=1)
    t_r = Button(root, text=positions[2], command=lambda: player_pos(2)).grid(row=5, column=2)
    m_l = Button(root, text=positions[3], command=lambda: player_pos(3)).grid(row=6, column=0)
    m_m = Button(root, text=positions[4], command=lambda: player_pos(4)).grid(row=6, column=1)
    m_r = Button(root, text=positions[5], command=lambda: player_pos(5)).grid(row=6, column=2)
    b_l = Button(root, text=positions[6], command=lambda: player_pos(6)).grid(row=7, column=0)
    b_m = Button(root, text=positions[7], command=lambda: player_pos(7)).grid(row=7, column=1)
    b_r = Button(root, text=positions[8], command=lambda: player_pos(8)).grid(row=7, column=2)


#widget definition 
main_label = Label(root, text='Welcome to Tic_Tact_Toe')
player_select_label = Label(root, text=' Select a character to play as!')
x_button = Button(root, text='X', command=x_select)
o_button = Button(root, text='O', command=o_select)

#draw onto screen 
main_label.grid(row=0, column=0)
player_select_label.grid(row=1, column=0)
x_button.grid(row=2, column=0)
o_button.grid(row=2, column=1)

root.mainloop()