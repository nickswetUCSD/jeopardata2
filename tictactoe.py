
import regex as re

#GLOBAL VARS
line = '=' * 20
game_running = True

def tictactoe():
    '''Plays an interactive game of tictactoe'''

    def interface(options):
        '''Provide a list of options (as strings) to assign to numerical commands to. Prints a UI string and starts and returns input.''' 

        ui = ''
        for idx in range(len(options)):
            ui += f'[{idx}]: {options[idx]}\n'
        print(ui)

        out = input()
        return out

    def assess_victory(spots):
        '''Determines victory of tic tac toe board described by "spots" in the game loop.'''
        #Create regex string
        ttt_string = ''
        for i in range(0, 3):
            ttt_string += spots[(3 * (i)) + 1] + spots[3 * (i) + 2] + spots[3 * (i) + 3]
            ttt_string += '-'
        ttt_string = ttt_string[:-1].replace(' ', '#')
        # print(f'I see this: {ttt_string}')

        #Format string for assessment
        board = '###'.join(ttt_string.split('-'))

        horizontal = re.findall('(X{3})|(O{3})', board)
        right_diagonal = re.findall('(X.{4}X.{4}X)|(O.{4}O.{4}O)', board)
        vertical = re.findall('(X.{5}X.{5}X)|(O.{5}O.{5}O)', board)
        left_diagonal = re.findall('(X.{6}X.{6}X)|(O.{6}O.{6}O)', board)

        match = horizontal + vertical + left_diagonal + right_diagonal
        if match:
            return True
        return False


    def game():
        '''Plays the game of Tic Tac Toe!'''
        #Initialize current player
        current_player = 1

        #Set up spots dictionary
        spots = {}
        for i in range(1, 10):
            spots[i] = ' '

        def update_board():
            '''Returns an updated game board ASCII Art.'''
            return f'\n\n{line}\nCurrent Board:\n\n {spots[1]} | {spots[2]} | {spots[3]} \n-----------\n {spots[4]} | {spots[5]} | {spots[6]} \n-----------\n {spots[7]} | {spots[8]} | {spots[9]}  '

        while game_running:
            # Print the game board
            board = update_board()
            print(board)

            # Prompt the player
            print(f"\nPLAYER {current_player} -- Where would you like to move? (Enter a number from 1 - 9)")
            
            # Input move
            try:
                move = int(input())
            except ValueError:
                move = 'notanumber'
            move_not_number = move not in list(range(1, 10))
            move_not_available = False
            if move in spots:
                move_not_available = spots[move] != ' '

            # Addressing illegal moves
            while move_not_number or move_not_available:
                if move_not_number:
                    print(f'\nPlease select a *number* from 1 - 9, PLAYER {current_player}')
                else:
                    print(f'\nPlease select an available space, PLAYER {current_player}... (Enter a number from 1 - 9)')
                # Input move
                try:
                    move = int(input())
                except ValueError:
                    move = 'notanumber'
                move_not_number = move not in list(range(1, 10))
                move_not_available = False
                if move in spots:
                    move_not_available = spots[move] != ' '

            if current_player == 1:
                spots[int(move)] = 'X'
                current_player = 2
            else:
                spots[int(move)] = 'O'
                current_player = 1

            victory = assess_victory(spots)
            if victory:
                board = update_board()
                print(board)
                print(f'\nPLAYER {3 - current_player} WINS!\n\nHUZZAH!\n{line}\n')
                break
            
            spaces_left = 0
            for i in range(1, 10):
                if spots[i] == ' ':
                    spaces_left += 1
            if spaces_left == 0:
                print(f'\nIT\'S A DRAW!\n\nNICE TRY EVERYBODY!\n{line}\n')
                break
                

    #MAIN MENU LOOP
    print('Welcome To Tic-Tac-Toe!\nWhat would you like to do?')
    menu_options = ['Play The Game!', 'Exit Game']
    choice = interface(menu_options)
    if choice == '0':
        while True:
            print('\nAwesome! Let\'s play!')
            game()
            return_to_menu_options = ['Play Again', 'Exit Game']
            choice = interface(return_to_menu_options)
            if choice == '1':
                break
    print(f'\nUntil next time!\nEXITING GAME . . .\n{line}')
    exit()


if __name__ == '__main__':
    tictactoe()