puzzle= [ '1','2','3',
          '4','5','6',
          '7','8',' ',]
is_game_over = False
position = []
input_key = ['a','s','d','w']

# display game board
def game_board():
    print('|' +puzzle[0] + '|' + puzzle[1]+'|'+puzzle[2]+'|')
    print('|' +puzzle[3] + '|' + puzzle[4]+'|'+puzzle[5]+'|')
    print('|' +puzzle[6] + '|' + puzzle[7]+'|'+puzzle[8]+'|')

# check for winning
def check():
    if puzzle == ['1','2','3','4','5','6','7','8',' ']:
        return is_game_over == True
    else: 
        return is_game_over == False

# sliding puzzle
def find_position():
    global position
    for i in puzzle:
        if i == ' ':
            return position.append(puzzle.index(i))

# Change position
def change_position():
    key = input('left = a, right = d, up = w, down = s: ')
    valid = False
    while not valid:
        
        while key not in input_key:
            key = input('left = a, right = d, up = w, down = s: ')
            if position == 0 and key == 'a' or key == 'w':
                print('you cannot move that way')
            elif position == 1 and key == 'w':
                print('you cannot move that way')
            elif position == 2 and key == 'w' or key == 'd':
                print('you cannot move that way')
            elif position == 3 and key == 'a':
                print('you cannot move that way')
            elif position == 5 and key == 'd':
                print('you cannot move that way')
            elif position == 6 and key == 'a' or key == 's':
                print('you cannot move that way')
            elif position == 7 and key == 's':
                print('you cannot move that way')
            elif position == 8 and key == 's' or key == 'd':
                print('you cannot move that way')
            else:
                valid = True
            
    
    


# Move left
def move_left():
    if input_key == 'a' and position not in [0,3,6]:
        if position == 1:
            puzzle[position-1], puzzle[position] = puzzle[position], puzzle[position-1]
        elif position == 2:
            puzzle[position-1],puzzle[position] = puzzle[position], puzzle[position-1]
        elif position == 4:
            puzzle[position-1],puzzle[position] = puzzle[position], puzzle[position-1]
        elif position == 5:
            puzzle[position-1],puzzle[position] = puzzle[position], puzzle[position-1]
        elif position == 7:
            puzzle[position-1],puzzle[position] = puzzle[position], puzzle[position-1]
        elif position == 8:
            puzzle[position-1],puzzle[position] = puzzle[position], puzzle[position-1]


# Play game
def play_game():
    while is_game_over != True:
        game_board()
        find_position()
        change_position()
        check()




            

play_game()



