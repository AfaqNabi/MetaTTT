#----------------------------------------------------
# Assignment 2: Tic Tac Toe classes
# 
# Author: 
# Collaborators:
# References: Lab 3, CMPUT 174 class ntoes
#----------------------------------------------------


class NumTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''
        self.board = []  # list of lists, where each internal list represents a row
        self.size = 3  # number of columns and rows of board

        # populate the empty squares in board with 0
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.board.append(row)

    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row
        indicies shown.
        Inputs: none
        Returns: None
        '''
        # for i in range(self.size):
        #     print('  ', i, end=' ')
        print('    0   1   2 ',end='')
        for row in range(self.size):
            print('\n', row, '', end=' ')
            # print(' -----------')
            for col in range(self.size):
                if self.board[row][col] == 0:
                    print(' ', end=' ')
                    # print('1')
                else:
                    print(self.board[row][col], end=' ')
                if col + 1 != self.size:
                    print('|', end=' ')
            if (row + 1) != self.size:
                print('\n   -----------', end='')
        print()

    def squareIsEmpty(self, row, col):

        '''
        Checks if a given square is empty, or if it already contains a number
        greater than 0.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is empty; False otherwise
        '''

        if self.board[row][col] == 0:
            return True
        else:
            return False

    def update(self, row, col, num):
        '''
        Assigns the integer, num, to the board at the provided row and column,
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           num (int) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        if self.squareIsEmpty(row, col):
            self.board[row][col] = num
            return True
        return False

    def boardFull(self):
        '''
        Checks if the board has any remaining empty squares.
        Inputs: none
        Returns: True if the board has no empty squares (full); False otherwise
        '''
        # TO DO: delete pass and complete method

        for i in range(self.size):
            for j in range(self.size):
                if self.squareIsEmpty(i, j):
                    return False
        return True

    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) that
        adds up to 15. That line can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move;
                 False otherwise
        '''
        zero = 0
        winner = False
        col_win = False
        row_win = False
        dia_win = False
        for row in self.board:
            # print(row)
            if zero not in row and sum(row)==15:
                row_win = True

        for row in range(self.size):
            column = []
            for col in range(self.size):
                # print(col)
                tile = self.board[col][row]
                column.append(tile)
            if zero not in column and sum(column)== 15:
                col_win = True
            # print(column)

        diagonal1 = []
        diagonal2 = []
        for index in range(self.size):
            # index will be 0,1,2
            tile = self.board[index][index]
            diagonal1.append(tile)
            tile = self.board[index][self.size - 1 - index]
            diagonal2.append(tile)
            # print(diagonal1)
            if (zero not in diagonal2 and sum(diagonal2) == 15) or (zero not in diagonal1 and sum(diagonal1) == 15):
                dia_win = True
        if col_win or dia_win or row_win:
            winner = True

        return winner

    def isNum(self):
        '''
        Checks whether this is a Numerical Tic Tac Toe board or not
        Inputs: none
        Returns: True
        '''
        # TO DO: delete pass (and this comment) and complete method
        return True
    
    
class ClassicTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Classic Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''
        self.board = []  # list of lists, where each internal list represents a row
        self.size = 3 # number of columns and rows of board
        self.player1='X'
        self.player2='O'

        # populate the empty squares in board with 0
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.board.append(row)

        # TO DO: delete pass (and this comment) and complete method

    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indices shown.
        Inputs: none
        Returns: None
        '''
        # for i in range(self.size):
        #     print('  ', i, end=' ')
        print('    0   1   2 ',end='')
        for row in range(self.size):
            print('\n', row, '', end=' ')
            for col in range(self.size):
                if self.board[row][col] == 0:
                    print(' ', end=' ')
                else:
                    print(self.board[row][col], end=' ')
                if col + 1 != self.size:
                    print('|', end=' ')
            if (row + 1) != self.size:
                print('\n   -----------', end='')
        print()
        # TO DO: delete pass (and this comment) and complete method



    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is "empty", or if it already contains an X or O.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is "empty"; False otherwise
        '''
         # TO DO: delete pass (and this comment) and complete method
        if self.board[row][col] == 0:
            return True
        else:
            return False
    
    
    def update(self, row, col, mark):
        '''
        Assigns the string, mark, to the board at the provided row and column, 
        but only if that square is "empty".
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           mark (str) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
         # TO DO: delete pass (and this comment) and complete method
        if self.squareIsEmpty(row, col):
            self.board[row][col] = mark
            return True
        return False


    def boardFull(self):
        '''
        Checks if the board has any remaining "empty" squares.
        Inputs: none
        Returns: True if the board has no "empty" squares (full); False otherwise
        '''
        # TO DO: delete pass (and this comment) and complete method
        for i in range (self.size):
            for j in range (self.size):
                if (self.squareIsEmpty(i,j) == True):
                    return False
        return True
        
           
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) with 
        matching marks (i.e. 3 Xs  or 3 Os). That line can be horizontal, vertical,
        or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        winner = False
        col_win = False
        row_win = False
        dia_win = False
        x=['X','X','X']
        o=['O','O','O']

        # row win
        for row in self.board:
            if row==x or row==o:
                row_win=True

        # diagonal win
        diagonal1 = []
        diagonal2 = []
        for index in range(self.size):
            # index will be 0,1,2
            tile = self.board[index][index]
            diagonal1.append(tile)
            tile = self.board[index][self.size - 1 - index]
            diagonal2.append(tile)
        if diagonal1==x or diagonal1==o or diagonal2==x or diagonal2==o:
            dia_win=True


        # column win
        for row in range(self.size):
            column = []
            for col in range(self.size):
                tile = self.board[col][row]
                column.append(tile)
            if column==x or column==o:
                col_win=True

        if col_win or dia_win or row_win:
            winner = True
        return winner

    
    def isNum(self):
        '''
        Checks whether this is a Numerical Tic Tac Toe board or not
        Inputs: none
        Returns: False
        '''
        # TO DO: delete pass (and this comment) and complete method
        return False


