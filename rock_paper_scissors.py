from random import *

def rock_paper_scissors():
    """
    user inputs: C = player v computer
    user inputs: P = player v player
    :return: winner
    """
    player_or_comp = ['C', 'P']
    options = {'R': 'P', 'P': 'S', 'S': 'R'}
    computer_options = ['R', 'P', 'S']

    def who_wins(player1, player2, computer=False):
        x, y = 'Player 2 Wins', 'Computer Wins'
        if computer is False:
            z = x
        else:
            z = y
        if options[player1] == player2:
            return z
        elif player1 == player2:
            return 'Draw'
        else:
            return 'Player 1 wins'

    while True:
        user_input = input("Enter either P = Player mode or C = Computer mode or Q = Quit : ")
        if len(user_input) == 0:
            return 'Nothing entered'
        else:
            user_input = user_input[0]
        if user_input not in player_or_comp:
            return 'Unknown Command'

        elif user_input == 'Q':
            return 'Exiting now'
        elif user_input == 'P':
            player_1, player_2 = '', ''
            while True:
                index = 0
                for i in range(2):
                    players = ['Player1', 'Player2']
                    print('')
                    user_input = input('R = Rock \n''P = Paper \n' 'S = Scissors \n \n'
                                       'Q = Quit \n' 'C = vs Computer \n'
                                       + str(players[index]) + ' : ')
                    if user_input == 'Q':
                        return 'Exiting Now'
                    if user_input == 'C':
                        rock_paper_scissors()
                        return
                    print('')
                    index += 1
                    if i == 0:
                        player_1 = user_input
                    else:
                        player_2 = user_input

                print(who_wins(player_1, player_2))

        elif user_input == 'C':
            while True:
                print('')
                user_input = input('R = Rock \n''P = Paper \n' 'S = Scissors \n \n'
                                   'Q = Quit \n' 'C = vs Computer \n'
                                   'Player : ')
                computer = computer_options[randrange(0, len(computer_options) - 1)]
                print('Computer chose : ' + str(computer))
                print(who_wins(user_input, computer, True))


rock_paper_scissors()
