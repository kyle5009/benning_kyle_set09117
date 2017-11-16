#layout of the board the board
board = [['_','b','_','b','_','b','_','b'],
         ['b','_','b','_','b','_','b','_'],
         ['_','b','_','b','_','b','_','b'],
         ['_','_','_','_','_','_','_','_'],
         ['_','_','_','_','_','_','_','_'],
         ['r','_','r','_','r','_','r','_'],
         ['_','r','_','r','_','r','_','r'],
         ['r','_','r','_','r','_','r','_']]

#prints out the board
def printBoard():
    print('   ' + '0' + ' ' + '1' + ' ' + '2' + ' ' + '3' + ' ' + '4' + ' ' + '5' + ' ' + '6' + ' ' + '7' + ' ')
    print('   ' + '_' + ' ' + '_' + ' ' + '_' + ' ' + '_' + ' ' + '_' + ' ' + '_' + ' ' + '_' + ' ' + '_' + ' ' )
    i = 0
    #loops through the range pf 0 to 8 and prints each line of the board
    for i in range(0,8):
        print(str(i) + ' ' + '|' + board[i][0] + '|' + board[i][1] + '|' + board[i][2] + '|' + board[i][3] + '|' + board[i][4] + '|' + board[i][5] +
                '|' + board[i][6] + '|' + board[i][7] + '|')

#makes sure the user cannot pick a piece that is blank
def checkNotBlank(coord_Ax,coord_Ay):
    if board[coord_Ay][coord_Ax] == '_':
        print('you must select a valid piece')
        return False
    else:
        return True

#changes the turn between red and black
def changeTurn():
    global turn
    if turn == 'r':
        turn = 'b'
    else:
        turn = 'r'

#makes sure that the user cannot pick a piece that isnt theres on blacks turn
def notYourPiece_B(coord_Ax,coord_Ay):
    if turn == 'b':
        if board[coord_Ay][coord_Ax] == 'r' and 'R':
            print ('you may only move your own piece')
            return False
        else:
            return True
    else:
        return True

#makes sure that the user cannot pick a piece that isnt theres on reds turn
def notYourPiece_R(coord_Ax,coord_Ay):
    if turn == 'r':
        if board[coord_Ay][coord_Ax] == 'b' and 'B':
            print ('you may only move your own piedce')
            return False
        else:
            return True
    else:
        return True

#makes sure that red pieces can only move one space diagonally, up the board
def moveOne_r1(coord_Ax,coord_Ay,coord_A2x,coord_A2y):
    if turn == 'r':
        if board[coord_Ay][coord_Ax] == 'r':
            if coord_A2y == (coord_Ay - 1) and ((coord_A2x == coord_Ax - 1) or (coord_A2x == coord_Ax + 1)):
                return True
            else:
                print('Illegal move')
                return False
        else:
            return True
    else:
       return True

#makes sure that king black pieces can only move one space diagonally, up and down the board
def moveOne_kb1(coord_Ax,coord_Ay,coord_A2x,coord_A2y):
    if turn == 'b':
        if board[coord_Ay][coord_Ax] == 'B':
            if ((coord_A2y == coord_Ay - 1) or (coord_Ay + 1)) and ((coord_A2x == coord_Ax - 1) or (coord_A2x == coord_Ax + 1)):
                return True
            else:
                print('Illegal move')
                return False
        else:
            print ('1')
            return True
    else:
        print('2')
        return True

#makes sure that black pieces can only move one space diagonally, down the board
def moveOne_b1(coord_Ax,coord_Ay,coord_A2x,coord_A2y):
    if turn == 'b':
        if board[coord_Ay][coord_Ax] == 'b':
            if coord_A2y == (coord_Ay + 1) and ((coord_A2x == coord_Ax - 1) or (coord_A2x == coord_Ax + 1)):
                return True
            else:
                print('Illegal move')
                return False
        else:
            return True
    else:
       return True

#makes sure that king red pieces can only move one space diagonally, up and down the board
def moveOne_kr1(coord_Ax,coord_Ay,coord_A2x,coord_A2y):
    if turn == 'r':
        if board[coord_Ay][coord_Ax] == 'R':
            if ((coord_A2y == coord_Ay - 1) or (coord_Ay + 1)) and ((coord_A2x == coord_Ax - 1) or (coord_A2x == coord_Ax + 1)):
                return True
            else:
                print('Illegal move')
                return False
        else:
            print ('1')
            return True
    else:
        print('2')
        return True

