# This program will run a tic tac toe game!
import functions
from tkinter import *

gamelist = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
game_board = ''
playerinput = ''
turn = 1
keyword = 'none'


willweplay = functions.startgame()

if willweplay:
    game_board = functions.createboard()
    while(functions.isgameover(gamelist) == False):
        print('This is our game board: \n' + game_board)
        game_board = functions.playamove(game_board,gamelist,turn)
        turn+=1
    print('This is the final board:\n' + game_board)

#add: a way to exit the game mid way