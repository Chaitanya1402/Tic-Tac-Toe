from tkinter import *
from tkinter import messagebox

chance = "X"

root = Tk()
root.title("Tic-Tac-Toe")
root.iconbitmap("C:\\Users\\admin\\Downloads\\tic_tac_toe5.ico")
root.geometry("600x400")


def main_body():
    Label(root, text="\tChance:", font=("Franklin Gothic Medium", 13)).grid(row=3, column=8)
    Label(root, text=" "*13 + chance, font=("Franklin Gothic Medium", 17),
          foreground="red").grid(row=4, column=8)
    play_button.grid_remove()

    Button(board, text="", padx=15, pady=10,
           command=lambda: click(2, 0, 1)).grid(row=2, column=0)
    Button(board, text="", padx=15, pady=10,
           command=lambda: click(2, 1, 2)).grid(row=2, column=1)
    Button(board, text="", padx=15, pady=10,
           command=lambda: click(2, 2, 3)).grid(row=2, column=2)

    Button(board, text="", padx=15, pady=10,
           command=lambda: click(3, 0, 4)).grid(row=3, column=0)
    Button(board, text="", padx=15, pady=10,
           command=lambda: click(3, 1, 5)).grid(row=3, column=1)
    Button(board, text="", padx=15, pady=10,
           command=lambda: click(3, 2, 6)).grid(row=3, column=2)

    Button(board, text="", padx=15, pady=10,
           command=lambda: click(4, 0, 7)).grid(row=4, column=0)
    Button(board, text="", padx=15, pady=10,
           command=lambda: click(4, 1, 8)).grid(row=4, column=1)
    Button(board, text="", padx=15, pady=10,
           command=lambda: click(4, 2, 9)).grid(row=4, column=2)


def check_for_win():
    if ((1 in player_x_loc and 2 in player_x_loc and 3 in player_x_loc) or
            (4 in player_x_loc and 5 in player_x_loc and 6 in player_x_loc) or
            (7 in player_x_loc and 8 in player_x_loc and 9 in player_x_loc) or
            (1 in player_x_loc and 4 in player_x_loc and 7 in player_x_loc) or
            (2 in player_x_loc and 5 in player_x_loc and 8 in player_x_loc) or
            (3 in player_x_loc and 6 in player_x_loc and 9 in player_x_loc) or
            (1 in player_x_loc and 5 in player_x_loc and 9 in player_x_loc) or
            (3 in player_x_loc and 5 in player_x_loc and 7 in player_x_loc)):
        ret = messagebox.showinfo("Win!", "Player X - {} won!".format(player1.get().title()))
        if ret == "ok":
            root.quit()
    elif ((1 in player_o_loc and 2 in player_o_loc and 3 in player_o_loc) or
          (4 in player_o_loc and 5 in player_o_loc and 6 in player_o_loc) or
          (7 in player_o_loc and 8 in player_o_loc and 9 in player_o_loc) or
          (1 in player_o_loc and 4 in player_o_loc and 7 in player_o_loc) or
          (2 in player_o_loc and 5 in player_o_loc and 8 in player_o_loc) or
          (3 in player_o_loc and 6 in player_o_loc and 9 in player_o_loc) or
          (1 in player_o_loc and 5 in player_o_loc and 9 in player_o_loc) or
          (3 in player_o_loc and 5 in player_o_loc and 7 in player_o_loc)):
        ret = messagebox.showinfo("Win!", "Player O - {} won!".format(player2.get().title()))
        if ret == "ok":
            root.quit()
    elif count == 9:
        tie = messagebox.showinfo("Tie!", "Its a tie!")
        if tie == "ok":
            root.quit()


def click(row_no, col_no, box_no):
    global chance
    global player_x_loc
    global player_o_loc
    global count

    if chance == "X":
        Label(board, text=chance, foreground="red", padx=11, pady=5, relief=GROOVE,
              font=("Franklin Gothic Medium", 17)).grid(row=row_no, column=col_no)
        player_x_loc.append(box_no)
        chance = "O"
        Label(root, text=" " * 13 + chance, font=("Franklin Gothic Medium", 17),
              foreground="blue").grid(row=4, column=8)
    else:
        Label(board, text=chance, foreground="blue", padx=10, pady=5, relief=GROOVE,
              font=("Franklin Gothic Medium", 17)).grid(row=row_no, column=col_no)
        player_o_loc.append(box_no)
        chance = "X"
        Label(root, text=" " * 13 + chance, font=("Franklin Gothic Medium", 17),
              foreground="red").grid(row=4, column=8)
    count += 1

    check_for_win()


blank0 = Label(root, text="")
blank0.grid(row=0, column=0)

Label(root, text="Enter Player X Name :   ", font=("Lucida Fax", 11)).grid(row=1, column=0)
Label(root, text="Enter Player O Name :   ", font=("Lucida Fax", 11)).grid(row=3, column=0)

player1 = Entry(root, width=20, font=("Times New Roman", 14))
player1.grid(row=1, column=1, columnspan=7)

blank1 = Label(root, text="")
blank1.grid(row=2, column=0)

player2 = Entry(root, width=20, font=("Times New Roman", 14))
player2.grid(row=3, column=1, columnspan=7)

blank2 = Label(root, text="")
blank2.grid(row=4, column=0)

board = LabelFrame(root)
board.grid(row=5, column=1)

player_x_loc = []
player_o_loc = []

count = 0

play_button = Button(root, text="Play Game!", background="#87ED6D",
                     font=("Franklin Gothic Medium", 13), command=main_body)
play_button.grid(row=5, column=1)

root.mainloop()
