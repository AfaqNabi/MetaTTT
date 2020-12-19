from UltimateMetaTTT import NumTicTacToe, MetaTicTacToe, ClassicTicTacToe


def localWinner(player):
    '''
    checks if it is player 1 or player 2 turn and returns a mark accordingly
    if the player two needs to be the X player
    :param player:
    :return: mark
    '''
    # check if the player is player 1 or player 2
    if player % 2 == 0:
        mark = 'O'
    else:
        mark = 'X'
    return mark


def localWinner1(player):
    '''
    checks if it is player 1 or player 2 turn and returns a mark accordingly
    :param player:
    :return: mark
    '''
    # check if the player is player 1 or player 2
    if player % 2 != 0:
        mark = 'O'
    else:
        mark = 'X'
    return mark



def global_entry(local_winner):
    '''
    returns the mark to be put on the global board
    :param local_winner:
    :return: entry
    '''
    entry = ''
    draw = 'D'
    if local_winner == 0: # if player 2 won
        entry = 'O'
    elif local_winner == 1: # if player 1 won
        entry = 'X'
    elif local_winner == draw: # if draw
        entry = draw
    return entry


def getEntry(player):
    '''
    Prompts specified player for number to place on board; reprompts if that
    number is not valid.
    this is one is for the player 2 if they have to start at odd
    Inputs:
       player (int) - number of current player (1 or 2)
       entries (list) - numbers already placed on board
    Returns: int to place on board
    '''

    if player % 2 != 0:
        numDescription = 'even'
        lowerRange = 2
        upperRange = 8
    else:
        numDescription = 'odd'
        lowerRange = 1
        upperRange = 9
    prompt = 'Player {}, please enter an {} number ({}-{}): '
    prompt = prompt.format(player, numDescription, lowerRange, upperRange)
    entry = input(prompt)
    # entries.append(entry)
    if numDescription == 'odd':
        while not int(entry) % 2:
            print('Error: entry not odd . ', end='')
            entry = input(prompt)
    elif numDescription == 'even':
        while int(entry) % 2:
            print('Error: entry not even . ', end='')
            entry = input(prompt)
    return int(entry)


def getEntry_odd(player):
    '''
    Prompts specified player for number to place on board; reprompts if that
    number is not valid.
    Inputs:
       player (int) - number of current player (1 or 2)
       entries (list) - numbers already placed on board
    Returns: int to place on board
    '''


    if player % 2 == 0:
        numDescription = 'even'
        lowerRange = 2
        upperRange = 8
    else:
        numDescription = 'odd'
        lowerRange = 1
        upperRange = 9
    prompt = 'Player {}, please enter an {} number ({}-{}): '
    prompt = prompt.format(player, numDescription, lowerRange, upperRange)
    entry = input(prompt)
    # entries.append(entry)
    if numDescription == 'odd':
        while not int(entry) % 2:
            print('Error: entry not odd . ', end='')
            entry = input(prompt)
    elif numDescription == 'even':
        while int(entry) % 2:
            print('Error: entry not even . ', end='')
            entry = input(prompt)
    return int(entry)


def getCoord(player, dimension):
    '''
    Prompts for an index value corresponding to either the row or column (as
    described by dimension) of a square on the board
    Inputs:
       player (int) - number of current player (1 or 2)
       dimension (str) - describes what the index relates to (e.g. 'row' or 'column')
    Returns: int index (either row or column)
    '''
    turn_condition = False
    while not turn_condition:  # handles anything other than the numbers 0 1 and 2 anything else will be reprompted
        try:
            index = int(input('Player ' + str(player) + ', please enter a ' + dimension + ': '))
            if index in (0, 1, 2):
                turn_condition = True
            else:
                raise
        except:
            try:
                if index not in (0, 1, 2):
                    print('Error: ' + dimension + ' not in correct range. ', end='')
            except:
                print('Error: Please enter an integer between 0 and 2')

    return index


def isGameOver(myBoard, player):
    '''
    The game is over if the current player has won, or there are no empty squares
    left for the next player to select.
    Inputs:
       myBoard (NumTicTacToe) - object containing current state of game board
       player (int) - number of current player (1 or 2)
    Returns: True if game if over; False otherwise
    '''
    if myBoard.isWinner(): # game over condtion for the game loop
        myBoard.drawBoard()
        print('Player', player, "wins. Congrats!")
        return True
    return False


def isGameOverMeta(myBoard, player):
    '''
    The game is over if the current player has won, or there are no empty squares
    left for the next player to select.
    Inputs:
       myBoard (NumTicTacToe) - object containing current state of game board
       player (int) - number of current player (1 or 2)
    Returns: True if game if over; False otherwise
    '''
    if player == 0:
        player = 1
    elif player == 1:
        player = 2
    if myBoard.isWinner(): # game over condition for the metaTT game loop
        myBoard.drawBoard()
        print('Player', player, "wins the Meta Tic Tac Toe game. GOOD GAME!")
        return True
    elif myBoard.boardFull() and (not myBoard.isWinner()):
        myBoard.drawBoard()
        print("It's a tie.")
        return True
    return False


