puzzle= [ '1','2','3',
          '4','5',' ',
          '7','8','6',]
is_game_over = False
position = [0]


# display game board
def game_board():
    print('|' +puzzle[0] + '|' + puzzle[1]+'|'+puzzle[2]+'|')
    print('|' +puzzle[3] + '|' + puzzle[4]+'|'+puzzle[5]+'|')
    print('|' +puzzle[6] + '|' + puzzle[7]+'|'+puzzle[8]+'|')

# check for winning
def check_game_over():
    
    if puzzle == ['1','2','3','4','5','6','7','8',' ']:
        
        return True
    else: 
        return False

# sliding puzzle
def find_position():
    global position
    for i in puzzle:
        if i == ' ':
            position.pop(0)
            position.append(puzzle.index(i))

# Move left
def move_left():
    if position not in [0,3,6]:
        puzzle[position[0]], puzzle[position[0]-1] = puzzle[position[0]-1] , puzzle[position[0]]
       
# Move right
def move_right():
    if position not in [2,5,8]:
        puzzle[position[0]], puzzle[position[0]+1] = puzzle[position[0]+1] , puzzle[position[0]]
       
# Move up
def move_up():
    if position not in [0,1,2]:
        puzzle[position[0]], puzzle[position[0]-3] = puzzle[position[0]-3] , puzzle[position[0]]
        
# Move down
def move_down():
    if position not in [6,7,8]:
        puzzle[position[0]], puzzle[position[0]+3] = puzzle[position[0]+3] , puzzle[position[0]]
        


              
        
        
    

# Change position
def change_position():
    key = input('left = a, right = d, up = w, down = s: ')
    if key == 'a':
        move_left()
    elif key == 'd':
        move_right()
    elif key == 'w':
        move_up()
    elif key == 's':
        move_down()    
    else:
        key = input('left = a, right = d, up = w, down = s: ')


# Play game
def play_game():
    while not check_game_over():
        game_board()
        find_position()
        change_position()
    
    print(' you are done!!')
        




            

play_game()



