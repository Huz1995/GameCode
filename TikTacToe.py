
from IPython.display import clear_output

def display_board(board):

    clear_output()
    print('       |       |       ')
    print('   '+ board[1] +'   |   '+ board[2]  +'   |   '  +board[3]  )
    print('       |       |       ')
    print('------- ------- -------')
    print('       |       |       ')
    print('   '+ board[4] +'   |   '+ board[5]  +'   |   '  +board[6]  )
    print('       |       |       ')
    print('------- ------- -------')
    print('       |       |       ')
    print('   '+ board[7] +'   |   '+ board[8]  +'   |   '  +board[9]  )
    print('       |       |       ')

def player_input():
    
    marker = ''
    
    while marker!= 'X' and marker!= 'O':
        marker = input('Player 1, choose X or O: ' ).upper()
        
    player1 = marker
        
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
            
    return (player1, player2)

def place_marker(board,marker,position):
    
    board[position] = marker

def win_check(board,marker):
      if board[1]==board[2]==board[3]==marker or board[1]==board[4]==board[7]==marker or board[1]==board[5]==board[9]==marker or board[7]==board[5]==board[3]==marker or board[7]==board[8]==board[9]==marker or board[3]==board[6]==board[9]==marker or board[4]==board[5]==board[6]==marker:
                return True    

import random

def choose_first():
    
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'  
        
def space_check(board,position):
    
    return board[position] == ' '
  
def full_board_check(board):
    
    for n in range(1,10):
        if space_check(board,n):
            return False
    
def player_choice(board):
    
    position = 0
    
    while position not in list(range(0,10)) or not space_check(board,position):
        position = int(input('Choose a position, one through nine where one starts at the top left'))
    return position             
 
def replay():
    
    choice = input('Oi, would you like to play again? Enter yes or no')
    
    return choice == 'yes'
    
 

def play_game():
    
    print('Hello user, I am currently reading your mind and sense you want to play tic tak toe!')

    while True:
    
        game_board = [' ']*10
        player1_marker,player2_marker = player_input()
    
        turn = choose_first()
        print(turn + ' is gunna go first. Awaken to your dreams')
    
        play_game = input('So READY TO PLAY? Enter yes or no?:')
    
        if play_game == 'yes':
            game_on = True
        else:
            game_on = False
        
        while game_on:
        
            if turn == 'Player 1':
                display_board(game_board)
                position = player_choice(game_board)
                place_marker(game_board,player1_marker,position)
            
                if win_check(game_board,player1_marker):
                    display_board(game_board)
                    print('Player 1 HAS WON!!')
                    break
                else:
                    if full_board_check(game_board):
                        display_board(game_board)
                        print('Tie Game!')
                        break
                    else:
                        turn = 'Player 2'
        
            else: 
           
                display_board(game_board)
                position = player_choice(game_board)
                place_marker(game_board,player2_marker,position)
            
                if win_check(game_board,player2_marker):
                    display_board(game_board)
                    print('Player 2 HAS WON!!')
                    break
                else:
                    if full_board_check(game_board):
                        display_board(game_board)
                        print('Tie Game!')
                        break
                    else:
                        turn = 'Player 1'
    
        if not replay():
            break