
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-'] 


current_player='X' 


def display_board():
  print(board[0] + ' | ' + board[1] + ' | ' + board[2])
  print(board[3] + ' | ' + board[4] + ' | ' + board[5])
  print(board[6] + ' | ' + board[7] + ' | ' + board[8])
  

def choose_location():
  print(current_player,"'s turn")
  Location = input('Choose a location from 1-9 : ')
  Location = int(Location) - 1
  if board[int(Location)] == '-':
    board[Location] = current_player
  else:
    print('Location is already occupied.Pls try again.')
    choose_location()
  
global game_run
game_run = True
def check_winner():  
  row1 = board[0]==board[1]==board[2] != '-'
  row2 = board[3]==board[4]==board[5] != '-'
  row3 = board[6]==board[7]==board[8] != '-'
  col1 = board[0]==board[3]==board[6] != '-'
  col2 = board[1]==board[4]==board[7] != '-'
  col3 = board[2]==board[5]==board[8] != '-'
  diag1= board[0]==board[4]==board[8] != '-'
  diag2= board[2]==board[4]==board[6] != '-'
  if row1 == True:
    print(board[0]+' is winner')
  elif row2 == True:
    print(board[3]+' is winner')
  elif row3 == True:
    print(board[6]+' is winner')
  elif col1 == True:
    print(board[0]+' is winner')
  elif col2 == True :
    print(board[1]+' is winner')
  elif col3 == True :
    print(board[2]+' is winner') 
  elif diag1 == True:
    print(board[8]+' is winner')
  elif diag2 == True:
    print(board[4]+' is winner')

  elif "-" not in board :
    print('Tie')

  global game_run
  if col1 or col2 or col3 or row1 or row2  or row3 or diag1 or diag2 or '-' not in board :
    game_run = False


def flip_player():
  global current_player
  if current_player=='X':
    current_player='O'
  elif current_player=='O':
    current_player='X'
 

display_board()
while game_run :
  choose_location()
  display_board()
  check_winner()
  flip_player()
  
  

