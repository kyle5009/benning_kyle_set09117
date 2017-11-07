board = [['_','b','_','b','_','b','_','b'],
         ['b','_','b','_','b','_','b','_'],
         ['_','b','_','b','_','b','_','b'],
         ['_','_','_','_','_','_','_','_'],
         ['_','_','_','_','_','_','_','_'],
         ['r','_','r','_','r','_','r','_'],
         ['_','r','_','r','_','r','_','r'],
         ['r','_','r','_','r','_','r','_']]

def printBoard():
    print('   ' + '0' + ' ' + '1' + ' ' + '2' + ' ' + '3' + ' ' + '4' + ' ' + '5' + ' ' + '6' + ' ' + '7' + ' ')
    print('   ' + '_' + ' ' + '_' + ' ' + '_' + ' ' + '_' + ' ' + '_' + ' ' + '_' + ' ' + '_' + ' ' + '_' + ' ' )
    i = 0
    for i in range(0,8):
        print(str(i) + ' ' + '|' + board[i][0] + '|' + board[i][1] + '|' + board[i][2] + '|' + board[i][3] + '|' + board[i][4] + '|' + board[i][5] +
                '|' + board[i][6] + '|' + board[i][7] + '|')

def checkNotBlank(coord_Ax,coord_Ay):
    if board[coord_Ay][coord_Ax] == '_':
        print('you must select a valid piece')
        return False
    else:
        return True

def changeTurn():
    global turn
    if turn == 'r':
        turn = 'b'
    else:
        turn = 'r'

def notYourPiece_B(coord_Ax,coord_Ay):
    if turn == 'b':
        if board[coord_Ay][coord_Ax] == 'r':

            print ('you may only move your own piece')
            return False
        else:
            return True
    else:
        return True



def notYourPiece_R(coord_Ax,coord_Ay):
    if turn == 'r':
        if board[coord_Ay][coord_Ax] == 'b':
            print ('you may only move your own piece')
            return False
        else:
            return True
    else:
        return True

def moveOne_r1(coord_Ax,coord_Ay):
    if turn == 'r':
        if coord_A2y == coord_Ay -1 and (coord_A2x == coord_Ax - 1 or coord_A2x == coord_Ax + 1):
            return True
        else:
           print('Illegal move')
           return False
    else:
       return True


def moveOne_b1(coord_Ax,coord_Ay):
    if turn == 'b':
        if coord_A2y == coord_Ay +1 and (coord_A2x == coord_Ax - 1 or coord_A2x == coord_Ax + 1):
            return True
        else:
            print('Illegal move')
            return False
    else:
        return True


printBoard()

turn = 'r'
gameWinner = True
while gameWinner == True:
    print (turn)
    print ('select the piece you wish to move')
    move = input()
    coord_A = move.split(",")
    coord_Ax = int(coord_A[0])
    coord_Ay = int(coord_A[1])
    print("At coordinate " + str(coord_Ax) + "," + str(coord_Ay) + " is an " + board[coord_Ay][coord_Ax])
    if checkNotBlank(int(coord_A[0]),int(coord_A[1])) == True:
        if notYourPiece_R(int(coord_A[0]),int(coord_A[1])) == True:
            if notYourPiece_B(int(coord_A[0]),int(coord_A[1])) == True:
    #         else:
    #             print("three")
    #     else:
    #         print("two")
    # else:
    #     print("one")
                print ('select where you wish to move that piece ')
                move2 = input()
                coord_A2 = move2.split(",")
                coord_A2x = int(coord_A2[0])
                coord_A2y = int(coord_A2[1])
                if moveOne_r1(coord_A2y,coord_A2y) == True:
                    if moveOne_b1(coord_A2y,coord_A2y) == True:
                       board[coord_Ay][coord_Ax] = '_'
                       board[coord_A2y][coord_A2x] = turn
                       print ("You have moved a piece!")
                       changeTurn()
                       printBoard()



printBoard()