#allows red pieces to jump and take black pieces
def jump_r1(coord_Ax,coord_Ay):
    if turn == 'r':
        if board[coord_Ay - 1][coord_Ax + 1] == 'b':
            if board[coord_Ay - 2][coord_Ax + 2] == '_':
                board[coord_Ay][coord_Ax] = '_'
                board[coord_Ay - 1][coord_Ax + 1] = '_'
                board[coord_Ay - 2][coord_Ax + 2] = 'r'
                changeTurn()
                printBoard()
                return True
            else:
                return True
        else:
            return True
    else:
        return True

#allows red pieces to jump and take black pieces
def jump_r2(coord_Ax,coord_Ay):
    if turn == 'r':
        if board[coord_Ay - 1][coord_Ax - 1] == 'b':
            if board[coord_Ay - 2][coord_Ax - 2] == '_':
                board[coord_Ay][coord_Ax] = '_'
                board[coord_Ay - 1][coord_Ax - 1] = '_'
                board[coord_Ay - 2][coord_Ax - 2] = 'b'
                changeTurn()
                printBoard()
                return True
            else:
                return True
        else:
            return True
    else:
        return True

#allows black pieces to jump and take red pieces
def jump_b1(coord_Ax,coord_Ay):
    if turn == 'b':
        if board[coord_Ay + 1][coord_Ax - 1] == 'r':
            if board[coord_Ay + 2][coord_Ax - 2] == '_':
                board[coord_Ay][coord_Ax] = '_'
                board[coord_Ay + 1][coord_Ax - 1] = '_'
                board[coord_Ay + 2][coord_Ax - 2] = board[coord_Ay][coord_Ax]
                changeTurn()
                printBoard()
                return True
            else:
                return True
        else:
            return True
    else:
        return True

#allows black pieces to jump and take red pieces
def jump_b2(coord_Ax,coord_Ay):
    if turn == 'b':
        if board[coord_Ay + 1][coord_Ax + 1] == 'r':
            if board[coord_Ay + 2][coord_Ax + 2] == '_':
                board[coord_Ay][coord_Ax] = '_'
                board[coord_Ay + 1][coord_Ax + 1] = '_'
                board[coord_Ay + 2][coord_Ax + 2] = board[coord_Ay][coord_Ax]
                changeTurn()
                printBoard()
                return True
            else:
                return True
        else:
            return True
    else:
        return True

# ______________________________________________________________________________________________

def jump_kr1(coord_Ax,coord_Ay):
    if turn == 'r':
        if board[coord_Ay - 1][coord_Ax + 1] == 'B':
            if board[coord_Ay - 2][coord_Ax + 2] == '_':
                board[coord_Ay][coord_Ax] = '_'
                board[coord_Ay - 1][coord_Ax + 1] = '_'
                board[coord_Ay - 2][coord_Ax + 2] = board[coord_Ay][coord_Ax]
                changeTurn()
                printBoard()
                return True
            else:
                return True
        else:
            return True
    else:
        return True

def jump_kr2(coord_Ax,coord_Ay):
    if turn == 'r':
        if board[coord_Ay - 1][coord_Ax - 1] == 'B':
            if board[coord_Ay - 2][coord_Ax - 2] == '_':
                board[coord_Ay][coord_Ax] = '_'
                board[coord_Ay - 1][coord_Ax - 1] = '_'
                board[coord_Ay - 2][coord_Ax - 2] = board[coord_Ay][coord_Ax]
                changeTurn()
                printBoard()
                return True
            else:
                return True
        else:
            return True
    else:
        return True

def jump_kb1(coord_Ax,coord_Ay):
    if turn == 'b':
        if board[coord_Ay + 1][coord_Ax - 1] == 'R':
            if board[coord_Ay + 2][coord_Ax - 2] == '_':
                board[coord_Ay][coord_Ax] = '_'
                board[coord_Ay + 1][coord_Ax - 1] = '_'
                board[coord_Ay + 2][coord_Ax - 2] = board[coord_Ay][coord_Ax]
                changeTurn()
                printBoard()
                return True
            else:
                return True
        else:
            return True
    else:
        return True

