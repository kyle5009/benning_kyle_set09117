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

print ('select the piece you wish to move')
turn = 'r'
move = input()
coord_A = move.split(",")
coord_Ax = int(coord_A[0])
coord_Ay = int(coord_A[1])
board[coord_Ay][coord_Ax] = turn


#Board[][] = turn
if turn == 'r':
    turn = 'b'
else:
    turn = 'r'

def move():

    if board == '_':
        print('you must select a valid piece')




printBoard()
