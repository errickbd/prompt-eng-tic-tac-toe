import random
# Pseudocode:
    # 1. Make a list with 3 lists inside that each contain 3 strings
    # 2. Make an input asking the user if they want: 'x' or 'o'
    # 3. Assign each player respective x or o in a dictionary
    # 4. Make an input selection Where to put mark: 'Top Left', 'Top Middle', 'Top Right', 
    #       'Middle Left', 'Middle', 'Middle Right', 'Bottom Left', 'Bottom Middle',
    #       'Middle Right' => corresponds to position in list
    # 5. replace string in list depending on input
    # 6. check to see if there's a win
    # 7. randomize opponents decision
    # 8. check to see if there's a win
    # 9. if there's a win: print the user that wins


#create grid:
grid = [['','',''],
 ['','',''],
['','','']]

#make function to print game grid:
def game_grid():
    for list in grid:
        print(list)

#make input to select x or o:

user_identifier = input('Let\'s play Tic-Tac-Toe. What identifier would you like, \'X\' or \'O\'? ').upper()

if user_identifier == 'X':
    computer_identifier = user_identifier.replace(user_identifier, 'O')
elif user_identifier == 'O':
    computer_identifier = user_identifier.replace(user_identifier, 'X')


#make question string for input
question_string = 'Where on the grid would you like to fill? \'Top Left\', \'Top Middle\', \'Top Right\', \'Middle Left\', \'Middle\', \'Middle Right\', \'Bottom Left\', \'Bottom Middle\', or \'Middle Right\'? '


#make a function to select position for user:
def select_position():
    
    place_identifier = input(question_string).lower()


    match place_identifier:
        case 'top left':
            if grid[0][0] == '': 
                grid[0][0] = user_identifier
            else:
                print('Already taken.')
        case 'top middle':
            if grid[0][1] == '': 
                grid[0][1] = user_identifier
            else:
                print('Already taken.')
        case 'top right':
            if grid[0][2] == '': 
                grid[0][2] = user_identifier
            else:
                print('Already taken.')
        case 'middle left':
            if grid[1][0] == '': 
                grid[1][0] = user_identifier
            else:
                print('Already taken.')
        case 'middle':
            if grid[1][1] == '': 
                grid[1][1] = user_identifier
            else:
                print('Already taken.')
        case 'middle right':
            if grid[1][2] == '': 
                grid[1][2] = user_identifier
            else:
                print('Already taken.')
        case 'bottom left':
            if grid[2][0] == '': 
                grid[2][0] = user_identifier
            else:
                print('Already taken.')
        case 'bottom middle':
            if grid[2][1] == '': 
                grid[2][1] = user_identifier
            else:
                print('Already taken.')
        case 'bottom right':
            if grid[2][2] == '': 
                grid[2][2] = user_identifier
            else:
                print('Already taken.')

    
#make a function to select position for computer:
def computer_move():
    

    place_identifier = random.choice(['top left', 'top middle', 'top right', 
                                      'middle left', 'middle', 'middle right',
                                       'bottom left', 'bottom middle', 'bottom right'])

    match place_identifier:
        case 'top left':
            if grid[0][0] == '': 
                grid[0][0] = computer_identifier
            else:
                print('Already taken.')
                computer_move()
        case 'top middle':
            if grid[0][1] == '': 
                grid[0][1] = computer_identifier
            else:
                print('Already taken.')
                computer_move()
        case 'top right':
            if grid[0][2] == '': 
                grid[0][2] = computer_identifier
            else:
                print('Already taken.')
                computer_move()
        case 'middle left':
            if grid[1][0] == '': 
                grid[1][0] = computer_identifier
            else:
                print('Already taken.')
                computer_move()
        case 'middle':
            if grid[1][1] == '': 
                grid[1][1] = computer_identifier
            else:
                print('Already taken.')
                computer_move()
        case 'middle right':
            if grid[1][2] == '': 
                grid[1][2] = computer_identifier
            else:
                print('Already taken.')
                computer_move()
        case 'bottom left':
            if grid[2][0] == '': 
                grid[2][0] = computer_identifier
            else:
                print('Already taken.')
                computer_move()
        case 'bottom middle':
            if grid[2][1] == '': 
                grid[2][1] = computer_identifier
            else:
                print('Already taken.')
                computer_move()
        case 'bottom right':
            if grid[2][2] == '': 
                grid[2][2] = computer_identifier
            else:
                print('Already taken.')
                computer_move()


#make a function to play game:
def play_game():
#used to check for a draw
    count = 0
#loops to see if there are still open spaces
    for list in grid:
        for item in list:
 #if open spot, it gets marked and new grid is printed
            if item == '':
                select_position()
                count += 1
                computer_move()
                count += 1
                game_grid()
                
                
                if count == 9:
                    return "The game is a draw!"

                
                
    
    #checks if there is a win horizontally
        if grid[0][0] and grid[0][1] and grid[0][2] == 'X':
            return 'X wins!'
        elif grid[0][0] and grid[0][1] and grid[0][2] == 'O':
            return 'O wins'

        elif grid[1][0] and grid[1][1] and grid[1][2] == 'X':
            return 'X wins'
        elif grid[1][0] and grid[1][1] and grid[1][2] == 'O':
            return 'O wins'

        elif grid[2][0] and grid[2][1] and grid[2][2] == 'X':
            return 'X wins'
        elif grid[2][0] and grid[2][1] and grid[2][2] == 'O':
            return 'O wins'

    #checks if there is a win vertically
        elif grid[0][0] and grid[1][0] and grid[2][0] == 'X':
            return 'X wins!'
        elif grid[0][0] and grid[1][0] and grid[2][0] == 'O':
            return 'O wins'

        elif grid[0][1] and grid[1][1] and grid[2][1] == 'X':
            return 'X wins'
        elif grid[0][1] and grid[1][1] and grid[2][1] == 'O':
            return 'O wins'

        elif grid[0][2] and grid[1][2] and grid[2][2] == 'X':
            return 'X wins'
        elif grid[0][2] and grid[1][2] and grid[2][2] == 'O':
            return 'O wins'
        
    #checks if there is a win diagonally:
        elif grid[0][0] and grid[1][1] and grid[2][2] == 'X':
            return 'X wins'
        elif grid[0][0] and grid[1][1] and grid[2][2] == 'O':
            return 'O wins'
        
        elif grid[0][2] and grid[1][1] and grid[2][0] == 'X':
            return 'X wins'
        elif grid[0][2] and grid[1][1] and grid[2][0] == 'O':
            return 'O wins'
        

print(play_game())

