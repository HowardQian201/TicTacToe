from tkinter import *
from tkmacosx import *

symbol = "O"
turnNumber = 0
gamelist = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def button_click(number,button):
    change_text(button)
    global turnNumber
    turnNumber = turnNumber + 1
    playamove(number, gamelist, turnNumber)
    if (isgameover(gamelist) == True):
        pass

def change_text(button):
    if (isgameover(gamelist) == True):
        button["state"] = "disabled"
    elif (isgameover(gamelist)==False):
        button.config(text=symbol)
        button["state"] = "disabled"

def playamove(number, gamelist, turn):
    if (turn % 2 == 1):
        global symbol
        symbol = 'X'
    elif (turn % 2 == 0):
        symbol = 'O'
    gamelist[number-1] = symbol
    isgameover(gamelist)

def isgameover(gamelist):
    if ((gamelist[0] == 'X' and gamelist[1] == 'X' and gamelist[2] == 'X') or
            (gamelist[3] == 'X' and gamelist[4] == 'X' and gamelist[5] == 'X') or
            (gamelist[6] == 'X' and gamelist[7] == 'X' and gamelist[8] == 'X') or
            (gamelist[0] == 'X' and gamelist[3] == 'X' and gamelist[6] == 'X') or
            (gamelist[1] == 'X' and gamelist[4] == 'X' and gamelist[7] == 'X') or
            (gamelist[2] == 'X' and gamelist[5] == 'X' and gamelist[8] == 'X') or
            (gamelist[0] == 'X' and gamelist[4] == 'X' and gamelist[8] == 'X') or
            (gamelist[2] == 'X' and gamelist[4] == 'X' and gamelist[6] == 'X')):
        label2 = Label(text="Congratulations! 'O' won! The game is over.")
        label2.grid(row=6,columnspan=3)
        return True
    elif ((gamelist[0] == 'O' and gamelist[1] == 'O' and gamelist[2] == 'O') or
            (gamelist[3] == 'O' and gamelist[4] == 'O' and gamelist[5] == 'O') or
            (gamelist[6] == 'O' and gamelist[7] == 'O' and gamelist[8] == 'O') or
            (gamelist[0] == 'O' and gamelist[3] == 'O' and gamelist[6] == 'O') or
            (gamelist[1] == 'O' and gamelist[4] == 'O' and gamelist[7] == 'O') or
            (gamelist[2] == 'O' and gamelist[5] == 'O' and gamelist[8] == 'O') or
            (gamelist[0] == 'O' and gamelist[4] == 'O' and gamelist[8] == 'O') or
            (gamelist[2] == 'O' and gamelist[4] == 'O' and gamelist[6] == 'O')):
        label2 = Label(text="Congratulations! 'X' won! The game is over.")
        label2.grid(row=6,columnspan=3)
        return True
    elif (gamelist[0] != ' ' and gamelist[1] != ' ' and gamelist[2] != ' ' and
          gamelist[3] != ' ' and gamelist[4] != ' ' and gamelist[5] != ' ' and
          gamelist[6] != ' ' and gamelist[7] != ' ' and gamelist[8] != ' ' ):
        label2 = Label(text="It's a tie. No one won.")
        label2.grid(row=6,columnspan=3)
        return True
    else:
        return False

class Board():
    def __init__(self):
        self.button1 = Button(text=" ", height = 25, width = 95, command=lambda: button_click(1,self.button1))
        self.button1.grid(row=2,column=0)
        self.button2 = Button(text=" ", height = 25, width = 95, command=lambda: button_click(2,self.button2))
        self.button2.grid(row=2, column=1)
        self.button3 = Button(text=" ", height = 25, width = 95, command=lambda: button_click(3,self.button3))
        self.button3.grid(row=2, column=2)
        self.button4 = Button(text=" ", height = 25, width = 95, command=lambda: button_click(4,self.button4))
        self.button4.grid(row=3, column=0)
        self.button5 = Button(text=" ", height = 25, width = 95, command=lambda: button_click(5,self.button5))
        self.button5.grid(row=3, column=1)
        self.button6 = Button(text=" ", height = 25, width = 95, command=lambda: button_click(6,self.button6))
        self.button6.grid(row=3, column=2)
        self.button7 = Button(text=" ", height = 25, width = 95, command=lambda: button_click(7,self.button7))
        self.button7.grid(row=4, column=0)
        self.button8 = Button(text=" ", height = 25, width = 95, command=lambda: button_click(8,self.button8))
        self.button8.grid(row=4, column=1)
        self.button9 = Button(text=" ", height = 25, width = 95, command=lambda: button_click(9,self.button9))
        self.button9.grid(row=4, column=2)

        self.label1 = Label(text='Welcome to Tic Tac Toe!\nClick on any empty square to begin.')
        self.label1.grid(row=0,column=0,columnspan=3)
        self.label2 = Label(text="The first move will be 'O' and moves\nwill alternate between 'X' and 'O'.")
        self.label2.grid(row=1,column=0,columnspan=3)

def main():
    root = Tk()
    Board()
    root.geometry("285x200")
    quitButton = Button(root, text = "Quit", height = 25, width = 285, command = root.destroy)
    quitButton.grid(row=5,columnspan=3,)
    root.title("Tic Tac Toe")
    root.mainloop()

if __name__ == '__main__':
    main()