def playAgain():
    '''
    Asks if a new game should be started. A valid answer is any entry that begins
    with y/Y/n/N.
    Inputs: none
    Returns: True if a new game should start; False otherwise
    '''
    playAgain = ' '
    # validate user's input
    while playAgain[0].upper() not in ['Y', 'N']:
        playAgain = input("Do you want to play another game? (Y/N) ")
    if not playAgain[0].upper() == "Y":
        print('Thanks for playing! Goodbye.')
        return False
    else:
        return True


def classicTTT(turn,X_player):
    '''
    returns the player that won or if the game ended in a draw
    runs the whole classic TTT
    the game retruns D if draw
    Meta TT processes the integer turn
    :param turn:
    :return: turn
    '''
    TITLE = "This is a Classical Tic Tac Toe."
    print('------------------------------------')
    print(TITLE)
    myBoard = ClassicTicTacToe()
    gameOver = False
    draw = 'D'
    while not gameOver: # runs the game until winner or draw
        if X_player == 1:  # if the player two needs to be the X player
            myBoard.drawBoard()

            # get input from user
            entry = localWinner1(turn + 1)
            row = getCoord(turn + 1, 'row')
            col = getCoord(turn + 1, 'column')

            # update board and check if game continues
            if myBoard.update(row, col, entry):
                gameOver = isGameOver(myBoard, turn + 1)
                turn = (turn + 1) % 2
                if myBoard.boardFull() and (not myBoard.isWinner):
                    return draw
                # need to reprompt for new input for given player
            else:
                print('Error: could not make move!')
        if X_player == 0:
            myBoard.drawBoard()

            # get input from user
            entry = localWinner(turn + 1)
            row = getCoord(turn + 1, 'row')
            col = getCoord(turn + 1, 'column')

            # update board and check if game continues
            if myBoard.update(row, col, entry):
                gameOver = isGameOver(myBoard, turn + 1)
                turn = (turn + 1) % 2
                if myBoard.boardFull() and (not myBoard.isWinner):
                    return draw
                # need to reprompt for new input for given player
            else:
                print('Error: could not make move!')
    return turn


def numTTT(turn,odd_player):
    '''
    returns the player that won to be processed by main
    runs the whole Numeric TTT game until a draw or a winner is found

    :param turn: switches turns
    :param odd_player: assigns the odd player
    :return: turn
    '''

    TITLE = 'This is a Numerical Tic Tac Toe.'
    print('------------------------------------')
    print(TITLE)
    print(odd_player)
    draw = 'D'

    myBoard = NumTicTacToe()
    gameOver = False
    entries = []
    while not gameOver: # runs game until there is a winner or draw
        # get input from user
        if odd_player==1:  # if the global player two is to start as the odd player
            myBoard.drawBoard()

            entry = getEntry(turn+1)
            # print(turn)
            while entry in entries:
                print('Error: that number has already been entered. ', end='')
                entry = getEntry(turn+1)

            row = getCoord(turn + 1, 'row')
            col = getCoord(turn + 1, 'column')

            # update board and check if game continues
            if myBoard.update(row, col, entry):
                entries.append(entry)
                gameOver = isGameOver(myBoard, turn + 1)
                turn = (turn + 1) % 2
                if myBoard.boardFull() and (not myBoard.isWinner):
                    return draw
            # need to reprompt for new input for given player
            else:
                print('Error: could not make move!')
        if odd_player == 0: # if the global player one is to start as the odd player
            myBoard.drawBoard()
            entry = getEntry_odd(turn + 1)
            # print(turn)
            while entry in entries:
                print('Error: that number has already been entered. ', end='')
                entry = getEntry_odd(turn + 1)

            row = getCoord(turn + 1, 'row')
            col = getCoord(turn + 1, 'column')

            # update board and check if game continues
            if myBoard.update(row, col, entry):
                entries.append(entry)
                gameOver = isGameOver(myBoard, turn + 1)
                turn = (turn + 1) % 2
                if myBoard.boardFull() and (not myBoard.isWinner):
                    return draw
            # need to reprompt for new input for given player
            else:
                print('Error: could not make move!')
    return turn


def main():
    '''
    runs the whole game
    intiailizes the metaTTT and calles the local TTT games accordingly
    :return:
    '''
    new_game = True
    while new_game:  # main game loop
        strTTT = 'Starting new Meta Tic Tac Toe game'
        print('-' * len(strTTT))
        print(strTTT)
        print('-' * len(strTTT))

        myBoard = MetaTicTacToe('MetaTTTconfig.txt')
        game_over = False
        global_turn = 0

        while not game_over:  # runs the local games
            myBoard.drawBoard()

            row = getCoord(global_turn + 1, 'row')
            col = getCoord(global_turn + 1, 'column')

            if myBoard.squareIsEmpty(row, col):  # so that the a used board cant be picked again
                if myBoard.local_game[row][col] == 'c':  # gets classic pr numeric board
                    local_winner = classicTTT(global_turn,global_turn)  # calls the local game function and gets an integer of the player that won
                else:
                    local_winner = numTTT(global_turn,global_turn)

                entry = global_entry(local_winner)

                if myBoard.update(row, col, entry):
                    game_over = isGameOverMeta(myBoard, global_turn)
                    global_turn = (global_turn + 1) % 2

            else:
                print('error could not make move')

        new_game = playAgain()


if __name__ == '__main__':
    main()
