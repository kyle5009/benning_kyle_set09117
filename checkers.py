board = [['_','b','_','b','_','b','_','b'],
         ['b','_','b','_','b','_','b','_'],
         ['_','b','_','b','_','b','_','b'],
         ['_','_','_','_','_','_','_','_'],
         ['_','_','_','_','_','_','_','_'],
         ['r','_','r','_','r','_','r','_'],
         ['_','r','_','r','_','r','_','r'],
         ['r','_','r','_','r','_','r','_']]

def printBoard():
    i = 0
    for i in range(0,8):
        print('|' + board[i][0] + '|' + board[i][1] + '|' + board[i][2] + '|' + board[i][3] + '|' + board[i][4] + '|' + board[i][5] +
                '|' + board[i][6] + '|' + board[i][7] + '|')

printBoard()

print ('select the piece you wish to move')
coord_A = move.split(",")
coord_Ax = int(coord_A[0])
coord_Ay = int(coord_A[1])
board[coord_Ay][coord_Ax] = '_'
#board[coord_Ay][coord_Ax] = turn
#Board[][] = turn
if turn == 'r':
    turn = 'b'
else:
    turn = 'r'

printBoard()

print ('select where you wish to move that piece ')
move2 = input()
coord_A2 = move2.split(",")
coord_A2x = int(coord_A2[0])
coord_A2y = int(coord_A2[1])
board[coord_A2y][coord_A2x] = turn

print ("You have moved a piece!")

def move():

    if board == '_':
        print('you must select a valid piece')

printBoard()