class MetaTicTacToe:
    def __init__(self, configFile):
        '''
        Initializes an empty Meta Tic Tac Toe board, based on the contents of a 
        configuration file.
        Inputs: 
           configFile (str) - name of a text file containing configuration information
        Returns: None
        '''
        self.local_game=[]

        self.f= open(configFile,'r')
        for line in self.f:
            x = line.strip()
            z = x.split()
            self.local_game.append(z)
        self.f.close()
        # self.local_copy = self.local_game

        # TO DO: delete pass (and this comment) and complete method
        self.board = []  # list of lists, where each internal list represents a row
        self.size = 3  # number of columns and rows of board

        # populate the empty squares in board with 0
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.board.append(row)
                
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indices shown.
        Inputs: none
        Returns: None
        '''
        print('    0   1   2 ',end='')
        # for i in range(self.size):
        #     print('   ',i, end='')
        for row in range(self.size):
            print('\n', row, '', end=' ')
            for col in range(self.size):
                if self.board[row][col] == 0:
                    print(self.local_game[row][col], end=' ')
                else:
                    print(self.board[row][col], end=' ')
                if col + 1 != self.size:
                    print('|', end=' ')
            if (row + 1) != self.size:
                print('\n   -----------', end='')
        print()


    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square contains a non-played local game board ("empty"),
        or the result of a played local game board (not "empty").
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is "empty"; False otherwise
        '''

         # TO DO: delete pass (and this comment) and complete method

        if self.board[row][col] == 0:
            return True
        else:
            return False


    def update(self, row, col, result):
        '''
        Assigns the string, result, to the board at the provided row and column, 
        but only if that square is "empty".
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           result (str) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
         # TO DO: delete pass (and this comment) and complete method
        if self.squareIsEmpty(row, col):
            self.board[row][col] = result
            return True
        elif not self.squareIsEmpty(row,col):
            return False


    def boardFull(self):
        '''
        Checks if the board has any remaining "empty" squares (i.e. any un-played
        local boards).
        Inputs: none
        Returns: True if the board has no "empty" squares (full); False otherwise
        '''
        # TO DO: delete pass (and this comment) and complete method
        for i in range (self.size):
            for j in range (self.size):
                if self.squareIsEmpty(i,j):
                    return False
        return True


    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) of their
        mark (three Xs for Player 1, three Os for Player 2), or 3 draws. That line
        can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        winner = False
        col_win = False
        row_win = False
        dia_win = False
        x=['X','X','X']
        o=['O','O','O']
        d=['D','D','D']

        # row win
        for row in self.board:
            if row==x or row==o or row==d:
                row_win=True

        # diagonal win
        diagonal1 = []
        diagonal2 = []
        for index in range(self.size):
            # index will be 0,1,2
            tile = self.board[index][index]
            diagonal1.append(tile)
            tile = self.board[index][self.size - 1 - index]
            diagonal2.append(tile)
        if diagonal1==x or diagonal1==o or diagonal2==x or diagonal2==o or diagonal1==d or diagonal2==d:
            dia_win=True


        # column win
        for row in range(self.size):
            column = []
            for col in range(self.size):
                tile = self.board[col][row]
                column.append(tile)
            if column==x or column==o or column==d:
                col_win=True

        if col_win or dia_win or row_win:
            winner = True
        return winner

        # TO DO: delete pass (and this comment) and complete method

    
    def getLocalBoard(self, row, col):
        '''
        Returns the instance of the empty local board at the specified row, col 
        location (i.e. either ClassicTicTacToe or NumTicTacToe).
        Inputs:
           row (int) - row index of square
           col (int) - column index of square
        Returns: instance of appropriate empty local board if un-played; 
                 None if local board has already been played
        '''
        if self.local_game[row][col] == 'c':
            return ClassicTicTacToe()
        else:
            return NumTicTacToe()

        # TO DO: delete pass (and this comment) and complete method


if __name__ == "__main__":
    # x=NumTicTacToe()
    # x.drawBoard()
    # x.update(0,0,4)
    # x.update(1,1,9)
    # x.update(2,2,2)
    # x.drawBoard()
    # print(x.isWinner())
    # myBoard = MetaTicTacToe('MetaTTTconfig.txt')
    # myBoard.drawBoard()
    # print(myBoard.board)
    # myBoard.update(1,1,'X')
    # print(myBoard.board)
    myBoard = NumTicTacToe()
    myBoard.drawBoard()
    myBoard.update(0,0,9)

    # y=myBoard.getLocalBoard(1,1)
    # y.drawBoard()
    # y.update(0,0,9)
    # y.update(1,1,4)
    # y.update(2,2,2)
    # y.drawBoard()
    # print(y.isWinner())
    # try:
    #     myBoard.update(1,1,'O')
    #     myBoard.drawBoard()
    #
    # except:
    #     print('hellos')
    # else:
    #     print('hi')

    # myBoard.drawBoard()
    # myBoard.update(0,0,'X')
    # myBoard.drawBoard()
    # myBoard.update(1,1,'O')
    # myBoard.update(2,2,'X')
    # myBoard.drawBoard()
    # # x.isWinner()
    # print(myBoard.isWinner())
    # print(x.isWinner())
    #
    # # suggested tests are provided as comments, but more tests may be required
    # #
    # # start by creating empty board and checking the contents of the board attribute
    # myBoard1 = ClassicTicTacToe()
    # print(myBoard1.board)
    # myBoard = ClassicTicTacToe()
    # myBoard1.drawBoard()
    # myBoard1.update(0,0,'X')
    # myBoard1.update(0,1,'X')
    # myBoard1.update(0,2,'X')
    # myBoard1.drawBoard()
    # print(myBoard1.board)
    # print(myBoard1.isWinner())
    # print('Contents of board attribute when object first created:')
    # print(myBoard.board)
    #
    # # does the empty board display properly?
    # myBoard.drawBoard()
    #
    # # print(myBoard.boardFull())
    #
    # #
    # myBoard.update(0, 0, 8)
    # # myBoard.update(0,0,4)
    # myBoard.update(0, 1, 1)
    # myBoard.update(0, 2, 6)
    # myBoard.update(1,0,5)
    # myBoard.drawBoard()
    # # print(myBoard.board)
    # print(myBoard.isWinner())