def jump_kb2(coord_Ax,coord_Ay):
    if turn == 'b':
        if board[coord_Ay + 1][coord_Ax + 1] == 'R':
            if board[coord_Ay + 2][coord_Ax + 2] == '_':
                board[coord_Ay][coord_Ax] = '_'
                board[coord_Ay + 1][coord_Ax + 1] = '_'
                board[coord_Ay + 2][coord_Ax + 2] = board[coord_Ay][coord_Ax]
                changeTurn()
                printBoard()
                return True
            else:
                return True
        else:
            return True
    else:
        return True

def gameWinner():
    global gameWinner



printBoard()

#sets the turn as r
turn = 'r'
#sets the game winner to true
gameWinner = True
#a loop to keep the game gpoing till a winner is decided
while gameWinner == True:
    #prints what turn it is
    print ('The current turn is ' + (turn))
    #asks the user which piece they wish to move
    print ('select the piece you wish to move')
    move = input()
    #splits the input into to seperate x and y coordinates
    coord_A = move.split(",")
    #converts the x and y inputs to integers
    coord_Ax = int(coord_A[0])
    coord_Ay = int(coord_A[1])
    #checks if the functions are true
    if jump_r1(coord_Ax,coord_Ay) == True:
        if jump_r2(coord_Ax,coord_Ay) == True:
            if jump_b1(coord_Ax,coord_Ay) == True:
                if jump_b2(coord_Ax,coord_Ay) == True:
                    #prints the piece they selected
                    print("At coordinate " + str(coord_Ax) + "," + str(coord_Ay) + " is an " + board[coord_Ay][coord_Ax])
                    #checks if the functions are True
                    if checkNotBlank(int(coord_A[0]),int(coord_A[1])) == True:
                        if notYourPiece_R(int(coord_A[0]),int(coord_A[1])) == True:
                            if notYourPiece_B(int(coord_A[0]),int(coord_A[1])) == True:
                                #asks the user where they wish to move their pice
                                print ('select where you wish to move that piece ')
                                move2 = input()
                                #splits the input to 2 seperate coordinates
                                coord_A2 = move2.split(",")
                                #converts the coordinates to integers
                                coord_A2x = int(coord_A2[0])
                                coord_A2y = int(coord_A2[1])
                                #checks if the functions are true
                                if moveOne_r1(coord_Ax,coord_Ay,coord_A2x,coord_A2y) == True:
                                    if moveOne_b1(coord_Ax,coord_Ay,coord_A2x,coord_A2y) == True:
                                       if moveOne_kb1(coord_Ax,coord_Ay,coord_A2x,coord_A2y) == True:
                                           if moveOne_kr1(coord_Ax,coord_Ay,coord_A2x,coord_A2y) == True:
                                               #moves the desired piece by setting the distination space to the piece that was moved
                                               board[coord_A2y][coord_A2x] = board[coord_Ay][coord_Ax]
                                               #sets the space where the piece was moved to to blank
                                               board[coord_Ay][coord_Ax] = '_'
                                               #informs the user that they have succesfully moved a piece
                                               print ("You have moved a piece!")
                                               #loop the check through the top line of the board for a red piece and kings it
                                               for i in range(0,8):
                                                   if board[0][i] == 'r':
                                                       board[0][i] = 'R'
                                               #loop the check through the bottom line of the board for a black piece and kings it
                                               for i in range(0,8):
                                                   if board[7][i] == 'b':
                                                       board[7][i] = 'B'

                                               #checks to see if there are any red pices left else winner is black
                                               for i in range(0,8):
                                                   for j in range(0,8):
                                                       if board[j][i] == 'r' or 'R':
                                                           gameWinner = True
                                                       else:
                                                           gameWinner = False
                                                           print ('winner black')

                                                #checks to see if there are any red pices left else winner is black
                                               for i in range(0,8):
                                                   for j in range(0,8):
                                                       if board[j][i] == 'b' or 'B':
                                                           gameWinner = True
                                                       else:
                                                           gameWinner = False
                                                           print ('winner red')
                                               #change turn function to change the turn
                                               changeTurn()
                                               #prints the board
                                               printBoard()

    printBoard()
