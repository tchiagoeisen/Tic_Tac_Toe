tic_tac_toe = {
             '1': ' ', '2': ' ', '3': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '7': ' ', '8': ' ', '9': ' '
              }

counter = 0
board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def welcome():
  print('')
  print('Welcome to Tic Tac Toe!')
  print('To play the game insert a position for X and O from 1 to 9 acording with the numpad:')
  print( '#########################')
  print(f'#       |       |       #')
  print(f'#   7   |   8   |   9   #')
  print(f'#_______|_______|_______#')
  print(f'#       |       |       #')
  print(f'#   4   |   5   |   6   #')
  print(f'#_______|_______|_______#')
  print(f'#       |       |       #')
  print(f'#   1   |   2   |   3   #')
  print(f'#       |       |       #')
  print( '#########################')
  print('')

def game_table():
  print( '#########################')
  print(f'#       |       |       #')
  print(f'#   {G}   |   {H}   |   {I}   #')
  print(f'#_______|_______|_______#')
  print(f'#       |       |       #')
  print(f'#   {D}   |   {E}   |   {F}   #')
  print(f'#_______|_______|_______#')
  print(f'#       |       |       #')
  print(f'#   {A}   |   {B}   |   {C}   #')
  print(f'#       |       |       #')
  print( '#########################')
  print('')

def game():
  game_solution = ['XXX','OOO',[tic_tac_toe['1'] + tic_tac_toe['2'] +tic_tac_toe['3'],
                                tic_tac_toe['4'] + tic_tac_toe['5'] +tic_tac_toe['6'],
                                tic_tac_toe['7'] + tic_tac_toe['8'] +tic_tac_toe['9'],
                                tic_tac_toe['1'] + tic_tac_toe['4'] +tic_tac_toe['7'],
                                tic_tac_toe['2'] + tic_tac_toe['5'] +tic_tac_toe['8'],
                                tic_tac_toe['3'] + tic_tac_toe['6'] +tic_tac_toe['9'],
                                tic_tac_toe['1'] + tic_tac_toe['5'] +tic_tac_toe['9'],
                                tic_tac_toe['3'] + tic_tac_toe['5'] +tic_tac_toe['7']]]

  for x in game_solution[2]:
    if x == game_solution[0]:
        print('X Won!')
        return True
    if x == game_solution[1]:
        print('O Won!')
        return True
  

welcome()


while True:
  
  input_x = input('Insert postion(1-9) for X: ')
  
  while input_x not in board or tic_tac_toe[input_x] != ' ':
    print('Error: Input is not between 1 and 9 or position already taken!')
    input_x = input('Insert position(1-9) for X: ')


  tic_tac_toe[input_x] = 'X'
  
  A = tic_tac_toe['1']
  B = tic_tac_toe['2']
  C = tic_tac_toe['3']
  D = tic_tac_toe['4']
  E = tic_tac_toe['5']
  F = tic_tac_toe['6']
  G = tic_tac_toe['7']
  H = tic_tac_toe['8']
  I = tic_tac_toe['9']
  
  game_table()

  if game() == True:
    break
  else:
    counter += 1
    if counter == 5:
      print('No Winner!')
      break

  input_o = input('Insert postion(1-9) for O: ')
  
  while input_o not in board or tic_tac_toe[input_o] != ' ':
    print('Error: Input is not between 1 and 9 or position already taken!')
    input_o = input('Insert position(1-9) for O: ')


  tic_tac_toe[input_o] = 'O'

  A = tic_tac_toe['1']
  B = tic_tac_toe['2']
  C = tic_tac_toe['3']
  D = tic_tac_toe['4']
  E = tic_tac_toe['5']
  F = tic_tac_toe['6']
  G = tic_tac_toe['7']
  H = tic_tac_toe['8']
  I = tic_tac_toe['9']

  game_table()
  if game() == True:
    break
