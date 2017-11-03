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
    if board[coord_Ax][coord_Ay] == '_':
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

def notYourPiece(coord_Ax,coord_Ay):
    if turn == 'b':
        if board[coord_Ax][coord_Ay] == 'r':
            print ('you may only move your own piece')
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
    if checkNotBlank(int(coord_A[0]),int(coord_A[1])) == True:
        if notYourPiece(int(coord_A[0]),int(coord_A[1])) == True:
            coord_Ax = int(coord_A[0])
            coord_Ay = int(coord_A[1])
            board[coord_Ay][coord_Ax] = '_'

            print ('select where you wish to move that piece ')
            move2 = input()
            coord_A2 = move2.split(",")
            coord_A2x = int(coord_A2[0])
            coord_A2y = int(coord_A2[1])
            board[coord_A2y][coord_A2x] = turn

            print ("You have moved a piece!")

            changeTurn()
            printBoard()

printBoard()
