#This class will define all the functions needed


def startgame():
    playgame = 'nothing'
    while ((playgame != 'Y' and playgame != 'y') and (playgame != 'N' and playgame != 'n')):
        playgame = input("Would you like to play tic tac toe? (Y/N): ")
    if (playgame=='Y' or playgame=='y'):
        return True
    else:
        print('Ok')

def createboard():
    gamelist = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    new_board = f' {gamelist[0]} | {gamelist[1]} | {gamelist[2]}\n-----------\n {gamelist[3]} | {gamelist[4]}' \
                f' | {gamelist[5]}\n-----------\n {gamelist[6]} | {gamelist[7]} | {gamelist[8]}'
    print('Each space on the board corresponds to a number (1,2,3:top row - 4,5,6:middle row - 7,8,9:bottom row)')
    print("The first player will be 'X' and the second player will be 'O'")
    return new_board

def playamove(game_board, gamelist, turn):
    playerinput = ''
    while (playerinput != '1' and playerinput !='2' and playerinput !='3' and playerinput !='4' and
           playerinput !='5' and playerinput !='6' and playerinput !='7' and playerinput !='8' and playerinput !='9'):
        if (turn%2==1):
            playerinput = input("Player 'X': Which square would you like to fill? (1-9) ")
        elif (turn%2==0):
            playerinput = input("Player 'O': Which square would you like to fill? (1-9) ")
        if (playerinput == '1' or playerinput =='2' or playerinput =='3' or playerinput =='4' or
           playerinput =='5' or playerinput =='6' or playerinput =='7' or playerinput =='8' or playerinput =='9'):
            if gamelist[int(playerinput)-1] != ' ':
                print("Sorry, that square is already taken")
                playerinput = 'nothing'
            else:
                pass
    if (turn % 2 == 1):
        gamelist[int(playerinput)-1] = 'X'
        game_board = f' {gamelist[0]} | {gamelist[1]} | {gamelist[2]}\n-----------\n {gamelist[3]} | {gamelist[4]}' \
                    f' | {gamelist[5]}\n-----------\n {gamelist[6]} | {gamelist[7]} | {gamelist[8]}'
    elif(turn % 2 == 0):
        gamelist[int(playerinput) - 1] = 'O'
        game_board = f' {gamelist[0]} | {gamelist[1]} | {gamelist[2]}\n-----------\n {gamelist[3]} | {gamelist[4]}' \
                     f' | {gamelist[5]}\n-----------\n {gamelist[6]} | {gamelist[7]} | {gamelist[8]}'
    if (isgameover(gamelist) == True):
        return isgameover(gamelist) and game_board
    elif (isgameover(gamelist) == False):
        return game_board

def isgameover(gamelist):
    if ((gamelist[0] == 'X' and gamelist[1] == 'X' and gamelist[2] == 'X') or
            (gamelist[3] == 'X' and gamelist[4] == 'X' and gamelist[5] == 'X') or
            (gamelist[6] == 'X' and gamelist[7] == 'X' and gamelist[8] == 'X') or
            (gamelist[0] == 'X' and gamelist[3] == 'X' and gamelist[6] == 'X') or
            (gamelist[1] == 'X' and gamelist[4] == 'X' and gamelist[7] == 'X') or
            (gamelist[2] == 'X' and gamelist[5] == 'X' and gamelist[8] == 'X') or
            (gamelist[0] == 'X' and gamelist[4] == 'X' and gamelist[8] == 'X') or
            (gamelist[2] == 'X' and gamelist[4] == 'X' and gamelist[6] == 'X')):
        print("Congratulations! 'X' won! The game is over.")
        return True
    elif ((gamelist[0] == 'O' and gamelist[1] == 'O' and gamelist[2] == 'O') or
            (gamelist[3] == 'O' and gamelist[4] == 'O' and gamelist[5] == 'O') or
            (gamelist[6] == 'O' and gamelist[7] == 'O' and gamelist[8] == 'O') or
            (gamelist[0] == 'O' and gamelist[3] == 'O' and gamelist[6] == 'O') or
            (gamelist[1] == 'O' and gamelist[4] == 'O' and gamelist[7] == 'O') or
            (gamelist[2] == 'O' and gamelist[5] == 'O' and gamelist[8] == 'O') or
            (gamelist[0] == 'O' and gamelist[4] == 'O' and gamelist[8] == 'O') or
            (gamelist[2] == 'O' and gamelist[4] == 'O' and gamelist[6] == 'O')):
        print("Congratulations! 'O' won! The game is over.")
        return True
    elif (gamelist[0] != ' ' and gamelist[1] != ' ' and gamelist[2] != ' ' and
          gamelist[3] != ' ' and gamelist[4] != ' ' and gamelist[5] != ' ' and
          gamelist[6] != ' ' and gamelist[7] != ' ' and gamelist[8] != ' ' ):
        print("It's a tie. No one won.")
        return True
    else:
        return False