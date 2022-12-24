#simple tic-tac-toe game runs on terminal


import random

def display_board(board):

    print('-------positions-------')
    print('---------7|8|9---------')
    print('---------4|5|6---------')
    print('---------1|2|3---------')
    print('=======================')
    print('---------Board---------')
    print('---------'+board[7]+'|'+board[8]+'|'+board[9]+'---------')
    print('-----------------------')
    print('---------'+board[4]+'|'+board[5]+'|'+board[6]+'---------')
    print('-----------------------')
    print('---------'+board[1]+'|'+board[2]+'|'+board[3]+'---------')
    print('=======================')

def player_input():
    mrkr = ''

    while (mrkr != 'X' or mrkr != 'O'):
        mrkr = input("Player1, please pick a marker 'X' or 'O' : ").upper()
        if mrkr == 'X':
            print("Player1's marker = X, Player2's marker = O")
            return('X','O')
        elif mrkr =='O':
            print("Player1's marker = O, Player2's marker = X")
            return('O','X')

def place_marker(board,marker,position):
    board[position]=marker

def check_win(board,mark):
    
    if ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark)):

            print('#######################')
            display_board(board)
            print('#######################')
            return True
    return False

def first_player_choose():
    if random.randint(0,1) == 0:
        return 'Player1'
    else:
        return 'Player2'

def check_space(board,pos):
    return board[pos] == ' '

def check_full_board(board):
    for i in range(1,10):
        if check_space(board,i):
            return False 
    return True

def player_choice(board,turn):
    pos = 0

    while pos not in range(1,10) or not check_space(board,pos):
        pos = int(input(turn+' please enter the position you want to mark : '))

    return pos

def play_again():
    return input('Enter Yes(y) for play again, anything else for end: ').lower().startswith('y')

while True:
    play_board = [' ']*10


    player1_mrkr, player2_mrkr = player_input()

    turn = first_player_choose()
    print(turn+' goes first')

    play = input('Enter Yes(y) for start the game: ')
    if play.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn=='Player1':
            display_board(play_board)
            pos = player_choice(play_board,turn)
            place_marker(play_board,player1_mrkr,pos)

            if check_win(play_board,player1_mrkr):
                print('Player1 won the game!')
                game_on = False
            else:
                if check_full_board(play_board):
                    display_board(play_board)
                    print('Game is a draw!')
                    break
                else:
                    turn='Player2'
        else:
            display_board(play_board)
            pos = player_choice(play_board,turn)
            place_marker(play_board,player2_mrkr,pos)

            if check_win(play_board,player2_mrkr):
                print('Player2 won the game!')
                game_on = False
            else:
                if check_full_board(play_board):
                    display_board(play_board)
                    print('Game is a draw!')
                    break
                else:
                    turn = 'Player1'
    if not play_again():
        break